"""Kommandozeile.

  python -m tradingbot backtest                 # Backtest mit echten Börsendaten (bots/config.yaml)
  python -m tradingbot backtest --synthetic     # Backtest mit simulierten Daten (offline)
  python -m tradingbot compare                  # alle Strategien vergleichen
  python -m tradingbot paper                    # Live-Kurse, simulierte Orders
  python -m tradingbot live                     # ECHTES Geld (Sicherheitsabfrage)
  python -m tradingbot dashboard --bots a.yaml b.yaml  # STATUS.md mit Tabellen und Charts
  python -m tradingbot youtube                  # neue Videos der YouTube-Kanäle in lernen/youtube/ speichern
  python -m tradingbot labor                    # Strategie-Labor: neue Strategien erfinden und prüfen
  python -m tradingbot report                   # Lernbericht aus daten/logs/trades*.csv
  python -m tradingbot walkforward              # Walk-Forward-Analyse (Schutz vor Overfitting)
  python -m tradingbot paper --once             # ein Durchlauf, Stand wird gespeichert (für tägliche Ausführung)
  python -m tradingbot status                   # aktueller Stand des Paper-Kontos
  python -m tradingbot schliessen --config bots/config_daytrading.yaml --symbols TRX/CHF   # Position von Hand schliessen
  python -m tradingbot historie --bots a.yaml b.yaml c.yaml   # komplette Bots über die ganze Krypto-Geschichte
  python -m tradingbot historie --bots ... --start 2022-01-01 # wie oben, aber erst ab diesem Tag handeln
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import logging
import os

import pandas as pd

from . import backtest, bot, data
from .backtest import walk_forward
from .config import Config
from .strategies import STRATEGIES, build


def _load_df(cfg: Config, args) -> pd.DataFrame:
    if args.synthetic:
        return data.synthetic(seed=args.seed)
    ex = data.make_exchange(cfg.history_exchange)
    symbol = cfg.history_symbol or cfg.symbols[0]
    print(f"Lade {args.days} Tage {symbol} ({cfg.timeframe}) von {cfg.history_exchange} ...")
    df = data.fetch_history(ex, symbol, cfg.timeframe, args.days)
    print(f"{len(df)} Kerzen von {df.index[0]:%d.%m.%Y} bis {df.index[-1]:%d.%m.%Y}\n")
    return df


def schliessen(cfg: Config, symbols: list[str]) -> None:
    """Schliesst offene Positionen des Paper-Kontos von Hand zum aktuellen Kurs (z.B. alte Shorts nach einer
    Regeländerung). Der Stand und das Trade-Protokoll werden wie nach einem Bot-Durchlauf gespeichert."""
    from datetime import datetime, timezone
    from . import buchhaltung, state
    from .bot import _write_trades, make_trader
    cfg.mode = "paper"
    ex = data.make_exchange(cfg.exchange, convert_to=cfg.symbols[0].split("/")[1])
    trader = make_trader(cfg, ex)
    last_bar = state.load(cfg.state_path, trader)
    if not last_bar:
        raise SystemExit(f"Kein gespeicherter Stand ({cfg.state_path}).")
    buchhaltung.nachbuchen(trader, cfg.state_path, cfg.starting_capital)     # wie im Bot: alte Trades zuerst
    now = datetime.now(timezone.utc)
    for s in symbols:
        if s not in trader.open_trades:
            print(f"{s}: keine offene Position")
            continue
        price = float(ex.fetch_ticker(s)["last"])
        trader.exit(s, price, "Von Hand geschlossen", now)
        print(f"{s}: geschlossen @ {price:.4f}, Ergebnis {trader.closed[-1]['pnl']:+.2f}")
    cfg.trades_path.parent.mkdir(parents=True, exist_ok=True)
    _write_trades(cfg.trades_path, trader.closed)
    state.save(cfg.state_path, trader, last_bar)


def report(trades: pd.DataFrame) -> None:
    """Wertet die bisherigen Trades aus: In welcher Marktlage verdient der Bot, in welcher verliert er?"""
    def table(by):
        g = trades.groupby(by)["pnl"]
        return pd.DataFrame({"Trades": g.size(), "Gewinn": g.sum().round(2),
                             "Trefferquote %": (g.apply(lambda s: (s > 0).mean()) * 100).round(1)})
    # ältere Protokolle haben keine Spalten für Gebühren und Zinsen: fehlende Werte zählen als 0
    kosten = {c: trades[c].fillna(0).sum() if c in trades else 0.0 for c in ("fees", "interest")}
    print(f"Trades: {len(trades)}, Gesamtergebnis: {trades['pnl'].sum():.2f}")
    print(f"Gebühren gesamt: {kosten['fees']:.2f}, Zinsen gesamt: {kosten['interest']:.2f}\n")
    print("Nach Richtung:\n", table("side"), "\n")
    print("Nach Ausstiegsgrund:\n", table("reason"), "\n")
    if "session" in trades:
        print("Nach Handelssitzung:\n", table("session"), "\n")
    if "fear_greed" in trades:
        buckets = pd.cut(trades["fear_greed"], [0, 25, 45, 55, 75, 100],
                         labels=["extreme Angst", "Angst", "neutral", "Gier", "extreme Gier"])
        print("Nach Fear & Greed beim Einstieg:\n", table(buckets), "\n")
    if "news_themes" in trades:
        print("Nach Nachrichtenthema beim Einstieg:\n", table("news_themes"))


def status(cfg: Config) -> None:
    """Zeigt Kapital, offene Positionen und das heutige Signal des Paper-Kontos."""
    from .broker import PaperBroker
    from .engine import Trader
    from .risk import RiskManager
    from . import state
    cfg.mode = "paper"
    trader = Trader(PaperBroker(cfg.starting_capital, cfg.fee_rate, cfg.slippage),
                    RiskManager(cfg.risk, cfg.starting_capital))
    if not state.load(cfg.state_path, trader):
        print(f"Noch kein gespeicherter Stand ({cfg.state_path}). Zuerst 'paper' laufen lassen.")
        return
    ex = data.make_exchange(cfg.exchange, convert_to=cfg.symbols[0].split("/")[1])
    from .bot import available_symbols
    cfg.symbols = available_symbols(ex, cfg.symbols)
    print(f"Beobachtete Coins: {', '.join(cfg.symbols)}")
    prices = {s: float(ex.fetch_ticker(s)["last"]) for s in cfg.symbols}
    eq = trader.equity(prices)
    print(f"Kapital: {eq:.2f} (Start {cfg.starting_capital:.2f}, {(eq / cfg.starting_capital - 1) * 100:+.2f} %)")
    print(f"Cash: {trader.broker.cash():.2f}")
    for s, t in trader.open_trades.items():
        pnl = t.side * (prices[s] - t.entry) * t.qty
        print(f"Offen seit {str(t.opened)[:16]}: {s} {'long' if t.side > 0 else 'short'} {t.qty:.6f} @ {t.entry:.2f}, "
              f"jetzt {prices[s]:.2f}, Gewinn/Verlust {pnl:+.2f}, Stop {t.stop:.2f}")
    if not trader.open_trades:
        print("Keine offene Position (in Cash).")
    print(f"Abgeschlossene Trades: {len(trader.closed)}")
    for t in trader.closed[-10:]:
        print(f"  {str(t['opened'])[:16]} bis {str(t['closed'])[:16]}: {t['side']} {t['symbol']} "
              f"{t['entry']:.2f} -> {t['exit']:.2f}, Ergebnis {t['pnl']:+.2f} ({t['reason']})")
    strat = build(cfg.strategy, allow_short=cfg.allow_short, **cfg.strategy_params)
    for s in cfg.symbols:
        sig = int(strat.signals(data.fetch_recent(ex, s, cfg.timeframe)).iloc[-1])
        print(f"Aktuelles Signal {s}: {({1: 'investiert sein', -1: 'raus / Cash', 0: 'neutral'})[sig]}")
    if trader.note:
        print(f"Letzte Entscheidung des Bots: {trader.note}")
    if trader.risk.halted:
        print(f"NOT-AUS aktiv: {trader.risk.halt_reason}")


def main() -> None:
    p = argparse.ArgumentParser(prog="tradingbot")
    p.add_argument("command", choices=["backtest", "compare", "walkforward", "paper", "live", "report", "status", "news", "dashboard", "labor", "youtube", "historie", "schliessen"])
    p.add_argument("--config", default="bots/config.yaml")
    p.add_argument("--bots", nargs="+", help="dashboard: Config-Dateien der Bots")
    p.add_argument("--chef", help="dashboard: Stand-Datei des Chef-Bots")
    p.add_argument("--days", type=int, default=365)
    p.add_argument("--synthetic", action="store_true", help="simulierte statt echter Kursdaten")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--strategy")
    p.add_argument("--timeframe", help="z.B. 1h, 4h, 1d")
    p.add_argument("--short", action="store_true", help="auch auf fallende Kurse setzen")
    p.add_argument("--once", action="store_true", help="nur ein Durchlauf, dann beenden")
    p.add_argument("--symbols", nargs="+", help="schliessen: diese Positionen des Paper-Kontos schliessen")
    p.add_argument("--start", help="historie: erst ab diesem Tag handeln, z.B. 2022-01-01 (Kurse davor als Vorlauf)")
    p.add_argument("-v", "--verbose", action="store_true")
    args = p.parse_args()

    logging.basicConfig(level=logging.INFO if args.verbose or args.command in ("paper", "live") else logging.WARNING,
                        format="%(asctime)s %(levelname)s %(message)s")
    cfg = Config.load(args.config)
    if args.strategy:
        cfg.strategy = args.strategy
    if args.timeframe:
        cfg.timeframe = args.timeframe
    if args.short:
        cfg.allow_short = True

    if args.command == "backtest":
        res = backtest.run(_load_df(cfg, args), build(cfg.strategy, allow_short=cfg.allow_short, **cfg.strategy_params), cfg, cfg.symbols[0])
        print(f"Strategie: {cfg.strategy}")
        for k, v in res.stats().items():
            print(f"  {k:<16} {v}")
    elif args.command == "compare":
        df = _load_df(cfg, args)
        rows = {name: backtest.run(df, build(name, allow_short=cfg.allow_short), cfg, cfg.symbols[0]).stats() for name in STRATEGIES}
        print(pd.DataFrame(rows).T.to_string())
    elif args.command == "walkforward":
        df = _load_df(cfg, args)
        # Mit --strategy wird nur diese eine Strategie getestet, sonst wählt der Bot je Abschnitt die beste
        names = [args.strategy] if args.strategy else [n for n in STRATEGIES if n != "ensemble"]
        # Gespeichertes Gedächtnis und Labor-Bibliothek nicht verwenden: sie kennen die Testkurse schon
        # (wäre ein Blick in die Zukunft). Im Test lernt das Gedächtnis Kerze für Kerze von vorne.
        params = {k: v for k, v in cfg.strategy_params.items() if k not in ("memory_file", "library_file")}
        factories = {n: (lambda n=n: build(n, allow_short=cfg.allow_short, **(params if n == cfg.strategy else {})))
                     for n in names}
        test_bars = max(len(df) // 10, 100)
        wf = walk_forward(df, cfg, factories, train_bars=3 * test_bars, test_bars=test_bars)
        if wf.empty:
            raise SystemExit("Zu wenig Kursdaten für eine Walk-Forward-Analyse. Mehr --days wählen.")
        print(wf.to_string(index=False))
        total = (1 + wf["Rendite Test %"] / 100).prod() - 1
        print(f"\nGesamt ausserhalb der Trainingsdaten: {total * 100:.2f} %")
    elif args.command == "report":
        report(pd.read_csv(cfg.trades_path))
    elif args.command == "labor":
        from . import labor
        df = _load_df(cfg, args)
        found = labor.evolve(df, fee=cfg.fee_rate, seed=args.seed if args.synthetic else None)
        lib = labor.update_library(found, df)
        text = labor.report(found, lib, df, cfg.history_symbol or cfg.symbols[0], cfg.timeframe)
        Path("lernen").mkdir(exist_ok=True)
        Path("lernen/LABOR.md").write_text(text)
        print(text)
    elif args.command == "historie":
        from . import historie
        # Reihenfolge wie im laufenden Bot: bei gleichzeitigen Signalen bekommt der erste Coin zuerst Kapital
        coins = list(dict.fromkeys(s.split("/")[0] for p in (args.bots or [args.config]) for s in Config.load(p).symbols))
        start = pd.Timestamp(args.start, tz="UTC") if args.start else None
        runs, chef, btc = historie.run_all(args.bots or [args.config], coins, start)
        btc = btc[btc.index >= start] if start is not None else btc
        text = historie.report(runs, chef, btc)
        Path("lernen").mkdir(exist_ok=True)
        Path("lernen/HISTORIE.md").write_text(text, encoding="utf-8")
        curves = pd.DataFrame({n: r.equity for n, r in runs.items()} | ({"chef": chef} if chef is not None else {})
                              | {"btc": btc})
        curves.to_csv(historie.CACHE / "kurven.csv")
        for n, r in runs.items():
            r.trades.to_csv(historie.CACHE / f"trades_{n}.csv", index=False)
            if r.cfg.phase_gate and r.cfg.phase_prior and len(r.trades):
                # Vorwissen für den laufenden Bot: was hat jeder Horizont in jeder Phase gebracht
                from .phase import PhaseBook
                stats = PhaseBook.summarize(r.trades.to_dict("records"))
                Path(r.cfg.phase_prior).write_text(json.dumps({"stats": stats, "bis": str(btc.index[-1].date())},
                                                              indent=1), encoding="utf-8")
        print(text)
    elif args.command == "youtube":
        from .youtube import update
        for f in update():
            print(f)
    elif args.command == "dashboard":
        from .dashboard import render
        print(render(args.bots or [args.config], chef_path=args.chef))
    elif args.command == "status":
        status(cfg)
    elif args.command == "schliessen":
        schliessen(cfg, args.symbols or [])
    elif args.command == "news":
        from .news import briefing
        cfg.mode = "paper"
        st = json.loads(cfg.state_path.read_text()) if cfg.state_path.exists() else {}
        print(briefing(st["news"]) if st.get("news") else "## Nachrichtenlage\n\nNoch keine Daten.")
    elif args.command == "paper":
        cfg.mode = "paper"
        bot.run(cfg, max_iterations=1 if args.once else None)
    elif args.command == "live":
        cfg.mode = "live"
        if os.getenv("CONFIRM_LIVE") != "JA":
            raise SystemExit("Live-Handel mit echtem Geld. Zum Bestätigen: CONFIRM_LIVE=JA setzen.")
        bot.run(cfg, max_iterations=1 if args.once else None)


if __name__ == "__main__":
    main()
