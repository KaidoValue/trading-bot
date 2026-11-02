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


def run(df: pd.DataFrame, strategy: Strategy, cfg: Config, symbol: str = "SYM", start=None) -> Result:
    from copy import copy
    from .evaluation import evaluation_params
    # Never import a persisted state that may already know this test period.
    strategy = copy(strategy)
    strategy.params = {**strategy.params, **evaluation_params(cfg)}
    if hasattr(strategy, "memory"):
        strategy.memory = None
    if hasattr(strategy, "members"):
        strategy.members = [m for m in strategy.members if not m.name.startswith("labor_")]
    strategy._pnl_cache = None
    from .evaluation import replay
    signals = strategy.signals(df)
    replayed = replay(df, signals, cfg, symbol=symbol, warmup=WARMUP, start=start, liquidate=start is not None)
    first = max(WARMUP, int(df.index.searchsorted(start)) if start is not None else WARMUP)
    equity = replayed.equity.iloc[first:]
    bh = df["close"].iloc[-1] / df["close"].iloc[first] - 1
    px = df["close"].iloc[first:]
    bh_dd = (px / px.cummax() - 1).min()
    return Result(equity, pd.DataFrame(replayed.trades), bh, replayed.exposure, bh_dd)


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
        # Retain all available indicator/learning history, but fund a fresh
        # account only at the first test bar. No training positions carry over.
        boundary = start + train_bars
        seg = df.iloc[:boundary + test_bars]
        res = run(seg, strategies[best](), cfg, symbol, start=seg.index[boundary])
        eq = res.equity
        rows.append({
            "Test ab": seg.index[boundary].date(), "Gewählt": best, "Sharpe Training": scores[best],
            "Rendite Test %": round((eq.iloc[-1] / cfg.starting_capital - 1) * 100, 2),
            "Buy & Hold Test %": round((seg["close"].iloc[-1] / seg["close"].iloc[boundary] - 1) * 100, 2),
        })
        start += test_bars
    return pd.DataFrame(rows)
