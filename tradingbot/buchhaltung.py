"""Buchhaltung: Kapital und Trade-Ergebnisse abgleichen, alte Trades einmalig nachbuchen.

Bis zum Bot-Lauf vom 28.10.2026 21:26 UTC zog der Bot beim Schliessen nur die Verkaufsgebühr vom Ergebnis ab, die
Kaufgebühr hatte der Broker aber schon vom Cash abgebucht; Zinsen gehörten zu keinem Trade. Das Cash stimmte, nur die
Ergebnisse (Trade-Protokoll, Tagebuch, Bericht) waren zu gut. `nachbuchen` korrigiert das beim nächsten Lauf einmal;
was danach noch nicht aufgeht (alte Zinsen), steht als Altlast in der Buchhaltung.
"""
from __future__ import annotations

import logging
import shutil
from datetime import date, datetime, timezone
from pathlib import Path

import pandas as pd

log = logging.getLogger(__name__)

CUTOFF = pd.Timestamp("2026-10-28T21:26:00+00:00")    # erster Bot-Lauf mit der Kaufgebühr im Trade-Ergebnis
SAETZE = (0.0026, 0.0052)        # Gebühr pro Order damals: CHF-Paar bei Kraken bzw. über USD umgerechnet
DIREKT = ("BTC/CHF", "ETH/CHF")  # die Coins mit echtem CHF-Paar
NAEHE = 0.0008                   # so nah muss der aus dem Ergebnis abgeleitete Satz bei 0,26 % bzw. 0,52 % liegen
TOLERANZ = 1.0                   # CHF: grössere Abweichungen zwischen Kapital und Trades sind ein Fehler


def _alt(opened) -> bool:
    """Vor dem Fix eröffnet? Dann fehlt dem Trade die Kaufgebühr."""
    if not isinstance(opened, (date, str)):       # datetime ist auch ein date; Zahlen gibt es nur in Tests
        return False
    try:
        t = pd.Timestamp(opened)
    except ValueError:
        return False
    return (t.tz_localize("UTC") if t.tzinfo is None else t) < CUTOFF


def _satz(symbol: str) -> float:
    """Gebühr pro Order nach Coin: BTC und ETH direkt in CHF, die anderen über USD umgerechnet (doppelte Gebühr)."""
    return SAETZE[0] if symbol in DIREKT else SAETZE[1]


def _brutto(c: dict) -> float:
    """Kursgewinn vor Gebühren und Zinsen (exit = Durchschnitt aller Verkäufe, qty = ganze Menge)."""
    return (1 if c["side"] == "long" else -1) * (c["exit"] - c["entry"]) * c["qty"]


def _saetze(c: dict, alt: bool) -> tuple[float, float]:
    """Gebührensatz für Kauf und Verkauf eines Trades ohne Gebührenangabe. Bei alten Trades steckt im Ergebnis nur
    die Verkaufsgebühr (und allfällige Zinsen): daraus der Satz, wenn er nahe bei 0,26 % bzw. 0,52 % liegt."""
    satz = _satz(c["symbol"])
    moeglich = [x for x in SAETZE if x <= satz]            # BTC und ETH kosteten nie 0,52 %
    if not alt or c["qty"] * c["exit"] <= 0:
        return satz, satz
    r = (_brutto(c) - c["pnl"]) / (c["qty"] * c["exit"])
    nah = min(moeglich, key=lambda x: abs(x - r))
    if abs(nah - r) <= NAEHE:
        return nah, nah
    # passt zu keinem Satz (z.B. von Hand ohne Umtauschgebühr geschlossen): Kauf nach Coin, Verkauf zum höchsten
    # Satz, der im Ergebnis Platz hat; der Rest sind Zinsen
    return satz, max([x for x in moeglich if x <= r], default=0.0)


def nachbuchen(trader, state_path: Path, start: float) -> dict | None:
    """Einmalige Nachbuchung, danach ohne Wirkung. Abgeschlossene Trades ohne Gebührenangabe bekommen `fees` und
    `interest`, alte zudem die fehlende Kaufgebühr im Ergebnis (`pnl_alt` behält den alten Wert); alte offene
    Positionen bekommen ihre Kaufgebühr. Was dann noch nicht aufgeht, wird als Altlast gebucht. Das Cash bleibt,
    wie es ist. Vorher wird der Stand nach daten/state/archiv/ kopiert. None, wenn es nichts zu tun gibt."""
    closed = [c for c in trader.closed if "fees" not in c]
    offen = {s: t for s, t in trader.open_trades.items() if t.fee == 0 and _alt(t.opened)}
    if not closed and not offen:
        return None
    jetzt = datetime.now(timezone.utc)
    state_path = Path(state_path)
    archiv = state_path.parent / "archiv" / f"{state_path.stem}_vor_nachbuchung_{jetzt:%Y-%m-%d}.json"
    if state_path.exists() and not archiv.exists():
        archiv.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(state_path, archiv)
    korrektur, n = 0.0, 0
    for c in closed:            # je Trade zuerst alles rechnen, dann eintragen: kein halb nachgebuchter Trade
        alt = _alt(c.get("opened"))
        kauf, verkauf = _saetze(c, alt)
        kauf, verkauf = kauf * c["qty"] * c["entry"], verkauf * c["qty"] * c["exit"]
        pnl = c["pnl"] - kauf if alt else c["pnl"]
        fees = max(0.0, min(kauf + verkauf, _brutto(c) - pnl))    # nie mehr Kosten, als im Ergebnis stecken
        zinsen = max(0.0, round(_brutto(c) - fees - pnl, 6))
        c.update(fees=fees, interest=zinsen, **({"pnl_alt": c["pnl"], "nachgebucht": True} if alt else {}))
        c["pnl"] = pnl
        if alt:
            korrektur, n = korrektur - kauf, n + 1
    for s, t in offen.items():
        fee = _satz(s) * (t.qty + t.sold) * t.entry
        # auch der Anteil schon verkaufter Teile gehört zum Trade
        t.fee, t.realized = fee, t.realized - fee * t.sold / (t.qty + t.sold)
        korrektur -= fee
    for s, t in trader.open_trades.items():     # Teilverkäufe vor diesem Update: Verkaufsgebühr nachtragen
        if t.sold and not t.fees_done:
            t.fees_done = _satz(s) * t.sold_value

    b = trader.broker
    zugeordnet = (sum(c.get("interest", 0.0) for c in trader.closed)
                  + sum(t.interest for t in trader.open_trades.values()))
    zinsen = max(0.0, getattr(b, "interest_paid", 0.0) - zugeordnet)
    bestand = getattr(b, "positions", {})
    soll = {s: t.side * t.qty for s, t in trader.open_trades.items()}
    fremd = sorted(s for s in set(bestand) | set(soll) if abs(bestand.get(s, 0.0) - soll.get(s, 0.0)) > 1e-9)
    info = {"nachgebucht_am": jetzt, "trades_korrigiert": n, "positionen_korrigiert": len(offen),
            "summe_korrektur": round(korrektur, 2), "zinsen_ohne_zuordnung": round(zinsen, 2)}
    was = [f"{n} Trade{'s' * (n != 1)}"] if n else []
    was += [f"{len(offen)} offene Position{'en' * (len(offen) != 1)}"] if offen else []
    text = (f"Buchhaltung nachgebucht: {' und '.join(was)} um die Kaufgebühr korrigiert ({korrektur:.2f} CHF)"
            if was else f"Buchhaltung nachgebucht: Gebühren und Zinsen bei {len(closed)} Trades eingetragen")
    text = text.replace("(-", "(−")
    if fremd:
        log.error("Buchhaltung: Bestand passt nicht zu den offenen Positionen (%s), Altlasten nicht berechnet",
                  ", ".join(fremd))
    else:
        # was nach der Nachbuchung noch fehlt (zum Einstiegskurs gerechnet, die Kurse heben sich auf)
        trader.altlasten = 0.0
        trader.altlasten = -trader.abgleich({}, start)["differenz"]
        rest = trader.altlasten - zinsen
        info["rest"] = round(rest, 2)
        text += f", Zinsen ohne Trade-Zuordnung {zinsen:.2f} CHF"
        if abs(rest) > 5:
            log.warning("Buchhaltung: %.2f CHF Altlasten sind keine Zinsen, Ursache unklar", rest)
    trader.buchhaltung = info | {"altlasten": trader.altlasten}
    trader.note = text
    log.warning(text)
    return trader.buchhaltung


def pruefen(trader, prices: dict[str, float], start: float) -> dict:
    """Abgleich für jeden Lauf (gerundet für den Stand). Eine Lücke über TOLERANZ kommt als Fehler ins Protokoll."""
    ab = {k: round(v, 2) + 0.0 for k, v in trader.abgleich(prices, start).items()}     # + 0.0: kein «-0.0»
    if abs(ab["differenz"]) > TOLERANZ:
        log.error("BUCHHALTUNG: Kapital %.2f CHF, aus den Trades erwartet %.2f CHF, Differenz %.2f CHF",
                  ab["kapital"], ab["erwartet"], ab["differenz"])
    return ab
