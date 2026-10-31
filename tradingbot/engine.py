"""Gemeinsame Handelslogik für Backtest, Paper- und Live-Betrieb."""
from __future__ import annotations

import logging
from dataclasses import dataclass, field
from datetime import datetime

from .broker import KRAKEN_TIERS, LIQUIDATION_FEE, Broker
from .news import MarketContext
from .phase import PhaseBook, stretch_ok, trend_of
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
    fee: float = 0.0          # Kaufgebühr, wird beim Schliessen anteilig vom Ergebnis abgezogen
    partial: float = 0.0      # Kurs für den Teilgewinn (0 = keiner oder schon erledigt)
    partial_pct: float = 0.0  # Anteil, der beim Teilgewinn verkauft wird
    trail: float = 0.0        # Abstand des Nachlauf-Stops zum besten Kurs (0 = keiner)
    best: float = 0.0         # bester Kurs seit Einstieg
    sold: float = 0.0         # schon verkaufte Menge (Teilgewinn)
    sold_value: float = 0.0   # Erlös daraus (Menge × Kurs)
    realized: float = 0.0     # Ergebnis der schon verkauften Teile nach Gebühren
    interest: float = 0.0     # Margin-Kosten bisher (Eröffnungsgebühr, Zinsen), werden vom Ergebnis abgezogen
    fees_done: float = 0.0    # Verkaufsgebühren der schon verkauften Teile
    margin_value: float = 0.0  # geliehener Teil beim Eröffnen (Margin-Position): Longs mit Hebel, Shorts ganz


MIN_SHARE, MAX_SHARE = 0.0, 1.0        # Grenzen für den Kapitalanteil eines Horizonts bei adaptive_shares
WEAK = 0.05             # ein Horizont, der verliert, schrumpft bis auf 5 % seines Startanteils (praktisch aus,
                        # handelt aber noch winzig weiter und kann sich so zurückkämpfen)
MINUTES = {"1m": 1, "5m": 5, "15m": 15, "30m": 30, "1h": 60, "4h": 240, "1d": 1440, "1w": 10080}
PROBATION = 0.25        # Short-Probezeit: so gross sind Shorts, bis sie sich bewährt haben


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
    priority: bool = False      # längerer Horizont darf eine Position eines kürzeren übernehmen bzw. drehen
    short_probation: bool = False   # Shorts nur klein (PROBATION), bis die letzten Shorts Gewinn gebracht haben
    phase_book: PhaseBook | None = None    # Marktphasen: welcher Horizont verdient in welcher Phase
    phase_exit: bool = False                # Position schliessen, wenn die Phase gegen sie kippt
    phases: dict = field(default_factory=dict)   # Coin -> aktuelle Marktphase
    altlasten: float = 0.0      # Kosten vor dem 28.10.2026, die zu keinem Trade gehören (buchhaltung.py)
    buchhaltung: dict = field(default_factory=dict)   # Angaben zur einmaligen Nachbuchung (buchhaltung.py)
    zaehler: dict = field(default_factory=dict)       # laufende Zähler im Stand (z.B. Stop-Treffer nur in Minutenkerzen)
    kurse: dict = field(default_factory=dict)         # letzter Kurs je Coin (Symbol -> [Kurs, Zeit]), für Ausfälle

    def shorts_proven(self) -> bool:
        """Haben sich Shorts bewährt? Mindestens 10 Shorts, die letzten 20 zusammen im Gewinn."""
        shorts = [t["pnl"] for t in self.closed if t.get("side") == "short"][-20:]
        return len(shorts) >= 10 and sum(shorts) > 0

    def charge_interest(self, prices: dict[str, float], hours: float, rate_per_day: float) -> None:
        """Rollover-Zinsen wie bei Kraken (alle 4 Std., hier anteilig nach Stunden), nur auf Geliehenes: bei Longs
        der geliehene Teil (margin_value, nach Teilverkäufen anteilig), bei Shorts der aktuelle Wert der geliehenen
        Coins. Jeder Trade trägt seine eigenen Zinsen, damit sein Ergebnis wirklich alle Kosten enthält."""
        b = self.broker
        if not hasattr(b, "book_interest") or rate_per_day <= 0 or hours <= 0:
            return
        for s, t in self.open_trades.items():
            base = (t.qty * prices.get(s, t.entry) if t.side < 0
                    else t.margin_value * t.qty / (t.qty + t.sold))
            fee = base * rate_per_day * hours / 24
            if fee > 0:
                b.book_interest(fee)
                t.interest += fee

    def shares(self) -> dict[str, float]:
        """Anteil jedes Horizonts am investierbaren Kapital. Mit adaptive_shares bekommt der Horizont mehr,
        dessen letzte 20 Trades mehr verdient haben (zwischen MIN_SHARE und MAX_SHARE). Ein Horizont, der
        verliert, wird bis auf WEAK seines Startanteils verkleinert: so schaltet der Bot ihn praktisch ab."""
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
            w[n] = b * min(max(1 + 10 * pnl / capital, WEAK), 2.0)
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

    def abgleich(self, prices: dict[str, float], start: float) -> dict:
        """Buchhaltung prüfen: Kapital = Startkapital + Ergebnisse aller Trades (offene zum aktuellen Kurs, alle
        nach Gebühren und Zinsen) - Altlasten. Die Kurse heben sich dabei auf: eine Differenz ist eine echte Lücke.
        Coins ohne Kurs zählen zum Einstiegskurs."""
        px = {s: t.entry for s, t in self.open_trades.items()} | prices
        kapital = self.equity(px)
        offen = sum(t.side * (px[s] - t.entry) * t.qty - t.fee * t.qty / (t.qty + t.sold) - t.interest + t.realized
                    for s, t in self.open_trades.items())
        erwartet = start + sum(c["pnl"] for c in self.closed) + offen - self.altlasten
        return {"kapital": kapital, "erwartet": erwartet, "differenz": kapital - erwartet}

    def gebuehren_bisher(self) -> float:
        """Alle bisher bezahlten Gebühren: abgeschlossene Trades und offene Positionen (Kauf und Teilverkäufe)."""
        return (sum(c.get("fees", 0.0) for c in self.closed)
                + sum(t.fee + t.fees_done for t in self.open_trades.values()))

    def costs(self, symbol: str) -> float:
        """Kosten für Kauf und Verkauf zusammen (Gebühren + Slippage) als Anteil am Kurs. Ein Broker ohne Satz
        rechnet vorsichtig mit der kleinsten Kraken-Stufe."""
        fee = self.broker.fee(symbol) if hasattr(self.broker, "fee") else KRAKEN_TIERS[0][2]
        return 2 * (fee + getattr(self.broker, "slippage", 0.0))

    def open_risk(self, equity: float) -> float:
        """Summe der Verluste bis zu den Stops aller offenen Positionen, als Anteil am Kapital."""
        if equity <= 0:
            return 1.0
        return sum(abs(t.entry - t.stop) * t.qty for t in self.open_trades.values()) / equity

    def on_signal(self, symbol: str, signal: int, price: float, atr: float, equity: float, when,
                  size_factor: float = 1.0, can_open_new: bool = True, horizon: str = "",
                  trend: int | None = None, phase: str | None = None, anchor: float | None = None,
                  extra: dict | None = None) -> None:
        """+1: long gehen (Short vorher schliessen), -1: Long schliessen und, falls erlaubt, short gehen.
        Pro Coin gibt es eine Position. Hält sie ein anderer Horizont, bleibt sie unberührt.
        trend: langfristige Richtung des Coins (Trendfilter); neue Positionen nur in diese Richtung.
        phase: Marktphase des Coins (phase.py); anchor: 20er-Linie des Horizonts für den besten Einstieg.
        extra: weitere Angaben zum Einstieg für das Trade-Protokoll (z.B. delay_min aus bot.py)."""
        if phase:
            self.phases[symbol] = phase
        if signal == 0:
            return
        t = self.open_trades.get(symbol)
        if t and t.horizon != horizon:
            if not (self.priority and self._longer(horizon, t.horizon)):
                self.note = f"{symbol}: Position gehört zum Horizont «{t.horizon or '-'}»"
                return
            if t.side == signal:                       # gleiche Richtung: längerer Horizont übernimmt
                self._take_over(symbol, t, horizon, price, atr, equity)
                return
            # Gegenrichtung: schliessen, dann neu
            equity = self._exit_equity(symbol, price, f"Vorrang {horizon}", when, equity)
            t = None
        if t and t.side != signal:
            equity = self._exit_equity(symbol, price, "Signal", when, equity)
            t = None
        if t:
            self.note = f"{symbol}: Position offen, Signal bestätigt"
            return
        h = self.horizons.get(horizon)
        if signal < 0 and not (h.allow_short if h and h.allow_short is not None else self.allow_short):
            self.note = f"{symbol}: Signal 'raus', bleibe in Cash"
            return
        if not can_open_new:
            self.note = f"{symbol}: kein Einstieg (Spread im Orderbuch zu gross)"
            return
        if trend is not None and signal != trend:
            self.note = f"{symbol}: kein Einstieg gegen den langfristigen Trend (200-Tage-Linie)"
            return
        if h and h.min_edge and atr > 0:
            first = (h.partial_atr or h.take_profit_atr or self.risk.cfg.take_profit_atr) * atr / price
            if first < h.min_edge * self.costs(symbol):
                self.note = f"{symbol}: kein Einstieg (erwartete Bewegung zu klein für die Gebühren)"
                return
        if h and not stretch_ok(signal, price, anchor, atr, h.max_stretch_atr):
            self.note = f"{symbol}: warte auf Rücksetzer (Kurs zu weit von der 20er-Linie entfernt)"
            return
        if self.phase_exit and signal == -trend_of(self.phases.get(symbol)):
            self.note = f"{symbol}: kein Einstieg gegen die Marktphase «{self.phases[symbol]}»"
            return
        phase_factor, phase_why = (self.phase_book.factor(self.closed, self.phases.get(symbol), horizon)
                                   if self.phase_book else (1.0, ""))
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
        factor = size_factor * phase_factor * (self.context.size_factor() if self.context else 1.0)
        if signal < 0 and self.short_probation and not self.shorts_proven():
            factor *= PROBATION
        exposure = sum(abs(t.qty) * t.entry for t in self.open_trades.values() if not h or t.horizon == horizon)
        total = sum(abs(t.qty) * t.entry for t in self.open_trades.values())
        plan = self.risk.plan(equity, self.broker.cash(), price, atr, side=signal, size_factor=factor,
                              exposure=exposure, exposure_total=total, risk_pct=risk_pct,
                              stop_atr=h.stop_loss_atr if h else None, target_atr=h.take_profit_atr if h else None,
                              budget_share=self.shares().get(horizon, 1.0))
        if not plan:
            self.note = f"{symbol}: kein Einstieg ({self.risk.last_block})"
            return
        leveraged = getattr(self.broker, "leverage", 1.0) > 1
        # freies Cash vor dem Kauf (Margin-Anteil): Kredite offener Hebel-Longs laufen bis zu deren Schliessen weiter;
        # das Cash ist um sie schon gekürzt, und sie tragen ihre Zinsen selbst
        cash = (self.broker.cash() + sum(o.margin_value * o.qty / (o.qty + o.sold)
                                         for o in self.open_trades.values() if o.side > 0)
                if signal > 0 and leveraged else 0.0)
        fill = (self.broker.buy(symbol, plan.qty, price, market=True) if signal > 0
                else self.broker.sell(symbol, plan.qty, price, short=True, market=True))
        if fill:
            info = self.context.summary() if self.context else {}
            info["session"] = session(when)
            if self.phases.get(symbol):
                info["phase"] = self.phases[symbol]
            quote = getattr(self.broker, "quotes", {}).get(symbol)
            if quote:
                bid, ask = quote
                info["spread"] = round((ask - bid) / ((ask + bid) / 2), 5)
            info.update(extra or {})
            # Geliehener Teil (bei Kraken eine Margin-Position bis zum Schliessen): Shorts ganz, Longs mit Hebel nur,
            # was das freie Cash vor dem Kauf nicht deckte
            margin = (fill.qty * fill.price if signal < 0
                      else max(0.0, fill.qty * fill.price + fill.fee - max(cash, 0.0)) if leveraged else 0.0)
            t = self.open_trades[symbol] = OpenTrade(
                signal, fill.price, fill.qty, plan.stop, plan.target, when, info, horizon, fee=fill.fee,
                partial=fill.price + signal * h.partial_atr * atr if h and h.partial_atr else 0.0,
                partial_pct=h.partial_pct if h else 0.0,
                trail=h.trail_atr * atr if h and h.trail_atr else 0.0, best=fill.price, margin_value=margin)
            opening = self.risk.cfg.margin_open_fee * margin
            if opening > 0 and hasattr(self.broker, "book_interest"):
                self.broker.book_interest(opening)       # Margin-Eröffnungsgebühr, zählt zu den Zinsen des Trades
                t.interest += opening
            self.risk.record_open()
            self.note = (f"{symbol}: {'gekauft' if signal > 0 else 'short eröffnet'} {fill.qty:.6f} @ {fill.price:.2f}"
                         + (f" ({phase_why})" if phase_why else ""))
            log.info("%s %s %s %.6f @ %.2f (Stop %.2f, Ziel %.2f)", when, "LONG" if signal > 0 else "SHORT",
                     symbol, fill.qty, fill.price, plan.stop, plan.target)

    def check_phase(self, symbol: str, phase: str, price: float, when) -> None:
        """Neue Marktphase des Coins merken. Mit phase_exit wird eine Position geschlossen, sobald die Phase gegen
        sie kippt (Long im Abwärtstrend, Short im Aufwärtstrend): bester Ausstieg, bevor der Trend dreht."""
        self.phases[symbol] = phase
        t = self.open_trades.get(symbol)
        h = self.horizons.get(t.horizon) if t else None
        if self.phase_exit and t and t.side == -trend_of(phase) and (h is None or h.phase_exit):
            self.exit(symbol, price, "Phase gekippt", when, market=True)

    def check_stops(self, symbol: str, open_: float, high: float, low: float, when, gap_label: str = "Gap") -> None:
        """Prüft Stop-Loss/Take-Profit innerhalb einer Kerze (konservativ: Stop zuerst), danach Teilgewinn und
        Nachlauf-Stop. Ein nachgezogener Stop gilt erst ab der nächsten Kerze (kein Blick in die Zukunft).
        Eröffnet die Kerze schon jenseits des Stops, wird zu diesem Kurs geschlossen, im Grund mit gap_label:
        «Gap» = echter Kurssprung, «Ticker» = nur mit dem Kurs beim Durchlauf geprüft (open = high = low)."""
        t = self.open_trades.get(symbol)
        if not t:
            return
        s = t.side
        if s > 0:
            gap, stop_hit, target_hit = open_ <= t.stop, low <= t.stop, high >= t.target
        else:
            gap, stop_hit, target_hit = open_ >= t.stop, high >= t.stop, low <= t.target
        reason = ("Stop-Loss" if s * (t.stop - t.entry) < 0
                  else "Nachlauf-Stop" if t.trail else "Stop auf Einstand")
        if gap:
            self.exit(symbol, open_, f"{reason} ({gap_label})", when)
        elif stop_hit:
            self.exit(symbol, t.stop, reason, when)
        elif target_hit:
            self.exit(symbol, t.target, "Take-Profit", when)
        else:
            if t.partial and (high >= t.partial if s > 0 else low <= t.partial):
                self.take_partial(symbol, t.partial, when)
            if t.trail:
                t.best = max(t.best, high) if s > 0 else min(t.best, low)
                trail_stop = t.best - s * t.trail
                t.stop = max(t.stop, trail_stop) if s > 0 else min(t.stop, trail_stop)

    def _reduce(self, symbol: str, t: OpenTrade, qty: float, price: float, market: bool = False) -> bool:
        """Einen Teil der Position schliessen; das Ergebnis zählt später zum ganzen Trade."""
        if qty <= 0 or qty * price < self.risk.cfg.min_order_value:
            return False
        fill = (self.broker.sell(symbol, qty, price, market=market) if t.side > 0
                else self.broker.buy(symbol, qty, price, market=market))
        if not fill:
            return False
        t.realized += t.side * (fill.price - t.entry) * fill.qty - fill.fee - t.fee * fill.qty / (t.qty + t.sold)
        t.fees_done += fill.fee
        t.qty -= fill.qty
        t.sold += fill.qty
        t.sold_value += fill.qty * fill.price
        return True

    def take_partial(self, symbol: str, price: float, when) -> None:
        """Teilgewinn: einen Teil zum Zwischenziel verkaufen und den Stop für den Rest auf den Einstand (plus
        Kosten) ziehen. Ab dann kann der Trade insgesamt kaum noch verlieren."""
        t = self.open_trades[symbol]
        t.partial = 0.0
        if self._reduce(symbol, t, t.qty * t.partial_pct, price):
            log.info("%s TEILGEWINN %s @ %.2f", when, symbol, price)
        breakeven = t.entry * (1 + t.side * self.costs(symbol))
        t.stop = max(t.stop, breakeven) if t.side > 0 else min(t.stop, breakeven)

    def _longer(self, a: str, b: str) -> bool:
        """Hat Horizont a längere Kerzen als Horizont b?"""
        ha, hb = self.horizons.get(a), self.horizons.get(b)
        return bool(ha and hb) and MINUTES.get(ha.timeframe, 0) > MINUTES.get(hb.timeframe, 0)

    def _take_over(self, symbol: str, t: OpenTrade, horizon: str, price: float, atr: float, equity: float) -> None:
        """Ein längerer Horizont übernimmt eine gleichgerichtete Position eines kürzeren: ab jetzt gelten seine
        Stops und seine Grösse (höchstens die vorhandene Menge, ein Überschuss wird verkauft)."""
        h = self.horizons[horizon]
        others = sum(abs(o.qty) * o.entry for s, o in self.open_trades.items() if o.horizon == horizon and s != symbol)
        total = sum(abs(o.qty) * o.entry for s, o in self.open_trades.items() if s != symbol)
        cash = self.broker.cash() + (t.qty * price if t.side > 0 else 0.0)
        plan = self.risk.plan(equity, cash, price, atr, side=t.side, exposure=others, exposure_total=total,
                              risk_pct=h.risk_per_trade, stop_atr=h.stop_loss_atr, target_atr=h.take_profit_atr,
                              budget_share=self.shares().get(horizon, 1.0))
        if not plan:
            self.note = f"{symbol}: Position gehört zum Horizont «{t.horizon}» ({self.risk.last_block})"
            return
        if plan.qty < t.qty:
            self._reduce(symbol, t, t.qty - plan.qty, price, market=True)
        t.horizon, t.stop, t.target, t.best = horizon, plan.stop, plan.target, price
        t.partial = price + t.side * h.partial_atr * atr if h.partial_atr else 0.0
        t.partial_pct = h.partial_pct
        t.trail = h.trail_atr * atr if h.trail_atr else 0.0
        self.note = f"{symbol}: Position vom Horizont «{horizon}» übernommen"

    def _exit_equity(self, symbol: str, price: float, reason: str, when, equity: float) -> float:
        """Position schliessen und das Kapital danach zurückgeben. `equity` bewertet schon alle Positionen zum
        aktuellen Kurs; der Ausstieg ändert es nur um seine Kosten (Gebühr, Slippage). Nicht aus Cash plus diesem
        Coin neu rechnen: dann fehlen die anderen Coins, und mit Shorts oder Hebel steckt geliehenes Geld im Cash."""
        t, cash = self.open_trades[symbol], self.broker.cash()
        side, qty = t.side, t.qty
        self.exit(symbol, price, reason, when, market=True)
        return equity + self.broker.cash() - cash - side * qty * price

    def exit(self, symbol: str, price: float, reason: str, when, market: bool = False) -> None:
        """Position schliessen. market=True: Market-Order (zum Geld- bzw. Briefkurs), sonst zum Kurs `price`
        (Stop, Ziel) plus/minus Slippage."""
        t = self.open_trades.pop(symbol)
        fill = (self.broker.sell(symbol, t.qty, price, market=market) if t.side > 0
                else self.broker.buy(symbol, t.qty, price, market=market))
        if not fill:
            return
        total = t.qty + t.sold
        # Ergebnis des ganzen Trades nach allen Gebühren: Rest + schon verkaufte Teile - anteilige Kaufgebühr
        pnl = (t.side * (fill.price - t.entry) * fill.qty - fill.fee - t.fee * fill.qty / total + t.realized
               - t.interest)
        exit_price = (fill.price * fill.qty + t.sold_value) / (fill.qty + t.sold)
        # fees: ganze Kaufgebühr + alle Verkaufsgebühren, interest: Zinsen; pnl = Kursgewinn - fees - interest
        self.closed.append(dict(symbol=symbol, side="long" if t.side > 0 else "short", opened=t.opened,
                                closed=when, entry=t.entry, exit=exit_price, qty=fill.qty + t.sold, pnl=pnl,
                                fees=t.fee + t.fees_done + fill.fee, interest=t.interest,
                                reason=reason, horizon=t.horizon, partial=t.sold > 0, **t.context))
        self.risk.record_close(pnl, when)
        log.info("%s SCHLIESSEN %s @ %.2f (%s) PnL %.2f", when, symbol, fill.price, reason, pnl)

    def close_all(self, prices: dict[str, float], reason: str, when) -> None:
        """Alles mit Market-Orders schliessen (Not-Aus, Zwangsschliessung). Bei der Zwangsschliessung verlangt die
        Börse statt der Handelsgebühr die Liquidationsgebühr (Kraken: 2 % des Positionswerts), aber nur für
        Margin-Positionen: Shorts ganz, Longs für den geliehenen Teil (margin_value); was mit eigenem Cash gekauft ist,
        zahlt beim Verkauf die normale Gebühr. Ein Coin ohne Kurs (Ticker ausgefallen) bleibt offen, bis der nächste
        Lauf einen Kurs hat: keine Order zu einem alten Kurs."""
        liquidation = reason == "Liquidation" and hasattr(self.broker, "fee_override")
        for s in list(self.open_trades):
            if s not in prices:
                log.warning("%s: kein Kurs, %s erst im nächsten Lauf", s, reason)
                continue
            if liquidation:     # Anteil der Margin-Position; fee(s) noch ohne Override: Stufe plus Zusatzkosten
                t = self.open_trades[s]
                w = 1.0 if t.side < 0 else min(1.0, t.margin_value / ((t.qty + t.sold) * t.entry))
                self.broker.fee_override = w * LIQUIDATION_FEE + (1 - w) * self.broker.fee(s)
            try:
                self.exit(s, prices[s], reason, when, market=True)
            finally:
                if liquidation:
                    self.broker.fee_override = None


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
