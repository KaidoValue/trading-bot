"""Causal, isolated strategy replay using the production Trader and PaperBroker.

Each member has a separate virtual account. This is counterfactual evidence,
not the multi-coin portfolio's realised PnL. News/order books are unavailable.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass

import pandas as pd

from . import indicators as ind
from .broker import paper_broker
from .config import Config
from .engine import MINUTES, Trader
from .risk import RiskManager

WARMUP = 250


@dataclass
class Replay:
    equity: pd.Series
    returns: pd.Series
    trades: list[dict]
    exposure: float = 0.0


def replay(df, signals, cfg: Config, horizon=None, symbol="SYM", start=None,
           end=None, liquidate=False, daily_history=None, warmup=WARMUP) -> Replay:
    """Signals at close t execute at open t+1; warmup never trades.

    start/end delimit a fresh funded account, while indicators retain their
    preceding history. Optional end liquidation charges the final exit costs.
    """
    from .strategies import trend_direction

    cfg = deepcopy(cfg)
    h = deepcopy(horizon or cfg.horizon_list()[0])
    h.share = 1.0
    broker = paper_broker(cfg)
    allow_short = cfg.allow_short if h.allow_short is None else h.allow_short
    trader = Trader(broker, RiskManager(cfg.risk, cfg.starting_capital), allow_short=allow_short)
    trader.horizons = {h.name: h}
    trader.short_probation = cfg.short_probation
    atr, anchor = ind.atr(df), ind.ema(df["close"], 20)
    trend = None
    if h.trend_filter:
        daily = daily_history if daily_history is not None else df.resample("1D").agg({"open": "first", "high": "max", "low": "min",
                                      "close": "last", "volume": "sum"}).dropna()
        # A daily candle is known only after its close, never within that day.
        direction = trend_direction(daily)
        direction.index = direction.index + pd.Timedelta(days=1)
        trend = direction.reindex(df.index, method="ffill").fillna(0)
    curve = pd.Series(cfg.starting_capital, index=df.index, dtype=float)
    first = max(warmup, int(df.index.searchsorted(start)) if start is not None else warmup)
    last = int(df.index.searchsorted(end)) if end is not None else len(df)
    last = min(last, len(df))
    previous = None
    in_market = 0
    for i in range(first, last):
        bar, when = df.iloc[i], df.index[i]
        broker.now = when.to_pydatetime()
        if previous is not None:
            trader.charge_interest({symbol: float(bar.open)}, (when - previous).total_seconds() / 3600,
                                   cfg.risk.margin_interest_per_day)
        previous = when
        eq = trader.equity({symbol: float(bar.open)})
        trader.risk.update(eq, when.date())
        signal = int(signals.iloc[i - 1])
        if signal:
            trader.on_signal(symbol, signal, float(bar.open), float(atr.iloc[i - 1]), eq,
                             when.to_pydatetime(), horizon=h.name,
                             trend=int(trend.iloc[i]) if trend is not None else None,
                             anchor=float(anchor.iloc[i - 1]))
        trader.check_stops(symbol, float(bar.open), float(bar.high), float(bar.low), when.to_pydatetime())
        eq = trader.equity({symbol: float(bar.close)})
        trader.risk.update(eq, when.date())
        notional = abs(broker.position(symbol)) * float(bar.close)
        if cfg.risk.leverage > 1 and eq < notional / cfg.risk.leverage * cfg.risk.liquidation_margin:
            trader.close_all({symbol: float(bar.close)}, "Liquidation", when.to_pydatetime())
        elif trader.risk.halted:
            trader.close_all({symbol: float(bar.close)}, "Not-Aus", when.to_pydatetime())
        if liquidate and i == last - 1:
            trader.close_all({symbol: float(bar.close)}, "Prüfende", when.to_pydatetime())
        curve.iloc[i] = trader.equity({symbol: float(bar.close)})
        in_market += bool(trader.open_trades)
    if last < len(curve) and last > first:
        curve.iloc[last:] = curve.iloc[last - 1]
    return Replay(curve, curve.pct_change().fillna(0), trader.closed, in_market / max(last - first, 1))


def evaluation_params(cfg, horizon=None):
    """Bind the same configured execution assumptions to adaptive learners."""
    return {"execution_config": deepcopy(cfg),
            "execution_horizon": deepcopy(horizon or cfg.horizon_list()[0])}
