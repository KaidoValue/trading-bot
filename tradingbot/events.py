"""Wichtige Ereignisse: Aussagen marktbewegender Personen, Behördenmitteilungen und Wirtschaftstermine.

Drei Bausteine:
1. **Offizielle Quellen** (Federal Reserve, SEC und frei konfigurierbare Feeds, z.B. ein RSS-Feed von Trumps
   Truth-Social- oder X-Konto). Eine Meldung direkt von der Quelle gilt als bestätigt.
2. **Schlüsselpersonen** in allen Schlagzeilen (Trump, Powell, Musk, ...). Erwähnt eine Schlagzeile eine
   dieser Personen zusammen mit einem marktrelevanten Thema, löst das einen Ereignis-Alarm aus.
3. **Wirtschaftskalender**: Rund um wichtige US-Termine (Zinsentscheid, Inflationsdaten, Arbeitsmarkt)
   eröffnet der Bot keine neuen Trades, weil die Kurse dann oft heftig und zufällig ausschlagen.

Reaktion: Ein Alarm pausiert neue Einstiege für `pause_minutes`. Offene Positionen bleiben durch ihre
Stop-Loss-Orders geschützt. Ist die Richtung klar (z.B. "Trump kündigt Bitcoin-Reserve an"), fliesst sie
zusätzlich in die Nachrichtenbewertung ein.

Ehrlicher Hinweis: Auf einen Tweet reagieren Hochfrequenz-Firmen in Millisekunden. Ein privater Bot ist
dafür zu langsam; sein Vorteil ist, sich in solchen Momenten zu schützen statt mitzuzocken.
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from .news import Headline, THEMES, fetch_headlines

log = logging.getLogger(__name__)

OFFICIAL_FEEDS = {
    "federalreserve": "https://www.federalreserve.gov/feeds/press_all.xml",
    "sec": "https://www.sec.gov/news/pressreleases.rss",
}

# Inoffizieller, weit verbreiteter JSON-Feed des Forex-Factory-Kalenders (aktuelle Woche)
CALENDAR_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"

KEY_PEOPLE = {
    "trump": ["trump"],
    "powell (fed)": ["powell", "fomc", "federal reserve"],
    "musk": ["musk"],
    "saylor": ["saylor", "microstrategy", "strategy inc"],
    "sec-chef": ["sec chair", "atkins"],
    "bessent (us-finanzminister)": ["bessent", "treasury secretary"],
    "lagarde (ezb)": ["lagarde", "ecb"],
    "fink (blackrock)": ["larry fink", "blackrock"],
}

# Themen, bei denen eine Aussage dieser Personen den Markt bewegen kann
MARKET_WORDS = ["bitcoin", "btc", "crypto", "tariff", "zoll", "rate", "inflation", "reserve", "ban",
                "sanction", "dollar", "stablecoin", "regulat", "executive order", "etf"]

EXTRA_THEMES = {
    "zoelle": (-0.6, ["tariff", "trade war", "zölle"]),
    "zinserhoehung": (-0.6, ["rate hike", "raises rates", "hawkish"]),
    "executive_order_krypto": (0.7, ["executive order on crypto", "crypto executive order", "bitcoin reserve"]),
}


@dataclass
class Alert:
    who: str
    title: str
    source: str
    published: datetime
    impact: float      # -1..+1, 0 = Richtung unklar


def detect_alerts(headlines: list[Headline], official_sources: set[str], now: datetime,
                  window_minutes: int = 60) -> list[Alert]:
    """Findet frische Meldungen über Schlüsselpersonen oder von offiziellen Quellen."""
    themes = {**THEMES, **EXTRA_THEMES}
    alerts = []
    for h in headlines:
        if now - h.published > timedelta(minutes=window_minutes) or h.published > now + timedelta(minutes=5):
            continue
        text = f" {h.title.lower()} "
        who = next((name for name, words in KEY_PEOPLE.items() if any(w in text for w in words)), None)
        official = h.source in official_sources
        if not (official or who):
            continue
        if not any(w in text for w in MARKET_WORDS):
            continue
        impacts = [imp for imp, words in themes.values() if any(w in text for w in words)]
        impact = sum(impacts) / len(impacts) if impacts else 0.0
        alerts.append(Alert(who or h.source, h.title, h.source, h.published, impact))
    return alerts


def parse_calendar(raw: bytes, currencies=("USD",), impact=("High",)) -> list[tuple[datetime, str]]:
    out = []
    for e in json.loads(raw):
        if e.get("country") in currencies and e.get("impact") in impact:
            try:
                when = datetime.fromisoformat(e["date"]).astimezone(timezone.utc)
            except (KeyError, ValueError):
                continue
            out.append((when, e.get("title", "")))
    return out


def blackout(calendar: list[tuple[datetime, str]], now: datetime, minutes: int = 30) -> str | None:
    """Name des Termins, falls `now` innerhalb ±minutes eines wichtigen Termins liegt."""
    for when, title in calendar:
        if abs((now - when).total_seconds()) <= minutes * 60:
            return f"{title} ({when:%H:%M} UTC)"
    return None


class EventMonitor:
    def __init__(self, extra_feeds: dict[str, str] | None = None, pause_minutes: int = 30,
                 calendar_minutes: int = 30, get=None):
        from .news import _get
        self.get = get or _get
        self.feeds = {**OFFICIAL_FEEDS, **(extra_feeds or {})}
        self.pause = pause_minutes
        self.calendar_minutes = calendar_minutes
        self.calendar: list[tuple[datetime, str]] = []
        self.calendar_fetched: datetime | None = None

    def check(self, media_headlines: list[Headline], now: datetime | None = None):
        """Gibt (Alarme, Kalender-Sperre) zurück."""
        now = now or datetime.now(timezone.utc)
        official = fetch_headlines(self.feeds, get=self.get)
        alerts = detect_alerts(official + media_headlines, set(self.feeds), now, self.pause)
        if self.calendar_fetched is None or now - self.calendar_fetched > timedelta(hours=6):
            try:
                self.calendar = parse_calendar(self.get(CALENDAR_URL))
            except Exception as e:
                log.warning("Wirtschaftskalender nicht abrufbar: %s", e)
            self.calendar_fetched = now
        block = blackout(self.calendar, now, self.calendar_minutes)
        for a in alerts:
            log.warning("EREIGNIS: %s | %s (%s)", a.who, a.title, a.source)
        return alerts, block
