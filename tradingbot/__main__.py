"""Kommandozeile.

  python -m tradingbot backtest                 # Backtest mit echten Börsendaten (config.yaml)
  python -m tradingbot backtest --synthetic     # Backtest mit simulierten Daten (offline)
  python -m tradingbot compare                  # alle Strategien vergleichen
  python -m tradingbot paper                    # Live-Kurse, simulierte Orders
  python -m tradingbot live                     # ECHTES Geld (Sicherheitsabfrage)
  python -m tradingbot report                   # Lernbericht aus logs/trades.csv
  python -m tradingbot walkforward              # Walk-Forward-Analyse (Schutz vor Overfitting)
  python -m tradingbot paper --once             # ein Durchlauf, Stand wird gespeichert (für tägliche Ausführung)
  python -m tradingbot status                   # aktueller Stand des Paper-Kontos
"""
from __future__ import annotations

import argparse
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


def report(trades: pd.DataFrame) -> None:
    """Wertet die bisherigen Trades aus: In welcher Marktlage verdient der Bot, in welcher verliert er?"""
    def table(by):
        g = trades.groupby(by)["pnl"]
        return pd.DataFrame({"Trades": g.size(), "Gewinn": g.sum().round(2),
                             "Trefferquote %": (g.apply(lambda s: (s > 0).mean()) * 100).round(1)})
    print(f"Trades: {len(trades)}, Gesamtergebnis: {trades['pnl'].sum():.2f}\n")
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
    ex = data.make_exchange(cfg.exchange)
    prices = {s: float(ex.fetch_ticker(s)["last"]) for s in cfg.symbols}
    eq = trader.equity(prices)
    print(f"Kapital: {eq:.2f} (Start {cfg.starting_capital:.2f}, {(eq / cfg.starting_capital - 1) * 100:+.2f} %)")
    print(f"Cash: {trader.broker.cash():.2f}")
    for s, t in trader.open_trades.items():
        pnl = t.side * (prices[s] - t.entry) * t.qty
        print(f"Offen: {s} {'long' if t.side > 0 else 'short'} {t.qty:.6f} @ {t.entry:.2f}, "
              f"jetzt {prices[s]:.2f}, Gewinn/Verlust {pnl:+.2f}, Stop {t.stop:.2f}")
    if not trader.open_trades:
        print("Keine offene Position (in Cash).")
    print(f"Abgeschlossene Trades: {len(trader.closed)}")
    strat = build(cfg.strategy, allow_short=cfg.allow_short, **cfg.strategy_params)
    for s in cfg.symbols:
        sig = int(strat.signals(data.fetch_recent(ex, s, cfg.timeframe)).iloc[-1])
        print(f"Aktuelles Signal {s}: {({1: 'investiert sein', -1: 'raus / Cash', 0: 'neutral'})[sig]}")
    if trader.risk.halted:
        print(f"NOT-AUS aktiv: {trader.risk.halt_reason}")


def main() -> None:
    p = argparse.ArgumentParser(prog="tradingbot")
    p.add_argument("command", choices=["backtest", "compare", "walkforward", "paper", "live", "report", "status"])
    p.add_argument("--config", default="config.yaml")
    p.add_argument("--days", type=int, default=365)
    p.add_argument("--synthetic", action="store_true", help="simulierte statt echter Kursdaten")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--strategy")
    p.add_argument("--timeframe", help="z.B. 1h, 4h, 1d")
    p.add_argument("--short", action="store_true", help="auch auf fallende Kurse setzen")
    p.add_argument("--once", action="store_true", help="nur ein Durchlauf, dann beenden")
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
        factories = {n: (lambda n=n: build(n, allow_short=cfg.allow_short, **(cfg.strategy_params if n == cfg.strategy else {})))
                     for n in names}
        test_bars = max(len(df) // 10, 100)
        wf = walk_forward(df, cfg, factories, train_bars=3 * test_bars, test_bars=test_bars)
        if wf.empty:
            raise SystemExit("Zu wenig Kursdaten für eine Walk-Forward-Analyse. Mehr --days wählen.")
        print(wf.to_string(index=False))
        total = (1 + wf["Rendite Test %"] / 100).prod() - 1
        print(f"\nGesamt ausserhalb der Trainingsdaten: {total * 100:.2f} %")
    elif args.command == "report":
        report(pd.read_csv("logs/trades.csv"))
    elif args.command == "status":
        status(cfg)
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
