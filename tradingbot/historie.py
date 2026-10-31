"""Geschichts-Simulation: spielt die kompletten Bots über die gesamte verfügbare Kursgeschichte durch.

Anders als `backtest` (eine Strategie, ein Coin) läuft hier jeder Bot so wie im Demo-Betrieb: alle Zeithorizonte
(kurz/mittel/lang), alle Coins auf einem Konto, mit Risikoregeln, Not-Aus, Hebel, Zinsen und Zwangsschliessung.
Dazu der Chef-Bot, der täglich auf die drei Bots verteilt.

Kursgeschichte: Jeder Coin kommt von der Börse mit der längsten Geschichte (Bitcoin bei Bitstamp ab 2011,
die meisten anderen bei Binance ab 2017). Ein Coin wird gehandelt, sobald es ihn gibt. Gerechnet wird in USD.

Kosten wie im Demo-Betrieb: Gebühren nach `fee_model` (Kraken-Staffel nach 30-Tage-Umsatz), Margin-Kosten auf den
geliehenen Teil, Liquidationsgebühr. Gebührenstufe (`fees`): «normiert» = wie für ein Konto mit Startkapital (der
Umsatz zählt im Verhältnis zum Kapital, ein über die Jahre gewachsenes Simulationskonto bekommt so keinen Rabatt, den
ein 1'000er-Konto nie hätte), «staffel» = nach dem echten Umsatz des Simulationskontos, «alt» = fest 0,26 % wie in
den früheren Berichten (nur zum Vergleich).

Grenzen (bewusst ehrlich): keine historischen News und Ereignisse, kein Orderbuch-Spread (Slippage statt Geld- und
Briefkurs), keine Korrelationsprüfung zwischen Coins. KI-Gedächtnis und Labor-Bibliothek werden nicht verwendet,
weil sie die Kurse schon kennen; die KI lernt hier Kerze für Kerze von vorne.
"""
from __future__ import annotations

import logging
import time
from collections import defaultdict
from dataclasses import dataclass
from datetime import timezone
from pathlib import Path

import numpy as np
import pandas as pd

from . import indicators as ind
from .backtest import WARMUP, Result
from .phase import PhaseBook
from .bot import liquidation
from .broker import paper_broker
from .config import Config
from .data import to_frame
from .engine import Trader
from .risk import RiskManager
from .strategies import build

log = logging.getLogger(__name__)

FEES = ("normiert", "staffel", "alt")      # Gebührenstufe in der Simulation (siehe oben)
OLD_FEE = 0.0026                           # fester Satz der früheren Berichte

# binance sperrt US-Server (auch GitHub): dann liefern binanceus oder kucoin die Altcoin-Geschichte
SOURCES = (("bitstamp", "USD"), ("binance", "USDT"), ("binanceus", "USD"), ("kucoin", "USDT"))
CACHE = Path("data/historie")
TF_MS = {"30m": 1_800_000, "1h": 3_600_000, "4h": 14_400_000, "1d": 86_400_000}
RULE = {"30m": "30min", "1h": "1h", "4h": "4h", "1d": "1D"}


def _first_candle(ex, symbol: str) -> int | None:
    """Ältester Tag, für den die Börse Kerzen liefert (manche Börsen liefern nichts vor dem Start)."""
    since, now = ex.parse8601("2010-01-01T00:00:00Z"), ex.milliseconds()
    while since < now:
        rows = ex.fetch_ohlcv(symbol, "1d", since=since, limit=1000)
        if rows:
            return rows[0][0]
        since += 90 * TF_MS["1d"]
    return None


def download(ex, symbol: str, timeframe: str, since: int) -> pd.DataFrame:
    """Alle Kerzen ab `since`, seitenweise. Lücken (Börse ohne Daten) werden übersprungen."""
    step, now, rows = TF_MS[timeframe], ex.milliseconds(), []
    while since < now - step:
        batch = ex.fetch_ohlcv(symbol, timeframe, since=since, limit=1000)
        if not batch:
            since += 1000 * step
            continue
        rows += batch
        since = max(batch[-1][0] + step, since + step)
    df = to_frame(rows)
    return df[~df.index.duplicated()].sort_index()


def load_coin(coin: str, timeframe: str, exchanges: dict | None = None) -> pd.DataFrame | None:
    """Kursgeschichte eines Coins von der Börse mit der längsten Geschichte (mit CSV-Cache in data/historie)."""
    CACHE.mkdir(parents=True, exist_ok=True)
    cached = sorted(CACHE.glob(f"*_{coin}_{timeframe}.csv"))
    if cached:
        df = pd.read_csv(cached[0], index_col=0, parse_dates=True)
        if time.time() - cached[0].stat().st_mtime < 7 * 86400:
            return df
    import ccxt
    exchanges = exchanges or {}
    found = []
    for name, quote in SOURCES:
        ex = exchanges.setdefault(name, getattr(ccxt, name)({"enableRateLimit": True}))
        symbol = f"{coin}/{quote}"
        try:
            if symbol not in ex.load_markets():
                continue
            first = _first_candle(ex, symbol)
        except Exception as e:          # Börse nicht erreichbar: nächste versuchen
            log.warning("%s %s: %s", name, symbol, e)
            continue
        if first is not None:
            found.append((first, name, ex, symbol))
    df = None
    for first, name, ex, symbol in sorted(found, key=lambda f: f[0]):     # längste Geschichte zuerst
        log.warning("Lade %s %s von %s ab %s ...", coin, timeframe, name, ex.iso8601(first)[:10])
        try:
            df = download(ex, symbol, timeframe, first)
            break
        except Exception as e:          # z.B. Börse liefert nur die letzten Kerzen: nächste versuchen
            log.warning("%s %s: %s", name, symbol, e)
    if df is None:
        return None
    for old in cached:
        old.unlink()
    df.to_csv(CACHE / f"{name}_{coin}_{timeframe}.csv")
    return df


def resample(df: pd.DataFrame, timeframe: str) -> pd.DataFrame:
    """Kerzen zu längeren Kerzen zusammenfassen (z.B. 1h -> 4h). Die letzte, evtl. unfertige Kerze fällt weg."""
    out = df.resample(RULE[timeframe], label="left", closed="left").agg(
        {"open": "first", "high": "max", "low": "min", "close": "last", "volume": "sum"}).dropna()
    return out.iloc[:-1]


@dataclass
class BotRun:
    cfg: Config
    equity: pd.Series           # Kapital am Ende jedes Tages
    trades: pd.DataFrame
    halts: int                  # wie oft der Not-Aus ausgelöst hat
    liquidations: int

    def stats(self, btc: pd.Series) -> dict:
        px = btc.reindex(self.equity.index, method="ffill").dropna()
        res = Result(self.equity, self.trades, px.iloc[-1] / px.iloc[0] - 1, 0.0, (px / px.cummax() - 1).min())
        s = res.stats()
        s.pop("Im Markt %")
        s["Not-Aus"], s["Liquidationen"] = self.halts, self.liquidations
        return s


_CACHE: dict = {}


def _cached(key, fn):
    """Signale nur einmal berechnen, auch wenn viele Varianten eines Bots getestet werden."""
    if key not in _CACHE:
        _CACHE[key] = fn()
    return _CACHE[key]


def _fingerprint(df: pd.DataFrame) -> tuple:
    """Kurzer Steckbrief einer Kursreihe für den Zwischenspeicher."""
    return len(df), df.index[0], df.index[-1], float(df["close"].iloc[-1]), float(df["close"].sum())


def _signals(h, params: dict, allow_short: bool, df: pd.DataFrame, base_tf: str):
    """Schlusszeit, Signal, ATR und 20er-Linie jeder Horizont-Kerze (nach der Vorlaufzeit)."""
    hdf = df if h.timeframe == base_tf else resample(df, h.timeframe)
    if len(hdf) <= WARMUP:
        return df.index[:0], np.array([]), np.array([]), np.array([])
    strat = build(h.strategy, allow_short=allow_short, **params)
    sig, atr = strat.signals(hdf).to_numpy(), ind.atr(hdf).to_numpy()
    ema = ind.ema(hdf["close"], 20).to_numpy()
    closes = hdf.index + pd.Timedelta(milliseconds=TF_MS[h.timeframe])
    return closes[WARMUP:], sig[WARMUP:], atr[WARMUP:], ema[WARMUP:]


def _trend_series(df: pd.DataFrame):
    """Richtung der 200-Tage-Linie, gültig ab Schluss der jeweiligen Tageskerze."""
    from .strategies import trend_direction
    daily = resample(df, "1d")
    return daily.index + pd.Timedelta(days=1), trend_direction(daily).to_numpy()


def _phase_series(df: pd.DataFrame):
    """Marktphase des Coins (phase.py), gültig ab Schluss der jeweiligen Tageskerze."""
    from .phase import coin_phases
    daily = resample(df, "1d")
    return daily.index + pd.Timedelta(days=1), coin_phases(daily).to_numpy()


def simulate(cfg: Config, coins: dict[str, pd.DataFrame], start: pd.Timestamp | None = None,
             fees: str = "normiert") -> BotRun:
    """Ein Bot über die ganze Geschichte. `coins`: Kerzen je Coin im kürzesten Zeitraum des Bots.
    Mit `start` beginnt der Handel (und das Startkapital) erst dann; Indikatoren, Trendfilter und KI-Gedächtnis
    nutzen die Kurse davor als Vorlauf, so wie ein Bot, der an diesem Tag eingeschaltet wird.
    `fees`: Gebührenstufe, siehe FEES."""
    if fees not in FEES:
        raise ValueError(f"Unbekanntes Gebührenmodell «{fees}» (erlaubt: {', '.join(FEES)})")
    hz = cfg.horizon_list()
    base_tf = min((h.timeframe for h in hz), key=TF_MS.get)
    broker = paper_broker(cfg)             # gerechnet wird in USD: quote_usd bleibt 1
    if fees == "alt":
        broker.tiers, broker.fee_rate = None, OLD_FEE
    trader = Trader(broker, RiskManager(cfg.risk, cfg.starting_capital), allow_short=cfg.allow_short)
    if cfg.horizons:
        trader.horizons, trader.adaptive_shares = {h.name: h for h in hz}, cfg.adaptive_shares
        trader.priority = cfg.horizon_priority
    trader.short_probation = cfg.short_probation
    if cfg.phase_gate:      # ohne Vorwissen: der Bot lernt in der Simulation Trade für Trade (kein Blick in die Zukunft)
        trader.phase_book = PhaseBook(probation=cfg.phase_probation, loser=cfg.phase_loser)
    trader.phase_exit = cfg.phase_exit
    use_phase = cfg.phase_gate or cfg.phase_exit
    phases = {s: _cached(("phase", s, _fingerprint(df)), lambda: _phase_series(df)) for s, df in coins.items()} \
        if use_phase else {}

    # Langfristige Richtung je Coin (Trendfilter): gilt ab Schluss der Tageskerze
    trends = {}
    if any(h.trend_filter for h in hz):
        for s, df in coins.items():
            trends[s] = _cached(("trend", s, _fingerprint(df)), lambda: _trend_series(df))

    # Wann schliesst welche Horizont-Kerze, mit welchem Signal: ausgeführt zum Eröffnungskurs danach
    events = defaultdict(list)
    for h in hz:
        params = {k: v for k, v in h.strategy_params.items() if k not in ("memory_file", "library_file")}
        for s, df in coins.items():
            key = (h.strategy, repr(sorted(params.items())), cfg.allow_short, h.timeframe, base_tf, s, _fingerprint(df))
            closes, sig, atr, ema = _cached(key, lambda: _signals(h, params, cfg.allow_short, df, base_tf))
            if h.trend_filter:
                p = trends[s][0].searchsorted(closes, side="right") - 1
                trend = np.where(p >= 0, trends[s][1][np.clip(p, 0, None)], 0)
            if use_phase:
                p = phases[s][0].searchsorted(closes, side="right") - 1
                phase = np.where(p >= 0, phases[s][1][np.clip(p, 0, None)], None)
            for i in np.flatnonzero((sig != 0) & (atr > 0)):
                events[closes[i]].append((h.name, s, int(sig[i]), float(atr[i]),
                                          int(trend[i]) if h.trend_filter else None,
                                          phase[i] if use_phase else None, float(ema[i])))
    # Phasenwechsel je Coin (für den Ausstieg, wenn die Phase kippt)
    for s, (times, ph) in phases.items():
        for i in np.flatnonzero(np.r_[True, ph[1:] != ph[:-1]]):
            events[times[i]].append(("", s, 0, 0.0, None, ph[i], None))

    idx = coins[next(iter(coins))].index
    for df in coins.values():
        idx = idx.union(df.index)
    # Fehlt genau zum Signalzeitpunkt eine Kerze (z.B. Börsenausfall): Signal bei der nächsten Kerze ausführen
    pos = idx.searchsorted(pd.DatetimeIndex(list(events)))
    moved = defaultdict(list)
    for (t, ev), p in zip(list(events.items()), pos):
        if p < len(idx):
            moved[idx[p]] += ev
    events = moved
    cols = {s: df.reindex(idx)[["open", "high", "low", "close"]].to_numpy() for s, df in coins.items()}
    hours = TF_MS[base_tf] / 3_600_000
    px: dict[str, float] = {}
    curve, halts, liqs, day = [], 0, 0, None
    for i, t in enumerate(idx):
        if start is not None and t < start:
            continue
        broker.now = t                      # für den 30-Tage-Umsatz (Gebührenstufe)
        bar = {s: c[i] for s, c in cols.items() if not np.isnan(c[i][0])}
        px.update({s: b[0] for s, b in bar.items()})
        for name, s, g, a, trend, phase, ema in events.get(t, ()):
            if s not in bar:
                continue
            if g == 0:
                trader.check_phase(s, phase, px[s], t)
            elif not trader.risk.halted:
                trader.on_signal(s, g, px[s], a, trader.equity(px), t, horizon=name, trend=trend, phase=phase,
                                 anchor=ema)
        for s in list(trader.open_trades):
            if s in bar:
                trader.check_stops(s, *bar[s][:3], t)
        px.update({s: b[3] for s, b in bar.items()})
        trader.charge_interest(px, hours, cfg.risk.margin_interest_per_day)
        if liquidation(trader, px, cfg.risk):
            trader.close_all(px, "Liquidation", t)
            liqs += 1
        eq = trader.equity(px)
        if fees == "normiert":              # Stufe der nächsten Orders wie bei einem Konto mit Startkapital
            broker.volume_scale = min(1.0, cfg.starting_capital / eq) if eq > 0 else 1.0
        was_halted = trader.risk.halted
        trader.risk.update(eq, t.date())
        if trader.risk.halted:
            if not was_halted:
                halts += 1
            trader.close_all(px, "Not-Aus", t)     # ohne halt_days bleibt der Bot (wie live) gestoppt
        if t.date() != day:
            day = t.date()
            curve.append((t.normalize(), trader.equity(px)))
    equity = pd.Series(dict(curve)).groupby(level=0).last()
    return BotRun(cfg, equity, pd.DataFrame(trader.closed), halts, liqs)


def segment(run: BotRun, start, end) -> dict:
    """Kennzahlen für einen Zeitabschnitt, z.B. Entwicklung (bis 2022) oder Prüfung (ab 2023).
    Calmar = Rendite pro Jahr geteilt durch den grössten Rückgang: Gewinn im Verhältnis zum Risiko."""
    start, end = pd.Timestamp(start, tz="UTC"), pd.Timestamp(end, tz="UTC")
    eq = run.equity[(run.equity.index >= start) & (run.equity.index < end)]
    t = run.trades
    if len(t):
        closed = pd.to_datetime(t["closed"], utc=True)
        t = t[(closed >= start) & (closed < end)]
    if len(eq) < 2:
        return {"Rendite %": None, "pro Jahr %": None, "Max. DD %": None, "Calmar": None, "Trades": 0,
                "Treffer %": None, "Profit Factor": None, "Kosten % pro Jahr": None}
    years = max((eq.index[-1] - eq.index[0]).days / 365.25, 1e-9)
    ret = eq.iloc[-1] / eq.iloc[0] - 1
    cagr = (1 + ret) ** (1 / years) - 1 if ret > -1 else -1.0
    dd = (eq / eq.cummax() - 1).min()
    pnl = t["pnl"] if len(t) else pd.Series(dtype=float)
    loss = -pnl[pnl < 0].sum()
    # Gebühren und Zinsen der in diesem Abschnitt geschlossenen Trades, im Verhältnis zum Ø Kapital
    costs = sum(t[c].fillna(0).sum() for c in ("fees", "interest") if c in t) if len(t) else 0.0
    return {"Rendite %": round(ret * 100, 1), "pro Jahr %": round(cagr * 100, 1), "Max. DD %": round(dd * 100, 1),
            "Calmar": round(cagr / abs(dd), 2) if dd < 0 else 0.0, "Trades": len(pnl),
            "Treffer %": round((pnl > 0).mean() * 100, 1) if len(pnl) else 0.0,
            "Profit Factor": round(pnl[pnl > 0].sum() / loss, 2) if loss else 0.0,
            "Kosten % pro Jahr": round(costs / eq.mean() / years * 100, 1)}


def simulate_chef(runs: dict[str, BotRun], btc_daily: pd.DataFrame, path: Path) -> pd.Series:
    """Chef-Bot: verteilt täglich auf die drei Bots (live macht er das alle 30 Minuten)."""
    from .chef import Chef
    from .memory import phases
    for f in (path, path.with_name("chef_gedaechtnis.json")):
        f.unlink(missing_ok=True)
    eq = pd.DataFrame({name: r.equity for name, r in runs.items()}).ffill().dropna()
    ph = phases(btc_daily).reindex(eq.index, method="ffill").fillna("Seitwärts, ruhig")
    chef = Chef(path)
    chef.runs_per_day = 1
    curve = {}
    for t, row in eq.iterrows():
        chef.update(row.to_dict(), ph[t], t.to_pydatetime().astimezone(timezone.utc))
        curve[t] = chef.equity
    return pd.Series(curve)


def _md(df: pd.DataFrame) -> str:
    """Tabelle als Markdown (ohne Zusatzpaket)."""
    def cell(v):
        if v is None or (isinstance(v, float) and np.isnan(v)):
            return "–"
        return f"{v:,.2f}".replace(",", "'").removesuffix(".00") if isinstance(v, float) else str(v)
    head = "| | " + " | ".join(map(str, df.columns)) + " |"
    rows = [f"| **{i}** | " + " | ".join(cell(v) for v in r) + " |" for i, r in zip(df.index, df.itertuples(index=False))]
    return "\n".join([head, "|---" * (len(df.columns) + 1) + "|", *rows])


def _group(trades: pd.DataFrame, by) -> pd.DataFrame:
    g = trades.groupby(by)["pnl"]
    win, loss = g.apply(lambda p: p[p > 0].sum()), g.apply(lambda p: -p[p < 0].sum())
    return pd.DataFrame({"Trades": g.size(), "Trefferquote %": (g.apply(lambda p: (p > 0).mean()) * 100).round(1),
                         "Ergebnis": g.sum().round(0), "Profit Factor": (win / loss.replace(0, np.nan)).round(2)})


def yearly(equity: pd.Series, trades: pd.DataFrame) -> pd.DataFrame:
    """Jahr für Jahr: Rendite, Trades, Trefferquote."""
    rows = {}
    for y, e in equity.groupby(equity.index.year):
        prev = equity[equity.index.year < y]
        start = prev.iloc[-1] if len(prev) else e.iloc[0]
        t = trades[pd.to_datetime(trades["closed"], utc=True).dt.year == y] if len(trades) else trades
        rows[y] = {"Rendite %": round((e.iloc[-1] / start - 1) * 100, 1), "Kapital Ende": round(e.iloc[-1], 0),
                   "Trades": len(t), "Trefferquote %": round((t["pnl"] > 0).mean() * 100, 1) if len(t) else None}
    return pd.DataFrame(rows).T


FEE_TEXT = {"normiert": "Kraken-Gebührenstaffel wie für ein Konto mit 1'000 (ab 0,80 % je Order; ein über die Jahre "
                        "gewachsenes Simulationskonto bekommt keinen Mengenrabatt)",
            "staffel": "Kraken-Gebührenstaffel nach dem Umsatz des Simulationskontos (mit Mengenrabatt, wenn es wächst)",
            "alt": "fest 0,26 % je Order wie in den früheren Berichten (zu billig, nur zum Vergleich)"}


def report(runs: dict[str, BotRun], chef: pd.Series | None, btc: pd.Series, fees: str = "normiert") -> str:
    """Bericht für lernen/HISTORIE.md."""
    first = min(r.equity.index[0] for r in runs.values())
    out = ["# 🕰️ Geschichts-Simulation: alle Bots über die ganze Krypto-Geschichte", "",
           f"Zeitraum: **{first:%d.%m.%Y} bis {btc.index[-1]:%d.%m.%Y}**, Startkapital je Bot 1'000 (USD). "
           "Jeder Bot handelt mit allen Zeithorizonten, allen Coins (sobald es sie gibt), seinen Risikoregeln, "
           "Hebel und Zinsen. Ohne historische News. Vergangene Ergebnisse sind keine Garantie.", "",
           f"Gebühren: {FEE_TEXT[fees]}. Dazu Slippage je Order, Margin-Kosten und Liquidationsgebühr.", "",
           "## Gesamtergebnis", ""]
    table = {r.cfg.title or r.cfg.name: r.stats(btc) for r in runs.values()}
    if chef is not None and len(chef):
        table["4️⃣ Chef-Bot"] = {"Endkapital": round(chef.iloc[-1], 2),
                                "Rendite %": round((chef.iloc[-1] / chef.iloc[0] - 1) * 100, 2),
                                "Max. Drawdown %": round((chef / chef.cummax() - 1).min() * 100, 2)}
    out += [_md(pd.DataFrame(table)), ""]
    # Entwicklung (Einstellungen wurden nur damit gewählt) und Prüfung (danach, unberührt), dazu Bitcoin halten
    periods = {"bis 2022": ("2011-01-01", "2023-01-01"), "ab 2023": ("2023-01-01", "2100-01-01")}
    split = {}
    for label, (a, b) in periods.items():
        for r in runs.values():
            s = segment(r, a, b)
            split.setdefault(r.cfg.title or r.cfg.name, {}).update(
                {f"{label}: pro Jahr %": s["pro Jahr %"], f"{label}: Max. DD %": s["Max. DD %"],
                 f"{label}: Treffer %": s["Treffer %"], f"{label}: Kosten %/Jahr": s["Kosten % pro Jahr"]})
        p = btc[(btc.index >= pd.Timestamp(a, tz="UTC")) & (btc.index < pd.Timestamp(b, tz="UTC"))]
        if len(p) < 2:
            continue
        years = (p.index[-1] - p.index[0]).days / 365.25
        split.setdefault("Bitcoin halten", {}).update(
            {f"{label}: pro Jahr %": round(((p.iloc[-1] / p.iloc[0]) ** (1 / years) - 1) * 100, 1),
             f"{label}: Max. DD %": round((p / p.cummax() - 1).min() * 100, 1), f"{label}: Treffer %": None,
             f"{label}: Kosten %/Jahr": None})
    out += ["## Entwicklung und Prüfung", "",
            "Die Einstellungen der Bots wurden nur mit den Jahren **bis 2022** gewählt. Die Jahre **ab 2023** waren dabei "
            "weggesperrt und zeigen, wie die Bots auf unbekannten Kursen abschneiden.", "",
            _md(pd.DataFrame(split).T), ""]
    for r in runs.values():
        out += [f"## {r.cfg.title or r.cfg.name}", "", "**Jahr für Jahr**", "", _md(yearly(r.equity, r.trades)), ""]
        if len(r.trades):
            out += ["**Nach Zeithorizont**", "", _md(_group(r.trades, "horizon")), "",
                    "**Nach Coin**", "", _md(_group(r.trades, "symbol")), "",
                    "**Nach Richtung**", "", _md(_group(r.trades, "side")), "",
                    *(["**Nach Marktphase und Horizont**", "", _md(_group(r.trades, ["phase", "horizon"])), ""]
                      if "phase" in r.trades else []),
                    "**Nach Ausstiegsgrund**", "", _md(_group(r.trades, "reason")), ""]
    return "\n".join(out)


def run_all(config_paths: list[str], coins: list[str], start: pd.Timestamp | None = None,
            fees: str = "normiert") -> tuple[dict[str, BotRun], pd.Series, pd.Series]:
    """Lädt die Geschichte, simuliert alle Bots und den Chef. Gibt Läufe, Chef-Kurve und BTC-Tageskurs zurück."""
    exchanges: dict = {}
    cfgs = [Config.load(p) for p in config_paths]
    data = {}
    runs = {}
    for cfg in cfgs:
        base_tf = min((h.timeframe for h in cfg.horizon_list()), key=TF_MS.get)
        for c in coins:
            if (c, base_tf) not in data:
                data[c, base_tf] = load_coin(c, base_tf, exchanges)
        frames = {f"{c}/USD": data[c, base_tf] for c in coins if data[c, base_tf] is not None}
        log.warning("Simuliere %s ...", cfg.name)
        runs[cfg.name] = simulate(cfg, frames, start, fees)
    btc = data["BTC", "1h"] if ("BTC", "1h") in data else next(v for (c, _), v in data.items() if c == "BTC")
    btc_daily = resample(btc, "1d")
    # Der Chef verteilt auf die drei Stil-Bots (die ersten drei); weitere Bots laufen nur zum Vergleich mit
    three = dict(list(runs.items())[:3])
    chef = simulate_chef(three, btc_daily, CACHE / "chef_sim.json") if len(three) == 3 else None
    return runs, chef, btc_daily["close"]
