"""Chef-Bot: verteilt sein eigenes Kapital selbstständig auf die drei Handelsstile der anderen Bots.

Er handelt nicht selbst, sondern legt sein Geld anteilig in die Stile Langfrist, KI (Daytrading) und Risiko
(Hebel) an, so als hätte er Anteile an diesen drei Bots. Sein Kapital entwickelt sich also mit deren Ergebnis,
gewichtet nach seiner Verteilung. Bei jedem Lauf entscheidet er neu:

- Wie lief jeder Stil in den letzten 7 Tagen?
- Was weiss sein Gedächtnis: Welcher Stil hat in der aktuellen Marktphase bisher am meisten gebracht?
- Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash; ist er mehr als 10 % im Minus,
  halbiert er den Risiko-Anteil. Laufen alle Stile schlecht, bleibt mehr in Cash.
- Notbremse: Verliert ein Stil in den letzten 3 Stunden mehr als 3 %, zieht er sofort fast alles aus diesem
  Stil ab, ohne auf den 7-Tage-Schnitt zu warten. Erst wenn sich der Stil wieder fängt, darf er zurück.
- Umschichten kostet Gebühren, deshalb nur, wenn sich ein Anteil um mehr als 5 Prozentpunkte ändert.
"""
from __future__ import annotations

import json
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd

from .memory import Memory

STYLES = {"config_langfrist": "Langfrist", "config_daytrading": "KI", "config_risiko": "Risiko"}
DEFAULT = {"config_langfrist": 0.5, "config_daytrading": 0.25, "config_risiko": 0.1}
MAX_RISK, MIN_CASH, MIN_CHANGE, FEE = 0.20, 0.10, 0.05, 0.0026
BRAKE_HOURS, BRAKE_LOSS = 3, -0.03


class Chef:
    def __init__(self, path: str | Path, capital: float = 1000.0):
        self.path = Path(path)
        raw = json.loads(self.path.read_text()) if self.path.exists() else {}
        self.start = raw.get("start", capital)
        self.equity = raw.get("equity", capital)
        self.peak = raw.get("peak", self.equity)
        self.weights: dict[str, float] = raw.get("weights", dict(DEFAULT))
        self.last: dict[str, float] = raw.get("last", {})            # Kapital der Stil-Bots beim letzten Lauf
        self.history: list[dict] = raw.get("history", [])
        self.fees = raw.get("fees", 0.0)
        self.reason = raw.get("reason", "Startverteilung")
        self.memory = Memory(self.path.with_name("chef_gedaechtnis.json"))

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps({"start": self.start, "equity": self.equity, "peak": self.peak,
                                         "weights": self.weights, "last": self.last, "history": self.history[-2000:],
                                         "fees": self.fees, "reason": self.reason}, indent=1))
        self.memory.save()

    def _recent(self, style: str, now: datetime, days: float = 7) -> float:
        """Rendite eines Stils in den letzten Tagen (aus der eigenen Aufzeichnung)."""
        since = now - timedelta(days=days)
        rows = [h for h in self.history if datetime.fromisoformat(h["t"]) >= since and style in h["r"]]
        total = 1.0
        for h in rows:
            total *= 1 + h["r"][style]
        return total - 1

    def target(self, phase: str, now: datetime) -> tuple[dict[str, float], str]:
        """Neue Wunsch-Verteilung und die Begründung in Worten."""
        scores, why = {}, []
        for s in DEFAULT:
            recent = self._recent(s, now)
            total, n = self.memory.prior(phase, s)
            trust = n / (n + 300)                     # je mehr Erfahrung in dieser Phase, desto mehr zählt sie
            remembered = (total / n * 48 * 7) if n else 0.0          # auf 7 Tage hochgerechnet (48 Läufe/Tag)
            scores[s] = (1 - trust) * recent + trust * remembered
            why.append(f"{STYLES[s]} {scores[s] * 100:+.1f} %")
        w = {s: DEFAULT[s] * min(max(1 + scores[s] * 10, 0.1), 2.5) for s in DEFAULT}
        for s in DEFAULT:
            short = self._recent(s, now, BRAKE_HOURS / 24)
            if short < BRAKE_LOSS:
                w[s] = min(w[s], DEFAULT[s] * 0.1)
                why.append(f"🚨 Notbremse {STYLES[s]} ({short * 100:+.1f} % in {BRAKE_HOURS} Std.)")
        w["config_risiko"] = min(w["config_risiko"], MAX_RISK)
        if self.equity < self.peak * 0.9:
            w["config_risiko"] *= 0.5
            why.append("Risiko halbiert (mehr als 10 % unter dem Höchststand)")
        total = sum(w.values())
        if total > 1 - MIN_CASH:
            w = {s: v * (1 - MIN_CASH) / total for s, v in w.items()}
        reason = f"Marktphase «{phase}», Einschätzung: " + ", ".join(why)
        return {s: round(v, 4) for s, v in w.items()}, reason

    def update(self, equities: dict[str, float], phase: str, now: datetime) -> dict | None:
        """Ein Lauf: Ergebnis der Stile seit dem letzten Lauf übernehmen, lernen, ggf. umschichten.
        Gibt die Umschichtung zurück (für das Lern-Tagebuch), sonst None."""
        returns = {s: equities[s] / self.last[s] - 1 for s in DEFAULT
                   if s in equities and self.last.get(s) and abs(equities[s] / self.last[s] - 1) < 0.5}
        if returns:
            self.equity *= 1 + sum(self.weights.get(s, 0) * r for s, r in returns.items())
            self.memory.learn(pd.DataFrame([returns], index=[pd.Timestamp(now)]), pd.Series([phase], index=[pd.Timestamp(now)]))
            self.history.append({"t": now.isoformat(), "r": returns, "equity": self.equity})
        self.peak = max(self.peak, self.equity)
        self.last = {s: equities[s] for s in DEFAULT if s in equities}
        new, reason = self.target(phase, now)
        change = None
        floor = {s: DEFAULT[s] * 0.1 + 1e-9 for s in DEFAULT}       # Anteil eines Stils nach der Notbremse
        brake = any(new[s] <= floor[s] < self.weights.get(s, 0) - 0.005 for s in new)
        if brake or max(abs(new[s] - self.weights.get(s, 0)) for s in new) > MIN_CHANGE:
            turnover = sum(abs(new[s] - self.weights.get(s, 0)) for s in new)
            fee = self.equity * turnover * FEE
            self.equity -= fee
            self.fees += fee
            change = {"old": self.weights, "new": new, "reason": reason, "fee": fee}
            self.weights = new
            self.reason = reason
        self.save()
        return change

    def allocation_text(self, weights: dict | None = None) -> str:
        w = weights or self.weights
        cash = 1 - sum(w.values())
        return " · ".join(f"{STYLES[s]} {w[s] * 100:.0f} %" for s in DEFAULT) + f" · Cash {cash * 100:.0f} %"
