"""Wächter für stille Fehler: Jeder Fehler eines Bot-Laufs kommt mit Zeit in ein Fehler-Protokoll, das die Übersicht
liest. Je Bot daten/logs/fehler_<Name>.txt (bot.py), für den ganzen Lauf fehler_zyklus.txt (scripts/zyklus.sh).

Eine Zeile: «JJJJ-MM-TT HH:MM UTC | Fehlerart | Meldung». Die Übersicht warnt oben (und auf der Kachel der
Trading-Oberfläche), wenn ein Stand älter als 90 Minuten ist oder der letzte Fehler keine 2 Stunden zurückliegt.
"""
from __future__ import annotations

import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path

log = logging.getLogger(__name__)

ZEILEN = 100                        # so viele Zeilen behält ein Fehler-Protokoll
FENSTER = timedelta(hours=2)        # so lange warnt die Übersicht nach einem Fehler
ALT = timedelta(minutes=90)         # älterer Stand: der Bot hängt (er speichert alle 30 Min.)
ZYKLUS = Path("daten/logs/fehler_zyklus.txt")


def melden(path: Path, e: BaseException, wo: str = "") -> None:
    """Eine Zeile anhängen, die letzten ZEILEN bleiben. Geht das nicht, nur eine Warnung: Der Wächter selbst darf den
    Bot nie stoppen."""
    try:
        text = " ".join(f"{wo}{e}".split())[:200]
        zeile = f"{datetime.now(timezone.utc):%Y-%m-%d %H:%M} UTC | {type(e).__name__} | {text}"
        path.parent.mkdir(parents=True, exist_ok=True)
        alt = path.read_text(encoding="utf-8", errors="replace").splitlines() if path.exists() else []
        path.write_text("\n".join((alt + [zeile])[-ZEILEN:]) + "\n", encoding="utf-8")
    except Exception as err:            # z.B. Datei gesperrt oder Platte voll
        log.warning("Fehler-Protokoll %s nicht schreibbar: %s", path, err)


def letzter(path: Path) -> tuple[datetime, str, str] | None:
    """Letzter Eintrag als (Zeit, Fehlerart bzw. Schritt, Meldung); None ohne Datei oder lesbaren Eintrag."""
    try:
        zeile = [z for z in path.read_text(encoding="utf-8", errors="replace").splitlines() if z.strip()][-1]
        zeit, art, text = (zeile.split(" | ", 2) + ["", ""])[:3]
        return datetime.strptime(zeit, "%Y-%m-%d %H:%M UTC").replace(tzinfo=timezone.utc), art, text
    except (OSError, IndexError, ValueError):
        return None
