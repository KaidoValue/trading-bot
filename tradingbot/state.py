"""Stand des Bots speichern und laden (Kapital, offene Positionen, Trades, Risiko-Status).

So kann der Bot beendet und später fortgesetzt werden, z.B. einmal täglich per Windows-Aufgabenplanung.
"""
from __future__ import annotations

import json
from datetime import date, datetime
from pathlib import Path

import pandas as pd

from .broker import PaperBroker
from .engine import OpenTrade, Trader


def _enc(v):
    if isinstance(v, (datetime, date, pd.Timestamp)):
        return {"__dt__": v.isoformat()}
    return v


def _dec(v):
    if isinstance(v, dict) and "__dt__" in v:
        s = v["__dt__"]
        return datetime.fromisoformat(s) if "T" in s or ":" in s else date.fromisoformat(s)
    return v


def _walk(obj, fn):
    if isinstance(obj, dict) and "__dt__" not in obj:
        return {k: _walk(v, fn) for k, v in obj.items()}
    if isinstance(obj, list):
        return [_walk(v, fn) for v in obj]
    return fn(obj)


def save(path: Path, trader: Trader, last_bar: dict) -> None:
    r = trader.risk
    state = {
        "open_trades": {s: vars(t) for s, t in trader.open_trades.items()},
        "closed": trader.closed,
        "last_bar": last_bar,
        "note": trader.note,
        "news": trader.context.to_dict() if trader.context else None,
        "updated": datetime.now().astimezone(),
        "risk": {"peak_equity": r.peak_equity, "day": r.day, "day_start_equity": r.day_start_equity,
                 "trades_today": r.trades_today, "loss_streak": r.loss_streak, "paused_until": r.paused_until,
                 "halted": r.halted, "halted_on": r.halted_on, "halt_reason": r.halt_reason},
    }
    if isinstance(trader.broker, PaperBroker):
        state["paper"] = {"cash": trader.broker._cash, "positions": trader.broker.positions,
                          "interest_paid": trader.broker.interest_paid, "interest_at": trader.broker.interest_at}
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(_walk(state, _enc), indent=2, default=str))
    tmp.replace(path)


def load(path: Path, trader: Trader) -> dict:
    """Lädt einen gespeicherten Stand in `trader`. Gibt last_bar zurück (leer, wenn kein Stand existiert)."""
    if not path.exists():
        return {}
    state = _walk(json.loads(path.read_text()), _dec)
    trader.open_trades = {s: OpenTrade(**t) for s, t in state["open_trades"].items()}
    trader.closed = state["closed"]
    trader.note = state.get("note", "")
    for k, v in state["risk"].items():
        setattr(trader.risk, k, v)
    if "paper" in state and isinstance(trader.broker, PaperBroker):
        trader.broker._cash = state["paper"]["cash"]
        trader.broker.positions = state["paper"]["positions"]
        trader.broker.interest_paid = state["paper"].get("interest_paid", 0.0)
        trader.broker.interest_at = state["paper"].get("interest_at")
    return {s: pd.Timestamp(v) for s, v in state["last_bar"].items()}
