"""Risikomanagement: Positionsgrösse, Stops, Limits und Not-Aus. Jede Order läuft hier durch.

Die Regeln gegen Overtrading und Verlustserien ersetzen beim Bot das, was beim Menschen Disziplin ist:
Er kann nicht aus Frust (Revenge Trading) oder Angst etwas zu verpassen (FOMO) zusätzliche Trades eröffnen.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta

from .config import RiskConfig


@dataclass
class TradePlan:
    qty: float
    stop: float
    target: float


class RiskManager:
    def __init__(self, cfg: RiskConfig, starting_equity: float):
        self.cfg = cfg
        self.peak_equity = starting_equity
        self.day = None
        self.day_start_equity = starting_equity
        self.trades_today = 0
        self.loss_streak = 0
        self.paused_until = None
        self.halted = False          # Not-Aus: bleibt aktiv bis manueller Neustart (oder halt_days)
        self.halted_on = None
        self.halt_reason = ""
        self.last_block = ""         # warum zuletzt kein Trade eröffnet wurde

    def update(self, equity: float, day) -> None:
        if day != self.day:
            self.day, self.day_start_equity, self.trades_today = day, equity, 0
        if self.halted and self.cfg.halt_days and isinstance(day, date) and \
                day >= self.halted_on + timedelta(days=self.cfg.halt_days):
            self.halted, self.peak_equity = False, equity      # Pause vorbei, neuer Höchststand
        self.peak_equity = max(self.peak_equity, equity)
        if not self.halted and equity < self.peak_equity * (1 - self.cfg.max_drawdown_pct):
            self.halted, self.halted_on = True, day
            self.halt_reason = f"Max. Drawdown {self.cfg.max_drawdown_pct:.0%} erreicht"

    def can_open(self, equity: float, when=None, open_risk: float = 0.0, n_open: int = 0) -> bool:
        checks = [
            (self.halted, "Not-Aus"),
            (equity < self.day_start_equity * (1 - self.cfg.max_daily_loss_pct), "Tagesverlust-Limit"),
            (self.trades_today >= self.cfg.max_trades_per_day, "max. Trades pro Tag"),
            (n_open >= self.cfg.max_open_positions, "max. offene Positionen"),
            (open_risk + self.cfg.risk_per_trade > self.cfg.max_total_risk_pct + 1e-9, "Gesamtrisiko"),
            (self.paused_until is not None and isinstance(when, datetime) and when < self.paused_until,
             "Pause nach Verlustserie"),
        ]
        for blocked, reason in checks:
            if blocked:
                self.last_block = reason
                return False
        return True

    def record_open(self) -> None:
        self.trades_today += 1

    def record_close(self, pnl: float, when=None) -> None:
        self.loss_streak = self.loss_streak + 1 if pnl < 0 else 0
        if self.loss_streak >= self.cfg.loss_streak_pause and isinstance(when, datetime):
            self.paused_until = when + timedelta(hours=self.cfg.pause_hours)
            self.loss_streak = 0

    def plan(self, equity: float, cash: float, price: float, atr: float, side: int = 1,
             size_factor: float = 1.0) -> TradePlan | None:
        """side = +1 long (auf steigende Kurse), -1 short (auf fallende Kurse).
        Chance-Risiko-Verhältnis (CRV) = take_profit_atr / stop_loss_atr, standardmässig 2:1."""
        if atr <= 0 or price <= 0:
            return None
        stop_dist = self.cfg.stop_loss_atr * atr
        qty = (equity * self.cfg.risk_per_trade * size_factor) / stop_dist
        qty = min(qty, equity * self.cfg.max_position_pct / price)
        if side > 0:
            qty = min(qty, cash * 0.99 / price)
            room = equity * self.cfg.max_invested_pct - (equity - cash)    # noch freier Platz bis zur Obergrenze
            qty = min(qty, max(room, 0.0) / price)
        if qty * price < self.cfg.min_order_value:
            self.last_block = "Order kleiner als Mindestgrösse"
            return None
        return TradePlan(qty=qty, stop=price - side * stop_dist, target=price + side * self.cfg.take_profit_atr * atr)
