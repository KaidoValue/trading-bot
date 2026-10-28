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
    max_invested_pct: float = 1.0       # höchstens so viel vom Kapital insgesamt investiert (alle Coins zusammen)
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
    leverage: float = 1.0               # Hebel, NUR Demo: Positionen bis zum x-fachen des Kapitals
    margin_interest_per_day: float = 0.0012   # Zinsen auf Geliehenes (Kraken ca. 0,02 % pro 4 Std.), auch für Shorts
    liquidation_margin: float = 0.5     # Zwangsschliessung, wenn Kapital < 50 % der hinterlegten Sicherheit


@dataclass
class Horizon:
    """Ein Zeithorizont eines Bots (kurz = Daytrading, mittel, lang). Alle Horizonte eines Bots teilen sich
    ein Konto; jeder hat eigene Kerzen, eigene Strategie und eigene Stops. Leere Werte = Wert aus `risk`."""
    name: str
    timeframe: str
    strategy: str
    strategy_params: dict = field(default_factory=dict)
    share: float = 1.0                  # Anteil am investierbaren Kapital (wird mit den anderen normiert)
    stop_loss_atr: float | None = None
    take_profit_atr: float | None = None
    risk_per_trade: float | None = None


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
    # Zeithorizonte (kurz/mittel/lang), alle auf einem Konto. Leer = ein Horizont aus strategy/timeframe.
    horizons: dict = field(default_factory=dict)
    main_horizon: str = ""              # dieser Horizont gilt für backtest/compare/status (Standard: der erste)
    adaptive_shares: bool = False       # Kapital zum Horizont verschieben, der zuletzt mehr verdient hat
    risk: RiskConfig = field(default_factory=RiskConfig)
    name: str = "config"             # Name der Konfigurationsdatei, für die Stand-Datei
    title: str = ""                     # Anzeigename in der Übersicht (STATUS.md)
    description: str = ""               # ein Satz: was dieser Bot macht (für die Übersicht)
    api_key: str | None = None
    api_secret: str | None = None

    @classmethod
    def load(cls, path: str | Path = "bots/config.yaml") -> "Config":
        raw = yaml.safe_load(Path(path).read_text()) if Path(path).exists() else {}
        risk = RiskConfig(**(raw.pop("risk", None) or {}))
        cfg = cls(**raw, risk=risk, name=Path(path).stem)
        cfg.api_key = os.getenv("EXCHANGE_API_KEY")
        cfg.api_secret = os.getenv("EXCHANGE_API_SECRET")
        if cfg.horizons:
            main = cfg.horizon_list()[0]
            cfg.timeframe, cfg.strategy, cfg.strategy_params = main.timeframe, main.strategy, main.strategy_params
        return cfg

    def horizon_list(self) -> list[Horizon]:
        """Alle Horizonte, der Haupthorizont zuerst."""
        if not self.horizons:
            return [Horizon("", self.timeframe, self.strategy, self.strategy_params)]
        hz = [Horizon(name=n, **(h or {})) for n, h in self.horizons.items()]
        return sorted(hz, key=lambda h: h.name != (self.main_horizon or hz[0].name))

    def horizon_text(self) -> str:
        """Kurzbeschreibung für die Übersicht, z.B. «kurz: adaptive 1h · lang: regime 1d»."""
        return " · ".join(f"{h.name + ': ' if h.name else ''}{h.strategy} {h.timeframe}" for h in self.horizon_list())

    @property
    def state_path(self) -> Path:
        return Path("daten/state") / f"{self.mode}_{self.name}.json"

    @property
    def trades_path(self) -> Path:
        """Trade-Protokoll, pro Bot getrennt (bots/config.yaml schreibt nach daten/logs/trades.csv)."""
        suffix = ("" if self.name == "config" else f"_{self.name}") + ("_live" if self.mode == "live" else "")
        return Path("daten/logs") / f"trades{suffix}.csv"
