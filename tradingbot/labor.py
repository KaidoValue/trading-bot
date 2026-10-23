"""Strategie-Labor: die KI erfindet aus den vorhandenen Bausteinen neue Strategien und behält nur die guten.

Ablauf (wie eine Evolution):
1. Zufällige Regeln aus Bausteinen bauen, z.B. "Kaufen, wenn RSI unter 30 UND Kurs über der 200er-Linie;
   verkaufen, wenn MACD negativ".
2. Jede Regel auf älteren Kursen testen (Training). Die besten werden kombiniert und leicht verändert,
   über mehrere Generationen.
3. Die Sieger auf neueren Kursen prüfen, die das Labor nie gesehen hat (Prüfung). Nur wer dort nach Gebühren
   Gewinn macht und genug Trades hat, kommt in die Strategie-Bibliothek.
4. Die KI (adaptive_memory) nimmt die Bibliothek als zusätzliche Mitglieder auf und gewichtet sie wie alle
   anderen nach ihrem Erfolg.

Sicherheit: Die KI schreibt keinen freien Programmcode, sie kombiniert nur geprüfte Bausteine. So kann sie
nichts kaputt machen, und jede erfundene Strategie ist in Worten nachlesbar.
"""
from __future__ import annotations

import json
import random
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from . import indicators as ind
from . import patterns as pat
from . import structure as st
from .strategies import Strategy, _holding

LIBRARY = Path("daten/state/strategie_bibliothek.json")


def blocks(df: pd.DataFrame) -> dict[str, tuple[str, pd.Series]]:
    """Alle Bausteine als Ja/Nein-Bedingung je Kerze, mit Beschreibung in Worten. Nur vergangene Daten."""
    c = df["close"]
    r = ind.rsi(c)
    lower, mid, upper = ind.bollinger(c)
    _, _, hist = ind.macd(c)
    a = st.analyze(df)
    vol_ma = df["volume"].rolling(20).mean()
    b = {
        "ema_trend_up": ("schneller EMA (20) über langsamem EMA (50)", ind.ema(c, 20) > ind.ema(c, 50)),
        "ema_trend_down": ("schneller EMA (20) unter langsamem EMA (50)", ind.ema(c, 20) < ind.ema(c, 50)),
        "above_sma200": ("Kurs über der 200er-Linie", c > ind.sma(c, 200)),
        "below_sma200": ("Kurs unter der 200er-Linie", c < ind.sma(c, 200)),
        "rsi_oversold": ("RSI unter 30 (überverkauft)", r < 30),
        "rsi_overbought": ("RSI über 70 (überkauft)", r > 70),
        "rsi_strong": ("RSI über 55", r > 55),
        "rsi_weak": ("RSI unter 45", r < 45),
        "macd_pos": ("MACD-Histogramm positiv", hist > 0),
        "macd_neg": ("MACD-Histogramm negativ", hist < 0),
        "macd_rising": ("MACD-Histogramm steigt", hist > hist.shift()),
        "bb_below": ("Kurs unter dem unteren Bollinger-Band", c < lower),
        "bb_above": ("Kurs über dem oberen Bollinger-Band", c > upper),
        "above_bb_mid": ("Kurs über der Bollinger-Mitte", c > mid),
        "high20_break": ("neues 20-Kerzen-Hoch", c > df["high"].rolling(20).max().shift()),
        "low20_break": ("neues 20-Kerzen-Tief", c < df["low"].rolling(20).min().shift()),
        "momentum_pos": ("Momentum (10 Kerzen) positiv", ind.momentum(c, 10) > 0),
        "volume_high": ("Volumen über dem Durchschnitt", df["volume"] > vol_ma),
        "bull_candle": ("bullishes Kerzenmuster", pat.bullish_candle_signal(df)),
        "bear_candle": ("bearishes Kerzenmuster", pat.bearish_candle_signal(df)),
        "bias_up": ("Marktstruktur aufwärts (höhere Hochs/Tiefs)", a["bias"] > 0),
        "bias_down": ("Marktstruktur abwärts", a["bias"] < 0),
        "bos_up": ("Strukturbruch nach oben (BOS)", a["BOS_up"].astype(bool)),
        "choch_down": ("Trendwechsel nach unten (CHoCH)", a["CHoCH_down"].astype(bool)),
        "discount": ("Kurs im unteren Teil der Range (Discount)", a["discount"].astype(bool)),
        "premium": ("Kurs im oberen Teil der Range (Premium)", a["premium"].astype(bool)),
        "bull_div": ("bullishe RSI-Divergenz", a["bullish_divergence"].astype(bool)),
    }
    return {k: (d, s.fillna(False).astype(bool)) for k, (d, s) in b.items()}


class Evolved(Strategy):
    """Eine vom Labor erfundene Strategie: Einstieg, wenn alle Einstiegs-Bausteine zutreffen;
    Ausstieg, wenn alle Ausstiegs-Bausteine zutreffen."""
    name = "evolved"

    def __init__(self, entry: list[str], exit: list[str], name: str | None = None, **params):
        super().__init__(**params)
        self.entry, self.exit = entry, exit
        if name:
            self.name = name

    def signals(self, df):
        b = blocks(df)
        sig = pd.Series(0, index=df.index)
        sig[pd.concat([b[k][1] for k in self.exit], axis=1).all(axis=1)] = -1
        sig[pd.concat([b[k][1] for k in self.entry], axis=1).all(axis=1)] = 1
        return sig

    def describe(self, df=None) -> str:
        names = {k: d for k, (d, _) in blocks(df).items()} if df is not None else {}
        e = " UND ".join(names.get(k, k) for k in self.entry)
        x = " UND ".join(names.get(k, k) for k in self.exit)
        return f"Kaufen, wenn {e}. Verkaufen, wenn {x}."


def _fitness(sig: pd.Series, ret: pd.Series, fee: float) -> tuple[float, int]:
    pos = _holding(sig, False)
    pnl = pos.shift().fillna(0) * ret - pos.diff().abs().fillna(0) * fee
    trades = int((pos.diff() > 0).sum())
    return float(pnl.sum()), trades


def _random_rule(keys: list[str], rng: random.Random) -> dict:
    return {"entry": rng.sample(keys, rng.randint(1, 3)), "exit": rng.sample(keys, rng.randint(1, 2))}


def _mutate(rule: dict, keys: list[str], rng: random.Random) -> dict:
    new = {"entry": list(rule["entry"]), "exit": list(rule["exit"])}
    part = rng.choice(["entry", "exit"])
    if rng.random() < 0.5 and len(new[part]) > 1:
        new[part].remove(rng.choice(new[part]))
    else:
        new[part][rng.randrange(len(new[part]))] = rng.choice(keys)
    new[part] = list(dict.fromkeys(new[part]))
    return new


def _cross(a: dict, b: dict, rng: random.Random) -> dict:
    pool = list(dict.fromkeys(a["entry"] + b["entry"]))
    return {"entry": rng.sample(pool, rng.randint(1, min(3, len(pool)))), "exit": list(rng.choice([a["exit"], b["exit"]]))}


def evolve(df: pd.DataFrame, fee: float = 0.0026, population: int = 100, generations: int = 25,
           test_share: float = 0.3, min_trades: int = 8, seed: int | None = None, log=print) -> list[dict]:
    """Sucht neue Strategien. Gibt die Kandidaten zurück, die auch auf den unbekannten Kursen bestehen."""
    rng = random.Random(seed)
    split = int(len(df) * (1 - test_share))
    train, test = df.iloc[:split], df.iloc[split - 250:]          # 250 Kerzen Vorlauf für Indikatoren
    b_train, b_test = blocks(train), blocks(test)
    keys = list(b_train)
    ret_train, ret_test = train["close"].pct_change().fillna(0), test["close"].pct_change().fillna(0)

    def score(rule, b, ret):
        e = pd.concat([b[k][1] for k in rule["entry"]], axis=1).all(axis=1)
        x = pd.concat([b[k][1] for k in rule["exit"]], axis=1).all(axis=1)
        sig = pd.Series(0, index=ret.index)
        sig[x] = -1
        sig[e] = 1
        return _fitness(sig, ret, fee)

    def fit(rule):
        total, trades = score(rule, b_train, ret_train)
        return total if trades >= min_trades else -1.0

    pop = [_random_rule(keys, rng) for _ in range(population)]
    for g in range(generations):
        ranked = sorted(pop, key=fit, reverse=True)
        elite = ranked[: population // 5]
        log(f"Generation {g + 1}: beste Trainings-Rendite {fit(elite[0]) * 100:+.1f} %")
        pop = elite + [_mutate(rng.choice(elite), keys, rng) if rng.random() < 0.6
                       else _cross(rng.choice(elite), rng.choice(elite), rng)
                       for _ in range(population - len(elite))]
    winners, seen = [], set()
    for rule in sorted(pop, key=fit, reverse=True):
        sig_key = (tuple(sorted(rule["entry"])), tuple(sorted(rule["exit"])))
        if sig_key in seen:
            continue
        seen.add(sig_key)
        test_ret, test_trades = score(rule, {k: (d, s.iloc[250:]) for k, (d, s) in b_test.items()},
                                      ret_test.iloc[250:])
        bh = float(test["close"].iloc[-1] / test["close"].iloc[250] - 1)
        winners.append({**rule, "train_return": fit(rule), "test_return": test_ret, "test_trades": test_trades,
                        "buy_hold_test": bh, "accepted": test_ret > 0 and test_trades >= min_trades // 2})
        if len(winners) >= 5:
            break
    return winners


def load_library(path: Path = LIBRARY) -> list[dict]:
    return json.loads(path.read_text()) if path.exists() else []


def update_library(found: list[dict], df: pd.DataFrame, path: Path = LIBRARY, max_size: int = 5) -> list[dict]:
    """Neue bestandene Strategien aufnehmen; die Bibliothek behält nur die besten (nach Prüfungs-Rendite)."""
    lib = load_library(path)
    known = {(tuple(sorted(s["entry"])), tuple(sorted(s["exit"]))) for s in lib}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for f in found:
        k = (tuple(sorted(f["entry"])), tuple(sorted(f["exit"])))
        if f["accepted"] and k not in known:
            n = max([int(s["name"].split("_")[-1]) for s in lib] + [0]) + 1
            lib.append({**f, "name": f"labor_{n}", "found": now,
                        "text": Evolved(f["entry"], f["exit"]).describe(df)})
            known.add(k)
    lib = sorted(lib, key=lambda s: -s["test_return"])[:max_size]
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(lib, indent=1, ensure_ascii=False))
    return lib


def library_strategies(path: Path = LIBRARY) -> list[Evolved]:
    return [Evolved(s["entry"], s["exit"], name=s["name"]) for s in load_library(path)]


def report(found: list[dict], lib: list[dict], df: pd.DataFrame, symbol: str, timeframe: str) -> str:
    lines = ["# Strategie-Labor", "",
             f"Letzter Lauf: {datetime.now(timezone.utc):%d.%m.%Y %H:%M} UTC · Daten: {symbol}, {timeframe}-Kerzen, "
             f"{df.index[0]:%d.%m.%Y} bis {df.index[-1]:%d.%m.%Y}", "",
             "Die KI erfindet aus den vorhandenen Bausteinen (Indikatoren, Kerzenmuster, Marktstruktur) neue "
             "Strategien. Sie werden auf den älteren 70 % der Kurse entwickelt und auf den neuesten 30 % geprüft, "
             "die das Labor nie gesehen hat. Nur wer dort nach Gebühren Gewinn macht, kommt in die Bibliothek.", "",
             "## Kandidaten dieses Laufs", "",
             "| Regel | Training | Prüfung | Trades (Prüfung) | Bitcoin halten (Prüfung) | Ergebnis |",
             "|---|---|---|---|---|---|"]
    for f in found:
        text = Evolved(f["entry"], f["exit"]).describe(df)
        lines.append(f"| {text} | {f['train_return'] * 100:+.1f} % | {f['test_return'] * 100:+.1f} % | "
                     f"{f['test_trades']} | {f['buy_hold_test'] * 100:+.1f} % | "
                     f"{'✅ aufgenommen' if f['accepted'] else '❌ durchgefallen'} |")
    lines += ["", "## Strategie-Bibliothek (wird vom KI-Bot benutzt)", ""]
    if lib:
        lines += ["| Name | Regel | Prüfung | Gefunden am |", "|---|---|---|---|"]
        lines += [f"| {s['name']} | {s['text']} | {s['test_return'] * 100:+.1f} % | {s['found']} |" for s in lib]
    else:
        lines.append("Noch leer: bisher hat keine erfundene Strategie die Prüfung bestanden.")
    lines += ["", "Hinweis: Auch eine bestandene Prüfung ist keine Garantie. Deshalb gewichtet der KI-Bot diese "
              "Strategien danach live weiter nach ihrem tatsächlichen Erfolg, wie alle anderen."]
    return "\n".join(lines)
