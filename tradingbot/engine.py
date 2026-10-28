"""Gemeinsame Handelslogik für Backtest, Paper- und Live-Betrieb."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime

from .broker import Broker
from .news import MarketContext
from .risk import RiskManager

log = logging.getLogger(__name__)


@dataclass
class OpenTrade:
    side: int          # +1 long, -1 short
    entry: float
    qty: float
    stop: float
    target: float
    opened: object
    context: dict = field(default_factory=dict)
    horizon: str = ""  # Zeithorizont, der die Position eröffnet hat (nur er darf sie per Signal schliessen)


MIN_SHARE, MAX_SHARE = 0.10, 0.70      # Grenzen für den Kapitalanteil eines Horizonts bei adaptive_shares


@dataclass
class Trader:
    broker: Broker
    risk: RiskManager
    allow_short: bool = False
    context: MarketContext | None = None      # Nachrichtenlage (nur Paper/Live)
    open_trades: dict[str, OpenTrade] = field(default_factory=dict)
    closed: list[dict] = field(default_factory=list)
    note: str = ""                             # letzte Entscheidung in Worten (für Status-Anzeige)
    horizons: dict = field(default_factory=dict)   # Name -> config.Horizon (kurz/mittel/lang)
    adaptive_shares: bool = False

    def shares(self) -> dict[str, float]:
        """Anteil jedes Horizonts am investierbaren Kapital. Mit adaptive_shares bekommt der Horizont mehr,
        dessen letzte 20 Trades mehr verdient haben (zwischen MIN_SHARE und MAX_SHARE)."""
        if not self.horizons:
            return {}
        total = sum(h.share for h in self.horizons.values()) or 1.0
        base = {n: h.share / total for n, h in self.horizons.items()}
        if not self.adaptive_shares or len(base) < 2:
            return base
        capital = max(self.risk.day_start_equity, 1e-9)
        w = {}
        for n, b in base.items():
            pnl = sum(t["pnl"] for t in [t for t in self.closed if t.get("horizon") == n][-20:])
            w[n] = b * min(max(1 + 10 * pnl / capital, 0.25), 2.0)
        # Normieren: wer über/unter die Grenze käme, wird dort festgehalten, der Rest wird neu verteilt
        fixed: dict[str, float] = {}
        for _ in range(len(w)):
            free = {n: v for n, v in w.items() if n not in fixed}
            rest, total = 1 - sum(fixed.values()), sum(free.values())
            scaled = {n: v / total * rest for n, v in free.items()}
            out = {n: min(max(v, MIN_SHARE), MAX_SHARE) for n, v in scaled.items() if not MIN_SHARE <= v <= MAX_SHARE}
            if not out:
                return fixed | scaled
            fixed |= out
        total = sum(fixed.values())
        return {n: v / total for n, v in fixed.items()}

    def equity(self, prices: dict[str, float]) -> float:
        return self.broker.cash() + sum(self.broker.position(s) * p for s, p in prices.items())

    def open_risk(self, equity: float) -> float:
        """Summe der Verluste bis zu den Stops aller offenen Positionen, als Anteil am Kapital."""
        if equity <= 0:
            return 1.0
        return sum(abs(t.entry - t.stop) * t.qty for t in self.open_trades.values()) / equity

    def on_signal(self, symbol: str, signal: int, price: float, atr: float, equity: float, when,
                  size_factor: float = 1.0, can_open_new: bool = True, horizon: str = "") -> None:
        """+1: long gehen (Short vorher schliessen), -1: Long schliessen und, falls erlaubt, short gehen.
        Pro Coin gibt es eine Position. Hält sie ein anderer Horizont, bleibt sie unberührt."""
        if signal == 0:
            return
        t = self.open_trades.get(symbol)
        if t and t.horizon != horizon:
            self.note = f"{symbol}: Position gehört zum Horizont «{t.horizon or '-'}»"
            return
        if t and t.side != signal:
            self.exit(symbol, price, "Signal", when)
            equity = self.equity({symbol: price})
            t = None
        if t:
            self.note = f"{symbol}: Position offen, Signal bestätigt"
            return
        if signal < 0 and not self.allow_short:
            self.note = f"{symbol}: Signal 'raus', bleibe in Cash"
            return
        if not can_open_new:
            self.note = f"{symbol}: kein Einstieg (Spread im Orderbuch zu gross)"
            return
        h = self.horizons.get(horizon)
        risk_pct = h.risk_per_trade if h else None
        if not self.risk.can_open(equity, when, self.open_risk(equity), len(self.open_trades), risk_pct=risk_pct):
            self.note = f"{symbol}: kein Einstieg ({self.risk.last_block})"
            log.info("%s %s", when, self.note)
            return
        if self.context and not self.context.allows(signal):
            s = self.context.summary()
            self.note = f"{symbol}: Einstieg pausiert wegen Nachrichtenlage ({s['event'] if s['event'] != '-' else 'bestätigte Themen: ' + s['news_themes'] + ', Wert ' + str(s['news_score'])})"
            log.info("%s %s", when, self.note)
            return
        factor = size_factor * (self.context.size_factor() if self.context else 1.0)
        exposure = sum(abs(t.qty) * t.entry for t in self.open_trades.values() if not h or t.horizon == horizon)
        plan = self.risk.plan(equity, self.broker.cash(), price, atr, side=signal, size_factor=factor,
                              exposure=exposure, risk_pct=risk_pct,
                              stop_atr=h.stop_loss_atr if h else None, target_atr=h.take_profit_atr if h else None,
                              budget_share=self.shares().get(horizon, 1.0))
        if not plan:
            self.note = f"{symbol}: kein Einstieg ({self.risk.last_block})"
            return
        fill = (self.broker.buy(symbol, plan.qty, price) if signal > 0
                else self.broker.sell(symbol, plan.qty, price, short=True))
        if fill:
            info = self.context.summary() if self.context else {}
            info["session"] = session(when)
            self.open_trades[symbol] = OpenTrade(signal, fill.price, fill.qty, plan.stop, plan.target, when, info,
                                                 horizon)
            self.risk.record_open()
            self.note = f"{symbol}: {'gekauft' if signal > 0 else 'short eröffnet'} {fill.qty:.6f} @ {fill.price:.2f}"
            log.info("%s %s %s %.6f @ %.2f (Stop %.2f, Ziel %.2f)", when, "LONG" if signal > 0 else "SHORT",
                     symbol, fill.qty, fill.price, plan.stop, plan.target)

    def check_stops(self, symbol: str, open_: float, high: float, low: float, when) -> None:
        """Prüft Stop-Loss/Take-Profit innerhalb einer Kerze (konservativ: Stop zuerst)."""
        t = self.open_trades.get(symbol)
        if not t:
            return
        if t.side > 0:
            gap, stop_hit, target_hit = open_ <= t.stop, low <= t.stop, high >= t.target
        else:
            gap, stop_hit, target_hit = open_ >= t.stop, high >= t.stop, low <= t.target
        if gap:
            self.exit(symbol, open_, "Stop-Loss (Gap)", when)
        elif stop_hit:
            self.exit(symbol, t.stop, "Stop-Loss", when)
        elif target_hit:
            self.exit(symbol, t.target, "Take-Profit", when)

    def exit(self, symbol: str, price: float, reason: str, when) -> None:
        t = self.open_trades.pop(symbol)
        fill = self.broker.sell(symbol, t.qty, price) if t.side > 0 else self.broker.buy(symbol, t.qty, price)
        if not fill:
            return
        pnl = t.side * (fill.price - t.entry) * fill.qty - fill.fee
        self.closed.append(dict(symbol=symbol, side="long" if t.side > 0 else "short", opened=t.opened,
                                closed=when, entry=t.entry, exit=fill.price, qty=fill.qty, pnl=pnl, reason=reason,
                                horizon=t.horizon, **t.context))
        self.risk.record_close(pnl, when)
        log.info("%s SCHLIESSEN %s @ %.2f (%s) PnL %.2f", when, symbol, fill.price, reason, pnl)

    def close_all(self, prices: dict[str, float], reason: str, when) -> None:
        for s in list(self.open_trades):
            self.exit(s, prices[s], reason, when)


def session(when) -> str:
    """Handelssitzung nach UTC-Stunde. Krypto handelt rund um die Uhr, aber Volumen und Volatilität
    sind während London und New York am höchsten."""
    if not isinstance(when, datetime):
        return "-"
    h = when.hour
    if h < 7:
        return "Asien"
    if h < 13:
        return "London"
    if h < 16:
        return "London+New York"
    if h < 21:
        return "New York"
    return "Nach US-Schluss"
