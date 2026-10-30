"""Broker-Adapter. PaperBroker simuliert Orders, CCXTBroker handelt echt über eine Krypto-Börse."""
from __future__ import annotations

import logging
from bisect import bisect_right
from collections import deque
from dataclasses import dataclass
from datetime import timedelta

log = logging.getLogger(__name__)

# Kraken-Gebührenstaffel Spot (seit 9.7.2026): ab 30-Tage-Umsatz in USD, Maker, Taker
KRAKEN_TIERS = [(0, 0.0040, 0.0080), (2_500, 0.0030, 0.0060), (10_000, 0.0022, 0.0038), (25_000, 0.0020, 0.0035),
                (50_000, 0.0015, 0.0030), (100_000, 0.0012, 0.0025), (250_000, 0.0010, 0.0022),
                (500_000, 0.0008, 0.0020), (1_000_000, 0.0006, 0.0018), (2_500_000, 0.0004, 0.0015),
                (5_000_000, 0.0002, 0.0012), (10_000_000, 0.0, 0.0010)]
LIQUIDATION_FEE = 0.02          # Zwangsschliessung: 2 % des Positionswerts statt der Handelsgebühr (Kraken)
WINDOW = timedelta(days=30)     # die Gebührenstufe richtet sich nach dem Umsatz der letzten 30 Tage


@dataclass
class Fill:
    symbol: str
    side: str
    qty: float
    price: float
    fee: float


class Broker:
    def cash(self) -> float: ...
    def position(self, symbol: str) -> float: ...
    def buy(self, symbol: str, qty: float, price: float, market: bool = False) -> Fill | None: ...
    def sell(self, symbol: str, qty: float, price: float, short: bool = False, market: bool = False) -> Fill | None: ...


class PaperBroker(Broker):
    """Simulierter Handel mit Gebühren, Geld-/Briefkurs bzw. Slippage und Margin-Kosten. Kein echtes Geld.
    tiers: Gebührenstaffel nach 30-Tage-Umsatz (z.B. KRAKEN_TIERS); None = immer fee_rate (Tests, Backtest)."""

    def __init__(self, cash: float, fee_rate: float, slippage: float, tiers: list | None = None):
        self._cash = cash
        self.fee_rate = fee_rate
        self.slippage = slippage
        self.tiers = tiers
        self.positions: dict[str, float] = {}
        self.extra_fee: dict[str, float] = {}     # Zusatzkosten je Coin
        self.fee_override: float | None = None    # Satz statt der Handelsgebühr (Zwangsschliessung)
        self.leverage = 1.0                       # > 1: Cash darf negativ werden (geliehenes Geld, nur Demo)
        self.interest_paid = 0.0                  # Zinsen und Margin-Gebühren
        self.interest_at = None                   # Zeitpunkt der letzten Zinsabrechnung
        self.now = None                           # aktuelle Zeit, setzt der Bot bzw. die Simulation
        self.quote_usd = 1.0                      # Wert einer Einheit der Kontowährung in USD (Staffel in USD)
        self.quotes: dict[str, tuple[float, float]] = {}   # Geld- und Briefkurs je Coin für Market-Orders
        self.volume_log: deque = deque()          # Fills der letzten 30 Tage: (Zeit, Betrag in Kontowährung)
        self.volume = 0.0                         # Summe davon

    def cash(self):
        return self._cash

    def tier(self) -> tuple[int, float, float, float]:
        """Gebührenstufe nach dem Umsatz der letzten 30 Tage: (Stufe, Maker, Taker, Umsatz in Kontowährung).
        Stufe 1 ist die teuerste; ohne Staffel (fester Satz) Stufe 0."""
        self._prune()
        if not self.tiers:
            return 0, self.fee_rate, self.fee_rate, self.volume
        stufe = max(bisect_right([t[0] for t in self.tiers], self.volume * self.quote_usd), 1)
        _, maker, taker = self.tiers[stufe - 1]
        return stufe, maker, taker, self.volume

    def fee(self, symbol):
        """Satz für die nächste Order: Market-Orders zahlen die Taker-Gebühr der Stufe, die der Umsatz vor der Order
        erreicht hat (bzw. den festen Satz), plus allfällige Zusatzkosten des Coins."""
        if self.fee_override is not None:
            return self.fee_override
        return self.tier()[2] + self.extra_fee.get(symbol, 0.0)

    def load_volume(self, fills) -> None:
        """Umsatz-Protokoll übernehmen: [(Zeit, Betrag), ...], ältester Fill zuerst."""
        self.volume_log = deque((t, float(v)) for t, v in fills)
        self.volume = sum(v for _, v in self.volume_log)

    def _record(self, notional: float) -> None:
        self.volume_log.append((self.now, notional))
        self.volume += notional

    def _prune(self) -> None:
        """Fills, die mehr als 30 Tage vor `now` liegen, fallen aus dem Umsatz (ohne `now` bleibt alles)."""
        if self.now is None:
            return
        cutoff, fills = self.now - WINDOW, self.volume_log
        while fills and fills[0][0] is not None and fills[0][0] < cutoff:
            self.volume -= fills.popleft()[1]
        if not fills:
            self.volume = 0.0

    def _price(self, symbol: str, price: float, side: int, market: bool) -> float:
        """Ausführungskurs: Market-Order zum Brief- (Kauf) bzw. Geldkurs (Verkauf), wenn einer bekannt ist; sonst
        (Stop, Ziel, Teilgewinn, Geschichts-Simulation) zum verlangten Kurs plus/minus Slippage."""
        quote = self.quotes.get(symbol) if market else None
        if quote:
            return quote[1] if side > 0 else quote[0]
        return price * (1 + side * self.slippage)

    def position(self, symbol):
        return self.positions.get(symbol, 0.0)

    def buy(self, symbol, qty, price, market=False):
        px, rate = self._price(symbol, price, 1, market), self.fee(symbol)
        if self.leverage <= 1 and self.position(symbol) >= 0 and qty * px * (1 + rate) > self._cash:
            qty = self._cash / (px * (1 + rate))
        if qty <= 0:
            return None
        fee = qty * px * rate
        self._cash -= qty * px + fee
        self.positions[symbol] = self.position(symbol) + qty
        self._record(qty * px)
        return Fill(symbol, "buy", qty, px, fee)

    def book_interest(self, amount: float) -> None:
        """Margin-Kosten (Eröffnungsgebühr, Rollover-Zinsen) vom Cash abbuchen; sie zählen zu interest_paid."""
        self._cash -= amount
        self.interest_paid += amount

    def sell(self, symbol, qty, price, short=False, market=False):
        """Verkauft Bestand. Mit short=True wird leerverkauft (Position wird negativ)."""
        if not short:
            qty = min(qty, self.position(symbol))
        if qty <= 0:
            return None
        px = self._price(symbol, price, -1, market)
        fee = qty * px * self.fee(symbol)
        self._cash += qty * px - fee
        self.positions[symbol] = self.position(symbol) - qty
        self._record(qty * px)
        return Fill(symbol, "sell", qty, px, fee)


def paper_broker(cfg) -> PaperBroker:
    """Demo-Konto nach der Config, überall gleich gebaut (Bot, Simulation, Übersicht, Befehle):
    fee_model «kraken» = Kraken-Gebührenstaffel nach 30-Tage-Umsatz, «fix» = immer fee_rate."""
    if cfg.fee_model not in ("fix", "kraken"):
        raise ValueError(f"Unbekanntes fee_model «{cfg.fee_model}» (erlaubt: fix, kraken)")
    b = PaperBroker(cfg.starting_capital, cfg.fee_rate, cfg.slippage,
                    KRAKEN_TIERS if cfg.fee_model == "kraken" else None)
    b.leverage = cfg.risk.leverage
    return b


class CCXTBroker(Broker):
    """Echter Handel über ccxt (Kraken, Bitstamp, Binance, ...). Nur Spot, nur Market-Orders."""

    def __init__(self, exchange, quote_currency: str):
        self.ex = exchange
        self.quote = quote_currency

    def _balance(self):
        return self.ex.fetch_balance()["free"]

    def cash(self):
        return float(self._balance().get(self.quote, 0.0))

    def position(self, symbol):
        return float(self._balance().get(symbol.split("/")[0], 0.0))

    def _order(self, side, symbol, qty):
        qty = float(self.ex.amount_to_precision(symbol, qty))
        if qty <= 0:
            return None
        o = self.ex.create_order(symbol, "market", side, qty)
        price = float(o.get("average") or o.get("price") or 0)
        fee = float((o.get("fee") or {}).get("cost") or 0)
        log.warning("ECHTE ORDER: %s %s %s @ %s", side, qty, symbol, price)
        return Fill(symbol, side, float(o.get("filled") or qty), price, fee)

    # market: hier ohne Wirkung, echte Orders sind immer Market-Orders
    def buy(self, symbol, qty, price, market=False):
        return self._order("buy", symbol, qty)

    def sell(self, symbol, qty, price, short=False, market=False):
        if short:
            raise NotImplementedError("Short-Handel ist live noch nicht umgesetzt (braucht Margin/Futures-Konto).")
        return self._order("sell", symbol, min(qty, self.position(symbol)))
