"""Kurs-Cache auf Lücken prüfen (nur lesen).

Liest alle Kursdateien «börse_COIN_tf.csv» in einem Ordner (Standard: data/historie) und meldet je Datei: erste und
letzte Kerze, Anzahl Kerzen, fehlende Kerzen (Zeitsprünge grösser als der Kerzenabstand) und lange Strecken ohne
Handel (Volumen 0 oder Kurs steht still). Dazu: fehlende Kerzen je Jahr, alle Lücken ab 2023, die Kerzen vor und
nach grossen Lücken, eine Plausibilitätsprüfung der Kerzen und die Prüfsummen. Schreibt kurs_luecken.md und
kurs_luecken.json in den Ausgabeordner und gibt den Bericht aus. Ändert keine Kursdatei, lädt nichts nach und
rechnet keine Simulation.

Aufruf: python scripts/kurs_luecken.py [--cache data/historie] [--aus ausgabe]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

import pandas as pd

SEKUNDEN = {"30m": 1800, "1h": 3600, "4h": 14400, "1d": 86400}
HAUPTQUELLEN = ("bitstamp", "binance", "binanceus", "kucoin")      # wie historie.SOURCES: zählen für den Fingerabdruck
STILL_TAGE = 3            # Strecken ohne Handel ab dieser Länge melden
DETAIL_TAGE = 1.0         # Lücken ab dieser Dauer einzeln auflisten
DETAIL_MAX = 25           # höchstens so viele Lücken je Datei einzeln (die längsten)
AB_PRUEFJAHRE = pd.Timestamp("2023-01-01", tz="UTC")      # ab hier die Jahre der Einmal-Prüfung
AB_MAX = 60               # höchstens so viele Lücken ab 2023 je Datei einzeln (nach Zeit)
GROSS_TAGE = 30           # um Lücken ab dieser Dauer die Kerzen davor und danach zeigen
OHLC = ("open", "high", "low", "close")


def fingerabdruck(dateien) -> str:
    """Gleich gerechnet wie historie.cache_fingerprint: je Datei «Name SHA-256», darüber SHA-256."""
    h = hashlib.sha256()
    for f in sorted({Path(f) for f in dateien}, key=lambda f: (f.name, str(f))):
        h.update(f"{f.name} {hashlib.sha256(f.read_bytes()).hexdigest()}\n".encode())
    return h.hexdigest()


def _tag(t) -> str:
    return pd.Timestamp(t).strftime("%Y-%m-%d %H:%M")


def pruefe(pfad: Path) -> dict:
    """Befund für eine Kursdatei."""
    teile = pfad.stem.split("_")
    boerse, coin, tf = teile[0], "_".join(teile[1:-1]), teile[-1]
    aus = {"datei": pfad.name, "boerse": boerse, "coin": coin, "kerzen_abstand": tf,
           "sha256": hashlib.sha256(pfad.read_bytes()).hexdigest()}
    if tf not in SEKUNDEN:
        return aus | {"fehler": f"unbekannter Kerzenabstand «{tf}»"}
    df = pd.read_csv(pfad, index_col=0, parse_dates=True)
    if df.empty:
        return aus | {"fehler": "Datei ohne Kerzen"}
    idx = pd.DatetimeIndex(pd.to_datetime(df.index, utc=True))
    df.index = idx
    doppelt, unsortiert = int(idx.duplicated().sum()), not idx.is_monotonic_increasing
    df = df[~df.index.duplicated()].sort_index()
    schritt = pd.Timedelta(seconds=SEKUNDEN[tf])
    zeiten = df.index.to_series()
    abstand = zeiten.diff()
    spruenge = abstand[abstand > schritt]
    close = df["close"] if "close" in df.columns else None
    luecken, je_jahr, ab_pruefjahre, umgebung = [], {}, [], []
    spalten = [s for s in (*OHLC, "volume") if s in df.columns]
    for nach, d in spruenge.items():
        vor = nach - d
        eintrag = {"letzte_kerze_davor": _tag(vor), "erste_kerze_danach": _tag(nach),
                   "fehlende_kerzen": int(round(d / schritt)) - 1,
                   "dauer_tage": round((d - schritt) / pd.Timedelta(days=1), 2)}
        if close is not None and close.loc[vor] > 0:
            eintrag |= {"kurs_davor": float(close.loc[vor]), "kurs_danach": float(close.loc[nach]),
                        "sprung_prozent": round((float(close.loc[nach]) / float(close.loc[vor]) - 1) * 100, 1)}
        luecken.append(eintrag)
        fehlende_zeiten = pd.date_range(vor + schritt, periods=eintrag["fehlende_kerzen"], freq=schritt)
        for jahr, anzahl in pd.Series(fehlende_zeiten.year).value_counts().items():
            je_jahr[int(jahr)] = je_jahr.get(int(jahr), 0) + int(anzahl)
        if nach >= AB_PRUEFJAHRE:                     # die Lücke endet in den Jahren der Einmal-Prüfung
            ab_pruefjahre.append(eintrag)
        if eintrag["dauer_tage"] >= GROSS_TAGE:
            teil = pd.concat([df.loc[:vor].tail(3), df.loc[nach:].head(3)])
            umgebung.append({"luecke": f"{_tag(vor)} bis {_tag(nach)}",
                             "kerzen": [{"zeit": _tag(t)} | {s: float(z[s]) for s in spalten}
                                        for t, z in teil.iterrows()]})
    luecken.sort(key=lambda e: -e["fehlende_kerzen"])
    # Plausibilität: leere oder unmögliche Kerzen und die grössten Bewegungen (ohne Sprünge über Lücken)
    plausibel = None
    if set(OHLC) <= set(df.columns):
        ohlc = df[list(OHLC)]
        o, h, l, c = (ohlc[s] for s in OHLC)
        aend = (c / c.shift() - 1)[(abstand == schritt) & (c.shift() > 0)].dropna()
        spanne = (h / l - 1)[l > 0].dropna()
        plausibel = {"ohne_wert": int(ohlc.isna().any(axis=1).sum()),
                     "nicht_positiv": int((ohlc <= 0).any(axis=1).sum()),
                     "hoch_unter_tief": int((h < l).sum()),
                     "ausserhalb_der_spanne": int(((c > h) | (c < l) | (o > h) | (o < l)).sum())}
        if len(aend):
            plausibel |= {"groesster_anstieg": {"zeit": _tag(aend.idxmax()), "prozent": round(float(aend.max()) * 100, 1)},
                          "groesster_rueckgang": {"zeit": _tag(aend.idxmin()), "prozent": round(float(aend.min()) * 100, 1)}}
        if len(spanne):
            plausibel["groesste_spanne"] = {"zeit": _tag(spanne.idxmax()), "prozent": round(float(spanne.max()) * 100, 1)}
    erwartet = int(round((df.index[-1] - df.index[0]) / schritt)) + 1
    fehlend = sum(e["fehlende_kerzen"] for e in luecken)
    # Strecken ohne Handel: Volumen 0, oder Kerze ohne Bewegung auf dem Schlusskurs der Vorkerze
    still = pd.Series(False, index=df.index)
    if "volume" in df.columns:
        still |= df["volume"].fillna(0) <= 0
    if {"high", "low", "close"} <= set(df.columns):
        still |= (df["high"] == df["low"]) & (df["close"] == df["close"].shift())
    strecken, gruppe = [], (still != still.shift()).cumsum()
    grenze = max(3, int(STILL_TAGE * 86400 / SEKUNDEN[tf]))
    for _, teil in still[still].groupby(gruppe[still]):
        if len(teil) >= grenze:
            strecken.append({"von": _tag(teil.index[0]), "bis": _tag(teil.index[-1]), "kerzen": int(len(teil)),
                             "dauer_tage": round(len(teil) * SEKUNDEN[tf] / 86400, 2)})
    strecken.sort(key=lambda e: -e["kerzen"])
    return aus | {
        "erste_kerze": _tag(df.index[0]), "letzte_kerze": _tag(df.index[-1]), "kerzen": int(len(df)),
        "kerzen_erwartet": erwartet, "kerzen_fehlend": int(fehlend),
        "fehlend_prozent": round(100 * fehlend / erwartet, 2) if erwartet else 0.0,
        "doppelte_zeilen": doppelt, "unsortiert": bool(unsortiert),
        "luecken_anzahl": len(luecken), "luecken_ab_1_tag": sum(e["dauer_tage"] >= DETAIL_TAGE for e in luecken),
        "groesste_luecke": luecken[0] if luecken else None,
        "luecken": [e for e in luecken if e["dauer_tage"] >= DETAIL_TAGE][:DETAIL_MAX],
        "ohne_handel_anzahl": len(strecken), "ohne_handel": strecken[:DETAIL_MAX],
        "fehlend_je_jahr": {str(j): je_jahr[j] for j in sorted(je_jahr)},
        "luecken_ab_2023_anzahl": len(ab_pruefjahre),
        "fehlend_ab_2023": sum(n for j, n in je_jahr.items() if j >= AB_PRUEFJAHRE.year),
        "luecken_ab_2023": sorted(ab_pruefjahre, key=lambda e: e["erste_kerze_danach"])[:AB_MAX],
        "kerzen_um_grosse_luecken": umgebung, "plausibilitaet": plausibel,
    }


def pruefe_sicher(pfad: Path) -> dict:
    """Wie pruefe; eine unlesbare Datei kommt als Fehlerzeile in den Bericht und stoppt die anderen nicht."""
    try:
        return pruefe(pfad)
    except Exception as e:
        return {"datei": pfad.name, "fehler": f"nicht lesbar ({type(e).__name__}: {e})"}


def bericht(befunde: list[dict], kopf: dict) -> str:
    z = ["# Kurs-Cache der Profi-Prüfung: Lücken", "",
         f"Ordner `{kopf['ordner']}`, {kopf['dateien']} Kursdateien. Fingerabdruck der Hauptquellen: "
         f"`{kopf['fingerabdruck_hauptquellen']}`"
         + {True: " (stimmt mit lernen/profi/cache_github.txt überein).", False: " (WEICHT AB von "
            "lernen/profi/cache_github.txt).", None: " (kein Vergleichswert gefunden)."}[kopf["fingerabdruck_stimmt"]],
         "", "Lücke = Zeitsprung zwischen zwei Kerzen, der grösser ist als der Kerzenabstand. «Ohne Handel» = "
         f"mindestens {STILL_TAGE} Tage mit Volumen 0 oder stehendem Kurs.", "",
         "| Datei | erste Kerze | letzte Kerze | Kerzen | fehlend | Lücken ab 1 Tag | grösste Lücke | Kurs davor → danach "
         "| längste Strecke ohne Handel |", "|---|---|---|---:|---:|---:|---|---|---|"]
    for b in befunde:
        if "fehler" in b:
            z.append(f"| {b['datei']} | {b['fehler']} | | | | | | | |")
            continue
        g, s = b["groesste_luecke"], (b["ohne_handel"][0] if b["ohne_handel"] else None)
        hinweis = ((f" (doppelte Zeilen: {b['doppelte_zeilen']})" if b["doppelte_zeilen"] else "")
                   + (" (unsortiert)" if b["unsortiert"] else ""))
        z.append(
            f"| {b['datei']}{hinweis} | {b['erste_kerze'][:10]} | {b['letzte_kerze'][:10]} | {b['kerzen']} | "
            f"{b['kerzen_fehlend']} ({b['fehlend_prozent']} %) | {b['luecken_ab_1_tag']} | "
            + (f"{g['dauer_tage']} Tage ({g['letzte_kerze_davor'][:10]} bis {g['erste_kerze_danach'][:10]})" if g else "keine")
            + " | " + (f"{g['kurs_davor']:.6g} → {g['kurs_danach']:.6g} ({g['sprung_prozent']:+.1f} %)"
                       if g and "sprung_prozent" in g else "")
            + " | " + (f"{s['dauer_tage']} Tage ({s['von'][:10]} bis {s['bis'][:10]})" if s else "keine") + " |")
    for b in befunde:
        if b.get("luecken"):
            z += ["", f"## {b['datei']}: Lücken ab 1 Tag (längste zuerst, höchstens {DETAIL_MAX})", "",
                  "| letzte Kerze davor | erste Kerze danach | fehlende Kerzen | Tage | Kurs davor → danach |",
                  "|---|---|---:|---:|---|"]
            for e in b["luecken"]:
                z.append(f"| {e['letzte_kerze_davor']} | {e['erste_kerze_danach']} | {e['fehlende_kerzen']} | "
                         f"{e['dauer_tage']} | "
                         + (f"{e['kurs_davor']:.6g} → {e['kurs_danach']:.6g} ({e['sprung_prozent']:+.1f} %)"
                            if "sprung_prozent" in e else "") + " |")
        if b.get("ohne_handel"):
            z += ["", f"## {b['datei']}: Strecken ohne Handel (längste zuerst, höchstens {DETAIL_MAX})", "",
                  "| von | bis | Kerzen | Tage |", "|---|---|---:|---:|"]
            z += [f"| {e['von']} | {e['bis']} | {e['kerzen']} | {e['dauer_tage']} |" for e in b["ohne_handel"]]
    gut = [b for b in befunde if "fehler" not in b]
    # fehlende Kerzen je Jahr
    jahre = sorted({j for b in gut for j in b["fehlend_je_jahr"]})
    z += ["", "## Fehlende Kerzen je Jahr", ""]
    if jahre:
        z += ["Nur Dateien mit fehlenden Kerzen; alle anderen sind vollständig. Leeres Feld = nichts fehlt.", "",
              "| Datei | " + " | ".join(jahre) + " | Summe |", "|---|" + "---:|" * (len(jahre) + 1)]
        for b in gut:
            if b["fehlend_je_jahr"]:
                z.append(f"| {b['datei']} | " + " | ".join(str(b["fehlend_je_jahr"].get(j, "")) for j in jahre)
                         + f" | {b['kerzen_fehlend']} |")
    else:
        z.append("In keiner Datei fehlt eine Kerze.")
    # alle Lücken ab 2023
    z += ["", "## Lücken ab 2023 (alle, auch einzelne Kerzen)", ""]
    ohne = [b["datei"] for b in gut if not b["luecken_ab_2023_anzahl"]]
    z.append("Ohne jede Lücke ab 2023: " + (", ".join(ohne) if ohne else "keine Datei") + ".")
    for b in gut:
        if b["luecken_ab_2023_anzahl"]:
            z += ["", f"### {b['datei']}: {b['luecken_ab_2023_anzahl']} Lücken ab 2023, zusammen "
                      f"{b['fehlend_ab_2023']} fehlende Kerzen in den Jahren ab 2023"
                      + (f" (gezeigt: die ersten {AB_MAX})" if b["luecken_ab_2023_anzahl"] > AB_MAX else ""), "",
                  "| letzte Kerze davor | erste Kerze danach | fehlende Kerzen |", "|---|---|---:|"]
            z += [f"| {e['letzte_kerze_davor']} | {e['erste_kerze_danach']} | {e['fehlende_kerzen']} |"
                  for e in b["luecken_ab_2023"]]
    # Kerzen um grosse Lücken
    if any(b["kerzen_um_grosse_luecken"] for b in gut):
        z += ["", f"## Kerzen vor und nach den grossen Lücken (ab {GROSS_TAGE} Tagen)"]
        for b in gut:
            for u in b["kerzen_um_grosse_luecken"]:
                spalten = [s for s in (*OHLC, "volume") if s in u["kerzen"][0]]
                z += ["", f"### {b['datei']}: Lücke {u['luecke']}", "", "| Zeit | " + " | ".join(spalten) + " |",
                      "|---|" + "---:|" * len(spalten)]
                z += [f"| {k['zeit']} | " + " | ".join(f"{k[s]:.6g}" for s in spalten) + " |" for k in u["kerzen"]]
    # Plausibilität
    z += ["", "## Plausibilität der Kerzen", "",
          "Leere Felder, Preise von 0 oder darunter, Hoch unter Tief, Schluss oder Eröffnung ausserhalb von Hoch und "
          "Tief; dazu die grössten Bewegungen von Kerze zu Kerze (ohne Sprünge über Lücken) und die grösste Spanne "
          "zwischen Hoch und Tief in einer Kerze.", "",
          "| Datei | leere Felder | Preis ≤ 0 | Hoch < Tief | ausserhalb Hoch/Tief | grösster Anstieg | grösster Rückgang "
          "| grösste Spanne |", "|---|---:|---:|---:|---:|---|---|---|"]
    for b in gut:
        q = b["plausibilitaet"]
        if not q:
            z.append(f"| {b['datei']} | Spalten fehlen | | | | | | |")
            continue
        zeigen = lambda e: f"{e['prozent']:+.1f} % ({e['zeit'][:10] if b['kerzen_abstand'] == '1d' else e['zeit']})" if e else ""
        z.append(f"| {b['datei']} | {q['ohne_wert']} | {q['nicht_positiv']} | {q['hoch_unter_tief']} | "
                 f"{q['ausserhalb_der_spanne']} | {zeigen(q.get('groesster_anstieg'))} | "
                 f"{zeigen(q.get('groesster_rueckgang'))} | {zeigen(q.get('groesste_spanne'))} |")
    # Prüfsummen
    z += ["", "## Prüfsummen der Kursdateien (SHA-256)", "", "| Datei | SHA-256 |", "|---|---|"]
    z += [f"| {b['datei']} | `{b['sha256']}` |" for b in befunde if "sha256" in b]
    return "\n".join(z) + "\n"


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("--cache", default="data/historie", help="Ordner mit den Kursdateien")
    p.add_argument("--aus", default="ausgabe", help="Ordner für kurs_luecken.md und kurs_luecken.json")
    a = p.parse_args(argv)
    ordner = Path(a.cache)
    dateien = sorted(ordner.glob("*_*_*.csv"))
    if not dateien:
        print(f"Keine Kursdateien in {ordner}", file=sys.stderr)
        return 1
    befunde = [pruefe_sicher(f) for f in dateien]
    haupt = [f for f in dateien if f.name.split("_")[0] in HAUPTQUELLEN]
    fp = fingerabdruck(haupt) if haupt else ""
    soll = Path("lernen/profi/cache_github.txt")
    kopf = {"ordner": str(ordner), "dateien": len(dateien), "fingerabdruck_hauptquellen": fp,
            "fingerabdruck_alle": fingerabdruck(dateien),
            "fingerabdruck_stimmt": (soll.read_text().strip() == fp) if soll.exists() else None}
    text = bericht(befunde, kopf)
    aus = Path(a.aus)
    aus.mkdir(parents=True, exist_ok=True)
    (aus / "kurs_luecken.md").write_text(text, encoding="utf-8")
    (aus / "kurs_luecken.json").write_text(json.dumps({"kopf": kopf, "dateien": befunde}, ensure_ascii=False, indent=1),
                                            encoding="utf-8")
    print(text)
    zusammenfassung = os.environ.get("GITHUB_STEP_SUMMARY")
    if zusammenfassung:
        with open(zusammenfassung, "a", encoding="utf-8") as f:
            f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
