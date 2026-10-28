"""Lern-Tagebuch: schreibt jeden Kauf und Verkauf in Worten nach lernen/tagebuch/JJJJ-MM-TT.md.

Pro Trade steht dort: welcher Bot, welcher Coin, zu welchem Kurs, warum (Strategie und Marktlage),
wo der Stop-Loss liegt, und beim Verkauf das Ergebnis mit einer kurzen Lehre daraus.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

TZ = "Europe/Zurich"
HORIZON_TEXT = {"kurz": "kurzfristig (Daytrading)", "mittel": "mittelfristig", "lang": "langfristig"}
FOLDER = Path("lernen/tagebuch")

WHY = {
    "regime": ("Der Kurs liegt über der 200-Tage-Linie: langfristiger Aufwärtstrend.",
               "Der Kurs ist unter die 200-Tage-Linie gefallen: der langfristige Trend ist gebrochen."),
    "adaptive": ("Die lernende KI: die Strategien, die in den letzten Wochen am besten funktioniert haben, "
                 "sagen gemeinsam «kaufen».",
                 "Die lernende KI: die zuletzt erfolgreichen Strategien sagen gemeinsam «raus»."),
    "adaptive_memory": ("Die KI mit Gedächtnis: die Strategien, die in dieser Marktphase bisher am besten "
                        "funktioniert haben, sagen gemeinsam «kaufen».",
                        "Die KI mit Gedächtnis: die in dieser Marktphase erfolgreichen Strategien sagen «raus»."),
    "trend": ("Trendfolge: der schnelle Durchschnitt liegt über dem langsamen (Aufwärtstrend).",
              "Trendfolge: der schnelle Durchschnitt liegt unter dem langsamen (Abwärtstrend)."),
    "breakout": ("Ausbruch: der Kurs hat ein neues kurzfristiges Hoch gemacht.",
                 "Der Kurs hat ein neues kurzfristiges Tief gemacht (Ausbruch nach unten)."),
}

LESSON = {
    "Stop-Loss": "Der Stop-Loss hat den Verlust auf den vorher geplanten Betrag begrenzt. Verluste klein "
                 "halten ist wichtiger als jeder einzelne Gewinn.",
    "Stop-Loss (Gap)": "Der Kurs ist über den Stop hinweg gesprungen (Gap). Stops schützen gut, aber nicht "
                       "immer exakt auf den Rappen.",
    "Take-Profit": "Das Gewinnziel wurde erreicht: Der Plan mit festem Chance-Risiko-Verhältnis ist aufgegangen.",
    "Liquidation": "Mit Hebel war die Sicherheit aufgebraucht: Die Börse hat alle Positionen zwangsweise "
                   "geschlossen. Hebel vervielfacht Verluste genauso wie Gewinne.",
    "Not-Aus": "Das Verlustlimit des ganzen Kontos wurde erreicht. Der Not-Aus verhindert, dass aus einem "
               "schlechten Lauf ein Totalverlust wird.",
}


def _local(ts) -> pd.Timestamp:
    t = pd.Timestamp(ts)
    return (t.tz_localize("UTC") if t.tzinfo is None else t).tz_convert(TZ)


def _chf(x: float) -> str:
    return f"{x:,.2f}".replace(",", "'")


def _market(ctx: dict) -> str:
    if "news_score" not in (ctx or {}):
        return "Dieser Bot beachtet keine Nachrichten."
    fg = ctx.get("fear_greed")
    parts = [f"Fear & Greed {fg}/100" if fg is not None else None,
             f"News-Wert {ctx.get('news_score', 0):+.2f}"]
    if ctx.get("news_themes", "-") != "-":
        parts.append(f"Themen: {ctx['news_themes']}")
    return ", ".join(p for p in parts if p)


def _horizon(cfg, name: str) -> tuple[str, str]:
    """Strategie und Beschreibung des Zeithorizonts, der einen Trade eröffnet hat."""
    hz = cfg.horizon_list()
    h = next((h for h in hz if h.name == name), hz[0])
    label = f"{HORIZON_TEXT.get(h.name, h.name)}, {h.timeframe}-Kerzen" if h.name else f"{h.timeframe}-Kerzen"
    return h.strategy, label


def opened(cfg, symbol: str, t, when) -> str:
    stake = t.entry * t.qty
    strategy, horizon = _horizon(cfg, getattr(t, "horizon", ""))
    why = WHY.get(strategy, ("Signal der Strategie.", "Signal der Strategie."))[0 if t.side > 0 else 1]
    action = "🟢 **Kauf**" if t.side > 0 else "🟣 **Short** (Wette auf fallende Kurse)"
    return (f"### {_local(when):%H:%M} · {cfg.title or cfg.name} · {action} {symbol}\n\n"
            f"- **Kurs:** {_chf(t.entry)} CHF, Menge {t.qty:.6f}, Einsatz {_chf(stake)} CHF\n"
            f"- **Horizont:** {horizon}\n"
            f"- **Warum:** {why}\n"
            f"- **Stop-Loss:** {_chf(t.stop)} CHF ({(t.stop / t.entry - 1) * 100:+.1f} %), "
            f"möglicher Verlust ca. {_chf(abs(t.entry - t.stop) * t.qty)} CHF\n"
            f"- **Marktlage:** {_market(t.context)}\n"
            + (f"- **Hebel:** {cfg.risk.leverage:g}×: jede Kursbewegung wirkt {cfg.risk.leverage:g}-fach auf das "
               f"Konto, dazu kommen Zinsen auf das geliehene Geld.\n" if cfg.risk.leverage > 1 else ""))


def closed(cfg, trade: dict) -> str:
    pnl, stake = trade["pnl"], trade["entry"] * trade["qty"]
    held = _local(trade["closed"]) - _local(trade["opened"])
    hours = held.total_seconds() / 3600
    held_txt = f"{hours:.0f} Stunden" if hours < 48 else f"{hours / 24:.0f} Tage"
    reason = trade["reason"]
    lesson = LESSON.get(reason) or (
        "Die Strategie hat rechtzeitig verlassen und den Gewinn mitgenommen." if pnl > 0 else
        "Das Signal hat gedreht, bevor der Trade aufging. Auch gute Strategien haben viele kleine Verlierer; "
        "entscheidend ist, dass die Gewinner grösser sind.")
    icon = "✅" if pnl > 0 else "❌"
    return (f"### {_local(trade['closed']):%H:%M} · {cfg.title or cfg.name} · 🔴 **Verkauf** {trade['symbol']}\n\n"
            f"- **Ergebnis:** {icon} {'+' if pnl >= 0 else ''}{_chf(pnl)} CHF ({pnl / stake * 100:+.2f} %), "
            f"nach Gebühren\n"
            f"- **Einstieg → Ausstieg:** {_chf(trade['entry'])} → {_chf(trade['exit'])} CHF, gehalten {held_txt}\n"
            f"- **Horizont:** {_horizon(cfg, trade.get('horizon', ''))[1]}\n"
            f"- **Grund:** {reason}\n"
            f"- **Was man daraus lernt:** {lesson}\n")


def write(cfg, before_open: set[tuple], before_closed: int, trader, when) -> None:
    """Hängt alle Trades dieses Durchlaufs an das Tagebuch des Tages an."""
    entries = [closed(cfg, t) for t in trader.closed[before_closed:]]
    entries += [opened(cfg, s, t, t.opened) for s, t in trader.open_trades.items() if (s, str(t.opened)) not in before_open]
    if not entries:
        return
    FOLDER.mkdir(parents=True, exist_ok=True)
    path = FOLDER / f"{_local(when):%Y-%m-%d}.md"
    head = "" if path.exists() else f"# Lern-Tagebuch {_local(when):%d.%m.%Y}\n\nAlle Zeiten in Schweizer Zeit.\n\n"
    with path.open("a") as f:
        f.write(head + "\n".join(entries) + "\n")


def write_chef(chef, change: dict, when) -> None:
    """Hält eine Umschichtung des Chef-Bots im Tagebuch fest."""
    FOLDER.mkdir(parents=True, exist_ok=True)
    path = FOLDER / f"{_local(when):%Y-%m-%d}.md"
    head = "" if path.exists() else f"# Lern-Tagebuch {_local(when):%d.%m.%Y}\n\nAlle Zeiten in Schweizer Zeit.\n\n"
    with path.open("a") as f:
        f.write(head + f"### {_local(when):%H:%M} · 4️⃣ Chef-Bot · 🔄 **Umschichtung**\n\n"
                f"- **Vorher:** {chef.allocation_text(change['old'])}\n"
                f"- **Nachher:** {chef.allocation_text(change['new'])}\n"
                f"- **Warum:** {change['reason']}\n"
                f"- **Kosten:** {_chf(change['fee'])} CHF Gebühren\n"
                f"- **Was man daraus lernt:** Kein Stil gewinnt immer. Wer das Geld dorthin verschiebt, wo es "
                f"gerade läuft, muss die Umschicht-Kosten und das Risiko von Fehlsignalen mitbezahlen.\n\n")
