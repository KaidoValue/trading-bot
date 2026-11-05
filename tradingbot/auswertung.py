"""Auswertung für den Profi-Bot (python -m tradingbot profi): die vorab registrierten Experimente E0 bis E6.

Jedes Fenster ist ein frischer Start mit dem Startkapital der Config (historie.simulate mit Start und Ende). Die
Kennzahlen kommen aus historie.segment, «Bitcoin halten nach Kosten» aus historie.hold_run. Varianten sind
Überlagerungen (deep merge) auf die Config des Amtsinhabers; die volle Config steht in jedem Ergebnis und geht durch
dieselbe Prüfung wie Config.load (unbekannte Schlüssel brechen ab).

Blind entwickeln: Fenster mit Tagen ab 2023-01-01 (auch ein offenes Ende bis Datenende) rechnet der Befehl nur mit
--pruefung, und jeder Lauf mit --pruefung kommt vor der Rechnung ins Prüfprotokoll (nur anhängen). Ohne --pruefung
werden alle Kurse ab 2023 vor allen Berechnungen abgeschnitten.

Ergebnisse: je Lauf (Bot und Fenster) eine JSON-Datei unter lernen/profi/<Schritt>/<Cache>/, daraus die Tabellen in
lernen/PROFI_ERGEBNISSE.md. Entschieden wird nur mit normierten Gebühren auf den Haupt-Caches (Standardquellen, z.B.
GitHub und Hirans PC); eine andere Quelle (--quellen) zählt nur zur Information.
"""
from __future__ import annotations

import copy
import json
import logging
import os
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, NamedTuple, Sequence

import numpy as np
import pandas as pd
import yaml

from . import historie
from .broker import KRAKEN_TIERS
from .chef import STYLES
from .config import Config

log = logging.getLogger(__name__)

ORDNER = Path("lernen/profi")
ERGEBNISSE = Path("lernen/PROFI_ERGEBNISSE.md")
PROTOKOLL = Path("lernen/PROFI_PRUEFPROTOKOLL.md")
SPERRE = pd.Timestamp("2023-01-01", tz="UTC")       # Kurse ab hier nur mit --pruefung
FERN = pd.Timestamp("2100-01-01", tz="UTC")
SCHRITTE = {"E0": "Messlatte", "E1": "Kern", "E2": "Sicherheitsnetz", "E3": "Wochentakt", "E4": "Grösse nachführen",
            "E5": "Robustheit", "E6": "Einmal-Prüfung"}
LEITER = ("E1", "E2", "E3", "E4")                   # Herausforderer gegen den Amtsinhaber nach Regel G
EPS = 1e-9                                          # Grenzwerte auf gerundeten Kennzahlen (0,30 + 0,05 ≤ 0,35)

# Vergleichs-Bots (Config-Dateien), Chef und Benchmark
PFADE = {"config_langfrist": "bots/config_langfrist.yaml", "config_daytrading": "bots/config_daytrading.yaml",
         "config_risiko": "bots/config_risiko.yaml", "config_phasen": "bots/config_phasen.yaml",
         "k1": "bots/profi/k1.yaml", "p_minus_1": "bots/profi/p_minus_1.yaml"}
CHEF, HALTEN, K1, P1 = "chef", "bitcoin_halten", "k1", "p_minus_1"
HEUTIGE = ("config_langfrist", "config_daytrading", "config_risiko", "config_phasen", CHEF)   # Go-Regel 6
REGEL_1 = HEUTIGE + (K1,)                                                                   # Go-Regel 1
L_DEV = REGEL_1 + (P1, HALTEN)                                                              # E0: L_dev
E1_AMT = "bots/profi/e1_kb3.yaml"                   # Amtsinhaber von E1, wenn --config fehlt
NAMEN = {"config_langfrist": "Langfrist", "config_daytrading": "KI", "config_risiko": "Risiko",
         "config_phasen": "Phasen", CHEF: "Chef", K1: "K1", P1: "P−1", HALTEN: "Bitcoin halten nach Kosten"}
ROLLEN = ("amtsinhaber", "herausforderer", "vergleich", "chef", "benchmark")


class Fenster(NamedTuple):
    """Frischer Start am Tag `start` mit dem Startkapital, letzter Tag `ende` (None = bis Datenende)."""
    name: str
    start: str
    ende: str | None = None

    @property
    def von(self) -> pd.Timestamp:
        return pd.Timestamp(self.start, tz="UTC")

    @property
    def bis(self) -> pd.Timestamp | None:
        """Erster Tag nach dem Fenster (für simulate und segment), None = offen."""
        return pd.Timestamp(self.ende, tz="UTC") + pd.Timedelta(days=1) if self.ende else None

    @property
    def gesperrt(self) -> bool:
        """Berührt Tage ab 2023-01-01 (ein offenes Ende reicht bis zum Datenende)."""
        return self.bis is None or self.bis > SPERRE


HAUPT, HAELFTEN, DRITTE = "2012-2022", ("2012-2019", "2020-2022"), "2016-2022"
STANDARD = (Fenster(HAUPT, "2012-01-01", "2022-12-31"), Fenster(HAELFTEN[0], "2012-01-01", "2019-12-31"),
            Fenster(HAELFTEN[1], "2020-01-01", "2022-12-31"))
CRASH = (Fenster("Crash-2014", "2014-01-01", "2022-12-31"), Fenster("Crash-2018", "2018-01-01", "2022-12-31"))
CRASH_2022 = Fenster("Crash-2022", "2022-01-01")             # nur mit --pruefung
PRUEFUNG = "ab-2023Q1"                                       # E6: frisch ab 01.01.2023 bis Datenende


def _quartale(von: int, bis: int) -> pd.DatetimeIndex:
    return pd.date_range(f"{von}-01-01", f"{bis}-10-01", freq="QS")


def gestaffelt() -> list[Fenster]:
    """E5 (d): 28 frische 3-Jahres-Fenster, Start vierteljährlich von 2013-Q1 bis 2019-Q4."""
    return [Fenster(f"3J-{q.year}Q{q.quarter}", f"{q:%Y-%m-%d}",
                    f"{q + pd.DateOffset(years=3) - pd.Timedelta(days=1):%Y-%m-%d}") for q in _quartale(2013, 2019)]


def gestaffelt_pruefung() -> list[Fenster]:
    """E6: 12 Starts vierteljährlich von 2023-Q1 bis 2025-Q4, jeweils bis Datenende (der erste ist das Prüffenster)."""
    return [Fenster(f"ab-{q.year}Q{q.quarter}", f"{q:%Y-%m-%d}") for q in _quartale(2023, 2025)]


def eigenes_fenster(start: str | None, ende: str | None) -> Fenster:
    """--start/--ende: ein Fenster statt der Fenster des Schritts (ohne --start ab 2012, ohne --ende bis Datenende)."""
    von = f"{pd.Timestamp(start or '2012-01-01'):%Y-%m-%d}"
    bis = f"{pd.Timestamp(ende):%Y-%m-%d}" if ende else None
    if bis is not None and bis < von:
        raise SystemExit("--start muss vor --ende liegen.")
    jahre = von[:4] if bis and von[:4] == bis[:4] else f"{von[:4]}-{(bis or '')[:4]}"
    ganz = von.endswith("-01-01") and bis is not None and bis.endswith("-12-31")
    return Fenster(jahre if ganz else f"{von}-bis-{bis or 'Ende'}", von, bis)


def plan(schritt: str, amt: str | None = None, varianten: Sequence[str] = (),
         eigenes: Fenster | None = None) -> dict[str, list[Fenster]]:
    """Vorab registriert: welcher Bot in welchen Fenstern gerechnet wird (amt, varianten: Namen wie von namen()).
    Bitcoin halten nach Kosten kommt in jedes Fenster; der Chef steht hinter den Stil-Bots, die er braucht."""
    if schritt not in SCHRITTE:
        raise SystemExit(f"Unbekannter Schritt «{schritt}» (erlaubt: {', '.join(SCHRITTE)})")
    if schritt == "E0" and varianten:
        raise SystemExit("E0 rechnet nur die Vergleichs-Bots, ohne --varianten.")
    if schritt != "E0" and not amt:
        raise SystemExit(f"{schritt}: Amtsinhaber mit --config angeben.")
    p: dict[str, list[Fenster]] = {}

    def dazu(name: str, fenster) -> None:
        liste = p.setdefault(name, [])
        for f in fenster:
            if f not in liste:
                liste.append(f)
    gp = gestaffelt_pruefung()
    if schritt == "E0":
        for b in [*PFADE, CHEF]:
            dazu(b, STANDARD[:1])
    elif schritt in LEITER:
        for b in [amt, *varianten, P1]:
            dazu(b, STANDARD)
    elif schritt == "E5":
        dritte = Fenster(DRITTE, "2016-01-01", "2022-12-31")
        dazu(amt, [STANDARD[0], dritte, *gestaffelt(), *CRASH])
        for v in varianten:
            dazu(v, STANDARD[:1])
        dazu(P1, [dritte])
    else:
        dazu(amt, [*gp, CRASH_2022])
        for v in varianten:
            dazu(v, [gp[0], CRASH_2022])
        dazu(K1, gp[:1])
        dazu(P1, [gp[0], CRASH_2022])
        for b in HEUTIGE:
            dazu(b, gp)
    if eigenes is not None:
        p = {name: [eigenes] for name in p}
    if CHEF in p:
        p[CHEF] = p.pop(CHEF)
    dazu(HALTEN, [f for fs in p.values() for f in fs])
    return p


def auswahl(p: dict[str, list[Fenster]], nur_bot: Sequence[str] | None = None,
            nur_fenster: Sequence[str] | None = None) -> dict[str, list[Fenster]]:
    """--nur-bot, --nur-fenster: nur ein Teil des Plans, z.B. ein Job einer GitHub-Matrix."""
    alle = {f.name for fs in p.values() for f in fs}
    for wahl, da, was in ((nur_bot, set(p), "Bot"), (nur_fenster, alle, "Fenster")):
        fremd = sorted(set(wahl or ()) - da)
        if fremd:
            raise SystemExit(f"{was} nicht im Plan: {', '.join(fremd)} (im Plan: {', '.join(sorted(da))})")
    out = {n: [f for f in fs if not nur_fenster or f.name in nur_fenster]
           for n, fs in p.items() if not nur_bot or n in nur_bot}
    return {n: fs for n, fs in out.items() if fs}


def sperre(fenster: Sequence[Fenster], pruefung: bool) -> None:
    """Blind entwickeln: Fenster mit Tagen ab 2023-01-01 (auch ein offenes Ende bis Datenende) nur mit --pruefung."""
    zu = sorted({f.name for f in fenster if f.gesperrt})
    if zu and not pruefung:
        raise SystemExit(f"Gesperrt: {', '.join(zu)} berühren Kurse ab 2023-01-01. Diese Jahre sind für die "
                         "Einmal-Prüfung E6 weggesperrt: nur mit --pruefung (jeder solche Lauf kommt ins Prüfprotokoll).")


# --- Configs: Überlagerungen auf den Amtsinhaber

def ueberlagern(basis: dict, ueber: dict) -> dict:
    """Deep merge: Dicts Schlüssel für Schlüssel, alles andere (auch Listen) ersetzt den Wert der Basis. Die Basis
    bleibt unverändert."""
    out = copy.deepcopy(basis)
    for k, v in (ueber or {}).items():
        out[k] = ueberlagern(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else copy.deepcopy(v)
    return out


def pruefen(raw: dict, name: str) -> Config:
    """Dieselbe Prüfung wie Config.load: unbekannte Schlüssel (auch in risk und den Horizonten) brechen ab."""
    try:
        return Config.from_dict(copy.deepcopy(raw), name)
    except TypeError as e:
        raise SystemExit(f"{name}: ungültige Config ({e})") from e


def _yaml(path) -> dict:
    if not Path(path).exists():
        raise SystemExit(f"Config {path} nicht gefunden.")
    return yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}


class Bot(NamedTuple):
    """Ein Bot eines Schritts mit seiner vollen Config (YAML-Inhalt nach allen Überlagerungen)."""
    name: str
    rolle: str                          # einer von ROLLEN
    cfg: Config | None = None
    config: dict | None = None
    dateien: tuple[str, ...] = ()       # Basis-Config, dann die Überlagerungen
    ueberlagerung: dict | None = None   # Herausforderer: seine eigene Überlagerung
    nr: int = 0                         # Herausforderer: Platz in --varianten (die einfachere zuerst)


def namen(amt: Sequence[str] = (), varianten: Sequence[str] = ()) -> tuple[str | None, list[str]]:
    """Namen aus den Dateinamen: Amtsinhaber «e1_kb3+e1_kb5» (Basis und Sieger), Herausforderer
    «e1_kb3+e1_kb5+e2_trail6»: Jeder Name sagt, woraus die Config besteht."""
    if not amt:
        return None, []
    a = "+".join(Path(f).stem for f in amt)
    return a, [f"{a}+{Path(v).stem}" for v in varianten]


def bot(name: str, amt: Sequence[str] = (), varianten: Sequence[str] = ()) -> Bot:
    """Bot `name` laden und prüfen. amt: Basis-Config des Amtsinhabers, dann die Überlagerungen früherer Sieger
    (--config, --sieger); varianten: je eine Überlagerung auf den Amtsinhaber (--varianten)."""
    a, vs = namen(amt, varianten)
    if name == a or name in vs:
        raw = _yaml(amt[0])
        for f in amt[1:]:
            raw = ueberlagern(raw, _yaml(f))
        if name == a:
            return Bot(name, "amtsinhaber", pruefen(raw, name), raw, tuple(map(str, amt)))
        i = vs.index(name)
        ueber = _yaml(varianten[i])
        raw = ueberlagern(raw, ueber)
        return Bot(name, "herausforderer", pruefen(raw, name), raw, (*map(str, amt), str(varianten[i])), ueber, i + 1)
    if name in PFADE:
        raw = _yaml(PFADE[name])
        return Bot(name, "vergleich", pruefen(raw, name), raw, (PFADE[name],))
    return Bot(name, "chef" if name == CHEF else "benchmark")


def liste(schritt: str, amt: Sequence[str] = (), varianten: Sequence[str] = (), eigenes: Fenster | None = None,
          pruefung: bool = False, nur_bot=None, nur_fenster=None) -> dict:
    """--liste: die Jobs (Bot und Fenster) für eine GitHub-Matrix, ohne zu rechnen; die Configs werden geprüft."""
    a, vs = namen(amt, varianten)
    jobs = auswahl(plan(schritt, a, vs, eigenes), nur_bot, nur_fenster)
    sperre([f for fs in jobs.values() for f in fs], pruefung)
    for n in jobs:
        bot(n, amt, varianten)
    return {"include": [{"bot": n, "fenster": f.name} for n, fs in jobs.items() for f in fs]}


# --- Herkunft: Cache, Commit, Prüfprotokoll

def cache_id(quellen: tuple = historie.SOURCES) -> str:
    """Fingerabdruck des ganzen Kurs-Caches der Quellen (alle Kursdateien dieser Börsen in data/historie): gleich für
    alle Läufe auf demselben eingefrorenen Cache, so lassen sich die Caches auseinanderhalten."""
    namen_ = {n for n, _ in quellen}
    return historie.cache_fingerprint([f for f in historie.CACHE.glob("*_*_*.csv") if f.name.split("_")[0] in namen_])


def _commit() -> tuple[str, bool]:
    """git-Commit und ob tradingbot/ und bots/ ohne ungespeicherte Änderungen sind (sonst nicht nachrechenbar)."""
    try:
        head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout
        offen = subprocess.run(["git", "status", "--porcelain", "--", "tradingbot", "bots"], capture_output=True,
                               text=True, check=True).stdout
    except (OSError, subprocess.CalledProcessError):
        return "unbekannt", False
    return head.strip(), not offen.strip()


def protokoll(befehl: str, quellen: tuple, cache: str, fest: bool, jobs: dict[str, list[Fenster]],
              pfad: Path | None = None) -> None:
    """Prüfprotokoll: Jeder Lauf mit --pruefung kommt vor der Rechnung mit Datum, Commit, Quellen,
    Cache-Fingerabdruck und Befehl dazu. Nur anhängen, nie überschreiben."""
    pfad = pfad or PROTOKOLL
    commit, sauber = _commit()
    zeilen = [f"## {datetime.now(timezone.utc):%Y-%m-%d %H:%M:%S} UTC", "",
              f"- Commit: `{commit}`" + ("" if sauber else " (tradingbot/ oder bots/ mit Änderungen ohne Commit)"),
              "- Quellen: " + ", ".join(f"{n} ({q})" for n, q in quellen),
              f"- Cache-Fingerabdruck: `{cache}`" + (" (eingefroren, --cache-fest)" if fest else " (nicht eingefroren)"),
              f"- Befehl: `{befehl}`",
              "- Läufe: " + "; ".join(f"{n}: {', '.join(f.name for f in fs)}" for n, fs in jobs.items())]
    if os.getenv("GITHUB_RUN_ID"):
        zeilen.append(f"- GitHub-Lauf: {os.getenv('GITHUB_RUN_ID')}")
    pfad.parent.mkdir(parents=True, exist_ok=True)
    neu = not pfad.exists()
    with pfad.open("a", encoding="utf-8") as f:
        if neu:
            f.write("# Profi-Bot: Prüfprotokoll\n\nJeder Lauf mit Kursen ab 2023 (`profi --pruefung`), automatisch "
                    "angehängt. Die Einmal-Prüfung E6 läuft genau einmal je Quelle.\n\n")
        f.write("\n".join(zeilen) + "\n\n")


# --- Rechnen: je Bot und Fenster ein frischer Start, eine Ergebnisdatei

def datei(schritt: str, cache: str, name: str, fenster: str, gebuehren: str) -> Path:
    """Ergebnisdatei eines Laufs: lernen/profi/<Schritt>/<Cache>/<Bot>__<Fenster>__<Gebühren>.json."""
    return ORDNER / schritt / cache[:12] / f"{name}__{fenster}__{gebuehren}.json"


def _json(d: dict) -> str:
    """Eine Zeile je Schlüssel: lesbar, und die lange Kapitalkurve bleibt eine Zeile."""
    roh = lambda o: o.item() if hasattr(o, "item") else str(o)
    return "{\n" + ",\n".join(f" {json.dumps(k)}: {json.dumps(v, ensure_ascii=False, default=roh)}"
                              for k, v in d.items()) + "\n}\n"


def _kurse(cfg: Config, laden: Callable) -> tuple[dict[str, pd.DataFrame], list[Path]]:
    """Kerzen der eigenen Coins im kürzesten Zeitraum der Horizonte, in der Reihenfolge der symbols (wie im Bot)."""
    tf = min((h.timeframe for h in cfg.horizon_list()), key=historie.TF_MS.get)
    frames, dateien = {}, []
    for coin in dict.fromkeys(s.split("/")[0] for s in cfg.symbols):
        df, benutzt = laden(coin, tf)
        dateien += benutzt
        if df is not None and len(df):
            frames[f"{coin}/USD"] = df
    if not frames:
        raise SystemExit(f"{cfg.name}: keine Kurse für {', '.join(cfg.symbols)}")
    return frames, dateien


def laden(schritt: str, amt: Sequence[str] = (), varianten: Sequence[str] = (), eigenes: Fenster | None = None,
          quellen: tuple = historie.SOURCES, fest: bool = False, nur_bot=None, nur_fenster=None) -> list[Path]:
    """--laden: die Kursdateien aller Jobs in den Cache data/historie holen, ohne zu rechnen (fehlende und solche, die
    älter als 7 Tage sind; mit --cache-fest nur prüfen, ob alle da sind). So wird der Cache vor dem ersten Lauf
    gefüllt und danach eingefroren."""
    a, vs = namen(amt, varianten)
    jobs = auswahl(plan(schritt, a, vs, eigenes), nur_bot, nur_fenster)
    exchanges, benutzt = {}, []

    def lade(coin: str, tf: str):
        return historie.load_coin(coin, tf, exchanges, quellen, fest, benutzt), []
    for n in jobs:
        if (b := bot(n, amt, varianten)).cfg is not None:
            _kurse(b.cfg, lade)
    if HALTEN in jobs or CHEF in jobs:
        lade("BTC", "1d")
    return sorted(set(benutzt))


def _notaus(run: historie.BotRun, cfg: Config, frames: dict) -> list[dict]:
    """E2: je Not-Aus-Verkauf der Kurs, die Rendite des Coins in den 90 Tagen danach (verpasste Erholung) und wann
    und zu welchem Kurs das Signal des Horizonts später verkauft hätte. None: Die Kurse reichen nicht so weit."""
    t = run.trades
    if not len(t):
        return []
    hz = {h.name: h for h in cfg.horizon_list()}
    tf = min((h.timeframe for h in hz.values()), key=historie.TF_MS.get)
    out = []
    for r in t[t["reason"] == "Not-Aus"].itertuples():
        df, zeit = frames[r.symbol], pd.Timestamp(r.closed)
        spaeter = df["close"][df.index >= zeit + pd.Timedelta(days=90)]
        h = hz.get(r.horizon, next(iter(hz.values())))
        params = {k: v for k, v in h.strategy_params.items() if k not in ("memory_file", "library_file")}
        schluss, sig, _, _ = historie._signals(h, params, cfg.allow_short, df, tf, cfg)
        verkauf = schluss[(schluss > zeit) & (sig < 0)]
        bar = df[df.index >= verkauf[0]] if len(verkauf) else df.iloc[:0]
        out.append({"tag": f"{zeit:%Y-%m-%d}", "coin": r.symbol, "kurs": round(float(r.exit), 4),
                    "rendite_90_tage_pct": round((spaeter.iloc[0] / r.exit - 1) * 100, 1) if len(spaeter) else None,
                    "linie_verkauft": f"{bar.index[0]:%Y-%m-%d}" if len(bar) else None,
                    "linie_kurs": round(float(bar["open"].iloc[0]), 4) if len(bar) else None})
    return out


def _kurve_aus(e: dict) -> pd.Series:
    s = pd.Series(e["kurve"], dtype=float)
    s.index = pd.to_datetime(s.index, utc=True)
    return s


def rechnen(schritt: str, amt: Sequence[str] = (), varianten: Sequence[str] = (), eigenes: Fenster | None = None,
            quellen: tuple = historie.SOURCES, fest: bool = False, gebuehren: str = "normiert",
            pruefung: bool = False, nur_bot=None, nur_fenster=None, befehl: str = "") -> list[Path]:
    """Rechnet die Jobs des Schritts (je Bot und Fenster ein frischer Start mit dem Startkapital), schreibt je Lauf
    eine Ergebnisdatei und baut danach PROFI_ERGEBNISSE.md neu. Der Chef braucht die Läufe der drei Stil-Bots im
    selben Fenster: aus diesem Lauf oder aus ihren Ergebnisdateien (gleicher Schritt, Cache und Gebühren)."""
    a, vs = namen(amt, varianten)
    jobs = auswahl(plan(schritt, a, vs, eigenes), nur_bot, nur_fenster)
    alle_fenster = [f for fs in jobs.values() for f in fs]
    sperre(alle_fenster, pruefung)
    bots = {n: bot(n, amt, varianten) for n in jobs}
    ref = (bots.get(a) or bot(a or "config_langfrist", amt, varianten)) if HALTEN in jobs else None  # für halten
    if pruefung:
        protokoll(befehl, quellen, cache_id(quellen), fest, jobs)
    grenze = SPERRE if not pruefung else (None if any(f.bis is None for f in alle_fenster)
                                          else max(f.bis for f in alle_fenster))
    exchanges, benutzt, daten = {}, [], {}

    def laden(coin: str, tf: str):
        if (coin, tf) not in daten:
            n = len(benutzt)
            df = historie.load_coin(coin, tf, exchanges, quellen, fest, benutzt)
            if df is not None and grenze is not None:
                df = df[df.index < grenze]
            daten[coin, tf] = df, benutzt[n:]
        return daten[coin, tf]
    frames, kursdateien = {}, {}
    for n, b in bots.items():
        if b.cfg is not None:
            frames[n], kursdateien[n] = _kurse(b.cfg, laden)
    if HALTEN in jobs or CHEF in jobs:
        btc, kursdateien[HALTEN] = laden("BTC", "1d")
        if btc is None or not len(btc):
            raise SystemExit("Keine BTC-Tageskerzen für Bitcoin halten und den Chef.")
        kursdateien[CHEF] = kursdateien[HALTEN]
    cache, (commit, sauber) = cache_id(quellen), _commit()
    kopf = {"schritt": schritt, "gebuehren": gebuehren, "quellen": [list(q) for q in quellen], "cache": cache,
            "cache_fest": fest, "commit": commit, "sauber": sauber, "befehl": befehl, "pruefung": pruefung,
            "erstellt": f"{datetime.now(timezone.utc):%Y-%m-%dT%H:%M:%SZ}"}
    fee = historie.OLD_FEE if gebuehren == "alt" else KRAKEN_TIERS[0][2]
    stil: dict = {}
    geschrieben = []
    for n, fs in jobs.items():
        b = bots[n]
        for f in fs:
            log.warning("Rechne %s, Fenster %s ...", n, f.name)
            notaus, config = [], b.config
            if n == HALTEN:
                prices = btc["close"] if f.bis is None else btc["close"][btc.index < f.bis]
                run = historie.hold_run(prices, ref.cfg.starting_capital, fee, ref.cfg.slippage, f.von)
                config = {"startkapital": ref.cfg.starting_capital, "gebuehr": fee, "slippage": ref.cfg.slippage}
            elif n == CHEF:
                runs = {}
                for s in STYLES:
                    if (s, f.name) in stil:
                        runs[s] = stil[s, f.name]
                        continue
                    pfad = datei(schritt, cache, s, f.name, gebuehren)
                    if not pfad.exists():
                        raise SystemExit(f"Chef: Lauf von {s} im Fenster {f.name} fehlt ({pfad}). Zuerst die drei "
                                         f"Stil-Bots rechnen ({', '.join(STYLES)}).")
                    e = json.loads(pfad.read_text(encoding="utf-8"))
                    runs[s] = historie.BotRun(Config(starting_capital=e["startkapital"]), _kurve_aus(e),
                                              pd.DataFrame(), 0, 0)
                capital = next(iter(runs.values())).cfg.starting_capital
                historie.CACHE.mkdir(parents=True, exist_ok=True)
                curve = historie.simulate_chef(runs, btc, historie.CACHE / "chef_sim.json", capital)
                run = historie.BotRun(Config(starting_capital=capital, name=CHEF), curve, pd.DataFrame(), 0, 0)
                config = {"stil_bots": list(STYLES), "startkapital": capital}
            else:
                run = historie.simulate(b.cfg, frames[n], f.von, gebuehren, end=f.bis)
                if schritt == "E2":
                    notaus = _notaus(run, b.cfg, frames[n])
            kz = historie.segment(run, f.von, f.bis or FERN)
            eq = run.equity
            e = kopf | {"name": n, "rolle": b.rolle, "amtsinhaber": a if b.rolle in ROLLEN[:2] else None,
                        "nr": b.nr, "fenster": f._asdict(),
                        "erster_tag": f"{eq.index[0]:%Y-%m-%d}" if len(eq) else None,
                        "letzter_tag": f"{eq.index[-1]:%Y-%m-%d}" if len(eq) else None,
                        "startkapital": run.cfg.starting_capital, "dateien": list(b.dateien),
                        "ueberlagerung": b.ueberlagerung, "config": config,
                        "kursdateien": sorted({p.name for p in kursdateien[n]}),
                        "kurs_fingerabdruck": historie.cache_fingerprint(kursdateien[n]),
                        "kennzahlen": {k: None if isinstance(v, float) and np.isnan(v) else v for k, v in kz.items()},
                        "notaus": notaus, "kurve": {f"{t:%Y-%m-%d}": round(float(v), 4) for t, v in eq.items()}}
            if n in STYLES:         # die Kurve wie in der Ergebnisdatei: so rechnet der Chef in jedem Fall gleich
                stil[n, f.name] = historie.BotRun(run.cfg, _kurve_aus(e), pd.DataFrame(), 0, 0)
            pfad = datei(schritt, cache, n, f.name, gebuehren)
            pfad.parent.mkdir(parents=True, exist_ok=True)
            pfad.write_text(_json(e), encoding="utf-8")
            geschrieben.append(pfad)
    zusammenfassen()
    return geschrieben


def bootstrap(a: pd.Series, b: pd.Series, block: int = 30, n: int = 1000, seed: int = 2026) -> float | None:
    """Gepaarter Block-Bootstrap: P(Calmar a > Calmar b). Die Tagesrenditen beider Kapitalkurven über dieselben Tage
    werden mit denselben zufälligen 30-Tage-Blöcken neu zusammengesetzt (n Ziehungen, fester Seed); Calmar = CAGR /
    |Max. DD| wie in segment(). None, wenn es keine 30 gemeinsamen Tage gibt."""
    v = pd.concat([a, b], axis=1, join="inner").to_numpy(dtype=float)
    with np.errstate(divide="ignore", invalid="ignore"):
        r = np.nan_to_num(v[1:] / v[:-1] - 1, nan=0.0, posinf=0.0, neginf=0.0)
    tage = len(r)
    if tage < block:
        return None
    starts = np.random.default_rng(seed).integers(0, tage - block + 1, size=(n, -(-tage // block)))
    jahre, besser = tage / 365.25, 0
    for teil in np.array_split(starts, max(n // 100, 1)):
        i = (teil[:, :, None] + np.arange(block)).reshape(len(teil), -1)[:, :tage]
        kurve = np.cumprod(1 + r[i], axis=1)                # Ziehung × Tag × (a, b), Start bei 1
        dd = (kurve / np.maximum.accumulate(np.maximum(kurve, 1.0), axis=1) - 1).min(axis=1)
        ende = kurve[:, -1]
        cagr = np.where(ende > 0, np.abs(ende) ** (1 / jahre) - 1, -1.0)
        calmar = np.where(dd < 0, cagr / np.where(dd < 0, -dd, 1.0), 0.0)
        besser += int((calmar[:, 0] > calmar[:, 1]).sum())
    return besser / n


# --- Entscheide auf Kennzahl-Tabellen k = {Bot: {Fenster: Kennzahlen aus segment()}} je Cache

class Ok(NamedTuple):
    """Ergebnis einer Bedingung (wahr oder falsch) mit den Zahlen dazu für die Tabelle."""
    ok: bool
    text: str = ""

    def __bool__(self) -> bool:
        return bool(self.ok)


def _wert(k: dict, name: str, fenster: str, feld: str):
    return ((k.get(name) or {}).get(fenster) or {}).get(feld)


def _mind(x, grenze) -> bool:
    """x ≥ grenze; fehlt eine Zahl, gilt die Bedingung als nicht erfüllt."""
    return x is not None and grenze is not None and x >= grenze - EPS


def _ueber(x, grenze) -> bool:
    return x is not None and grenze is not None and x > grenze + EPS


def _z(x, stellen: int = 2) -> str:
    return "–" if x is None else f"{x:.{stellen}f}"


def _vz(zeichen: tuple | None) -> str:
    return "–" if zeichen is None else "/".join({1: "+", -1: "−", 0: "0"}[x] for x in zeichen)


def _dd(k: dict, name: str, fenster: str) -> Ok:
    """Max. DD höchstens 0,6 × der von Bitcoin halten nach Kosten im selben Fenster (ab demselben Tag)."""
    dd, halten = _wert(k, name, fenster, "Max. DD %"), _wert(k, HALTEN, fenster, "Max. DD %")
    return Ok(dd is not None and halten is not None and abs(dd) <= 0.6 * abs(halten) + EPS,
              f"{_z(dd, 1)} % gegen {_z(halten, 1)} %")


def regel_g(k: dict, amt: str, her: str, p: float | None) -> dict[str, Ok]:
    """Regel G in einem Cache: ersetzt der Herausforderer den Amtsinhaber? G1 Calmar 2012-2022 mindestens Amtsinhaber
    + 0,05; G2 in keiner Hälfte (2012-2019, 2020-2022) ein tieferer Calmar; G3 Bootstrap P(Calmar besser) ≥ 0,65 (p);
    G4 Kosten ≤ 3 % pro Jahr und Umschlag ≤ 4 × Kapital pro Jahr. Fehlt eine Zahl, ist die Bedingung nicht erfüllt."""
    c = lambda n, f: _wert(k, n, f, "Calmar")
    a = c(amt, HAUPT)
    kosten, umschlag = _wert(k, her, HAUPT, "Kosten % pro Jahr"), _wert(k, her, HAUPT, "Umschlag pro Jahr")
    g = {"G1": Ok(_mind(c(her, HAUPT), None if a is None else a + 0.05), f"{_z(c(her, HAUPT))} gegen {_z(a)}"),
         "G2": Ok(all(_mind(c(her, h), c(amt, h)) for h in HAELFTEN),
                  " · ".join(f"{_z(c(her, h))} gegen {_z(c(amt, h))}" for h in HAELFTEN)),
         "G3": Ok(_mind(p, 0.65), f"P = {_z(p)}"),
         "G4": Ok(_mind(3.0, kosten) and _mind(4.0, umschlag), f"{_z(kosten)} %, {_z(umschlag)}×")}
    return g | {"besteht": Ok(all(g.values()))}


def ersetzt(ks: dict[str, dict], amt: str, her: str, p: Callable) -> bool:
    """Regel G über die Caches: nur wenn sie in jedem Haupt-Cache besteht; urteilen die Caches verschieden, bleibt
    der Amtsinhaber. p(cache, a, b): Bootstrap P(Calmar a > Calmar b) über 2012-2022."""
    return bool(ks) and all(regel_g(k, amt, her, p(c, her, amt))["besteht"] for c, k in ks.items())


def sieger(ks: dict[str, dict], amt: str, hers: Sequence[str], p: Callable) -> str:
    """Sieger einer Leiter-Stufe: Ein Herausforderer ersetzt den Amtsinhaber nur nach Regel G in allen Caches, bei
    Gleichstand bleibt der Amtsinhaber. Bestehen mehrere (hers in der Reihenfolge der Vorab-Registrierung, die
    einfachere zuerst), muss jeder weitere Regel G auch gegen den bisherigen Sieger bestehen, sonst bleibt die
    einfachere Variante."""
    best = amt
    for her in hers:
        if ersetzt(ks, amt, her, p) and (best == amt or ersetzt(ks, best, her, p)):
            best = her
    return best


def l_dev(k0: dict) -> tuple[float | None, str | None]:
    """L_dev aus E0 in einem Cache: höchster Calmar 2012-2022 von Langfrist, KI, Risiko, Phasen, Chef, K1, P−1 und
    Bitcoin halten nach Kosten. Fehlt einer davon, gibt es (noch) kein L_dev."""
    werte = {n: _wert(k0, n, HAUPT, "Calmar") for n in L_DEV}
    if any(v is None for v in werte.values()):
        return None, None
    best = max(werte, key=werte.get)
    return werte[best], best


def tor(k: dict, sieger_e1: str, ldev: float | None) -> dict[str, Ok]:
    """Tor nach E1 in einem Cache: Calmar 2012-2022 des E1-Siegers ≥ 0,85 × L_dev und Kosten ≤ 3 % pro Jahr."""
    calmar, kosten = _wert(k, sieger_e1, HAUPT, "Calmar"), _wert(k, sieger_e1, HAUPT, "Kosten % pro Jahr")
    grenze = None if ldev is None else 0.85 * ldev
    t = {"Calmar ≥ 0,85 × L_dev": Ok(_mind(calmar, grenze), f"{_z(calmar)} gegen {_z(grenze)}"),
         "Kosten ≤ 3 %": Ok(_mind(3.0, kosten), f"{_z(kosten)} %")}
    return t | {"besteht": Ok(all(t.values()))}


def e2_flagge(ks: dict[str, dict], amt: str, sieger_e2: str) -> Ok:
    """E2: Bleibt der Not-Aus (der Amtsinhaber gewinnt) und hat er 2012-2022 in einem Cache höchstens zweimal
    ausgelöst, hängt sein Vorteil an höchstens 2 Ereignissen: Flagge. Dann muss in E6 auch die Variante ohne Not-Aus
    die Go-Regeln 1-4 erfüllen."""
    n = [_wert(k, amt, HAUPT, "Not-Aus") for k in ks.values()]
    return Ok(sieger_e2 == amt and any(x is not None and x <= 2 for x in n),
              "Not-Aus 2012-2022: " + ", ".join("–" if x is None else str(x) for x in n))


def ist_kostenstress(ueberlagerung: dict | None) -> bool:
    """E5 (b): Eine Überlagerung, die nur Gebühren (fee_factor) und Slippage ändert, ist Kostenstress; alle anderen
    Herausforderer in E5 sind Nachbarwerte (a)."""
    return bool(ueberlagerung) and set(ueberlagerung) <= {"fee_factor", "slippage"}


def e5(k: dict, kandidat: str, nachbarn: Sequence[str], stress: Sequence[str],
       dritte: Sequence[dict] = ()) -> dict[str, Ok]:
    """E5-Kriterien in einem Haupt-Cache (keine Auswahl, nur bis 2022). dritte: Kennzahl-Tabellen derselben Rechnung
    auf einer dritten Quelle (Fenster 2016-2022).
    (a) Jeder Nachbarwert erreicht mindestens 75 % des Calmar 2012-2022.
    (b) Unter Kostenstress ist der Calmar mindestens so hoch wie bei Bitcoin halten nach Kosten.
    (c) Die Vorzeichen der Calmar-Unterschiede zu Bitcoin halten und zu P−1 (2016-2022) sind auf der dritten Quelle
        dieselben.
    (d) In mindestens 60 % der 28 Fenster liegt der Calmar über Bitcoin halten, und in mindestens 75 % beträgt der
        Max. DD höchstens 0,6 × Bitcoin halten.
    (e) Bei den Crash-Starts 2014 und 2018 beträgt der Max. DD höchstens 0,6 × Bitcoin halten ab demselben Tag."""
    c = lambda kk, n, f: _wert(kk, n, f, "Calmar")
    basis = c(k, kandidat, HAUPT)
    tief = min((c(k, n, HAUPT) for n in nachbarn if c(k, n, HAUPT) is not None), default=None)

    def zeichen(kk):
        w = [c(kk, n, DRITTE) for n in (kandidat, HALTEN, P1)]
        return None if None in w else (int(np.sign(round(w[0] - w[1], 6))), int(np.sign(round(w[0] - w[2], 6))))
    hier = zeichen(k)
    fenster = [f.name for f in gestaffelt()]
    besser = sum(_ueber(c(k, kandidat, f), c(k, HALTEN, f)) for f in fenster)
    flach = sum(bool(_dd(k, kandidat, f)) for f in fenster)
    crash = [_dd(k, kandidat, f.name) for f in CRASH]
    r = {"(a)": Ok(bool(nachbarn) and all(_mind(c(k, n, HAUPT), None if basis is None else 0.75 * basis)
                                          for n in nachbarn),
                   f"tiefster {_z(tief)} gegen 0,75 × {_z(basis)}" if nachbarn else "keine Nachbarwerte"),
         "(b)": Ok(bool(stress) and all(_mind(c(k, s, HAUPT), c(k, HALTEN, HAUPT)) for s in stress),
                   " · ".join(_z(c(k, s, HAUPT)) for s in stress) + f" gegen {_z(c(k, HALTEN, HAUPT))}"
                   if stress else "keine Kostenstress-Variante"),
         "(c)": Ok(hier is not None and bool(dritte) and all(zeichen(d) == hier for d in dritte),
                   f"gegen halten/P−1 hier {_vz(hier)}, dritte Quelle " + (", ".join(_vz(zeichen(d)) for d in dritte)
                                                                          or "fehlt")),
         "(d)": Ok(besser >= 0.6 * len(fenster) - EPS and flach >= 0.75 * len(fenster) - EPS,
                   f"Calmar über halten {besser} von {len(fenster)}, DD ≤ 0,6 × {flach} von {len(fenster)}"),
         "(e)": Ok(all(crash), " · ".join(x.text for x in crash))}
    return r | {"bestanden": Ok(all(r.values()))}


def _besser_als_heute(k: dict, kandidat: str, fenster: str) -> bool:
    """Go-Regel 6 in einem Fenster: Calmar höher als beim besten heutigen Bot; ist die Rendite bei beiden negativ,
    zählt die höhere Rendite."""
    heute = [b for b in HEUTIGE if b != kandidat]
    werte = [_wert(k, b, fenster, "Calmar") for b in heute]
    ck, rk = _wert(k, kandidat, fenster, "Calmar"), _wert(k, kandidat, fenster, "Rendite %")
    if None in werte or ck is None or rk is None:
        return False
    best = heute[int(np.argmax(werte))]
    rb = _wert(k, best, fenster, "Rendite %")
    return _ueber(rk, rb) if rk < 0 and rb is not None and rb < 0 else _ueber(ck, max(werte))


def go(k: dict, kandidat: str, flagge: bool = False, ohne_notaus: Sequence[str] = ()) -> dict[str, Ok]:
    """Go-Regeln von E6 in einem Haupt-Cache (frisch ab 01.01.2023 bis Datenende):
    1. Calmar ≥ bester Wert aus Langfrist, KI, Risiko, Phasen, Chef und K1, plus 0,10.
    2. Calmar ≥ Bitcoin halten nach Kosten und ≥ P−1 − 0,05.
    3. Max. DD ≤ 0,6 × Bitcoin halten, ebenso beim Crash-Start 2022.
    4. CAGR ≥ ⅓ von Bitcoin halten.
    5. Kosten ≤ 3 % pro Jahr und Kostenanteil ≤ 25 %.
    6. In mindestens 8 von 12 gestaffelten Fenstern besser als der beste heutige Bot (Langfrist, KI, Risiko,
       Phasen, Chef; nach Calmar, bei beiden negativer Rendite nach Rendite).
    7. Bei gesetzter E2-Flagge erfüllen auch die Varianten ohne Not-Aus die Regeln 1-4."""
    f = PRUEFUNG
    c = lambda n: _wert(k, n, f, "Calmar")
    andere = [c(b) for b in REGEL_1 if b != kandidat]
    r1 = None if None in andere else max(andere) + 0.10
    p1 = None if c(P1) is None else c(P1) - 0.05
    cagr, cagr_h = _wert(k, kandidat, f, "pro Jahr %"), _wert(k, HALTEN, f, "pro Jahr %")
    kosten, anteil = _wert(k, kandidat, f, "Kosten % pro Jahr"), _wert(k, kandidat, f, "Kostenanteil am Bruttogewinn %")
    dd, crash = _dd(k, kandidat, f), _dd(k, kandidat, CRASH_2022.name)
    besser = sum(_besser_als_heute(k, kandidat, x.name) for x in gestaffelt_pruefung())
    r = {"1": Ok(_mind(c(kandidat), r1), f"{_z(c(kandidat))} gegen {_z(r1)}"),
         "2": Ok(_mind(c(kandidat), c(HALTEN)) and _mind(c(kandidat), p1),
                 f"{_z(c(kandidat))} gegen halten {_z(c(HALTEN))}, P−1 − 0,05 {_z(p1)}"),
         "3": Ok(dd.ok and crash.ok, f"{dd.text}; Crash 2022 {crash.text}"),
         "4": Ok(_mind(cagr, None if cagr_h is None else cagr_h / 3), f"{_z(cagr, 1)} % gegen ⅓ × {_z(cagr_h, 1)} %"),
         "5": Ok(_mind(3.0, kosten) and _mind(25.0, anteil), f"{_z(kosten)} %/Jahr, Kostenanteil {_z(anteil, 1)} %"),
         "6": Ok(besser >= 8, f"{besser} von 12")}
    if not flagge:
        r["7"] = Ok(True, "keine E2-Flagge")
    else:
        teil = {v: all(go(k, v)[i] for i in "1234") for v in ohne_notaus}
        r["7"] = Ok(bool(teil) and all(teil.values()),
                    ", ".join(f"{_label(v)} {'✓' if x else '✗'}" for v, x in teil.items()) or "Variante fehlt")
    return r | {"Go": Ok(all(r.values()))}


def sonderfall_p1(k: dict, kandidat: str) -> dict[str, Ok]:
    """Ist P−1 im Prüffenster um mehr als 0,05 besser (Calmar), ist es ein No-Go für den Kandidaten; P−1 wird dann
    vorgeschlagen, falls es die Go-Regeln 1 und 3-5 erfüllt."""
    ck, cp = _wert(k, kandidat, PRUEFUNG, "Calmar"), _wert(k, P1, PRUEFUNG, "Calmar")
    g = go(k, P1)
    return {"P−1 besser um mehr als 0,05": Ok(_ueber(cp, None if ck is None else ck + 0.05),
                                             f"{_z(cp)} gegen {_z(ck)}"),
            "P−1 erfüllt die Regeln 1 und 3-5": Ok(all(g[i] for i in "1345"),
                                                  " ".join(f"{i}{'✓' if g[i] else '✗'}" for i in "1345"))}


# --- Zusammenfassen: alle Ergebnisdateien zu lernen/PROFI_ERGEBNISSE.md

SPALTEN = {"pro Jahr %": "CAGR %", "Max. DD %": "Max. DD %", "Calmar": "Calmar", "Trades": "Trades",
           "Gebühren bezahlt": "Gebühren", "Kosten % pro Jahr": "Kosten %/Jahr", "Umschlag pro Jahr": "Umschlag/Jahr",
           "Ø investiert %": "Ø investiert %", "Kostenanteil am Bruttogewinn %": "Kostenanteil %",
           "Not-Aus": "Not-Aus"}


TITEL = {"G1": "G1 Calmar +0,05", "G2": "G2 keine Hälfte schlechter", "G3": "G3 Bootstrap ≥ 0,65",
         "G4": "G4 Kosten ≤ 3 %, Umschlag ≤ 4×",
         "(a)": "(a) Nachbarwerte ≥ 75 % des Calmar", "(b)": "(b) Kostenstress ≥ Bitcoin halten",
         "(c)": "(c) dritte Quelle mit gleichen Vorzeichen", "(d)": "(d) 28 Fenster: ≥ 60 % über halten, ≥ 75 % DD ≤ 0,6×",
         "(e)": "(e) Crash-Starts: DD ≤ 0,6 × halten",
         "1": "1. Calmar ≥ bester Vergleichs-Bot + 0,10", "2": "2. Calmar ≥ halten und ≥ P−1 − 0,05",
         "3": "3. Max. DD ≤ 0,6 × halten, auch Crash 2022", "4": "4. CAGR ≥ ⅓ von halten",
         "5": "5. Kosten ≤ 3 %, Kostenanteil ≤ 25 %", "6": "6. in ≥ 8 von 12 Fenstern besser als der beste heutige Bot",
         "7": "7. bei E2-Flagge: ohne Not-Aus erfüllt 1-4"}


def _label(name: str) -> str:
    return NAMEN.get(name, name)


def _zelle(x: Ok) -> str:
    return ("✓" if x else "✗") + (f" {x.text}" if x.text else "")


def _tabelle(zeilen: dict[str, dict]) -> str:
    return historie._md(pd.DataFrame.from_dict(zeilen, orient="index"))


def lesen(ordner: Path | None = None) -> list[dict]:
    """Alle Ergebnisdateien unter lernen/profi/."""
    return [json.loads(p.read_text(encoding="utf-8")) for p in sorted(Path(ordner or ORDNER).rglob("*.json"))]


def _ordnung(e: dict):
    """Hauptfenster (2012-2022 bzw. ab 2023) zuerst, dann nach Start und Ende; je Fenster nach Rolle."""
    f = e["fenster"]
    return (f["name"] not in (HAUPT, PRUEFUNG), f["start"], f["ende"] or "9999", ROLLEN.index(e["rolle"]), e["nr"],
            e["name"])


def tabelle_kennzahlen(eintraege: list[dict]) -> str:
    """Kennzahlen je Lauf (Fenster und Bot), dazu der Calmar-Unterschied zu Bitcoin halten nach Kosten und zu P−1 im
    selben Fenster."""
    calmar = {(e["fenster"]["name"], e["name"]): e["kennzahlen"].get("Calmar") for e in eintraege}
    zeilen, index = [], []
    for e in sorted(eintraege, key=_ordnung):
        f, kz = e["fenster"]["name"], e["kennzahlen"]
        zeile = {"Fenster": f if e["fenster"]["ende"] else f"{f} (bis {e['letzter_tag'] or '–'})"}
        zeile |= {spalte: kz.get(k) for k, spalte in SPALTEN.items()}
        for ref, spalte in ((HALTEN, "Δ Calmar halten"), (P1, "Δ Calmar P−1")):
            x, y = kz.get("Calmar"), calmar.get((f, ref))
            zeile[spalte] = round(x - y, 2) if e["name"] != ref and x is not None and y is not None else None
        zeilen.append(zeile)
        index.append(_label(e["name"]))
    return historie._md(pd.DataFrame(zeilen, index=index))


def bericht(erg: list[dict]) -> str:
    """Tabellen aus allen Ergebnisdateien: Kennzahlen je Schritt, Cache und Gebühren, dazu L_dev (E0), Regel G, Sieger
    und Tor (E1-E4), E5-Kriterien und Go-Regeln (E6), je Haupt-Cache und über die Caches."""
    idx = {(e["schritt"], e["cache"], e["gebuehren"], e["name"], e["fenster"]["name"]): e for e in erg}
    standard = [list(q) for q in historie.SOURCES]
    caches: dict[str, dict] = {}
    for e in erg:
        c = caches.setdefault(e["cache"], {"quellen": e["quellen"], "boersen": set(), "fest": True, "laeufe": 0})
        c["boersen"] |= {d.split("_")[0] for d in e["kursdateien"]}
        c["fest"] &= bool(e["cache_fest"])
        c["laeufe"] += 1
    haupt = sorted(c for c, v in caches.items() if v["quellen"] == standard)
    zusatz = sorted(c for c in caches if c not in haupt)

    def kz(schritt: str, cache: str) -> dict:
        k: dict = {}
        for (s, c, g, n, f), e in idx.items():
            if s == schritt and c == cache and g == "normiert":
                k.setdefault(n, {})[f] = e["kennzahlen"]
        return k

    def ks(schritt: str) -> dict[str, dict]:
        return {c: k for c in haupt if (k := kz(schritt, c))}
    memo: dict = {}

    def p(schritt: str, fenster: str = HAUPT) -> Callable:
        def wahrscheinlich(cache: str, a: str, b: str):
            if (schritt, cache, a, b, fenster) not in memo:
                ea, eb = (idx.get((schritt, cache, "normiert", n, fenster)) for n in (a, b))
                memo[schritt, cache, a, b, fenster] = bootstrap(_kurve_aus(ea), _kurve_aus(eb)) if ea and eb else None
            return memo[schritt, cache, a, b, fenster]
        return wahrscheinlich

    def bots(schritt: str, rolle: str, amt: str | None = None) -> list[str]:
        es = {e["name"]: e for e in erg if e["schritt"] == schritt and e["rolle"] == rolle
              and (amt is None or e["amtsinhaber"] == amt)}
        return [n for n, _ in sorted(es.items(), key=lambda x: (x[1]["nr"], x[0]))]
    kurz = lambda c: f"Cache {c[:12]}"
    out = ["# Profi-Bot: Ergebnisse der Auswertung", "",
           f"Aus {len(erg)} Ergebnisdateien in `lernen/profi/` (`python -m tradingbot profi --zusammenfassen`). Jedes "
           "Fenster ist ein frischer Start mit dem Startkapital. Calmar = CAGR / |Max. DD|. Entschieden wird nach den "
           "vorab registrierten Regeln, nur mit normierten Gebühren und in jedem Haupt-Cache; andere Quellen zählen "
           "nur zur Information. ✓ erfüllt, ✗ nicht erfüllt oder Zahl fehlt (–).", "", "## Caches", ""]
    out += [_tabelle({kurz(c): {"Quellen": ", ".join(f"{n} ({q})" for n, q in caches[c]["quellen"]),
                                "Börsen der Kursdateien": ", ".join(sorted(caches[c]["boersen"])) or "–",
                                "eingefroren": "ja" if caches[c]["fest"] else "nein",
                                "Läufe": caches[c]["laeufe"],
                                "zählt für": "Entscheide" if c in haupt else "nur Information"}
                     for c in haupt + zusatz}), ""]
    if len(haupt) == 1:
        out += ["Nur ein Haupt-Cache: Die Entscheide stützen sich auf eine einzige Datenquelle (Schwäche).", ""]

    # Leiter zuerst entscheiden: E1 braucht für das Tor L_dev aus E0, E6 die Flagge aus E2
    leiter, flagge = {}, Ok(False, "E2 nicht gerechnet")
    for s in LEITER:
        gruppen = {a: bots(s, "herausforderer", a) for a in bots(s, "amtsinhaber")}
        if not gruppen:
            continue
        je = {a: sieger(ks(s), a, hers, p(s)) for a, hers in gruppen.items()}
        wurzel = next((a for a in gruppen if all(a not in h for h in gruppen.values())), next(iter(gruppen)))
        weg = [wurzel]
        while je[weg[-1]] in gruppen and je[weg[-1]] not in weg:
            weg.append(je[weg[-1]])
        leiter[s] = (gruppen, je, je[weg[-1]], wurzel)
        if s == "E2":
            flagge = e2_flagge(ks(s), wurzel, je[wurzel])

    for s, titel in SCHRITTE.items():
        eintraege = [e for e in erg if e["schritt"] == s]
        if not eintraege:
            continue
        out += [f"## {s} {titel}", ""]
        for c in haupt + zusatz:
            for g in sorted({e["gebuehren"] for e in eintraege if e["cache"] == c}):
                teil = [e for e in eintraege if e["cache"] == c and e["gebuehren"] == g]
                out += [f"### Kennzahlen: {kurz(c)}, Gebühren {g}", "", tabelle_kennzahlen(teil), ""]
        k = ks(s)
        if s == "E0":
            werte = {kurz(c): l_dev(x) for c, x in k.items()}
            out += ["### L_dev (höchster Calmar 2012-2022 der Vergleichs-Bots)", "",
                    _tabelle({c: {"L_dev": _z(v), "Bot": _label(n) if n else "E0 unvollständig"}
                              for c, (v, n) in werte.items()}) if werte else "Keine Läufe auf einem Haupt-Cache.", ""]
            for c in haupt + zusatz:
                paar: dict = {}
                for e in sorted(eintraege, key=_ordnung):
                    if e["cache"] == c:
                        paar.setdefault(e["fenster"]["name"], {}).setdefault(e["name"], {})[e["gebuehren"]] = \
                            e["kennzahlen"]
                for fenster, je_bot in paar.items():
                    zeilen = {_label(n): {f"{spalte} {g}": x[g].get(feld) for feld, spalte in SPALTEN.items()
                                          if spalte in ("CAGR %", "Calmar", "Kosten %/Jahr") for g in ("alt", "normiert")}
                              for n, x in je_bot.items() if {"alt", "normiert"} <= set(x)}
                    if zeilen:
                        out += [f"### Alte (fest 0,26 %) gegen normierte Kosten: {kurz(c)}, {fenster}", "",
                                _tabelle(zeilen), ""]
        elif s in leiter:
            gruppen, je, final, wurzel = leiter[s]
            for a, hers in gruppen.items():
                zeilen = {}
                gut = [h for h in hers if ersetzt(k, a, h, p(s))]     # bestehen mehrere: auch gegeneinander
                for her, gegen in [(h, a) for h in hers] + [(h, v) for i, v in enumerate(gut) for h in gut[i + 1:]]:
                    for c, x in k.items():
                        g = regel_g(x, gegen, her, p(s)(c, her, gegen))
                        zeilen[f"{_label(her)}{'' if gegen == a else ' gegen ' + _label(gegen)} · {kurz(c)}"] = {
                            TITEL.get(n, n): _zelle(v) for n, v in g.items()}
                out += [f"### Regel G gegen den Amtsinhaber {_label(a)}", "",
                        _tabelle(zeilen) if zeilen else "Keine Herausforderer.", "",
                        f"**Sieger: {_label(je[a])}**" + (" (der Amtsinhaber bleibt)" if je[a] == a else ""), ""]
            out += [f"**Sieger von {s}: {_label(final)}**", ""]
            if s == "E1":
                k0 = ks("E0")
                t = {kurz(c): tor(x, final, l_dev(k0.get(c, {}))[0]) for c, x in k.items()}
                bestanden = bool(t) and all(v["besteht"] for v in t.values())
                out += ["### Tor nach E1", "",
                        _tabelle({c: {n: _zelle(v) for n, v in x.items()} for c, x in t.items()}) if t else "–",
                        "", "**Tor bestanden:** weiter mit E2." if bestanden else
                        "**Tor nicht bestanden:** Die Leiter wird abgebrochen; E6 prüft nur P−1 und K1 als Kandidaten.",
                        ""]
            if s == "E2":
                notaus = {f"{kurz(e['cache'])} · {x['tag']} {x['coin']}":
                          {"Kurs": x["kurs"], "Rendite 90 Tage danach %": x["rendite_90_tage_pct"],
                           "Linie verkauft am": x["linie_verkauft"], "zum Kurs": x["linie_kurs"]}
                          for e in eintraege if e["name"] == wurzel and e["fenster"]["name"] == HAUPT
                          and e["gebuehren"] == "normiert" and e["cache"] in haupt for x in e["notaus"]}
                out += ["### Not-Aus des Amtsinhabers 2012-2022", "",
                        _tabelle(notaus) if notaus else "Kein Not-Aus.", "",
                        f"**E2-Flagge: {'gesetzt' if flagge else 'nicht gesetzt'}** ({flagge.text}).", ""]
        elif s == "E5":
            for kand in bots(s, "amtsinhaber"):
                hers = bots(s, "herausforderer", kand)
                ueber = {n: next(e["ueberlagerung"] for e in eintraege if e["name"] == n) for n in hers}
                stress = [n for n in hers if ist_kostenstress(ueber[n])]
                dritte = [kz(s, c) for c in zusatz if kz(s, c)]
                r = {kurz(c): e5(x, kand, [n for n in hers if n not in stress], stress, dritte) for c, x in k.items()}
                bestanden = bool(r) and all(v["bestanden"] for v in r.values())
                out += [f"### E5-Kriterien für {_label(kand)}", "",
                        _tabelle({TITEL.get(n, n): {c: _zelle(v[n]) for c, v in r.items()} for n in next(iter(r.values()))})
                        if r else "Keine Läufe auf einem Haupt-Cache.", "",
                        f"**E5 {'bestanden' if bestanden else 'nicht bestanden'}**" +
                        ("" if bestanden else ": zurück zum E1-Sieger und nur diesen prüfen, keine neuen Varianten."),
                        ""]
        elif s == "E6":
            for kand in bots(s, "amtsinhaber"):
                ohne = bots(s, "herausforderer", kand)
                r = {kurz(c): go(x, kand, bool(flagge), ohne) | sonderfall_p1(x, kand) for c, x in k.items()}
                regeln = bool(r) and all(v["Go"] for v in r.values())
                p1 = any(v["P−1 besser um mehr als 0,05"] for v in r.values())
                vorschlag = p1 and all(v["P−1 erfüllt die Regeln 1 und 3-5"] for v in r.values())
                entscheid = ("Go" if regeln and not p1 else
                             "No-Go für den Kandidaten, Vorschlag P−1" if vorschlag else "No-Go")
                out += [f"### Go-Regeln für {_label(kand)}", "",
                        _tabelle({TITEL.get(n, n): {c: _zelle(v[n]) for c, v in r.items()} for n in next(iter(r.values()))})
                        if r else "Keine Läufe auf einem Haupt-Cache.", "", f"**Entscheid: {entscheid}**", ""]
                info = {}
                for c, x in k.items():
                    info[kurz(c)] = {"Bootstrap P(besser als halten)": _z(p(s, PRUEFUNG)(c, kand, HALTEN))}
                hier = {c: [np.sign(round(d, 6)) for d in _regel_2(x, kand)] for c, x in k.items()}
                for c in zusatz:
                    if x := kz(s, c):
                        zeichen = [np.sign(round(d, 6)) for d in _regel_2(x, kand)]
                        anders = [kurz(h) for h, z in hier.items() if z and zeichen and z != zeichen]
                        info[kurz(c)] = {"Bootstrap P(besser als halten)": _z(p(s, PRUEFUNG)(c, kand, HALTEN)),
                                         "Warnung": ("Regel 2 mit anderem Vorzeichen als " + ", ".join(anders))
                                         if anders else "–"}
                out += ["Nur zur Information (dritte Quelle und Bootstrap):", "", _tabelle(info), ""] if info else []
    return "\n".join(out)


def _regel_2(k: dict, kandidat: str) -> list[float]:
    """Abstände von Go-Regel 2 (Calmar gegen Bitcoin halten und gegen P−1 − 0,05); leer, wenn eine Zahl fehlt."""
    w = [_wert(k, n, PRUEFUNG, "Calmar") for n in (kandidat, HALTEN, P1)]
    return [] if None in w else [w[0] - w[1], w[0] - w[2] + 0.05]


def zusammenfassen(ordner: Path | None = None, ziel: Path | None = None) -> str:
    """PROFI_ERGEBNISSE.md aus allen Ergebnisdateien neu bauen, ohne zu simulieren. Schreibt nie lernen/HISTORIE.md."""
    text = bericht(lesen(ordner))
    ziel = Path(ziel or ERGEBNISSE)
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(text + "\n", encoding="utf-8")
    return text
