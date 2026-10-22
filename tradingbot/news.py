"""Marktinformationen aus dem Netz: Stimmungsindex und Krypto-News.

Quellen (kostenlos, ohne Konto):
- Crypto Fear & Greed Index von alternative.me (0 = extreme Angst, 100 = extreme Gier)
- RSS-Feeds grosser Krypto-Newsportale

"Bestätigt" heisst hier: Ein Nachrichtenthema zählt nur, wenn mindestens `min_sources` verschiedene
Portale innerhalb von `max_age_hours` darüber berichten. Einzelmeldungen und Gerüchte werden ignoriert.

Die Bewertung der Schlagzeilen geschieht über eine Stichwortliste (THEMES). Sie ist bewusst einfach und
nachvollziehbar; neue Themen lassen sich dort ergänzen.
"""
from __future__ import annotations

import json
import logging
import time
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

log = logging.getLogger(__name__)

FEAR_GREED_URL = "https://api.alternative.me/fng/?limit=1"
FEEDS = {
    "coindesk": "https://www.coindesk.com/arc/outboundfeeds/rss/",
    "cointelegraph": "https://cointelegraph.com/rss",
    "decrypt": "https://decrypt.co/feed",
    "bitcoinmagazine": "https://bitcoinmagazine.com/.rss/full/",
}

# Thema -> (Wirkung von -1 bis +1, Stichwörter in Kleinbuchstaben)
THEMES = {
    "hack": (-1.0, ["hack", "exploit", "stolen", "drained", "breach"]),
    "verbot": (-0.8, ["ban ", "bans ", "banned", "crackdown", "prohibit"]),
    "klage": (-0.6, ["lawsuit", "sues ", "charged", "indictment", "sec sues"]),
    "insolvenz": (-1.0, ["bankrupt", "insolvency", "collapse", "halts withdrawals", "suspends withdrawals"]),
    "crash": (-0.7, ["crash", "plunge", "liquidations", "sell-off", "selloff"]),
    "etf_zulassung": (0.8, ["etf approv", "approves etf", "etf inflow", "record inflows"]),
    "adoption": (0.6, ["adopt", "legal tender", "reserve asset", "strategic reserve", "partnership"]),
    "rally": (0.5, ["rally", "all-time high", "record high", "surge"]),
    "zinssenkung": (0.5, ["rate cut", "cuts rates"]),
}

ASSET_WORDS = {
    "BTC": ["bitcoin", "btc"],
    "ETH": ["ethereum", "ether", "eth "],
    "SOL": ["solana", "sol "],
}
GENERAL_WORDS = ["crypto", "krypto", "market", "sec", "fed", "regulat", "stablecoin", "exchange"]


@dataclass
class Headline:
    source: str
    title: str
    published: datetime
    link: str = ""


@dataclass
class MarketContext:
    """Zusammenfassung der aktuellen Nachrichtenlage, die der Bot bei Entscheidungen nutzt."""
    fear_greed: int | None = None
    news_score: float = 0.0                       # -1 sehr negativ ... +1 sehr positiv
    confirmed: dict[str, list[str]] = field(default_factory=dict)   # Thema -> Quellen
    fetched_at: float = 0.0
    alerts: list = field(default_factory=list)    # aktuelle Ereignis-Alarme (siehe events.py)
    evidence: list = field(default_factory=list)  # Schlagzeilen hinter den bestätigten Themen
    blackout: str | None = None                   # wichtiger Wirtschaftstermin steht an

    def allows(self, side: int, block_level: float = 0.5) -> bool:
        """Keine neuen Trades rund um Wirtschaftstermine und bei Ereignissen mit unklarer Richtung.
        Keine Longs bei klar negativer, keine Shorts bei klar positiver Nachrichtenlage."""
        if self.blackout:
            return False
        if self.alerts:
            impact = sum(a.impact for a in self.alerts) / len(self.alerts)
            if abs(impact) < 0.3 or impact * side < 0:
                return False
        if side > 0:
            return self.news_score > -block_level
        return self.news_score < block_level

    def size_factor(self) -> float:
        """Bei extremer Angst oder Gier ist der Markt nervös: Positionen halbieren."""
        if self.fear_greed is not None and (self.fear_greed <= 15 or self.fear_greed >= 85):
            return 0.5
        return 1.0

    def to_dict(self) -> dict:
        return {"fear_greed": self.fear_greed, "news_score": self.news_score, "themes": self.confirmed,
                "blackout": self.blackout, "evidence": self.evidence,
                "alerts": [{"who": a.who, "title": a.title, "source": a.source,
                            "published": a.published.isoformat()} for a in self.alerts]}

    def summary(self) -> dict:
        return {"fear_greed": self.fear_greed, "news_score": round(self.news_score, 2),
                "news_themes": ",".join(sorted(self.confirmed)) or "-",
                "event": "; ".join(f"{a.who}: {a.title}" for a in self.alerts)[:200] or (self.blackout or "-")}


def _get(url: str, timeout: float = 10.0) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (tradingbot)"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def fetch_fear_greed(get=_get) -> int | None:
    try:
        return int(json.loads(get(FEAR_GREED_URL))["data"][0]["value"])
    except Exception as e:
        log.warning("Fear & Greed nicht abrufbar: %s", e)
        return None


def parse_feed(source: str, xml_bytes: bytes) -> list[Headline]:
    out = []
    for item in ET.fromstring(xml_bytes).iter("item"):
        title = (item.findtext("title") or "").strip()
        try:
            published = parsedate_to_datetime(item.findtext("pubDate") or "")
        except (TypeError, ValueError):
            continue
        if published.tzinfo is None:
            published = published.replace(tzinfo=timezone.utc)
        if title:
            out.append(Headline(source, title, published, (item.findtext("link") or "").strip()))
    return out


def fetch_headlines(feeds: dict[str, str] = FEEDS, get=_get) -> list[Headline]:
    out = []
    for source, url in feeds.items():
        try:
            out += parse_feed(source, get(url))
        except Exception as e:
            log.warning("Feed %s nicht abrufbar: %s", source, e)
    return out


def score_headlines(headlines: list[Headline], asset: str, min_sources: int = 2, max_age_hours: float = 24,
                    now: datetime | None = None) -> tuple[float, dict[str, list[str]]]:
    """Bewertet Schlagzeilen. Nur Themen, die von mehreren Quellen bestätigt sind, fliessen ein."""
    now = now or datetime.now(timezone.utc)
    relevant_words = ASSET_WORDS.get(asset.upper(), [asset.lower()]) + GENERAL_WORDS
    sources_per_theme: dict[str, set[str]] = {}
    for h in headlines:
        if now - h.published > timedelta(hours=max_age_hours):
            continue
        text = f" {h.title.lower()} "
        if not any(w in text for w in relevant_words):
            continue
        for theme, (_, words) in THEMES.items():
            if any(w in text for w in words):
                sources_per_theme.setdefault(theme, set()).add(h.source)
    confirmed = {t: sorted(s) for t, s in sources_per_theme.items() if len(s) >= min_sources}
    if not confirmed:
        return 0.0, {}
    impacts = [THEMES[t][0] for t in confirmed]
    score = sum(impacts) / len(impacts)
    if min(impacts) <= -0.8:  # Hack oder Insolvenz wiegt schwerer als jede gute Schlagzeile
        score = min(impacts)
    return max(-1.0, min(1.0, score)), confirmed


def evidence(headlines: list[Headline], asset: str, themes, max_age_hours: float = 24,
             now: datetime | None = None, limit: int = 8) -> list[dict]:
    """Die Schlagzeilen, auf denen die bestätigten Themen beruhen (neueste zuerst)."""
    now = now or datetime.now(timezone.utc)
    relevant_words = ASSET_WORDS.get(asset.upper(), [asset.lower()]) + GENERAL_WORDS
    out = []
    for h in sorted(headlines, key=lambda h: h.published, reverse=True):
        if now - h.published > timedelta(hours=max_age_hours):
            continue
        text = f" {h.title.lower()} "
        if not any(w in text for w in relevant_words):
            continue
        hit = next((t for t in themes if any(w in text for w in THEMES[t][1])), None)
        if hit:
            out.append({"theme": hit, "source": h.source, "title": h.title, "link": h.link,
                        "published": h.published.isoformat()})
    return out[:limit]


def briefing(ctx: dict) -> str:
    """Kurzinfo zur Nachrichtenlage als Markdown (für STATUS.md)."""
    lines = ["## Nachrichtenlage", ""]
    fg = ctx.get("fear_greed")
    if fg is not None:
        mood = ("extreme Angst" if fg <= 25 else "Angst" if fg <= 45 else "neutral" if fg <= 55
                else "Gier" if fg <= 75 else "extreme Gier")
        lines.append(f"- **Stimmung (Fear & Greed):** {fg} von 100, {mood}")
    else:
        lines.append("- **Stimmung (Fear & Greed):** nicht abrufbar")
    score = ctx.get("news_score", 0)
    themes = ctx.get("themes") or {}
    lines.append(f"- **Bewertung News:** {score:+.2f} (−1 sehr negativ bis +1 sehr positiv)")
    if themes:
        lines.append("- **Bestätigte Themen:** " + "; ".join(f"{t} (gemeldet von {', '.join(s)})" for t, s in themes.items()))
    else:
        lines.append("- **Bestätigte Themen:** keine")
    if ctx.get("blackout"):
        lines.append(f"- **Wirtschaftstermin:** {ctx['blackout']}, keine neuen Trades")
    for a in ctx.get("alerts") or []:
        lines.append(f"- **Ereignis:** {a['who']}: {a['title']} ({a['source']}, {a['published'][11:16]} UTC)")
    ev = ctx.get("evidence") or []
    if ev:
        lines += ["", "**Schlagzeilen dazu:**", ""]
        for e in ev:
            when = e["published"][:16].replace("T", " ")
            title = f"[{e['title']}]({e['link']})" if e.get("link") else e["title"]
            lines.append(f"- {when} UTC · **{e['source']}** · {title} _(Thema: {e['theme']})_")
    return "\n".join(lines)


class NewsMonitor:
    """Holt die Nachrichtenlage alle `refresh_minutes` neu (schont die Quellen) und prüft
    Ereignisse (Schlüsselpersonen, Behörden, Wirtschaftstermine) alle `event_seconds`."""

    def __init__(self, asset: str, refresh_minutes: int = 15, min_sources: int = 2, get=_get,
                 events: bool = True, extra_feeds: dict[str, str] | None = None, event_seconds: int = 120,
                 pause_minutes: int = 30):
        from .events import EventMonitor
        self.asset = asset
        self.refresh = refresh_minutes * 60
        self.min_sources = min_sources
        self.get = get
        self.context = MarketContext()
        self.headlines: list[Headline] = []
        self.events = EventMonitor(extra_feeds, pause_minutes, get=get) if events else None
        self.event_seconds = event_seconds
        self.events_checked = 0.0

    def current(self) -> MarketContext:
        now = time.time()
        if now - self.context.fetched_at >= self.refresh:
            self.headlines = fetch_headlines(get=self.get)
            score, confirmed = score_headlines(self.headlines, self.asset, self.min_sources)
            self.context = MarketContext(fetch_fear_greed(self.get), score, confirmed, now)
            self.context.evidence = evidence(self.headlines, self.asset, confirmed)
            log.info("Marktlage: Fear&Greed=%s, News=%.2f, bestätigte Themen=%s",
                     self.context.fear_greed, score, confirmed or "-")
            self.events_checked = 0.0
        if self.events and now - self.events_checked >= self.event_seconds:
            self.context.alerts, self.context.blackout = self.events.check(self.headlines)
            self.events_checked = now
            if self.context.blackout:
                log.warning("Wirtschaftstermin: %s, keine neuen Trades", self.context.blackout)
        return self.context
