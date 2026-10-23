"""Übersicht aller Demo-Bots als STATUS.md mit Tabellen und Kurs-Charts (für GitHub).

Aufruf: python -m tradingbot dashboard --bots config_langfrist.yaml config_daytrading.yaml
Schreibt STATUS.md und die Charts nach charts/. Die Nachrichtenlage hängt der Workflow separat an.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from . import data, state
from .broker import PaperBroker
from .config import Config
from .engine import Trader
from .risk import RiskManager
from .strategies import build

TZ = "Europe/Zurich"
SIGNALS = {1: "🟢 investiert sein", -1: "🔴 raus / Cash", 0: "⚪ neutral"}


def chf(x: float) -> str:
    return f"{x:,.2f}".replace(",", "'")


def pnl_text(x: float, pct: float | None = None) -> str:
    icon = "🟢" if x > 0 else "🔴" if x < 0 else "⚪"
    return f"{icon} {'+' if x >= 0 else ''}{chf(x)} CHF" + (f" ({pct:+.2f} %)" if pct is not None else "")


def utc(ts) -> pd.Timestamp:
    t = pd.Timestamp(ts)
    return t.tz_localize("UTC") if t.tzinfo is None else t.tz_convert("UTC")


def local(ts) -> str:
    return utc(ts).tz_convert(TZ).strftime("%d.%m.%Y %H:%M")


def live_chart(symbol: str) -> str:
    return f"https://www.tradingview.com/chart/?symbol=KRAKEN:{symbol.replace('/', '')}"


@dataclass
class Bot:
    cfg: Config
    trader: Trader
    equity: float
    invested: float


def load_bot(path: str, prices: dict[str, float]) -> Bot | None:
    cfg = Config.load(path)
    cfg.mode = "paper"
    trader = Trader(PaperBroker(cfg.starting_capital, cfg.fee_rate, cfg.slippage),
                    RiskManager(cfg.risk, cfg.starting_capital))
    if not state.load(cfg.state_path, trader):
        return None
    invested = sum(trader.broker.position(s) * prices[s] for s in prices)
    return Bot(cfg, trader, trader.broker.cash() + invested, invested)


def overview(bots: list[Bot]) -> list[str]:
    head = "| | " + " | ".join(f"**{b.cfg.title or b.cfg.name}**" for b in bots) + " |"
    rows = [
        ("Startkapital", lambda b: f"{chf(b.cfg.starting_capital)} CHF"),
        ("**Kapital jetzt**", lambda b: f"**{chf(b.equity)} CHF**"),
        ("Gewinn / Verlust", lambda b: pnl_text(b.equity - b.cfg.starting_capital,
                                                (b.equity / b.cfg.starting_capital - 1) * 100)),
        ("Im Einsatz (investiert)", lambda b: f"{chf(b.invested)} CHF ({b.invested / b.equity * 100:.0f} %)"),
        ("Cash (nicht investiert)", lambda b: f"{chf(b.trader.broker.cash())} CHF"),
        ("Offene Positionen", lambda b: str(len(b.trader.open_trades))),
        ("Abgeschlossene Trades", lambda b: str(len(b.trader.closed))),
        ("Strategie", lambda b: f"{b.cfg.strategy}, {b.cfg.timeframe}-Kerzen"),
    ]
    out = [head, "|---" * (len(bots) + 1) + "|"]
    out += [f"| {label} | " + " | ".join(fn(b) for b in bots) + " |" for label, fn in rows]
    if any(b.trader.risk.halted for b in bots):
        out.append("")
        out += [f"> ⛔ **Not-Aus bei {b.cfg.title or b.cfg.name}:** {b.trader.risk.halt_reason}"
                for b in bots if b.trader.risk.halted]
    return out


def prices_table(tickers: dict[str, dict]) -> list[str]:
    out = ["| Coin | Kurs jetzt | 24 Std. | Live-Chart |", "|---|---|---|---|"]
    for s, t in tickers.items():
        ch = t.get("percentage")
        ch = f"{'🟢' if ch >= 0 else '🔴'} {ch:+.2f} %" if ch is not None else "–"
        out.append(f"| **{s.split('/')[0]}** | {chf(t['last'])} CHF | {ch} | [öffnen]({live_chart(s)}) |")
    return out


def bot_section(b: Bot, prices: dict[str, float], frames: dict) -> list[str]:
    out = [f"## {b.cfg.title or b.cfg.name}", ""]
    if b.trader.open_trades:
        out += ["**Offene Positionen**", "",
                "| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |",
                "|---|---|---|---|---|---|---|---|---|"]
        for s, t in b.trader.open_trades.items():
            p = prices[s]
            stake, value = t.entry * t.qty, p * t.qty
            pnl = t.side * (p - t.entry) * t.qty
            out.append(f"| **{s.split('/')[0]}** {'long' if t.side > 0 else 'short'} | {local(t.opened)} | "
                       f"{chf(t.entry)} | {chf(p)} | {t.qty:.6f} | {chf(stake)} CHF | {chf(value)} CHF | "
                       f"{pnl_text(pnl, pnl / stake * 100)} | {chf(t.stop)} ({(t.stop / p - 1) * 100:+.0f} %) |")
    else:
        out.append("Keine offene Position, alles in Cash.")
    strat = build(b.cfg.strategy, allow_short=b.cfg.allow_short, **b.cfg.strategy_params)
    out += ["", "**Signale jetzt**", "", "| Coin | Signal |", "|---|---|"]
    for s in b.cfg.symbols:
        if (s, b.cfg.timeframe) in frames:
            sig = int(strat.signals(frames[s, b.cfg.timeframe]).iloc[-1])
            out.append(f"| {s.split('/')[0]} | {SIGNALS[sig]} |")
    if b.trader.note:
        out += ["", "**Letzte Entscheidung:** " + b.trader.note.replace(" | ", " · ")]
    if b.trader.closed:
        out += ["", "**Letzte abgeschlossene Trades**", "",
                "| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |", "|---|---|---|---|---|---|---|"]
        for t in reversed(b.trader.closed[-10:]):
            out.append(f"| {t['symbol'].split('/')[0]} {t['side']} | {local(t['opened'])} | {local(t['closed'])} | "
                       f"{chf(t['entry'])} | {chf(t['exit'])} | {pnl_text(t['pnl'])} | {t['reason']} |")
    return out + [""]


def chart(symbol: str, daily: pd.DataFrame, hourly: pd.DataFrame, bots: list[Bot], path: Path) -> None:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 1, figsize=(11, 7.5), gridspec_kw={"height_ratios": [3, 2]})
    panels = [(axes[0], daily.iloc[-180:], "1d", "letzte 6 Monate (Tageskerzen)"),
              (axes[1], hourly.iloc[-120:], "1h", "letzte 5 Tage (Stundenkerzen)")]
    for ax, df, tf, label in panels:
        ax.plot(df.index, df["close"], color="#1f77b4", lw=1.4, label="Kurs")
        if tf == "1d":
            ma = daily["close"].rolling(200).mean().reindex(df.index)
            ax.plot(df.index, ma, color="#ff7f0e", lw=1.2, ls="--", label="200-Tage-Linie")
        start = df.index[0]
        for b in bots:
            if b.cfg.timeframe != tf:
                continue
            for t in b.trader.closed:
                if t["symbol"] == symbol and utc(t["closed"]) >= start:
                    ax.scatter(utc(t["opened"]), t["entry"], marker="^", color="green", s=70, zorder=5)
                    ax.scatter(utc(t["closed"]), t["exit"], marker="v", color="red", s=70, zorder=5)
            t = b.trader.open_trades.get(symbol)
            if t:
                ax.scatter(max(utc(t.opened), start), t.entry, marker="^", color="green", s=110,
                           zorder=6, label=f"Kauf {chf(t.entry)}")
                ax.axhline(t.entry, color="green", lw=0.8, ls=":")
                ax.axhline(t.stop, color="red", lw=1, ls="--", label=f"Stop-Loss {chf(t.stop)}")
        last = df["close"].iloc[-1]
        ax.annotate(f"{chf(last)}", (df.index[-1], last), xytext=(5, 0), textcoords="offset points",
                    fontsize=9, fontweight="bold", va="center")
        ax.set_title(f"{symbol}: {label}", fontsize=11, loc="left")
        ax.grid(alpha=0.3)
        ax.legend(loc="upper left", fontsize=8)
        ax.yaxis.set_major_formatter(matplotlib.ticker.FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", "'")))
    fig.tight_layout()
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=90)
    plt.close(fig)


def render(config_paths: list[str], out: str = "STATUS.md", exchange=None) -> str:
    first = Config.load(config_paths[0])
    ex = exchange or data.make_exchange(first.exchange)
    from .bot import available_symbols
    cfgs = [Config.load(p) for p in config_paths]
    symbols = available_symbols(ex, list(dict.fromkeys(s for c in cfgs for s in c.symbols)))
    tickers = {s: ex.fetch_ticker(s) for s in symbols}
    prices = {s: float(t["last"]) for s, t in tickers.items()}
    bots = [b for p in config_paths if (b := load_bot(p, prices))]
    frames = {}
    for s in symbols:
        for tf, bars in (("1d", 400), ("1h", 300)):
            frames[s, tf] = data.fetch_recent(ex, s, tf, bars)
    for c in cfgs:
        for s in symbols:
            if (s, c.timeframe) not in frames:
                frames[s, c.timeframe] = data.fetch_recent(ex, s, c.timeframe)

    now = datetime.now(timezone.utc)
    lines = ["# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)", "",
             f"Stand: **{local(now)}** Schweizer Zeit · wird jede Stunde automatisch aktualisiert", "",
             "## Auf einen Blick", ""]
    lines += overview(bots) if bots else ["Noch kein Bot gelaufen."]
    lines += ["", "## Kurse", ""] + prices_table(tickers) + [""]
    for b in bots:
        lines += bot_section(b, prices, frames)
    lines += ["## Charts", "",
              "▲ grün = Kauf, ▼ rot = Verkauf, rote Linie = Stop-Loss, orange = 200-Tage-Linie. "
              "Die Bilder zeigen den Stand der letzten Aktualisierung; für den Live-Kurs auf «Live-Chart» klicken.", ""]
    for s in symbols:
        name = s.replace("/", "-")
        chart(s, frames[s, "1d"], frames[s, "1h"], bots, Path("charts") / f"{name}.png")
        lines += [f"### {s} · [Live-Chart]({live_chart(s)})", "", f"![{s}](charts/{name}.png)", ""]
    text = "\n".join(lines)
    Path(out).write_text(text)
    return text
