"""Technische Indikatoren auf pandas-Basis."""
import numpy as np
import pandas as pd


def sma(s: pd.Series, n: int) -> pd.Series:
    return s.rolling(n).mean()


def ema(s: pd.Series, n: int) -> pd.Series:
    return s.ewm(span=n, adjust=False).mean()


def rsi(s: pd.Series, n: int = 14) -> pd.Series:
    delta = s.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / n, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / n, adjust=False).mean()
    rs = gain / loss.replace(0, 1e-12)
    return 100 - 100 / (1 + rs)


def atr(df: pd.DataFrame, n: int = 14) -> pd.Series:
    prev_close = df["close"].shift()
    tr = pd.concat([
        df["high"] - df["low"],
        (df["high"] - prev_close).abs(),
        (df["low"] - prev_close).abs(),
    ], axis=1).max(axis=1)
    return tr.ewm(alpha=1 / n, adjust=False).mean()


def bollinger(s: pd.Series, n: int = 20, k: float = 2.0):
    mid = sma(s, n)
    std = s.rolling(n).std()
    return mid - k * std, mid, mid + k * std


def macd(s: pd.Series, fast: int = 12, slow: int = 26, signal: int = 9):
    """MACD-Linie, Signallinie, Histogramm."""
    line = ema(s, fast) - ema(s, slow)
    sig = ema(line, signal)
    return line, sig, line - sig


def momentum(s: pd.Series, n: int = 10) -> pd.Series:
    """Rate of Change: prozentuale Veränderung über n Kerzen."""
    return s.pct_change(n)


def vwap(df: pd.DataFrame) -> pd.Series:
    """Volumengewichteter Durchschnittspreis, täglich (UTC) neu gestartet."""
    typical = (df["high"] + df["low"] + df["close"]) / 3
    day = df.index.floor("D")
    pv = (typical * df["volume"]).groupby(day).cumsum()
    return pv / df["volume"].groupby(day).cumsum()


def volume_spike(df: pd.DataFrame, n: int = 20, factor: float = 2.0) -> pd.Series:
    """True, wenn das Volumen mehr als `factor` x den Durchschnitt der letzten n Kerzen beträgt."""
    return df["volume"] > factor * df["volume"].rolling(n).mean().shift()


def volatility(s: pd.Series, n: int = 20) -> pd.Series:
    """Standardabweichung der Renditen (rollierend)."""
    return s.pct_change().rolling(n).std()


def volume_profile_poc(df: pd.DataFrame, n: int = 200, bins: int = 30) -> pd.Series:
    """Point of Control: Preisniveau mit dem meisten gehandelten Volumen in den letzten n Kerzen."""
    typical = ((df["high"] + df["low"] + df["close"]) / 3).to_numpy()
    vol = df["volume"].to_numpy()
    out = np.full(len(df), np.nan)
    for i in range(n, len(df) + 1):
        p, v = typical[i - n:i], vol[i - n:i]
        hist, edges = np.histogram(p, bins=bins, weights=v)
        k = hist.argmax()
        out[i - 1] = (edges[k] + edges[k + 1]) / 2
    return pd.Series(out, index=df.index)


FIB_RETRACEMENTS = (0.236, 0.382, 0.5, 0.618, 0.786)
FIB_EXTENSIONS = (1.272, 1.618, 2.0, 2.618)


def fibonacci(low: float, high: float, up: bool = True) -> dict[str, float]:
    """Fibonacci-Retracements und -Extensions für eine Bewegung von low nach high (up) oder umgekehrt."""
    rng = high - low
    if up:
        levels = {f"ret_{r}": high - r * rng for r in FIB_RETRACEMENTS}
        levels.update({f"ext_{e}": low + e * rng for e in FIB_EXTENSIONS})
    else:
        levels = {f"ret_{r}": low + r * rng for r in FIB_RETRACEMENTS}
        levels.update({f"ext_{e}": high - e * rng for e in FIB_EXTENSIONS})
    return levels
