"""Marktdaten: historische Kerzen über ccxt laden (mit CSV-Cache) oder simulierte Daten erzeugen."""
from __future__ import annotations

import time
from pathlib import Path

import numpy as np
import pandas as pd

COLUMNS = ["timestamp", "open", "high", "low", "close", "volume"]


def make_exchange(name: str, api_key: str | None = None, api_secret: str | None = None,
                  convert_to: str | None = None):
    """Mit convert_to="CHF" werden fehlende X/CHF-Paare aus X/USD umgerechnet (nur Demo, siehe Converted)."""
    import ccxt
    cls = getattr(ccxt, name)
    params = {"enableRateLimit": True}
    if api_key:
        params.update(apiKey=api_key, secret=api_secret)
    ex = cls(params)
    return Converted(ex, convert_to) if convert_to else ex


class Converted:
    """Bietet Coins, die die Börse nicht direkt in CHF handelt (z.B. SOL), als SOL/CHF an: Kurse (auch Geld- und
    Briefkurs) kommen von SOL/USD und werden mit dem USD/CHF-Kurs der Börse umgerechnet. So läuft das ganze
    Demo-Konto in Franken. Vereinfachung: Ein echtes Konto hielte für diese Coins ein USD-Guthaben und handelte
    direkt SOL/USD zur gleichen Gebühr; den einmaligen Umtausch CHF -> USD rechnet der Demo-Bot nicht ein."""

    def __init__(self, exchange, quote: str = "CHF", via: str = "USD"):
        self.ex, self.quote, self.via = exchange, quote, via
        self.id = exchange.id
        self.bridge = f"{via}/{quote}"
        self.virtual: dict[str, str] = {}      # z.B. "SOL/CHF" -> "SOL/USD"
        self.markets: dict | None = None
        self._cache: dict = {}

    def _cached(self, key, fn, seconds=60):
        """Den USD/CHF-Kurs nur einmal pro Minute abfragen statt für jeden Coin (schont das Abfrage-Limit)."""
        hit = self._cache.get(key)
        if hit and time.time() - hit[0] < seconds:
            return hit[1]
        value = fn()
        self._cache[key] = (time.time(), value)
        return value

    def __getattr__(self, name):
        return getattr(self.ex, name)

    def load_markets(self):
        if self.markets is None:
            m = dict(self.ex.load_markets())
            if self.bridge in m:
                for s, info in list(m.items()):
                    base, _, q = s.partition("/")
                    if q == self.via and info.get("spot", True) and f"{base}/{self.quote}" not in m:
                        self.virtual[f"{base}/{self.quote}"] = s
                        m[f"{base}/{self.quote}"] = {"spot": True, "virtual": s}
            self.markets = m
        return self.markets

    def source(self, symbol: str) -> str | None:
        self.load_markets()
        return self.virtual.get(symbol)

    def fetch_ticker(self, symbol):
        src = self.source(symbol)
        if not src:
            return self.ex.fetch_ticker(symbol)
        t, fx = self.ex.fetch_ticker(src), self._fx_last()
        return {**t, **{k: float(t[k]) * fx for k in ("last", "bid", "ask") if t.get(k) is not None}}

    def _fx_last(self) -> float:
        """CHF pro USD (letzter USD/CHF-Kurs)."""
        return float(self._cached("ticker", lambda: self.ex.fetch_ticker(self.bridge))["last"])

    def usd_value(self) -> float:
        """Wert einer Einheit der Kontowährung in USD (1 CHF = 1 / USD/CHF), für die Gebührenstufe in USD."""
        return 1.0 if self.quote == self.via else 1 / self._fx_last()

    def fetch_ohlcv(self, symbol, timeframe="1h", since=None, limit=None):
        src = self.source(symbol)
        if not src:
            return self.ex.fetch_ohlcv(symbol, timeframe, since=since, limit=limit)
        rows = self.ex.fetch_ohlcv(src, timeframe, since=since, limit=limit)
        fx_rows = self._cached(("ohlcv", timeframe, since, limit),
                               lambda: self.ex.fetch_ohlcv(self.bridge, timeframe, since=since, limit=limit))
        fx = pd.Series({r[0]: r[4] for r in fx_rows}, dtype=float).sort_index()
        last = self._fx_last()
        rate = fx.reindex(sorted(set(fx.index) | {r[0] for r in rows})).ffill().bfill().fillna(last)
        return [[r[0], *(v * rate[r[0]] for v in r[1:5]), r[5]] for r in rows]

    def fetch_order_book(self, symbol, limit=None):
        return self.ex.fetch_order_book(self.source(symbol) or symbol, limit)


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
