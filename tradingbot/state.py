"""Stand des Bots speichern und laden (Kapital, offene Positionen, Trades, Risiko-Status).

So kann der Bot beendet und später fortgesetzt werden, z.B. einmal täglich per Windows-Aufgabenplanung.
"""
from __future__ import annotations

import json
from datetime import date, datetime, timezone
from pathlib import Path

import pandas as pd

from .broker import WINDOW, PaperBroker
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


def save(path: Path, trader: Trader, last_bar: dict, abgleich: dict | None = None) -> None:
    """abgleich: Ergebnis von Trader.abgleich (bot.py), für die Anzeige gespeichert."""
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
    if trader.buchhaltung or trader.altlasten:
        state["buchhaltung"] = trader.buchhaltung | {"altlasten": trader.altlasten}
    if trader.zaehler:
        state["zaehler"] = trader.zaehler
    if abgleich:
        state["abgleich"] = abgleich
    if isinstance(trader.broker, PaperBroker):
        b = trader.broker
        b._prune()
        state["paper"] = {"cash": b._cash, "positions": b.positions, "interest_paid": b.interest_paid,
                          "interest_at": b.interest_at, "quote_usd": b.quote_usd,
                          "volume": [[t, round(v, 2)] for t, v in b.volume_log]}     # Umsatz der letzten 30 Tage
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
    trader.buchhaltung = state.get("buchhaltung") or {}
    trader.altlasten = trader.buchhaltung.get("altlasten", 0.0)
    trader.zaehler = state.get("zaehler") or {}
    for k, v in state["risk"].items():
        setattr(trader.risk, k, v)
    if "paper" in state and isinstance(trader.broker, PaperBroker):
        p, b = state["paper"], trader.broker
        b._cash = p["cash"]
        b.positions = p["positions"]
        b.interest_paid = p.get("interest_paid", 0.0)
        b.interest_at = p.get("interest_at")
        b.quote_usd = p.get("quote_usd", 1.0)
        now = b.now or datetime.now(timezone.utc)
        b.load_volume(p["volume"] if "volume" in p else _volume_from_trades(trader, now))
        _margin_alt(trader, state["open_trades"])
    return {s: pd.Timestamp(v) for s, v in state["last_bar"].items()}


def _utc(x) -> datetime | None:
    """Zeitpunkt mit Zeitzone (UTC); None, wenn keiner (z.B. Zahlen statt Zeiten in Tests)."""
    if not isinstance(x, (date, str)):          # datetime ist auch ein date
        return None
    try:
        t = pd.Timestamp(x)
    except ValueError:
        return None
    return (t.tz_localize("UTC") if t.tzinfo is None else t.tz_convert("UTC")).to_pydatetime()


def _volume_from_trades(trader: Trader, now: datetime) -> list:
    """Stand ohne Umsatz-Protokoll (vor der Gebührenstaffel): die Fills der letzten 30 Tage aus den Trades
    nachbilden. Abgeschlossene: Kauf beim Eröffnen, Verkauf beim Schliessen; offene: Kauf der ganzen Menge."""
    fills = [f for c in trader.closed
             for f in ((c.get("opened"), c["qty"] * c["entry"]), (c.get("closed"), c["qty"] * c["exit"]))]
    fills += [(t.opened, (t.qty + t.sold) * t.entry) for t in trader.open_trades.values()]
    fills = [(z, v) for z, v in ((_utc(z), v) for z, v in fills) if z is not None and z >= now - WINDOW]
    return sorted(fills, key=lambda f: f[0])


def _margin_alt(trader: Trader, raw: dict) -> None:
    """Positionen von vor der Margin-Rechnung (ohne margin_value): Shorts sind ganz geliehen; Longs mit Hebel teilen
    sich das geliehene Cash nach ihrem Wert, so wie bisher die Zinsen verteilt wurden."""
    alt = [t for s, t in trader.open_trades.items() if "margin_value" not in raw[s]]
    b = trader.broker
    debt = max(0.0, -b.cash()) if b.leverage > 1 else 0.0
    longs = sum(t.qty * t.entry for t in alt if t.side > 0)
    for t in alt:
        t.margin_value = ((t.qty + t.sold) * t.entry if t.side < 0
                          else debt * (t.qty + t.sold) * t.entry / longs if longs else 0.0)
