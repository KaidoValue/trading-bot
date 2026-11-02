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
from .strategies import Strategy, _holding, fib_retracement

LIBRARY = Path("daten/state/strategie_bibliothek.json")


def blocks(df: pd.DataFrame) -> dict[str, tuple[str, pd.Series]]:
    """Alle Bausteine als Ja/Nein-Bedingung je Kerze, mit Beschreibung in Worten. Nur vergangene Daten."""
    c = df["close"]
    r = ind.rsi(c)
    lower, mid, upper = ind.bollinger(c)
    _, _, hist = ind.macd(c)
    a = st.analyze(df)
    vol_ma = df["volume"].rolling(20).mean()
    retr, impulse = fib_retracement(df)
    fib_zone = impulse & (retr >= 0.382) & (retr <= 0.618)
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
        # aus YouTube-Videos (lernen/YOUTUBE.md)
        "fib_zone": ("Rücksetzer in die Fibonacci-Zone 38,2-61,8 % nach einem Aufwärtsimpuls", fib_zone),
        "deep_drawdown": ("Kurs mehr als 40 % unter dem Hoch der letzten 365 Kerzen",
                          c < c.rolling(365, min_periods=50).max() * 0.6),
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
           test_share: float = 0.5, min_trades: int = 20, min_test_trades: int = 30, seed: int | None = None,
           log=print, cfg=None) -> list[dict]:
    """Sucht neue Strategien. Gibt die Kandidaten zurück, die auch auf den unbekannten Kursen bestehen."""
    rng = random.Random(seed)
    split = int(len(df) * (1 - test_share))
    if not 0.2 <= test_share <= 0.6 or split < 250 or len(df) - split < 90:
        raise ValueError("Need >=250 training candles and >=90 out-of-sample candles")
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

    if population < 5 or generations < 1:
        raise ValueError("population >=5 and generations >=1 required")
    # The genetic search sees training data only. Expensive production replay
    # is reserved for a fixed shortlist; validation cannot mutate the rules.
    from .config import Config
    from .broker import KRAKEN_TIERS
    from .evaluation import replay
    cfg = cfg or Config(fee_rate=fee)
    training_fee = KRAKEN_TIERS[0][2] if cfg.fee_model == "kraken" else cfg.fee_rate
    fee = training_fee + cfg.slippage
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
        strategy = Evolved(rule["entry"], rule["exit"])
        signals = strategy.signals(df)
        boundaries = [split, split + (len(df) - split) // 3,
                      split + 2 * (len(df) - split) // 3, len(df)]
        folds = []
        # Two validation windows plus one final, later holdout. Each starts
        # flat with the same capital and closes all positions at its end.
        for lo, hi in zip(boundaries, boundaries[1:]):
            segment = df.iloc[:hi]
            res = replay(segment, signals.iloc[:hi], cfg, start=df.index[lo], liquidate=True)
            equity = res.equity.iloc[lo:hi]
            ret = float(equity.iloc[-1] / cfg.starting_capital - 1)
            dd = float((equity / equity.cummax().clip(lower=cfg.starting_capital) - 1).min())
            pnl = pd.Series([t["pnl"] for t in res.trades], dtype=float)
            win, loss = float(pnl[pnl > 0].sum()), float(-pnl[pnl < 0].sum())
            pf = win / loss if loss else (1000.0 if win else 0.0)
            bh = float(segment["close"].iloc[-1] * (1 - training_fee - cfg.slippage) /
                       (segment["open"].iloc[lo] * (1 + training_fee + cfg.slippage)) - 1)
            folds.append({"start": str(df.index[lo]), "end": str(df.index[hi - 1]),
                          "return": ret, "drawdown": dd, "trades": len(res.trades),
                          "profit_factor": pf, "buy_hold": bh})
        test_ret = float(pd.Series([1 + f["return"] for f in folds]).prod() - 1)
        test_trades = sum(f["trades"] for f in folds)
        accepted = (fit(rule) > 0 and test_trades >= min_test_trades
                    and all(f["return"] > 0 and f["profit_factor"] >= 1.2
                            and f["drawdown"] >= -0.15 for f in folds)
                    and test_ret > float(pd.Series([1 + f["buy_hold"] for f in folds]).prod() - 1))
        winners.append({**rule, "train_return": fit(rule), "test_return": test_ret, "test_trades": test_trades,
                        "buy_hold_test": float(pd.Series([1 + f["buy_hold"] for f in folds]).prod() - 1),
                        "accepted": accepted, "folds": folds, "validation_version": 2,
                        "evaluation_end": df.index[-1].isoformat()})
        if len(winners) >= 5:
            break
    return winners


def load_library(path: Path = LIBRARY) -> list[dict]:
    return json.loads(path.read_text(encoding="utf-8")) if path.exists() else []


def update_library(found: list[dict], df: pd.DataFrame, path: Path = LIBRARY, max_size: int = 5, cfg=None) -> list[dict]:
    """Neue bestandene Strategien aufnehmen; die Bibliothek behält nur die besten (nach Prüfungs-Rendite)."""
    lib = load_library(path)
    known = {(tuple(sorted(s["entry"])), tuple(sorted(s["exit"]))) for s in lib
             if s.get("validation_version") == 2}
    now = datetime.now(timezone.utc).strftime("%Y-%m-%d")
    for f in found:
        k = (tuple(sorted(f["entry"])), tuple(sorted(f["exit"])))
        if f["accepted"] and k not in known:
            n = max([int(s["name"].split("_")[-1]) for s in lib] + [0]) + 1
            lib.append({**f, "name": f"labor_{n}", "found": now,
                        "discovered_at": datetime.now(timezone.utc).isoformat(),
                        "probe_config": probe_signature(cfg) if cfg is not None else None,
                        "text": Evolved(f["entry"], f["exit"]).describe(df)})
            known.add(k)
    # Preserve active strategies; old, unvalidated entries never silently enter
    # the new learner. Fresh candidates have to pass a later paper-only probe.
    for s in lib:
        s.setdefault("status", "legacy" if s.get("validation_version") != 2 else "probation")
    lib = sorted(lib, key=lambda s: (s.get("status") == "active", s.get("validation_version") == 2,
                                     s["test_return"]), reverse=True)[:max_size]
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(".tmp")
    tmp.write_text(json.dumps(lib, indent=1, ensure_ascii=False), encoding="utf-8")
    tmp.replace(path)
    return lib


def library_strategies(path: Path = LIBRARY) -> list[Evolved]:
    return [Evolved(s["entry"], s["exit"], name=s["name"]) for s in load_library(path)
            if s.get("status") == "active" and s.get("validation_version") == 2]


def probe_signature(cfg):
    from dataclasses import asdict
    return json.dumps({"risk": asdict(cfg.risk), "fee_model": cfg.fee_model,
                       "fee_rate": cfg.fee_rate, "slippage": cfg.slippage,
                       "horizon": asdict(cfg.horizon_list()[0]),
                       "capital": cfg.starting_capital}, sort_keys=True)


def review_probation(df, cfg, path: Path = LIBRARY, now=None) -> list[dict]:
    """Paper-only prospective evaluation of frozen rules on post-discovery data.

    Recomputed from the same starting account, never added to real portfolio
    equity. Weekly laboratory runs collect later candles before searching anew.
    """
    from .evaluation import replay
    lib = load_library(path)
    now = pd.Timestamp(now or datetime.now(timezone.utc))
    signature = probe_signature(cfg)
    for s in lib:
        if s.get("validation_version") != 2 or s.get("status") not in ("probation", "active"):
            continue
        discovery = pd.Timestamp(s["discovered_at"])
        if s.get("probe_config") not in (None, signature):
            s["status"], s["probe_note"] = "rejected", "Ausführungsregeln während der Probe geändert"
            continue
        s["probe_config"] = signature
        lo = int(df.index.searchsorted(discovery))
        hi = int(df.index.searchsorted(now, side="right"))
        if lo < 250:
            s["status"], s["probe_note"] = "rejected", "Kursgeschichte der Probe nicht vollständig verfügbar"
            continue
        if hi <= lo:
            continue
        # No future timestamps accepted, even if input data contains them.
        segment = df.iloc[:hi]
        signal = Evolved(s["entry"], s["exit"]).signals(segment)
        result = replay(segment, signal, cfg, start=discovery, liquidate=True)
        equity = result.equity.iloc[lo:]
        # The forced closing fill is charged but not counted as a naturally
        # completed trade in the minimum sample requirement.
        pnl = pd.Series([t["pnl"] for t in result.trades if t["reason"] != "Prüfende"], dtype=float)
        win, loss = float(pnl[pnl > 0].sum()), float(-pnl[pnl < 0].sum())
        stats = {"days": (segment.index[-1] - discovery).total_seconds() / 86400,
                 "trades": len(pnl), "return": float(equity.iloc[-1] / cfg.starting_capital - 1),
                 "drawdown": float((equity / equity.cummax().clip(lower=cfg.starting_capital) - 1).min()),
                 "profit_factor": win / loss if loss else (1000.0 if win else 0.0),
                 "checked_at": now.isoformat()}
        s["paper_forward"] = stats
        if stats["drawdown"] < -0.15:
            s["status"] = "rejected"
        elif stats["days"] >= 14 and stats["trades"] >= 20:
            s["status"] = "active" if stats["return"] > 0 and stats["profit_factor"] >= 1.2 else "rejected"
        elif stats["days"] > 90 and s["status"] != "active":
            s["status"] = "rejected"
    if path.exists():
        tmp = path.with_suffix(".tmp")
        tmp.write_text(json.dumps(lib, indent=1, ensure_ascii=False), encoding="utf-8")
        tmp.replace(path)
    return lib


def report(found: list[dict], lib: list[dict], df: pd.DataFrame, symbol: str, timeframe: str) -> str:
    lines = ["# Strategie-Labor", "",
             f"Letzter Lauf: {datetime.now(timezone.utc):%d.%m.%Y %H:%M} UTC · Daten: {symbol}, {timeframe}-Kerzen, "
             f"{df.index[0]:%d.%m.%Y} bis {df.index[-1]:%d.%m.%Y}", "",
             "Die KI erfindet aus den vorhandenen Bausteinen (Indikatoren, Kerzenmuster, Marktstruktur) neue "
             "Strategien. Standard: Suche auf den älteren 50 %; danach zwei getrennte Validierungsfenster "
             "und ein späterer Holdout. Prüfung mit Trader/PaperBroker, Gebühren, Slippage, Stops und Risikolimits. "
             "Erforderlich: mindestens 30 abgeschlossene Trades insgesamt, positive Rendite und Profit Factor >=1,2 "
             "in jedem Fenster, höchstens 15 % Drawdown und insgesamt besser als kostenbereinigtes Halten. "
             "Ein Bestehen startet nur die Paper-Probe: mindestens 14 Tage nach Fund und 20 regulär geschlossene Trades. "
             "Erst Status active darf im KI-Bot mitstimmen.", "",
             "## Kandidaten dieses Laufs", "",
             "| Regel | Training | Prüfung | Trades (Prüfung) | Bitcoin halten (Prüfung) | Ergebnis |",
             "|---|---|---|---|---|---|"]
    for f in found:
        text = Evolved(f["entry"], f["exit"]).describe(df)
        lines.append(f"| {text} | {f['train_return'] * 100:+.1f} % | {f['test_return'] * 100:+.1f} % | "
                     f"{f['test_trades']} | {f['buy_hold_test'] * 100:+.1f} % | "
                     f"{'Paper-Probe' if f['accepted'] else 'durchgefallen'} |")
    lines += ["", "## Strategie-Bibliothek und Freigabestatus", ""]
    if lib:
        lines += ["| Name | Regel | Prüfung | Gefunden am | Status |", "|---|---|---|---|---|"]
        lines += [f"| {s['name']} | {s['text']} | {s['test_return'] * 100:+.1f} % | {s['found']} | {s.get('status', 'legacy')} |" for s in lib]
        for s in lib:
            probe = s.get("paper_forward")
            if probe:
                lines.append(f"\n{s['name']}: Paper-Probe {probe['days']:.1f} Tage, {probe['trades']} Trades, "
                             f"Rendite {probe['return']:.2%}, Drawdown {probe['drawdown']:.2%}, "
                             f"Profit Factor {probe['profit_factor']:.2f}.")
    else:
        lines.append("Noch leer: bisher hat keine erfundene Strategie die Prüfung bestanden.")
    lines += ["", "Grenzen: isolierte virtuelle Konten pro Regel, keine historischen News oder Orderbücher. "
              "Die Paper-Probe ist eine Simulation auf später hinzugekommenen Kursen. "
              "Wiederholte Forschung auf ähnlichen Zeiträumen kann weiterhin überanpassen. "
              "Ein Bestehen beweist keine künftigen Gewinne."]
    return "\n".join(lines)
