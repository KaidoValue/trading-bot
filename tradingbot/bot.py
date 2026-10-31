"""Laufender Bot: holt regelmässig neue Kurse, entscheidet und handelt (Paper oder Live)."""
from __future__ import annotations

import csv
import logging
import math
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

from . import data, indicators as ind
from .broker import CCXTBroker, PaperBroker, paper_broker
from .config import Config
from .engine import MINUTES, Trader
from .news import NewsMonitor
from .phase import PhaseBook, coin_phases
from .risk import RiskManager
from .strategies import build, trend_direction
from . import buchhaltung, journal, state, waechter

log = logging.getLogger(__name__)

STOP_BACK = timedelta(minutes=35)   # erste Stop-Prüfung ohne gespeicherte Zeit: so weit zurück (alle 30 Min. ein Lauf)
MAX_CANDLES = 720                   # mehr Kerzen liefert Kraken nicht: 1m reicht 12 Std. zurück, 5m 60 Std.
AUFTRAEGE = Path("daten/auftraege")  # Aufträge von Hand an die Demo-Bots (Format: README.md dort)


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
        broker = paper_broker(cfg)
        start = cfg.starting_capital
    return Trader(broker, RiskManager(cfg.risk, start), allow_short=cfg.allow_short)


def run(cfg: Config, max_iterations: int | None = None) -> None:
    quote = cfg.symbols[0].split("/")[1]
    exchange = data.make_exchange(cfg.exchange, cfg.api_key, cfg.api_secret,
                                  convert_to=None if cfg.mode == "live" else quote)
    horizons = cfg.horizon_list()
    strategies = {h.name: build(h.strategy, allow_short=cfg.allow_short, **h.strategy_params) for h in horizons}
    for h in horizons:
        _pretrain(strategies[h.name], cfg, h.timeframe)
    trader = make_trader(cfg, exchange)
    if cfg.horizons:
        trader.horizons = {h.name: h for h in horizons}
        trader.adaptive_shares, trader.priority = cfg.adaptive_shares, cfg.horizon_priority
    trader.short_probation = cfg.short_probation
    if cfg.phase_gate:
        trader.phase_book = PhaseBook.load(cfg.phase_prior, cfg.phase_probation, cfg.phase_loser)
    trader.phase_exit = cfg.phase_exit
    cfg.symbols = available_symbols(exchange, cfg.symbols)
    news = NewsMonitor(cfg.symbols[0].split("/")[0], cfg.news_refresh_minutes, cfg.news_min_sources,
                       events=cfg.use_events, extra_feeds=cfg.event_feeds,
                       pause_minutes=cfg.event_pause_minutes) if cfg.use_news else None
    last_bar: dict[str, object] = state.load(cfg.state_path, trader)
    paper, hinweis = isinstance(trader.broker, PaperBroker), ""
    try:                        # einmalig: alte Trades um die Kaufgebühr korrigieren (buchhaltung.py)
        if paper and buchhaltung.nachbuchen(trader, cfg.state_path, cfg.starting_capital):
            hinweis = trader.note
    except Exception as e:      # die Nachbuchung darf den Handel nicht stoppen; die Übersicht zeigt die Lücke
        log.exception("Nachbuchung der Buchhaltung fehlgeschlagen: %s", e)
    for t in trader.open_trades.values():      # Positionen aus der Zeit vor den Horizonten: Haupthorizont
        t.horizon = t.horizon if t.horizon in trader.horizons else horizons[0].name
    if last_bar:
        log.info("Gespeicherter Stand geladen (%s): %d offene Position(en), %d abgeschlossene Trades",
                 cfg.state_path, len(trader.open_trades), len(trader.closed))
    log_path = cfg.trades_path
    log_path.parent.mkdir(parents=True, exist_ok=True)
    log.info("Bot gestartet: Modus=%s, Börse=%s, Symbole=%s, Horizonte=%s",
             cfg.mode, cfg.exchange, cfg.symbols, cfg.horizon_text())
    n, failed = 0, False
    while max_iterations is None or n < max_iterations:
        n, failed = n + 1, False
        before_open = {(s, str(t.opened)) for s, t in trader.open_trades.items()}
        before_closed = len(trader.closed)
        try:
            tickers = _tickers(exchange, cfg.symbols, cfg.fehler_path)      # ein Coin ohne Kurs stoppt nicht alle
            prices = {s: float(t["last"]) for s, t in tickers.items()}       # bewertet wird zum letzten Kurs
            if news:
                trader.context = news.current()
            now = datetime.now(timezone.utc)
            trader.kurse |= {s: [p, now.isoformat(timespec="seconds")] for s, p in prices.items()}
            px, ohne = _bewertung(trader, prices, cfg.symbols)    # Kapital: Coins ohne Kurs zum letzten Kurs
            if paper:
                sync_paper(trader.broker, exchange, tickers, now)
            fertig, auftrag = auftraege(trader, cfg, prices, now) if paper else ([], [])    # von Hand, vor den Stops
            for s in prices:    # ohne Kurs keine Stop-Prüfung: der nächste Lauf spielt die Minuten nach
                if paper:       # Demo: Minutenkerzen seit dem letzten Lauf, wie eine Stop-Order an der Börse
                    replay_stops(trader, exchange, s, prices[s], now, last_bar)
                else:           # live: eine echte Order kann nicht rückwirkend laufen, also zum Kurs von jetzt
                    p = prices[s]
                    trader.check_stops(s, p, p, p, now)
            if paper:
                b = trader.broker
                if b.interest_at is not None:
                    trader.charge_interest(px, (now - b.interest_at).total_seconds() / 3600,
                                           cfg.risk.margin_interest_per_day)
                b.interest_at = now
            eq = _liquidate(trader, px, prices, cfg.risk, now)
            trader.risk.update(eq, now.date())
            if trader.risk.halted:
                trader.close_all(prices, "Not-Aus", now)
                if not cfg.risk.halt_days:
                    log.error("NOT-AUS: %s. Bot stoppt.", trader.risk.halt_reason)
                    break
                log.error("NOT-AUS: %s. Pause für %s Tage.", trader.risk.halt_reason, cfg.risk.halt_days)
            notes, spreads, trends = ([hinweis] if hinweis and n == 1 else []) + auftrag + ohne, {}, {}
            if (cfg.phase_gate or cfg.phase_exit) and not trader.risk.halted:
                for s in prices:
                    phase = _phase(exchange, s)
                    if phase:
                        trader.check_phase(s, phase, prices[s], now)
            for h in ([] if trader.risk.halted else horizons):
                strategy = strategies[h.name]
                prefix = f"[{h.name}] " if h.name else ""
                # zuerst alle Kerzen holen: die Korrelations-Sperre braucht auch die Coins, die später drankommen
                frames = _frames(exchange, [s for s in cfg.symbols if s in prices or s in trader.open_trades],
                                 h.timeframe, cfg.fehler_path)
                for s in prices:
                    if s not in frames:
                        notes.append(f"{prefix}{s}: keine Kerzen, Signal ausgesetzt")
                        continue
                    key = f"{h.name}:{s}" if h.name else s
                    df = frames[s]
                    if last_bar.get(key) == df.index[-1] and not cfg.reevaluate:
                        continue  # keine neue abgeschlossene Kerze
                    last_bar[key] = df.index[-1]
                    sig = int(strategy.signals(df).iloc[-1])
                    if hasattr(strategy, "learn"):
                        strategy.learn(s, df)        # KI-Gedächtnis: neue Kerzen merken
                    if sig == 0:
                        notes.append(f"{prefix}{s}: kein Signal")
                        continue
                    if s not in spreads:
                        spreads[s] = _spread(exchange, s)
                    spread = spreads[s]
                    liquid = spread is None or spread <= cfg.risk.max_spread_pct
                    if not liquid:
                        log.info("%s: Spread %.3f%% zu gross, kein Einstieg", s, spread * 100)
                    factor = _correlation_factor(s, sig, frames, trader, cfg.risk.correlation_limit)
                    if h.trend_filter and s not in trends:
                        trends[s] = _trend(exchange, s)
                    trader.on_signal(s, sig, prices[s], float(ind.atr(df).iloc[-1]), eq, now,
                                     size_factor=factor, can_open_new=liquid, horizon=h.name,
                                     trend=trends[s] if h.trend_filter else None,
                                     anchor=float(ind.ema(df["close"], 20).iloc[-1]))
                    eq = trader.equity(px)
                    notes.append(prefix + trader.note)
            eq = _liquidate(trader, px, prices, cfg.risk, now)      # nochmals: neue Positionen brauchen Sicherheit
            if notes:
                trader.note = " | ".join(notes)
            log.info("Kapital %.2f | offen: %s", eq, list(trader.open_trades) or "-")
            abgleich = buchhaltung.pruefen(trader, px, cfg.starting_capital) if paper else None
            _write_trades(log_path, trader.closed)
            state.save(cfg.state_path, trader, last_bar, abgleich)
            _erledigt(fertig)               # erst jetzt: bricht der Lauf vorher ab, führt der nächste sie nochmals aus
            journal.write(cfg, before_open, before_closed, trader, now)
        except KeyboardInterrupt:
            raise
        except Exception as e:  # Netzwerkfehler etc.: ins Fehler-Protokoll (die Übersicht warnt) und weiterlaufen
            log.exception("Fehler im Durchlauf: %s", e)
            waechter.melden(cfg.fehler_path, e)
            failed = True
        if max_iterations is None or n < max_iterations:
            time.sleep(cfg.poll_seconds)
    if failed and max_iterations == 1:      # --once (zyklus.sh): Exit-Code 1, sonst bliebe der Fehler unsichtbar
        raise SystemExit(1)


def _pretrain(strategy, cfg: Config, timeframe: str | None = None) -> None:
    """Füllt ein leeres KI-Gedächtnis einmalig mit Kursgeschichte (BTC und ETH): ein Jahr bei kurzen Kerzen,
    mehr bei 4h- und Tageskerzen, damit genug Kerzen zusammenkommen."""
    memory = getattr(strategy, "memory", None)
    if memory is None or memory.pretrained:
        return
    timeframe = timeframe or cfg.timeframe
    days = {"4h": 1095, "1d": 2500}.get(timeframe, 365)
    try:
        ex = data.make_exchange(cfg.history_exchange)
        frames = [data.fetch_history(ex, s, timeframe, days) for s in dict.fromkeys([cfg.history_symbol, "ETH/USD"])]
        n = strategy.pretrain(frames)
        log.info("KI-Gedächtnis mit %d Kerzen Kursgeschichte vorgefüllt", n)
    except Exception as e:
        log.warning("Vorwissen für das KI-Gedächtnis nicht abrufbar: %s", e)


def sync_paper(broker: PaperBroker, exchange, tickers: dict, now) -> None:
    """Demo-Konto auf den Stand der Börse bringen: Zeit (30-Tage-Umsatz), Geld- und Briefkurs je Coin für
    Market-Orders und den USD-Wert der Kontowährung (Kraken rechnet die Gebührenstufe in USD)."""
    broker.now = now
    broker.quotes = {s: (float(t["bid"]), float(t["ask"])) for s, t in tickers.items()
                     if t.get("bid") and t.get("ask")}
    if hasattr(exchange, "usd_value"):          # Converted: CHF-Konto; ohne (Tests): 1 Einheit = 1 USD
        try:
            broker.quote_usd = exchange.usd_value()
        except Exception as e:                  # Kurs nicht abrufbar: mit dem letzten bekannten weiterrechnen
            log.warning("USD-Kurs der Kontowährung nicht abrufbar, Gebührenstufe mit dem letzten Kurs: %s", e)


def auftrag_ablegen(name: str, befehl: str, now: datetime | None = None) -> Path:
    """Auftrag für den nächsten Durchlauf des Demo-Bots `name` ablegen (Workflow «Position schliessen», Befehl
    «schliessen»): daten/auftraege/<Zeit UTC>_<name>.txt, z.B. 20261030T201500_config_daytrading.txt, je Zeile ein
    Befehl. Ein zweiter Auftrag in derselben Sekunde kommt als weitere Zeile dazu."""
    path = AUFTRAEGE / f"{now or datetime.now(timezone.utc):%Y%m%dT%H%M%S}_{name}.txt"
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(befehl + "\n")
    return path


def auftraege(trader: Trader, cfg: Config, prices: dict[str, float], now) -> tuple[list[Path], list[str]]:
    """Aufträge von Hand für diesen Demo-Bot ausführen, ältester zuerst. So schreibt nur der Bot selbst in seinen
    Stand. «schliessen <Coins>»: jede offene Position davon per Market-Order zum aktuellen Kurs schliessen (Grund «Von
    Hand geschlossen»), ein Coin ohne Position wird übersprungen. Hat ein Coin mit Position keinen Kurs, wartet der
    ganze Auftrag auf den nächsten Lauf. Unbekannte Befehle: Warnung, der Auftrag gilt trotzdem als erledigt.
    Gibt die erledigten Dateien (run verschiebt sie nach dem Speichern) und je Auftrag eine Notiz zurück."""
    fertig, notes = [], []
    for f in sorted(AUFTRAEGE.glob(f"*_{cfg.name}.txt")):
        if f.name.partition("_")[2] != f"{cfg.name}.txt":         # z.B. «…_x_config.txt» gehört einem anderen Bot
            continue
        try:
            wer = _auftrag_zeit(f)
            zeilen = [z.replace(",", " ").split() for z in f.read_text(encoding="utf-8-sig", errors="replace")
                      .splitlines() if z.strip() and not z.lstrip().startswith("#")]
            coins = [c.upper() for befehl, *args in zeilen if befehl.lower() == "schliessen" for c in args]
            warten = [s for s in dict.fromkeys(coins) if s in trader.open_trades and s not in prices]
            if warten:
                log.warning("%s (%s) wartet auf den nächsten Lauf, kein aktueller Kurs für %s", wer, f.name,
                            ", ".join(warten))
                notes.append(f"{wer} wartet: kein aktueller Kurs für {', '.join(warten)}")
                continue
            teile = []
            for befehl, *args in zeilen:
                if befehl.lower() != "schliessen":
                    log.warning("%s (%s): unbekannter Befehl «%s», übersprungen", wer, f.name,
                                " ".join([befehl, *args]))
                    teile.append(f"unbekannter Befehl «{befehl}»")
                    continue
                for s in dict.fromkeys(c.upper() for c in args):
                    n = len(trader.closed)
                    if s in trader.open_trades:
                        trader.exit(s, prices[s], "Von Hand geschlossen", now, market=True)
                    if len(trader.closed) == n:
                        log.info("%s (%s): %s hat keine offene Position, übersprungen", wer, f.name, s)
                        teile.append(f"{s} ohne offene Position")
                        continue
                    c = trader.closed[-1]
                    teile.append(f"{s} geschlossen @ {c['exit']:.4f} (Ergebnis {c['pnl']:+.2f})")
            if not teile:
                log.warning("%s (%s) ist leer", wer, f.name)
            fertig.append(f)
            notes.append(f"{wer}: {', '.join(teile) or 'leer, nichts ausgeführt'}")
        except Exception as e:      # ein kaputter Auftrag stoppt den Lauf nicht: er bleibt liegen, Fehler-Protokoll
            log.exception("Auftrag %s nicht ausführbar: %s", f.name, e)
            waechter.melden(cfg.fehler_path, e, f"Auftrag {f.name}: ")
    return fertig, notes


def _auftrag_zeit(f: Path) -> str:
    """«Auftrag vom 30.10. 20:15 UTC» aus dem Dateinamen, sonst «Auftrag <Dateiname>»."""
    try:
        return f"Auftrag vom {datetime.strptime(f.name.partition('_')[0], '%Y%m%dT%H%M%S'):%d.%m. %H:%M} UTC"
    except ValueError:
        return f"Auftrag {f.name}"


def _erledigt(files: list[Path]) -> None:
    """Ausgeführte Aufträge nach daten/auftraege/erledigt/ (gleicher Name), erst nach dem Speichern des Stands. Bleibt
    einer liegen, führt ihn der nächste Lauf nochmals aus: Coins ohne Position werden dann übersprungen."""
    for f in files:
        try:
            (f.parent / "erledigt").mkdir(exist_ok=True)
            f.replace(f.parent / "erledigt" / f.name)
        except OSError as e:
            log.warning("Auftrag %s nicht nach erledigt/ verschoben: %s", f.name, e)


def replay_stops(trader: Trader, exchange, symbol: str, price: float, now, last_bar: dict) -> None:
    """Stops wie eine Stop-Order, die an der Börse liegt (Demo): die 1-Minuten-Kerzen seit der letzten Prüfung (über
    12 Std. her: 5-Minuten-Kerzen) der Reihe nach durch check_stops, geschlossen zur Schlusszeit der Kerze, an der Marke
    minus Slippage; ein Gap nur, wenn eine Kerze schon jenseits des Stops eröffnet. Danach die laufende Minute mit dem
    Ticker. Ohne Kerzen (nicht abrufbar, letzte Prüfung über 60 Std. her) zählt nur der Ticker: «Stop-Loss (Ticker)».
    Die letzte Prüfung steht in last_bar["stop:<Coin>"]; Treffer, die der Ticker allein verpasst hätte, zählt
    trader.zaehler["minutenkerze_getroffen"]."""
    t = trader.open_trades.get(symbol)
    if t is None:
        return
    key, opened = f"stop:{symbol}", state._utc(t.opened)
    start = last_bar.get(key) or now - STOP_BACK
    if opened is not None:
        start = max(start, opened)
    minutes = max((now - start).total_seconds(), 0) / 60
    need = {tf: math.ceil(minutes / MINUTES[tf]) + 5 for tf in ("1m", "5m")}       # Kerzen seit der Prüfung + 5
    tf = next((tf for tf, n in need.items() if n <= MAX_CANDLES), None)
    rows = []
    if tf is None:              # so weit reichen keine Kerzen: nur der Ticker, ab jetzt wieder lückenlos
        log.warning("%s: letzte Stop-Prüfung vor %.0f Std., so weit reichen keine Kerzen: nur der Kurs beim Durchlauf",
                    symbol, minutes / 60)
        last_bar[key] = now
    else:
        try:
            df = data.fetch_recent(exchange, symbol, tf, need[tf])
            close = df.index + timedelta(minutes=MINUTES[tf])
            rows = list(df[["open", "high", "low"]].set_axis(close)[(close > start) & (close <= now)].itertuples())
        except Exception as e:  # wie früher nur mit dem Ticker; der nächste Lauf spielt die Kerzen nach
            log.warning("%s: Kerzen für die Stops nicht abrufbar, nur der Kurs beim Durchlauf: %s", symbol, e)
    for when, o, h, l in rows:
        stop, target, partial, n = t.stop, t.target, t.partial, len(trader.closed)
        trader.check_stops(symbol, o, h, l, when.to_pydatetime())
        last_bar[key] = when
        hit = None
        if len(trader.closed) > n:
            hit = ("Ziel", target, False) if trader.closed[-1]["reason"] == "Take-Profit" else ("Stop", stop, True)
        elif partial and not t.partial:
            hit = ("Teilgewinn", partial, False)
        if hit and _missed(t.side, price, hit[1], hit[2]):
            trader.zaehler["minutenkerze_getroffen"] = trader.zaehler.get("minutenkerze_getroffen", 0) + 1
            log.info("%s: %s %.4f in der Kerze bis %s berührt, der Kurs beim Durchlauf (%.4f) ist wieder auf der "
                     "sicheren Seite: nur mit dem Ticker wäre das verpasst worden", symbol, *hit[:2], when, price)
        if symbol not in trader.open_trades:
            break
    trader.check_stops(symbol, price, price, price, now, gap_label="Ticker")


def _missed(side: int, price: float, level: float, stop: bool) -> bool:
    """Liegt der Kurs beim Durchlauf wieder auf der sicheren Seite der Marke (Long: über dem Stop, unter Ziel bzw.
    Teilgewinn; Short umgekehrt)? Dann hätte die alte Prüfung nur mit dem Ticker diesen Treffer verpasst."""
    return side * (price - level) > 0 if stop else side * (level - price) > 0


def liquidation(trader: Trader, prices: dict[str, float], risk) -> bool:
    """Wie an der Börse: mit Hebel muss das Kapital mindestens `liquidation_margin` der Sicherheit decken,
    die für die offenen Positionen hinterlegt ist (Positionswert / Hebel). Sonst wird alles geschlossen."""
    if risk.leverage <= 1:
        return False
    notional = sum(abs(trader.broker.position(s)) * p for s, p in prices.items())
    return notional > 0 and trader.equity(prices) < notional / risk.leverage * risk.liquidation_margin


def _liquidate(trader: Trader, px: dict[str, float], prices: dict[str, float], risk, now) -> float:
    """Zwangsschliessung prüfen (Bewertungskurse px) und ausführen (vor und nach den Signalen; geschlossen wird zum
    aktuellen Kurs, ein Coin ohne Kurs im nächsten Lauf). Gibt das Kapital danach zurück."""
    if liquidation(trader, px, risk):
        log.error("LIQUIDATION: Sicherheit aufgebraucht, alle Positionen zwangsweise geschlossen")
        trader.close_all(prices, "Liquidation", now)
    return trader.equity(px)


def ticker(exchange, symbol: str) -> dict:
    """Ticker eines Coins; ohne gültigen letzten Kurs ein Fehler wie jeder andere (auch für die Übersicht)."""
    t = exchange.fetch_ticker(symbol)
    if not float(t.get("last") or 0) > 0:
        raise ValueError(f"kein gültiger Kurs ({t.get('last')!r})")
    return t


def _tickers(exchange, symbols: list[str], fehler_path: Path) -> dict:
    """Ticker je Coin. Fällt einer aus (z.B. Kraken «EGeneral:No data»), fehlt nur dieser Coin und der Fehler kommt
    ins Fehler-Protokoll. Fehlen alle Kurse, ist der Durchlauf fehlgeschlagen."""
    tickers, fehler = {}, {}
    for s in symbols:
        try:
            tickers[s] = ticker(exchange, s)
        except Exception as e:
            fehler[s] = e
    if fehler and not tickers:
        raise next(iter(fehler.values()))
    for s, e in fehler.items():
        log.warning("%s: Kurs nicht abrufbar, Signale und Stops ausgesetzt: %s", s, e)
        waechter.melden(fehler_path, e, f"Kurs {s}: ")
    return tickers


def _bewertung(trader: Trader, prices: dict[str, float], symbols: list[str]) -> tuple[dict[str, float], list[str]]:
    """Kurse für Kapital, Drawdown, Hebel und Zinsen: die aktuellen, für offene Positionen ohne aktuellen Kurs der
    letzte gespeicherte (ohne einen der Einstiegskurs). Nur zum Bewerten: Orders gibt es nur zum aktuellen Kurs.
    Dazu je Coin ohne Kurs ein Hinweis für die Notiz."""
    px, notes = dict(prices), []
    for s in dict.fromkeys([*symbols, *trader.open_trades]):
        if s in prices:
            continue
        t, kurs = trader.open_trades.get(s), trader.kurse.get(s)
        if t is None:
            notes.append(f"{s}: kein aktueller Kurs, Signale ausgesetzt")
            continue
        px[s] = float(kurs[0]) if kurs else t.entry
        wie = (f"zum letzten Kurs vom {datetime.fromisoformat(kurs[1]).astimezone(timezone.utc):%d.%m. %H:%M} UTC"
               if kurs else "zum Einstiegskurs")
        notes.append(f"{s}: kein aktueller Kurs, Position {wie} bewertet, Stops und Signale ausgesetzt")
    return px, notes


def _frames(exchange, symbols: list[str], timeframe: str, fehler_path: Path) -> dict:
    """Kerzen je Coin für die Signale. Ohne Kerzen fehlt der Coin (Fehler-Protokoll), sein Signal kommt im nächsten
    Lauf; die anderen Coins handeln weiter."""
    frames = {}
    for s in symbols:
        try:
            frames[s] = data.fetch_recent(exchange, s, timeframe)
        except Exception as e:
            log.warning("%s: %s-Kerzen nicht abrufbar, Signal ausgesetzt: %s", s, timeframe, e)
            waechter.melden(fehler_path, e, f"Kerzen {s} {timeframe}: ")
    return frames


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


def _trend(exchange, symbol: str) -> int:
    """Richtung der 200-Tage-Linie des Coins (Trendfilter), 0 wenn nicht abrufbar oder zu wenig Geschichte."""
    try:
        return int(trend_direction(data.fetch_recent(exchange, symbol, "1d", 400)).iloc[-1])
    except Exception as e:
        log.warning("%s: Tageskerzen für den Trendfilter nicht abrufbar: %s", symbol, e)
        return 0


def _phase(exchange, symbol: str) -> str | None:
    """Marktphase des Coins aus den Tageskerzen (phase.py), None wenn nicht abrufbar."""
    try:
        return str(coin_phases(data.fetch_recent(exchange, symbol, "1d", 400)).iloc[-1])
    except Exception as e:
        log.warning("%s: Tageskerzen für die Marktphase nicht abrufbar: %s", symbol, e)
        return None


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
