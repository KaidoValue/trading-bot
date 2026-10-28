"""Übersicht aller Demo-Bots als STATUS.md mit Tabellen und Kurs-Charts (für GitHub).

Aufruf: python -m tradingbot dashboard --bots bots/config_langfrist.yaml bots/config_daytrading.yaml
Schreibt STATUS.md und die Charts nach daten/charts/. Die Nachrichtenlage hängt der Workflow separat an.
"""
from __future__ import annotations

import os

import logging
import time
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

log = logging.getLogger(__name__)
TZ = "Europe/Zurich"


def _retry(fn, tries: int = 3, wait: float = 3.0):
    """Börsen-Abfrage bei kurzzeitigen Fehlern (z.B. zu viele Anfragen) nochmals versuchen."""
    for i in range(tries):
        try:
            return fn()
        except Exception:
            if i == tries - 1:
                raise
            time.sleep(wait * (i + 1))
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


def live_chart(symbol: str, exchange=None) -> str:
    symbol = getattr(exchange, "virtual", {}).get(symbol, symbol)
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
    value = sum(trader.broker.position(s) * prices[s] for s in prices)          # Shorts zählen negativ
    invested = sum(abs(trader.broker.position(s)) * prices[s] for s in prices)
    return Bot(cfg, trader, trader.broker.cash() + value, invested)


def _shares_text(b: Bot) -> str:
    hz = b.cfg.horizon_list()
    if len(hz) < 2:
        return "–"
    b.trader.horizons, b.trader.adaptive_shares = {h.name: h for h in hz}, b.cfg.adaptive_shares
    return " · ".join(f"{n} {v * 100:.0f} %" for n, v in b.trader.shares().items())


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
        ("Horizonte (Strategie, Kerzen)", lambda b: b.cfg.horizon_text()),
        ("Kapitalanteil je Horizont", lambda b: _shares_text(b)),
        ("Short erlaubt", lambda b: "ja" if b.cfg.allow_short else "nein"),
        ("Hebel", lambda b: (f"{b.cfg.risk.leverage:g}× (Zinsen bisher {chf(b.trader.broker.interest_paid)} CHF)"
                             if b.cfg.risk.leverage > 1 else "ohne")),
    ]
    out = [head, "|---" * (len(bots) + 1) + "|"]
    out += [f"| {label} | " + " | ".join(fn(b) for b in bots) + " |" for label, fn in rows]
    if any(b.trader.risk.halted for b in bots):
        out.append("")
        out += [f"> ⛔ **Not-Aus bei {b.cfg.title or b.cfg.name}:** {b.trader.risk.halt_reason}"
                for b in bots if b.trader.risk.halted]
    return out


def prices_table(tickers: dict[str, dict], ex=None) -> list[str]:
    out = ["| Coin | Kurs jetzt | 24 Std. | Live-Chart |", "|---|---|---|---|"]
    for s, t in tickers.items():
        ch = t.get("percentage")
        ch = f"{'🟢' if ch >= 0 else '🔴'} {ch:+.2f} %" if ch is not None else "–"
        out.append(f"| **{s.split('/')[0]}** | {chf(t['last'])} CHF | {ch} | [öffnen]({live_chart(s, ex)}) |")
    return out


def bot_section(b: Bot, prices: dict[str, float], frames: dict) -> list[str]:
    out = [f"## {b.cfg.title or b.cfg.name}", ""]
    if b.cfg.description:
        out += [f"_{b.cfg.description}_", ""]
    if b.trader.open_trades:
        out += ["**Offene Positionen**", "",
                "| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |",
                "|---|---|---|---|---|---|---|---|---|"]
        for s, t in b.trader.open_trades.items():
            p = prices[s]
            stake, value = t.entry * t.qty, p * t.qty
            pnl = t.side * (p - t.entry) * t.qty
            hz = f" ({t.horizon})" if t.horizon else ""
            out.append(f"| **{s.split('/')[0]}** {'long' if t.side > 0 else 'short'}{hz} | {local(t.opened)} | "
                       f"{chf(t.entry)} | {chf(p)} | {t.qty:.6f} | {chf(stake)} CHF | {chf(value)} CHF | "
                       f"{pnl_text(pnl, pnl / stake * 100)} | {chf(t.stop)} ({(t.stop / p - 1) * 100:+.0f} %) |")
    else:
        out.append("Keine offene Position, alles in Cash.")
    hz = b.cfg.horizon_list()
    strats = {h.name: build(h.strategy, allow_short=b.cfg.allow_short, **h.strategy_params) for h in hz}
    strat = strats[hz[0].name]
    names = [f"{h.name} ({h.timeframe})" if h.name else "Signal" for h in hz]
    out += ["", "**Signale jetzt**", "", "| Coin | " + " | ".join(names) + " |", "|---" * (len(hz) + 1) + "|"]
    for s in b.cfg.symbols:
        cells = [SIGNALS[int(strats[h.name].signals(frames[s, h.timeframe]).iloc[-1])]
                 if (s, h.timeframe) in frames else "–" for h in hz]
        if any(c != "–" for c in cells):
            out.append(f"| {s.split('/')[0]} | " + " | ".join(cells) + " |")
    memory = getattr(strat, "memory", None)
    if memory is not None and memory.stats:
        from .memory import phases
        out += ["", f"**🧠 KI-Gedächtnis:** {memory.experience():,} Kerzen Erfahrung".replace(",", "'")
                + " (wächst bei jedem Lauf)", "", "| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |",
                "|---|---|---|"]
        for s in b.cfg.symbols:
            if (s, b.cfg.timeframe) in frames:
                ph = phases(frames[s, b.cfg.timeframe]).iloc[-1]
                best = ", ".join(f"{n} ({v:+.3f} %/Kerze)" for n, v in memory.best(ph)) or "noch keine Erfahrung"
                out.append(f"| {s.split('/')[0]} | {ph} | {best} |")
        invented = [m.name for m in strat.members if m.name.startswith("labor_")]
        out += ["", f"**🧪 Selbst erfundene Strategien im Einsatz:** {len(invented)} "
                    f"({', '.join(invented) or 'noch keine hat die Prüfung bestanden'}), "
                    "Details in [lernen/LABOR.md](lernen/LABOR.md)"]
    if b.trader.note:
        out += ["", "**Letzte Entscheidung:** " + b.trader.note.replace(" | ", " · ")]
    if b.trader.closed:
        out += ["", "**Letzte abgeschlossene Trades**", "",
                "| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |", "|---|---|---|---|---|---|---|"]
        for t in reversed(b.trader.closed[-10:]):
            hz = f" ({t['horizon']})" if t.get("horizon") else ""
            out.append(f"| {t['symbol'].split('/')[0]} {t['side']}{hz} | {local(t['opened'])} | {local(t['closed'])} | "
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
            # Trades auf Tageskerzen oben, alle kürzeren Horizonte unten
            daily = {h.name: h.timeframe == "1d" for h in b.cfg.horizon_list()}
            here = lambda name, daily=daily, b=b: daily.get(name or "", b.cfg.timeframe == "1d") == (tf == "1d")
            for t in b.trader.closed:
                if t["symbol"] == symbol and utc(t["closed"]) >= start and here(t.get("horizon")):
                    ax.scatter(utc(t["opened"]), t["entry"], marker="^", color="green", s=70, zorder=5)
                    ax.scatter(utc(t["closed"]), t["exit"], marker="v", color="red", s=70, zorder=5)
            t = b.trader.open_trades.get(symbol)
            if t and here(t.horizon):
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


def chef_section(chef, phase: str) -> list[str]:
    from .chef import STYLES
    gain = chef.equity - chef.start
    out = ["## 4️⃣ Chef-Bot (verteilt auf die drei Stile)", "",
           "Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an "
           "und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % "
           "im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.", "",
           "| | |", "|---|---|",
           f"| Startkapital | {chf(chef.start)} CHF |",
           f"| **Kapital jetzt** | **{chf(chef.equity)} CHF** |",
           f"| Gewinn / Verlust | {pnl_text(gain, (chef.equity / chef.start - 1) * 100)} |",
           f"| **Aktuelle Verteilung** | {chef.allocation_text()} |",
           f"| Marktphase (BTC, Tageskerzen) | {phase} |",
           f"| Letzte Begründung | {chef.reason} |",
           f"| Umschicht-Gebühren bisher | {chf(chef.fees)} CHF |",
           f"| Erfahrung im Gedächtnis | {len(chef.history)} Läufe |", ""]
    best = chef.memory.best(phase)
    if best:
        out += ["**Was das Gedächtnis in dieser Phase weiss:** "
                + ", ".join(f"{STYLES.get(s, s)} {v:+.3f} %/Lauf" for s, v in best), ""]
    return out


def chart_url(name: str) -> str:
    """Auf GitHub liegen die Bilder im Branch «charts», der immer nur die neueste Version enthält
    (sonst würde jede alte Version gespeichert und das Repository mit der Zeit riesig)."""
    repo = os.environ.get("GITHUB_REPOSITORY")
    return f"https://raw.githubusercontent.com/{repo}/charts/{name}.png" if repo else f"daten/charts/{name}.png"


def render(config_paths: list[str], out: str = "STATUS.md", exchange=None, chef_path: str | None = None) -> str:
    first = Config.load(config_paths[0])
    ex = exchange or data.make_exchange(first.exchange, convert_to=first.symbols[0].split("/")[1])
    from .bot import available_symbols
    cfgs = [Config.load(p) for p in config_paths]
    symbols = available_symbols(ex, list(dict.fromkeys(s for c in cfgs for s in c.symbols)))
    tickers = {s: _retry(lambda: ex.fetch_ticker(s)) for s in symbols}
    prices = {s: float(t["last"]) for s, t in tickers.items()}
    bots = [b for p in config_paths if (b := load_bot(p, prices))]
    frames = {}
    wanted = [(s, tf, bars) for s in symbols for tf, bars in (("1d", 400), ("1h", 300))]
    wanted += [(s, h.timeframe, 300) for c in cfgs for h in c.horizon_list() for s in symbols
               if h.timeframe not in ("1d", "1h")]
    for s, tf, bars in dict.fromkeys(wanted):
        try:
            frames[s, tf] = _retry(lambda: data.fetch_recent(ex, s, tf, bars))
        except Exception as e:      # ein Coin ohne Daten soll nicht die ganze Übersicht verhindern
            log.warning("Kerzen %s %s nicht abrufbar: %s", s, tf, e)

    now = datetime.now(timezone.utc)
    lines = ["# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)", "",
             f"Stand: **{local(now)}** Schweizer Zeit · wird jede Stunde automatisch aktualisiert", "",
             "> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)", "",
             "## Auf einen Blick", ""]
    lines += [f"- **{b.cfg.title or b.cfg.name}:** {b.cfg.description}" for b in bots if b.cfg.description]
    chef_lines = []
    if chef_path and bots and (symbols[0], "1d") in frames:
        from . import journal
        from .chef import Chef
        from .memory import phases
        chef = Chef(chef_path)
        phase = phases(frames[symbols[0], "1d"]).iloc[-1]
        change = chef.update({b.cfg.name: b.equity for b in bots}, phase, now)
        if change:
            journal.write_chef(chef, change, now)
        lines.append("- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, "
                     "je nachdem, was in der aktuellen Marktphase am besten läuft.")
        chef_lines = chef_section(chef, phase)
    lines += [""] + (overview(bots) if bots else ["Noch kein Bot gelaufen."])
    lines += [""] + chef_lines
    lines += ["", "## Kurse", ""] + prices_table(tickers, ex) + [""]
    for b in bots:
        lines += bot_section(b, prices, frames)
    lines += ["## Charts", "",
              "▲ grün = Kauf, ▼ rot = Verkauf, rote Linie = Stop-Loss, orange = 200-Tage-Linie. "
              "Die Bilder zeigen den Stand der letzten Aktualisierung; für den Live-Kurs auf «Live-Chart» klicken.", ""]
    for s in symbols:
        name = s.replace("/", "-")
        if (s, "1d") not in frames or (s, "1h") not in frames:
            continue
        chart(s, frames[s, "1d"], frames[s, "1h"], bots, Path("daten/charts") / f"{name}.png")
        lines += [f"### {s} · [Live-Chart]({live_chart(s, ex)})", "", f"![{s}]({chart_url(name)})", ""]
    if chef_path:
        from . import web
        values = {b.cfg.name: b.equity for b in bots} | ({"chef": chef.equity} if chef_lines else {})
        history = web.record(Path("daten/state/verlauf.csv"), now, values)
        Path("daten/charts").mkdir(parents=True, exist_ok=True)
        Path("daten/charts/index.html").write_text(
            web.page(bots, chef if chef_lines else None, tickers, prices, history, now, ex))
    text = "\n".join(lines)
    Path(out).write_text(text)
    return text
