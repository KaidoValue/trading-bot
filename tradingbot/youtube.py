"""YouTube-Wissen: holt die Abschriften neuer Videos ausgewählter Kanäle in den Lern-Ordner.

Läuft täglich auf GitHub. Für jedes neue Video entsteht lernen/youtube/<kanal>/<datum>_<titel>.md mit Titel, Link,
Beschreibung und dem gesprochenen Text. Die Regeln daraus werden danach einmal pro Woche herausgezogen und im
Strategie-Labor an echten Kursdaten getestet; übernommen wird nur, was den Test besteht.
"""
from __future__ import annotations

import json
import logging
import re
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

log = logging.getLogger(__name__)

CHANNELS = ["hkcm", "phantombyhkcm", "STA_Solutions"]
FOLDER = Path("lernen/youtube")
INDEX = FOLDER / "index.json"
FIRST_RUN = 5                       # beim ersten Mal nur die letzten Videos je Kanal, nicht das ganze Archiv
NS = {"a": "http://www.w3.org/2005/Atom", "yt": "http://www.youtube.com/xml/schemas/2015",
      "media": "http://search.yahoo.com/mrss/"}
HEADERS = {"User-Agent": "Mozilla/5.0", "Accept-Language": "de-CH,de;q=0.9,en;q=0.8", "Cookie": "CONSENT=YES+1"}


def _get(url: str) -> str:
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


def channel_id(html: str) -> str | None:
    """Kanal-ID (UC...) aus der Kanalseite."""
    m = (re.search(r'<link rel="canonical" href="https://www\.youtube\.com/channel/(UC[\w-]{22})"', html)
         or re.search(r'"(?:channelId|externalId)":"(UC[\w-]{22})"', html))
    return m.group(1) if m else None


def parse_feed(xml: str) -> list[dict]:
    """Videos aus dem RSS-Feed eines Kanals, neueste zuerst."""
    root = ET.fromstring(xml)
    out = []
    for e in root.findall("a:entry", NS):
        desc = e.find("media:group/media:description", NS)
        out.append({"id": e.findtext("yt:videoId", namespaces=NS), "title": e.findtext("a:title", namespaces=NS),
                    "published": e.findtext("a:published", namespaces=NS),
                    "description": desc.text if desc is not None and desc.text else ""})
    return out


def transcript(video_id: str) -> str | None:
    from youtube_transcript_api import YouTubeTranscriptApi
    try:
        t = YouTubeTranscriptApi().fetch(video_id, languages=["de", "de-DE", "en"])
        return " ".join(s.text.replace("\n", " ") for s in t)
    except Exception as e:          # keine Untertitel oder von YouTube gesperrt
        log.warning("Abschrift %s nicht abrufbar: %s", video_id, type(e).__name__)
        return None


def slug(text: str) -> str:
    text = text.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return re.sub(r"[^a-z0-9]+", "-", text).strip("-")[:60]


def note(channel: str, v: dict, text: str | None) -> str:
    body = text or "*(Keine Abschrift erhältlich: Das Video hat keine Untertitel oder YouTube hat den Abruf gesperrt.)*"
    return (f"# {v['title']}\n\n"
            f"- **Kanal:** @{channel}\n- **Veröffentlicht:** {v['published'][:10]}\n"
            f"- **Link:** https://www.youtube.com/watch?v={v['id']}\n"
            f"- **Auswertung:** noch offen (wird wöchentlich ausgewertet und im Strategie-Labor getestet)\n\n"
            f"## Beschreibung\n\n{v['description'].strip() or '-'}\n\n## Abschrift\n\n{body}\n")


def retry_missing(index: dict, channel: str, fetch_transcript, days: int = 30) -> None:
    """Videos ohne Abschrift nochmals versuchen (z.B. vom PC aus, wo YouTube nicht sperrt)."""
    import pandas as pd
    since = pd.Timestamp.now(tz="UTC") - pd.Timedelta(days=days)
    for vid, v in index["videos"].items():
        if v["channel"] != channel or v["transcript"] or pd.Timestamp(v["published"]) < since:
            continue
        text = fetch_transcript(vid)
        if text and Path(v["file"]).exists():
            old = Path(v["file"]).read_text()
            head = old.split("## Abschrift")[0]
            Path(v["file"]).write_text(head + "## Abschrift\n\n" + text + "\n")
            v["transcript"] = True


def update(channels: list[str] = CHANNELS, get=_get, fetch_transcript=transcript) -> list[str]:
    """Neue Videos holen und speichern. Gibt die neu geschriebenen Dateien zurück."""
    index = json.loads(INDEX.read_text()) if INDEX.exists() else {"ids": {}, "videos": {}}
    written = []
    for ch in channels:
        try:
            cid = index["ids"].get(ch) or channel_id(get(f"https://www.youtube.com/@{ch}"))
            if not cid:
                log.warning("Kanal @%s: ID nicht gefunden", ch)
                continue
            index["ids"][ch] = cid
            videos = parse_feed(get(f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"))
        except Exception as e:
            log.warning("Kanal @%s nicht abrufbar: %s", ch, e)
            continue
        retry_missing(index, ch, fetch_transcript)
        known = [v for v in index["videos"].values() if v["channel"] == ch]
        new = [v for v in videos if v["id"] not in index["videos"]]
        if not known:
            new = new[:FIRST_RUN]
        for v in reversed(new):
            text = fetch_transcript(v["id"])
            path = FOLDER / ch / f"{v['published'][:10]}_{slug(v['title']) or v['id']}.md"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(note(ch, v, text))
            index["videos"][v["id"]] = {"channel": ch, "title": v["title"], "published": v["published"],
                                        "file": str(path), "transcript": text is not None, "evaluated": False}
            written.append(str(path))
    FOLDER.mkdir(parents=True, exist_ok=True)
    INDEX.write_text(json.dumps(index, indent=1, ensure_ascii=False))
    return written
