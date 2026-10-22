"""Kerzenmuster (Candlestick-Patterns). Jede Funktion gibt eine True/False-Serie zurück.

Begriffe: Körper = Abstand Open-Close, Docht oben = High bis Körper, Docht unten = Körper bis Low.
"""
from __future__ import annotations

import pandas as pd


def _parts(df: pd.DataFrame):
    body = (df["close"] - df["open"]).abs()
    rng = (df["high"] - df["low"]).replace(0, 1e-12)
    upper = df["high"] - df[["open", "close"]].max(axis=1)
    lower = df[["open", "close"]].min(axis=1) - df["low"]
    return body, rng, upper, lower


def doji(df, max_body: float = 0.1) -> pd.Series:
    """Unentschlossenheit: Körper sehr klein im Verhältnis zur Kerzenspanne."""
    body, rng, _, _ = _parts(df)
    return body / rng <= max_body


def hammer(df) -> pd.Series:
    """Bullish: langer unterer Docht (>= 2x Körper), kaum oberer Docht, nach Kursrückgang."""
    body, rng, upper, lower = _parts(df)
    falling = df["close"] < df["close"].shift(5)
    return (lower >= 2 * body) & (upper <= 0.3 * rng) & (body / rng > 0.05) & falling


def shooting_star(df) -> pd.Series:
    """Bearish: langer oberer Docht (>= 2x Körper), kaum unterer Docht, nach Kursanstieg."""
    body, rng, upper, lower = _parts(df)
    rising = df["close"] > df["close"].shift(5)
    return (upper >= 2 * body) & (lower <= 0.3 * rng) & (body / rng > 0.05) & rising


def bullish_engulfing(df) -> pd.Series:
    """Grüne Kerze, deren Körper den Körper der vorherigen roten Kerze komplett umschliesst."""
    o, c, po, pc = df["open"], df["close"], df["open"].shift(), df["close"].shift()
    return (pc < po) & (c > o) & (c >= po) & (o <= pc)


def bearish_engulfing(df) -> pd.Series:
    o, c, po, pc = df["open"], df["close"], df["open"].shift(), df["close"].shift()
    return (pc > po) & (c < o) & (c <= po) & (o >= pc)


def inside_bar(df) -> pd.Series:
    """Hoch und Tief liegen innerhalb der Vorkerze: Konsolidierung, oft vor einem Ausbruch."""
    return (df["high"] < df["high"].shift()) & (df["low"] > df["low"].shift())


def outside_bar(df) -> pd.Series:
    """Hoch und Tief übertreffen die Vorkerze auf beiden Seiten: hohe Volatilität, mögliche Wende."""
    return (df["high"] > df["high"].shift()) & (df["low"] < df["low"].shift())


def bullish_candle_signal(df) -> pd.Series:
    return hammer(df) | bullish_engulfing(df)


def bearish_candle_signal(df) -> pd.Series:
    return shooting_star(df) | bearish_engulfing(df)


ALL = {
    "doji": doji, "hammer": hammer, "shooting_star": shooting_star,
    "bullish_engulfing": bullish_engulfing, "bearish_engulfing": bearish_engulfing,
    "inside_bar": inside_bar, "outside_bar": outside_bar,
}


def detect(df) -> pd.DataFrame:
    """Alle Kerzenmuster als Tabelle (eine Spalte pro Muster)."""
    return pd.DataFrame({name: f(df) for name, f in ALL.items()})
