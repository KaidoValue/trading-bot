"""Marktphase je Coin und welcher Zeithorizont in welcher Phase verdient.

Der Bot bestimmt für jeden Coin aus den Tageskerzen die Marktphase: Aufwärtstrend, Abwärtstrend oder Seitwärts
(50- und 200-Tage-Linie), jeweils ruhig oder wild (Schwankung gegenüber den letzten 100 Tagen).

Danach entscheidet er selbst, welcher Horizont (kurz, mittel, lang) in dieser Phase handeln darf: Er schaut,
was die Trades jedes Horizonts in genau dieser Phase gebracht haben (Vorwissen aus der Geschichte plus eigene
Trades). Ein Horizont, der in der Phase bewiesen Geld verdient, handelt mit voller Grösse. Einer, der verliert
oder noch zu wenig Erfahrung hat, handelt nur klein weiter (Probezeit), damit der Bot weiter lernt, ob sich das
ändert. Alles nur aus der Vergangenheit (kein Blick in die Zukunft).
"""
from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from . import indicators as ind

TREND = {1: "Aufwärtstrend", -1: "Abwärtstrend", 0: "Seitwärts"}
MIN_TRADES = 8          # so viele Trades braucht ein Horizont in einer Phase, bevor er voll handeln darf
RECENT = 30             # nur die letzten so vielen eigenen Trades je Phase und Horizont zählen
PRIOR_WEIGHT = 20       # Vorwissen aus der Geschichte zählt höchstens wie so viele eigene Trades


def coin_phases(daily: pd.DataFrame) -> pd.Series:
    """Marktphase je Tageskerze, z.B. «Aufwärtstrend, ruhig». Gilt ab Schluss der Kerze.
    Aufwärtstrend: Kurs über der 200-Tage-Linie und 50er über 200er. Abwärtstrend: beides darunter.
    Alles dazwischen (auch die ersten 200 Tage) ist Seitwärts bzw. Übergang."""
    close = daily["close"]
    ma50, ma200 = ind.sma(close, 50), ind.sma(close, 200)
    trend = pd.Series(0, index=daily.index)
    trend[(close > ma200) & (ma50 > ma200)] = 1
    trend[(close < ma200) & (ma50 < ma200)] = -1
    vol = ind.atr(daily) / close
    wild = vol > vol.rolling(100, min_periods=20).median()
    return trend.map(TREND) + wild.map({True: ", wild", False: ", ruhig"})


def trend_of(phase: str | None) -> int:
    """+1 Aufwärtstrend, -1 Abwärtstrend, 0 sonst."""
    if not phase:
        return 0
    return 1 if phase.startswith("Aufwärts") else -1 if phase.startswith("Abwärts") else 0


def trade_return(t: dict) -> float:
    """Ergebnis eines Trades im Verhältnis zum Einsatz (unabhängig davon, wie gross das Konto gerade ist)."""
    value = abs(float(t.get("entry") or 0) * float(t.get("qty") or 0))
    return float(t["pnl"]) / value if value else 0.0


class PhaseBook:
    """Was hat jeder Horizont in jeder Phase gebracht? Vorwissen (aus der Geschichts-Simulation) plus eigene Trades."""

    def __init__(self, prior: dict | None = None, probation: float = 0.25):
        self.prior = prior or {}            # "Phase|Horizont" -> [Summe der Trade-Renditen, Anzahl]
        self.probation = probation

    @classmethod
    def load(cls, path: str | Path | None, probation: float = 0.25) -> "PhaseBook":
        p = Path(path) if path else None
        prior = json.loads(p.read_text()).get("stats", {}) if p and p.exists() else {}
        return cls(prior, probation)

    @staticmethod
    def summarize(trades: list[dict]) -> dict:
        """Trades zu Vorwissen zusammenfassen (für die Datei, die der laufende Bot lädt)."""
        out: dict[str, list] = {}
        for t in trades:
            if t.get("phase"):
                b = out.setdefault(f"{t['phase']}|{t.get('horizon', '')}", [0.0, 0])
                b[0] += trade_return(t)
                b[1] += 1
        return out

    def record(self, closed: list[dict], phase: str, horizon: str) -> tuple[float, float]:
        """Durchschnittliche Trade-Rendite und Erfahrung (Anzahl, Vorwissen gedeckelt) in dieser Phase."""
        own = [trade_return(t) for t in closed if t.get("phase") == phase and t.get("horizon", "") == horizon][-RECENT:]
        s, n = self.prior.get(f"{phase}|{horizon}", (0.0, 0))
        w = min(1.0, PRIOR_WEIGHT / n) if n else 0.0
        total, count = s * w + sum(own), n * w + len(own)
        return (total / count if count else 0.0), count

    def factor(self, closed: list[dict], phase: str | None, horizon: str) -> tuple[float, str]:
        """Grössenfaktor für einen neuen Trade und die Begründung in Worten."""
        if not phase:
            return 1.0, ""
        avg, n = self.record(closed, phase, horizon)
        if n < MIN_TRADES:
            return self.probation, f"Probezeit, erst {n:.0f} Trades in der Phase «{phase}»"
        if avg <= 0:
            return self.probation, f"klein, verliert in der Phase «{phase}» ({avg * 100:+.2f} % pro Trade)"
        return 1.0, f"voll, verdient in der Phase «{phase}» ({avg * 100:+.2f} % pro Trade)"

    def table(self, closed: list[dict], horizons: list[str]) -> dict[str, dict[str, str]]:
        """Übersicht Phase × Horizont für die Anzeige."""
        phases = sorted({k.split("|")[0] for k in self.prior} | {t["phase"] for t in closed if t.get("phase")})
        out = {}
        for p in phases:
            row = {}
            for h in horizons:
                avg, n = self.record(closed, p, h)
                row[h] = "–" if not n else f"{avg * 100:+.2f} % ({n:.0f})"
            out[p] = row
        return out


def stretch_ok(side: int, price: float, anchor: float | None, atr: float, max_atr: float | None) -> bool:
    """Bester Einstieg: nicht hinterherlaufen. Long nur, wenn der Kurs höchstens `max_atr` × ATR über der
    20er-Linie liegt (Rücksetzer abwarten), Short spiegelbildlich."""
    if not max_atr or anchor is None or not atr or np.isnan(anchor):
        return True
    return side * (price - anchor) <= max_atr * atr
