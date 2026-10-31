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

    def can_open(self, equity: float, when=None, open_risk: float = 0.0, n_open: int = 0,
                 risk_pct: float | None = None) -> bool:
        risk_pct = self.cfg.risk_per_trade if risk_pct is None else risk_pct
        checks = [
            (self.halted, "Not-Aus"),
            (equity < self.day_start_equity * (1 - self.cfg.max_daily_loss_pct), "Tagesverlust-Limit"),
            (self.trades_today >= self.cfg.max_trades_per_day, "max. Trades pro Tag"),
            (n_open >= self.cfg.max_open_positions, "max. offene Positionen"),
            (open_risk + risk_pct > self.cfg.max_total_risk_pct + 1e-9, "Gesamtrisiko"),
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
             size_factor: float = 1.0, exposure: float | None = None, stop_atr: float | None = None,
             target_atr: float | None = None, risk_pct: float | None = None,
             budget_share: float = 1.0, exposure_total: float | None = None) -> TradePlan | None:
        """side = +1 long (auf steigende Kurse), -1 short (auf fallende Kurse).
        Chance-Risiko-Verhältnis (CRV) = take_profit_atr / stop_loss_atr, standardmässig 2:1.
        stop_atr/target_atr/risk_pct überschreiben die Werte aus der Config (je Zeithorizont), budget_share
        ist der Anteil des Horizonts an max_invested_pct (exposure dann nur die Positionen dieses Horizonts).
        exposure_total: alle offenen Positionen aller Horizonte; zusammen nie mehr als max_invested_pct × Hebel,
        auch wenn ein Horizont mehr hält, als sein Anteil heute erlaubt (Anteile wandern, Übernahmen)."""
        if atr <= 0 or price <= 0:
            return None
        stop_dist = (self.cfg.stop_loss_atr if stop_atr is None else stop_atr) * atr
        target_dist = (self.cfg.take_profit_atr if target_atr is None else target_atr) * atr
        risk_pct = self.cfg.risk_per_trade if risk_pct is None else risk_pct
        qty = (equity * risk_pct * size_factor) / stop_dist
        lev = self.cfg.leverage                     # mit Hebel darf die Position grösser als das Kapital sein
        qty = min(qty, equity * self.cfg.max_position_pct * lev / price)
        if side > 0:
            qty = min(qty, (cash + equity * (lev - 1)) * 0.99 / price)
        # Obergrenze für alle offenen Positionen zusammen (long und short), mit Hebel entsprechend höher
        if exposure is None:
            exposure = max(equity - cash, 0.0)
        room = equity * self.cfg.max_invested_pct * lev * budget_share - exposure
        if exposure_total is not None:
            room = min(room, equity * self.cfg.max_invested_pct * lev - exposure_total)
        qty = min(qty, max(room, 0.0) / price)
        if qty * price < self.cfg.min_order_value:
            self.last_block = ("Obergrenze für investiertes Kapital erreicht" if room < self.cfg.min_order_value
                               else "Order kleiner als Mindestgrösse")
            return None
        return TradePlan(qty=qty, stop=price - side * stop_dist, target=price + side * target_dist)
