"""Broker-Adapter. PaperBroker simuliert Orders, CCXTBroker handelt echt über eine Krypto-Börse."""
from __future__ import annotations

import logging
from dataclasses import dataclass

log = logging.getLogger(__name__)


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
    def buy(self, symbol: str, qty: float, price: float) -> Fill | None: ...
    def sell(self, symbol: str, qty: float, price: float, short: bool = False) -> Fill | None: ...


class PaperBroker(Broker):
    """Simulierter Handel mit Gebühren und Slippage. Kein echtes Geld."""

    def __init__(self, cash: float, fee_rate: float, slippage: float):
        self._cash = cash
        self.fee_rate = fee_rate
        self.slippage = slippage
        self.positions: dict[str, float] = {}
        self.extra_fee: dict[str, float] = {}     # Zusatzkosten je Coin, z.B. Umtausch CHF -> USD
        self.leverage = 1.0                       # > 1: Cash darf negativ werden (geliehenes Geld, nur Demo)
        self.interest_paid = 0.0
        self.interest_at = None                   # Zeitpunkt der letzten Zinsabrechnung

    def cash(self):
        return self._cash

    def fee(self, symbol):
        return self.fee_rate + self.extra_fee.get(symbol, 0.0)

    def position(self, symbol):
        return self.positions.get(symbol, 0.0)

    def buy(self, symbol, qty, price):
        px = price * (1 + self.slippage)
        fee = qty * px * self.fee(symbol)
        if self.leverage <= 1 and self.position(symbol) >= 0 and qty * px + fee > self._cash:
            qty = self._cash / (px * (1 + self.fee(symbol)))
            fee = qty * px * self.fee(symbol)
        if qty <= 0:
            return None
        self._cash -= qty * px + fee
        self.positions[symbol] = self.position(symbol) + qty
        return Fill(symbol, "buy", qty, px, fee)

    def borrowed(self, prices: dict[str, float]) -> float:
        """Geliehener Betrag: negatives Cash (Kauf mit Hebel) plus Wert der leerverkauften Coins (Short)."""
        return max(0.0, -self._cash) + sum(-q * prices[s] for s, q in self.positions.items() if q < 0 and s in prices)

    def charge_interest(self, prices: dict[str, float], hours: float, rate_per_day: float) -> float:
        fee = self.borrowed(prices) * rate_per_day * max(hours, 0.0) / 24
        self._cash -= fee
        self.interest_paid += fee
        return fee

    def sell(self, symbol, qty, price, short=False):
        """Verkauft Bestand. Mit short=True wird leerverkauft (Position wird negativ)."""
        if not short:
            qty = min(qty, self.position(symbol))
        if qty <= 0:
            return None
        px = price * (1 - self.slippage)
        fee = qty * px * self.fee(symbol)
        self._cash += qty * px - fee
        self.positions[symbol] = self.position(symbol) - qty
        return Fill(symbol, "sell", qty, px, fee)


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

    def buy(self, symbol, qty, price):
        return self._order("buy", symbol, qty)

    def sell(self, symbol, qty, price, short=False):
        if short:
            raise NotImplementedError("Short-Handel ist live noch nicht umgesetzt (braucht Margin/Futures-Konto).")
        return self._order("sell", symbol, min(qty, self.position(symbol)))
