"""KI-Gedächtnis: merkt sich dauerhaft, welche Strategie in welcher Marktphase funktioniert.

Die normale lernende Strategie (adaptive) schaut nur auf die letzten Wochen und vergisst alles davor.
Das Gedächtnis sammelt dagegen über die ganze Laufzeit: Für jede Marktphase (z.B. "Aufwärtstrend, ruhig")
und jede Strategie wird aufsummiert, wie viel sie in dieser Phase gebracht hätte. Je mehr Stunden Erfahrung
das Gedächtnis hat, desto stärker verlässt sich der Bot darauf. So wird er mit der Zeit klüger, statt
nur dem kurzfristigen Trend hinterherzulaufen.

Alles wird nur aus vergangenen Kursen gelernt (kein Blick in die Zukunft).
"""
from __future__ import annotations

import json
from pathlib import Path

import pandas as pd

from . import indicators as ind

TREND = {1: "Aufwärtstrend", -1: "Abwärtstrend", 0: "Seitwärts"}


def phases(df: pd.DataFrame, trend_period: int = 100) -> pd.Series:
    """Marktphase je Kerze: Trendrichtung (Kurs gegenüber dem Durchschnitt) und Schwankung (ruhig / wild)."""
    ma = ind.sma(df["close"], trend_period).fillna(df["close"].expanding().mean())
    trend = pd.Series(0, index=df.index)
    trend[df["close"] > ma * 1.01] = 1
    trend[df["close"] < ma * 0.99] = -1
    vol = ind.atr(df) / df["close"]
    wild = vol > vol.rolling(trend_period, min_periods=20).median()
    return trend.map(TREND) + wild.map({True: ", wild", False: ", ruhig"})


class Memory:
    """Summe der Rendite pro Kerze und Anzahl Kerzen, je Marktphase und Strategie. Wird als JSON gespeichert."""

    def __init__(self, path: str | Path | None = None):
        self.path = Path(path) if path else None
        self.stats: dict[str, dict[str, list[float]]] = {}     # phase -> strategie -> [summe, anzahl]
        self.seen: dict[str, str] = {}                          # symbol -> letzte gelernte Kerze
        self.pretrained = False
        if self.path and self.path.exists():
            raw = json.loads(self.path.read_text())
            self.stats, self.seen = raw.get("stats", {}), raw.get("seen", {})
            self.pretrained = raw.get("pretrained", False)

    def save(self) -> None:
        if not self.path:
            return
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({"stats": self.stats, "seen": self.seen, "pretrained": self.pretrained},
                                        indent=1))

    def learn(self, pnl: pd.DataFrame, phase: pd.Series, key: str | None = None) -> int:
        """Nimmt neue Kerzen ins Gedächtnis auf. Mit `key` (z.B. dem Coin) wird jede Kerze nur einmal gelernt."""
        if key and key in self.seen:
            new = pnl.index > pd.Timestamp(self.seen[key])
            pnl, phase = pnl[new], phase[new]
        if pnl.empty:
            return 0
        for p, rows in pnl.groupby(phase):
            bucket = self.stats.setdefault(p, {})
            for s in pnl.columns:
                b = bucket.setdefault(s, [0.0, 0])
                b[0] += float(rows[s].sum())
                b[1] += int(len(rows))
        if key:
            self.seen[key] = pnl.index[-1].isoformat()
        return len(pnl)

    def prior(self, phase: str, strategy: str) -> tuple[float, int]:
        return tuple(self.stats.get(phase, {}).get(strategy, (0.0, 0)))

    def experience(self) -> int:
        """Anzahl gelernter Kerzen (Stunden bei 1-Stunden-Kerzen)."""
        return sum(max(v[1] for v in b.values()) for b in self.stats.values() if b)

    def best(self, phase: str, top: int = 3) -> list[tuple[str, float]]:
        """Die Strategien mit dem besten Durchschnitt in dieser Phase (Rendite pro Kerze in %)."""
        rows = [(s, v[0] / v[1] * 100) for s, v in self.stats.get(phase, {}).items() if v[1]]
        return sorted(rows, key=lambda r: -r[1])[:top]
