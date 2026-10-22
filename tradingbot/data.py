"""Marktdaten: historische Kerzen über ccxt laden (mit CSV-Cache) oder simulierte Daten erzeugen."""
from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import pandas as pd

COLUMNS = ["timestamp", "open", "high", "low", "close", "volume"]


def make_exchange(name: str, api_key: str | None = None, api_secret: str | None = None):
    import ccxt
    cls = getattr(ccxt, name)
    params = {"enableRateLimit": True}
    if api_key:
        params.update(apiKey=api_key, secret=api_secret)
    return cls(params)


def to_frame(rows) -> pd.DataFrame:
    df = pd.DataFrame(rows, columns=COLUMNS)
    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms", utc=True)
    return df.set_index("timestamp").astype(float)


def fetch_history(exchange, symbol: str, timeframe: str, days: int, cache_dir="data") -> pd.DataFrame:
    """Lädt `days` Tage Kerzen, seitenweise, und speichert sie als CSV."""
    path = Path(cache_dir) / f"{exchange.id}_{symbol.replace('/', '-')}_{timeframe}_{days}d.csv"
    if path.exists() and time.time() - path.stat().st_mtime < 3600:
        return pd.read_csv(path, index_col=0, parse_dates=True)
    since = exchange.milliseconds() - days * 86_400_000
    rows = []
    while True:
        batch = exchange.fetch_ohlcv(symbol, timeframe, since=since, limit=720)
        if not batch:
            break
        rows += batch
        if batch[-1][0] + 1 <= since:
            break
        since = batch[-1][0] + 1
        if len(batch) < 2 or since >= exchange.milliseconds():
            break
    df = to_frame(rows)
    df = df[~df.index.duplicated()].sort_index()
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path)
    return df


def fetch_recent(exchange, symbol: str, timeframe: str, bars: int = 300) -> pd.DataFrame:
    """Letzte Kerzen für den Live-/Paper-Betrieb. Die noch offene letzte Kerze wird verworfen."""
    return to_frame(exchange.fetch_ohlcv(symbol, timeframe, limit=bars + 1)).iloc[:-1]


def synthetic(bars: int = 5000, seed: int = 42, start_price: float = 50_000.0) -> pd.DataFrame:
    """Zufällige Kursreihe mit wechselnden Trend-/Seitwärtsphasen. Nur zum Testen der Mechanik."""
    rng = np.random.default_rng(seed)
    drift = np.repeat(rng.normal(0, 0.0008, bars // 250 + 1), 250)[:bars]
    vol = np.repeat(rng.uniform(0.004, 0.012, bars // 250 + 1), 250)[:bars]
    close = start_price * np.exp(np.cumsum(drift + vol * rng.standard_normal(bars)))
    open_ = np.r_[start_price, close[:-1]]
    spread = np.abs(rng.normal(0, vol, bars)) * close
    idx = pd.date_range("2024-01-01", periods=bars, freq="h", tz="UTC")
    return pd.DataFrame({
        "open": open_, "close": close,
        "high": np.maximum(open_, close) + spread,
        "low": np.minimum(open_, close) - spread,
        "volume": rng.uniform(1, 10, bars),
    }, index=idx)
