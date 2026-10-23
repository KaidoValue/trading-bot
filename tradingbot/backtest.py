"""Backtest: Strategie auf historischen Daten durchspielen, inkl. Gebühren, Slippage und Risikoregeln."""
from __future__ import annotations

from dataclasses import dataclass

import numpy as np
import pandas as pd

from . import indicators as ind
from .broker import PaperBroker
from .config import Config
from .engine import Trader
from .risk import RiskManager
from .strategies import Strategy

WARMUP = 60


@dataclass
class Result:
    equity: pd.Series
    trades: pd.DataFrame
    buy_and_hold: float
    exposure: float = 0.0        # Anteil der Zeit mit offener Position
    buy_and_hold_dd: float = 0.0

    def stats(self) -> dict:
        eq = self.equity
        rets = eq.pct_change().dropna()
        years = max((eq.index[-1] - eq.index[0]).days / 365.25, 1e-9)
        per_year = len(eq) / years
        pnl = self.trades["pnl"] if len(self.trades) else pd.Series(dtype=float)
        wins = pnl > 0
        gross_win, gross_loss = pnl[pnl > 0].sum(), -pnl[pnl < 0].sum()
        avg_win = pnl[pnl > 0].mean() if (pnl > 0).any() else 0.0
        avg_loss = -pnl[pnl < 0].mean() if (pnl < 0).any() else 0.0
        streak = (pnl < 0).astype(int)
        max_streak = int(streak.groupby((streak == 0).cumsum()).sum().max()) if len(pnl) else 0
        return {
            "Endkapital": round(eq.iloc[-1], 2),
            "Rendite %": round((eq.iloc[-1] / eq.iloc[0] - 1) * 100, 2),
            "Buy & Hold %": round(self.buy_and_hold * 100, 2),
            "B&H Drawdown %": round(self.buy_and_hold_dd * 100, 2),
            "Im Markt %": round(self.exposure * 100, 1),
            "Max. Drawdown %": round(((eq / eq.cummax()) - 1).min() * 100, 2),
            "Sharpe": round(rets.mean() / rets.std() * np.sqrt(per_year), 2) if rets.std() > 0 else 0.0,
            "Trades": len(self.trades),
            "Trefferquote %": round(wins.mean() * 100, 1) if len(wins) else 0.0,
            "CRV": round(avg_win / avg_loss, 2) if avg_loss else 0.0,
            "Expectancy": round(pnl.mean(), 2) if len(pnl) else 0.0,     # Ø Gewinn pro Trade
            "Profit Factor": round(gross_win / gross_loss, 2) if gross_loss else 0.0,
            "Max. Verlustserie": max_streak,
        }


def run(df: pd.DataFrame, strategy: Strategy, cfg: Config, symbol: str = "SYM") -> Result:
    signals = strategy.signals(df)
    atr = ind.atr(df)
    broker = PaperBroker(cfg.starting_capital, cfg.fee_rate, cfg.slippage)
    broker.leverage = cfg.risk.leverage
    trader = Trader(broker, RiskManager(cfg.risk, cfg.starting_capital), allow_short=cfg.allow_short)
    curve = []
    in_market = 0
    pending = 0
    for i in range(WARMUP, len(df)):
        bar, when = df.iloc[i], df.index[i]
        # 1) Signal der Vorkerze zum Eröffnungskurs ausführen (kein Blick in die Zukunft)
        if pending:
            eq = trader.equity({symbol: bar["open"]})
            trader.on_signal(symbol, pending, bar["open"], atr.iloc[i - 1], eq, when)
        # 2) Stops innerhalb der Kerze
        trader.check_stops(symbol, bar["open"], bar["high"], bar["low"], when)
        # 3) Risiko-Status aktualisieren, Not-Aus schliesst alles
        eq = trader.equity({symbol: bar["close"]})
        trader.risk.update(eq, when.date())
        if trader.risk.halted and trader.open_trades:
            trader.close_all({symbol: bar["close"]}, "Not-Aus", when)
            eq = trader.equity({symbol: bar["close"]})
        curve.append((when, eq))
        in_market += bool(trader.open_trades)
        pending = int(signals.iloc[i])
    equity = pd.Series(dict(curve))
    bh = df["close"].iloc[-1] / df["close"].iloc[WARMUP] - 1
    px = df["close"].iloc[WARMUP:]
    bh_dd = (px / px.cummax() - 1).min()
    return Result(equity, pd.DataFrame(trader.closed), bh, in_market / max(len(curve), 1), bh_dd)


def walk_forward(df: pd.DataFrame, cfg: Config, strategies: dict, train_bars: int = 2000, test_bars: int = 500,
                 symbol: str = "SYM") -> pd.DataFrame:
    """Walk-Forward-Analyse gegen Overfitting.

    Für jedes Fenster wird die beste Strategie nur auf den Trainingsdaten gewählt (nach Sharpe) und dann auf
    den direkt folgenden, nie gesehenen Testdaten gehandelt. Nur die Testergebnisse zählen. Liegt dieses
    Ergebnis deutlich unter dem Backtest, ist die Strategie überangepasst.
    """
    rows = []
    start = 0
    while start + train_bars + test_bars <= len(df):
        train = df.iloc[start:start + train_bars]
        scores = {name: run(train, factory(), cfg, symbol).stats()["Sharpe"] for name, factory in strategies.items()}
        best = max(scores, key=scores.get)
        # Testlauf mit Vorlauf aus den Trainingsdaten (für Indikatoren), gewertet wird nur der Testteil
        warm = 300
        seg = df.iloc[start + train_bars - warm:start + train_bars + test_bars]
        res = run(seg, strategies[best](), cfg, symbol)
        eq = res.equity.iloc[warm - WARMUP:]
        rows.append({
            "Test ab": seg.index[warm].date(), "Gewählt": best, "Sharpe Training": scores[best],
            "Rendite Test %": round((eq.iloc[-1] / eq.iloc[0] - 1) * 100, 2),
            "Buy & Hold Test %": round((seg["close"].iloc[-1] / seg["close"].iloc[warm] - 1) * 100, 2),
        })
        start += test_bars
    return pd.DataFrame(rows)
