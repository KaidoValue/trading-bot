"""Konfiguration laden (config.yaml + Umgebungsvariablen für API-Schlüssel)."""
from __future__ import annotations

import os
from dataclasses import dataclass, field
from pathlib import Path

import yaml


@dataclass
class RiskConfig:
    risk_per_trade: float = 0.01        # max. 1 % des Kapitals pro Trade riskieren
    stop_loss_atr: float = 2.0          # Stop-Loss = Einstieg - 2 x ATR
    take_profit_atr: float = 4.0        # Take-Profit = Einstieg + 4 x ATR
    max_position_pct: float = 0.25      # max. 25 % des Kapitals in einer Position
    max_daily_loss_pct: float = 0.03    # Tagesverlust > 3 % -> heute nicht mehr handeln
    max_drawdown_pct: float = 0.15      # Rückgang > 15 % vom Höchststand -> Not-Aus
    halt_days: float = 0                # 0 = Not-Aus bis zum manuellen Neustart, sonst Pause in Tagen
    min_order_value: float = 10.0       # Mindestordergrösse der Börse (in Quote-Währung)
    max_total_risk_pct: float = 0.03    # Gesamtrisiko aller offenen Positionen (Summe der Stop-Abstände)
    max_open_positions: int = 3
    max_trades_per_day: int = 6         # gegen Overtrading
    loss_streak_pause: int = 3          # nach so vielen Verlusten in Folge ...
    pause_hours: float = 12             # ... so lange keine neuen Trades (gegen "Revenge Trading")
    max_spread_pct: float = 0.003       # kein Einstieg, wenn Spread grösser (Liquiditätsfilter, nur Paper/Live)
    correlation_limit: float = 0.8      # stark korrelierte Positionen in gleicher Richtung nur halb so gross


@dataclass
class Config:
    mode: str = "paper"                 # backtest | paper | live
    exchange: str = "kraken"
    symbols: list[str] = field(default_factory=lambda: ["BTC/CHF"])
    timeframe: str = "1h"
    # Historische Daten für Backtests: Kraken liefert nur die letzten 720 Kerzen, Bitstamp viele Jahre
    history_exchange: str = "bitstamp"
    history_symbol: str = "BTC/USD"
    starting_capital: float = 1000.0
    fee_rate: float = 0.0026            # 0.26 % pro Order (Taker-Gebühr, an Börse anpassen)
    slippage: float = 0.0005
    strategy: str = "adaptive"
    allow_short: bool = False           # auch auf fallende Kurse setzen (nur Backtest/Paper)
    strategy_params: dict = field(default_factory=dict)
    poll_seconds: int = 60
    reevaluate: bool = False            # Signal bei jedem Lauf neu prüfen, nicht nur bei neuer Kerze
    use_news: bool = True               # Fear & Greed Index und bestätigte News berücksichtigen
    news_refresh_minutes: int = 15
    news_min_sources: int = 2           # so viele Portale müssen ein Thema melden
    use_events: bool = True             # Schlüsselpersonen, Fed/SEC, Wirtschaftskalender
    event_pause_minutes: int = 30       # so lange nach einem Ereignis keine neuen Trades
    event_feeds: dict = field(default_factory=dict)   # zusätzliche RSS-Feeds, z.B. Trump/Musk-Konten
    risk: RiskConfig = field(default_factory=RiskConfig)
    name: str = "config"                # Name der Konfigurationsdatei, für die Stand-Datei
    api_key: str | None = None
    api_secret: str | None = None

    @classmethod
    def load(cls, path: str | Path = "config.yaml") -> "Config":
        raw = yaml.safe_load(Path(path).read_text()) if Path(path).exists() else {}
        risk = RiskConfig(**(raw.pop("risk", None) or {}))
        cfg = cls(**raw, risk=risk, name=Path(path).stem)
        cfg.api_key = os.getenv("EXCHANGE_API_KEY")
        cfg.api_secret = os.getenv("EXCHANGE_API_SECRET")
        return cfg

    @property
    def state_path(self) -> Path:
        return Path("state") / f"{self.mode}_{self.name}.json"
