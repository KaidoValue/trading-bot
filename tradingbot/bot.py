"""Laufender Bot: holt regelmässig neue Kurse, entscheidet und handelt (Paper oder Live)."""
from __future__ import annotations

import csv
import logging
import time
from datetime import datetime, timezone
from pathlib import Path

from . import data, indicators as ind
from .broker import CCXTBroker, PaperBroker
from .config import Config
from .engine import Trader
from .news import NewsMonitor
from .risk import RiskManager
from .strategies import build
from . import journal, state

log = logging.getLogger(__name__)


def make_trader(cfg: Config, exchange) -> Trader:
    if cfg.mode == "live":
        if cfg.risk.leverage > 1:
            raise SystemExit("Hebel ist nur im Demo-Modus verfügbar.")
        if cfg.allow_short:
            raise SystemExit("Short-Handel ist nur im Backtest und Paper-Modus verfügbar.")
        if not cfg.api_key:
            raise SystemExit("Live-Modus braucht EXCHANGE_API_KEY und EXCHANGE_API_SECRET.")
        broker = CCXTBroker(exchange, cfg.symbols[0].split("/")[1])
        start = broker.cash()
    else:
        broker = PaperBroker(cfg.starting_capital, cfg.fee_rate, cfg.slippage)
        broker.leverage = cfg.risk.leverage
        start = cfg.starting_capital
    return Trader(broker, RiskManager(cfg.risk, start), allow_short=cfg.allow_short)


def run(cfg: Config, max_iterations: int | None = None) -> None:
    quote = cfg.symbols[0].split("/")[1]
    exchange = data.make_exchange(cfg.exchange, cfg.api_key, cfg.api_secret,
                                  convert_to=None if cfg.mode == "live" else quote)
    strategy = build(cfg.strategy, allow_short=cfg.allow_short, **cfg.strategy_params)
    _pretrain(strategy, cfg)
    trader = make_trader(cfg, exchange)
    cfg.symbols = available_symbols(exchange, cfg.symbols)
    if isinstance(trader.broker, PaperBroker):
        # Umgerechnete Coins: real müssten CHF erst in USD getauscht werden (hin und zurück je eine Order)
        trader.broker.extra_fee = {s: cfg.fee_rate for s in cfg.symbols if getattr(exchange, "virtual", {}).get(s)}
    news = NewsMonitor(cfg.symbols[0].split("/")[0], cfg.news_refresh_minutes, cfg.news_min_sources,
                       events=cfg.use_events, extra_feeds=cfg.event_feeds,
                       pause_minutes=cfg.event_pause_minutes) if cfg.use_news else None
    last_bar: dict[str, object] = state.load(cfg.state_path, trader)
    if last_bar:
        log.info("Gespeicherter Stand geladen (%s): %d offene Position(en), %d abgeschlossene Trades",
                 cfg.state_path, len(trader.open_trades), len(trader.closed))
    log_path = cfg.trades_path
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log.info("Bot gestartet: Modus=%s, Börse=%s, Symbole=%s, Strategie=%s",
             cfg.mode, cfg.exchange, cfg.symbols, cfg.strategy)
    n = 0
    while max_iterations is None or n < max_iterations:
        n += 1
        before_open = {(s, str(t.opened)) for s, t in trader.open_trades.items()}
        before_closed = len(trader.closed)
        try:
            prices = {s: float(exchange.fetch_ticker(s)["last"]) for s in cfg.symbols}
            if news:
                trader.context = news.current()
            now = datetime.now(timezone.utc)
            for s in cfg.symbols:
                p = prices[s]
                trader.check_stops(s, p, p, p, now)
            if isinstance(trader.broker, PaperBroker):
                b = trader.broker
                if b.interest_at is not None:
                    b.charge_interest(prices, (now - b.interest_at).total_seconds() / 3600,
                                      cfg.risk.margin_interest_per_day)
                b.interest_at = now
            eq = trader.equity(prices)
            if liquidation(trader, prices, cfg.risk):
                log.error("LIQUIDATION: Sicherheit aufgebraucht, alle Positionen zwangsweise geschlossen")
                trader.close_all(prices, "Liquidation", now)
                eq = trader.equity(prices)
            trader.risk.update(eq, now.date())
            if trader.risk.halted:
                trader.close_all(prices, "Not-Aus", now)
                if not cfg.risk.halt_days:
                    log.error("NOT-AUS: %s. Bot stoppt.", trader.risk.halt_reason)
                    break
                log.error("NOT-AUS: %s. Pause für %s Tage.", trader.risk.halt_reason, cfg.risk.halt_days)
            frames, notes = {}, []
            for s in ([] if trader.risk.halted else cfg.symbols):
                df = frames[s] = data.fetch_recent(exchange, s, cfg.timeframe)
                if last_bar.get(s) == df.index[-1] and not cfg.reevaluate:
                    continue  # keine neue abgeschlossene Kerze
                last_bar[s] = df.index[-1]
                sig = int(strategy.signals(df).iloc[-1])
                if hasattr(strategy, "learn"):
                    strategy.learn(s, df)        # KI-Gedächtnis: neue Kerzen merken
                if sig == 0:
                    notes.append(f"{s}: kein Signal")
                    continue
                spread = _spread(exchange, s)
                liquid = spread is None or spread <= cfg.risk.max_spread_pct
                if not liquid:
                    log.info("%s: Spread %.3f%% zu gross, kein Einstieg", s, spread * 100)
                factor = _correlation_factor(s, sig, frames, trader, cfg.risk.correlation_limit)
                trader.on_signal(s, sig, prices[s], float(ind.atr(df).iloc[-1]), eq, now,
                                 size_factor=factor, can_open_new=liquid)
                notes.append(trader.note)
            if notes:
                trader.note = " | ".join(notes)
            log.info("Kapital %.2f | offen: %s", eq, list(trader.open_trades) or "-")
            _write_trades(log_path, trader.closed)
            state.save(cfg.state_path, trader, last_bar)
            journal.write(cfg, before_open, before_closed, trader, now)
        except KeyboardInterrupt:
            raise
        except Exception as e:  # Netzwerkfehler etc.: protokollieren und weiterlaufen
            log.exception("Fehler im Durchlauf: %s", e)
        if max_iterations is None or n < max_iterations:
            time.sleep(cfg.poll_seconds)


def _pretrain(strategy, cfg: Config, days: int = 365) -> None:
    """Füllt ein leeres KI-Gedächtnis einmalig mit einem Jahr Kursgeschichte (BTC und ETH)."""
    memory = getattr(strategy, "memory", None)
    if memory is None or memory.pretrained:
        return
    try:
        ex = data.make_exchange(cfg.history_exchange)
        frames = [data.fetch_history(ex, s, cfg.timeframe, days) for s in dict.fromkeys([cfg.history_symbol, "ETH/USD"])]
        n = strategy.pretrain(frames)
        log.info("KI-Gedächtnis mit %d Kerzen Kursgeschichte vorgefüllt", n)
    except Exception as e:
        log.warning("Vorwissen für das KI-Gedächtnis nicht abrufbar: %s", e)


def liquidation(trader: Trader, prices: dict[str, float], risk) -> bool:
    """Wie an der Börse: mit Hebel muss das Kapital mindestens `liquidation_margin` der Sicherheit decken,
    die für die offenen Positionen hinterlegt ist (Positionswert / Hebel). Sonst wird alles geschlossen."""
    if risk.leverage <= 1:
        return False
    notional = sum(abs(trader.broker.position(s)) * p for s, p in prices.items())
    return notional > 0 and trader.equity(prices) < notional / risk.leverage * risk.liquidation_margin


def available_symbols(exchange, symbols: list[str]) -> list[str]:
    """Lässt Coins weg, die die Börse nicht anbietet, damit ein Tippfehler nicht den ganzen Bot stoppt."""
    try:
        markets = exchange.load_markets()
    except Exception as e:
        log.warning("Märkte nicht abrufbar, nutze alle Symbole: %s", e)
        return symbols
    missing = [s for s in symbols if s not in markets]
    if missing:
        log.warning("Von %s nicht angeboten, wird übersprungen: %s", exchange.id, ", ".join(missing))
    return [s for s in symbols if s in markets]


def _spread(exchange, symbol: str) -> float | None:
    """Relativer Abstand zwischen bestem Kauf- (Bid) und Verkaufskurs (Ask) im Orderbuch."""
    try:
        ob = exchange.fetch_order_book(symbol, 5)
        bid, ask = ob["bids"][0][0], ob["asks"][0][0]
        return (ask - bid) / ((ask + bid) / 2)
    except Exception:
        return None


def _correlation_factor(symbol: str, side: int, frames: dict, trader: Trader, limit: float) -> float:
    """Halbe Grösse, wenn bereits eine stark korrelierte Position in gleicher Richtung offen ist
    (z.B. BTC und ETH bewegen sich oft gemeinsam: zwei Positionen wären fast doppeltes Risiko)."""
    ret = frames[symbol]["close"].pct_change()
    for other, t in trader.open_trades.items():
        if other == symbol or other not in frames or t.side != side:
            continue
        if ret.corr(frames[other]["close"].pct_change()) > limit:
            return 0.5
    return 1.0


def _write_trades(path: Path, trades: list[dict]) -> None:
    if not trades:
        return
    with path.open("w", newline="") as f:
        fields = list(dict.fromkeys(k for t in trades for k in t))
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(trades)
