"""Messwerkzeug für den Profi-Bot (Stufe 1a): Geschichts-Simulation blind, reproduzierbar und mit ehrlichen Kennzahlen."""
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from tradingbot import historie
from tradingbot.config import Config

BOTS = Path(__file__).resolve().parent.parent / "bots"


def _kerzen(seed: int, start: str, preis: float, knoten: list[tuple[int, float]]) -> pd.DataFrame:
    """Synthetische Kerzen alle 12 Stunden (statt stündlich, damit der Test schnell bleibt): Trend zwischen den Knoten
    (Tag, Kursfaktor), dazu Zufall in ruhigen und wilden Abschnitten von je 30 Tagen."""
    rng = np.random.default_rng(seed)
    tage, faktor = zip(*knoten)
    n = 2 * tage[-1]
    trend = np.interp(np.arange(n) / 2, tage, np.log(faktor))
    vol = np.repeat(rng.choice([0.5, 1.0, 1.5], n // 60 + 1), 60)[:n] * 0.03 / np.sqrt(2)
    noise = np.cumsum(rng.standard_normal(n) * vol)
    noise -= np.linspace(0, noise[-1], n)          # Zufall ohne eigene Richtung: die Knoten bestimmen den Trend
    close = preis * np.exp(trend + noise)
    open_ = np.r_[preis, close[:-1]]
    wick = np.abs(rng.standard_normal(n)) * vol / 2 * close
    idx = pd.date_range(start, periods=n, freq="12h", tz="UTC")
    return pd.DataFrame({"open": open_, "high": np.maximum(open_, close) + wick, "low": np.minimum(open_, close) - wick,
                         "close": close, "volume": rng.uniform(1, 10, n)}, index=idx)


@pytest.fixture(scope="module")
def coins():
    """BTC 440 Tage, ETH kommt nach 100 Tagen dazu; beide kreuzen die 200-Tage-Linie mehrmals."""
    return {"BTC/USD": _kerzen(1, "2020-01-01", 8000.0, [(0, 1.0), (120, 1.8), (200, 1.1), (260, 1.8), (320, 1.0),
                                                          (400, 1.9), (440, 1.4)]),
            "ETH/USD": _kerzen(2, "2020-04-10", 200.0, [(0, 1.0), (100, 1.6), (160, 0.9), (220, 1.7), (300, 2.6),
                                                         (340, 1.5)])}


def _fingerabdruck(run) -> tuple[float, int, str]:
    kurve = "\n".join(f"{t:%Y-%m-%d} {v:.2f}" for t, v in run.equity.items())
    return round(float(run.equity.iloc[-1]), 2), len(run.trades), hashlib.sha256(kurve.encode()).hexdigest()


# Berechnet mit dem Code vor Stufe 1a (main 2de1021): Endkapital, Zahl der Trades, SHA-256 der Kapitalkurve.
# Mit 100 Startkapital bleibt der Umsatz in der untersten Kraken-Stufe: «staffel» und «normiert» rechnen gleich.
VORHER = {
    ("config_langfrist", "staffel"): (96.81, 4, "656414481f50f97552a7b0f2b052d547f76747f22935eb713ec033647bb15f5e"),
    ("config_langfrist", "normiert"): (96.81, 4, "656414481f50f97552a7b0f2b052d547f76747f22935eb713ec033647bb15f5e"),
    ("config_daytrading", "staffel"): (95.34, 6, "a1dafb64cb9d3b98d4377e5ab3b90d3252bba5f5a90e91c549f3dd0650f663e1"),
    ("config_daytrading", "normiert"): (95.34, 6, "a1dafb64cb9d3b98d4377e5ab3b90d3252bba5f5a90e91c549f3dd0650f663e1"),
    ("config_risiko", "staffel"): (94.46, 5, "045818077364463e6beb5f04f32f01c5101cc9642e737a998315ae91cdd71455"),
    ("config_risiko", "normiert"): (94.46, 5, "045818077364463e6beb5f04f32f01c5101cc9642e737a998315ae91cdd71455"),
    ("config_phasen", "staffel"): (95.44, 4, "15513754955ef9312353c6c5ec4e045bf5356bb0dccf02fea78647e6e4b4bb07"),
    ("config_phasen", "normiert"): (95.44, 4, "15513754955ef9312353c6c5ec4e045bf5356bb0dccf02fea78647e6e4b4bb07"),
}


@pytest.mark.parametrize("name", ["config_langfrist", "config_daytrading", "config_risiko", "config_phasen"])
def test_die_vier_bots_bleiben_unveraendert(coins, name):
    """Neue Optionen und Kennzahlen dürfen die Simulation der heutigen Bots nicht verändern."""
    for fees in ("staffel", "normiert"):
        run = historie.simulate(Config.load(BOTS / f"{name}.yaml"), coins, fees=fees)
        assert _fingerabdruck(run) == VORHER[name, fees], (name, fees, _fingerabdruck(run))
