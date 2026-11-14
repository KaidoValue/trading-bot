"""Messwerkzeug für den Profi-Bot (Stufe 1a): Geschichts-Simulation blind, nachprüfbar und mit ehrlichen Kennzahlen."""
import hashlib
import os
import sys
import time
import types
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from tradingbot import historie
from tradingbot.config import Config

BOTS = Path(__file__).resolve().parent.parent / "bots"


def _kerzen(seed: int, start: str, preis: float, knoten: list[tuple[int, float]]) -> pd.DataFrame:
    """Synthetische Kerzen alle 12 Stunden (statt stündlich, damit der Test schnell bleibt): Trend zwischen den Knoten
    (Tag, Kursfaktor), dazu Zufall in ruhigen und wilden Abschnitten von je 30 Tagen."""
    rng = np.random.default_rng(seed)
    tage, faktor = zip(*knoten)
    n = 2 * tage[-1]
    trend = np.interp(np.arange(n) / 2, tage, np.log(faktor))
    vol = np.repeat(rng.choice([0.5, 1.0, 1.5], n // 60 + 1), 60)[:n] * 0.03 / np.sqrt(2)
    noise = np.cumsum(rng.standard_normal(n) * vol)
    noise -= np.linspace(0, noise[-1], n)          # Zufall ohne eigene Richtung: die Knoten bestimmen den Trend
    close = preis * np.exp(trend + noise)
    open_ = np.r_[preis, close[:-1]]
    wick = np.abs(rng.standard_normal(n)) * vol / 2 * close
    idx = pd.date_range(start, periods=n, freq="12h", tz="UTC")
    return pd.DataFrame({"open": open_, "high": np.maximum(open_, close) + wick, "low": np.minimum(open_, close) - wick,
                         "close": close, "volume": rng.uniform(1, 10, n)}, index=idx)


@pytest.fixture(scope="module")
def coins():
    """BTC 440 Tage, ETH kommt nach 100 Tagen dazu; beide kreuzen die 200-Tage-Linie mehrmals."""
    return {"BTC/USD": _kerzen(1, "2020-01-01", 8000.0, [(0, 1.0), (120, 1.8), (200, 1.1), (260, 1.8), (320, 1.0),
                                                          (400, 1.9), (440, 1.4)]),
            "ETH/USD": _kerzen(2, "2020-04-10", 200.0, [(0, 1.0), (100, 1.6), (160, 0.9), (220, 1.7), (300, 2.6),
                                                         (340, 1.5)])}


def _fingerabdruck(run) -> tuple[float, int, str]:
    kurve = "\n".join(f"{t:%Y-%m-%d} {v:.2f}" for t, v in run.equity.items())
    return round(float(run.equity.iloc[-1]), 2), len(run.trades), hashlib.sha256(kurve.encode()).hexdigest()


# Berechnet mit dem Code vor Stufe 1a (main 2de1021): Endkapital, Zahl der Trades, SHA-256 der Kapitalkurve.
# Mit 100 Startkapital bleibt der Umsatz in der untersten Kraken-Stufe: «staffel» und «normiert» rechnen gleich.
VORHER = {
    ("config_langfrist", "staffel"): (96.81, 4, "656414481f50f97552a7b0f2b052d547f76747f22935eb713ec033647bb15f5e"),
    ("config_langfrist", "normiert"): (96.81, 4, "656414481f50f97552a7b0f2b052d547f76747f22935eb713ec033647bb15f5e"),
    ("config_daytrading", "staffel"): (95.34, 6, "a1dafb64cb9d3b98d4377e5ab3b90d3252bba5f5a90e91c549f3dd0650f663e1"),
    ("config_daytrading", "normiert"): (95.34, 6, "a1dafb64cb9d3b98d4377e5ab3b90d3252bba5f5a90e91c549f3dd0650f663e1"),
    ("config_risiko", "staffel"): (94.46, 5, "045818077364463e6beb5f04f32f01c5101cc9642e737a998315ae91cdd71455"),
    ("config_risiko", "normiert"): (94.46, 5, "045818077364463e6beb5f04f32f01c5101cc9642e737a998315ae91cdd71455"),
    ("config_phasen", "staffel"): (95.44, 4, "15513754955ef9312353c6c5ec4e045bf5356bb0dccf02fea78647e6e4b4bb07"),
    ("config_phasen", "normiert"): (95.44, 4, "15513754955ef9312353c6c5ec4e045bf5356bb0dccf02fea78647e6e4b4bb07"),
}


@pytest.mark.parametrize("name", ["config_langfrist", "config_daytrading", "config_risiko", "config_phasen"])
def test_die_vier_bots_bleiben_unveraendert(coins, name):
    """Neue Optionen und Kennzahlen dürfen die Simulation der heutigen Bots nicht verändern."""
    for fees in ("staffel", "normiert"):
        run = historie.simulate(Config.load(BOTS / f"{name}.yaml"), coins, fees=fees)
        assert _fingerabdruck(run) == VORHER[name, fees], (name, fees, _fingerabdruck(run))


# --- Hilfen für die kleinen Szenarien

def _tage(start: str, preise) -> pd.DataFrame:
    """Tageskerzen mit diesen Schlusskursen (Eröffnung = Schluss, Hoch und Tief ±1 %)."""
    close = np.asarray(preise, dtype=float)
    idx = pd.date_range(start, periods=len(close), freq="D", tz="UTC")
    return pd.DataFrame({"open": close, "high": close * 1.01, "low": close * 0.99, "close": close, "volume": 1.0},
                        index=idx)


def _welle(start: str, tage: int, preis: float = 100.0) -> pd.DataFrame:
    """Auf und ab um die 200-Tage-Linie (Periode rund 190 Tage)."""
    return _tage(start, preis * np.exp(0.4 * np.sin(np.arange(tage) / 30)))


def _bot(tmp_path, name: str = "config_test", symbols=("BTC/CHF",), **risk) -> str:
    """Kleiner Bot (200-Tage-Linie auf Tageskerzen) als Config-Datei."""
    path = tmp_path / f"{name}.yaml"
    path.write_text(yaml.safe_dump({"symbols": list(symbols), "timeframe": "1d", "strategy": "regime",
                                    "starting_capital": 100, "fee_model": "kraken", "risk": risk}), encoding="utf-8")
    return str(path)


def _laden(kurse: dict):
    """Ersatz für historie.load_coin: Kurse aus dem Speicher statt von der Börse."""
    def load(coin, timeframe, exchanges=None, sources=historie.SOURCES, fixed=False, used=None):
        return kurse.get(coin)
    return load


class Skript:
    """Strategie mit festen Signalen {Coin: {Tag der Signalkerze: +1/-1}}; der Coin wird am Kurs erkannt (BTC 100,
    ETH 10). Ausgeführt wird zur Eröffnung der nächsten Kerze."""
    def __init__(self, plan):
        self.plan = plan

    def signals(self, df):
        sig = pd.Series(0, index=df.index)
        for tag, s in self.plan["BTC" if df["close"].iloc[0] > 50 else "ETH"].items():
            sig[pd.Timestamp(tag, tz="UTC")] = s
        return sig


def _skript(monkeypatch, plan):
    monkeypatch.setattr(historie, "build", lambda *a, **k: Skript(plan))
    monkeypatch.setattr(historie, "_CACHE", {})          # Signale nicht mit anderen Tests teilen


# --- Daten: --ende, --cache-fest, --quellen, Fingerabdruck

def test_ende_schneidet_die_kurse_vor_allen_berechnungen_ab(monkeypatch, tmp_path):
    """--ende: Kurse nach dem Ende kommen gar nicht erst in die Simulation, und was danach geschieht, ändert nichts."""
    monkeypatch.setattr(historie, "CACHE", tmp_path)
    path, end = _bot(tmp_path), pd.Timestamp("2021-01-01", tz="UTC")       # --ende 2020-12-31
    real, seen = historie.simulate, []

    def spy(cfg, coins, *a, **k):
        seen.append(max(df.index[-1] for df in coins.values()))
        return real(cfg, coins, *a, **k)
    monkeypatch.setattr(historie, "simulate", spy)
    kurse = _welle("2019-03-01", 900)
    monkeypatch.setattr(historie, "load_coin", _laden({"BTC": kurse}))
    g = historie.run_all([path], ["BTC"], end=end)
    wild = kurse.copy()
    wild.loc[wild.index >= end, ["open", "high", "low", "close"]] *= 5          # nach dem Ende ganz andere Kurse
    monkeypatch.setattr(historie, "load_coin", _laden({"BTC": wild}))
    g2 = historie.run_all([path], ["BTC"], end=end)
    run, run2 = g.runs["config_test"], g2.runs["config_test"]
    assert seen == [pd.Timestamp("2020-12-31", tz="UTC")] * 2 and g.btc.index[-1] < end
    assert run.equity.index[-1] == pd.Timestamp("2020-12-31", tz="UTC") and len(run.trades) >= 2
    pd.testing.assert_series_equal(run.equity, run2.equity)
    pd.testing.assert_frame_equal(run.trades, run2.trades)
    full = historie.run_all([path], ["BTC"]).runs["config_test"]             # ohne --ende: bis zur letzten Kerze
    assert full.equity.index[-1] > end
    pd.testing.assert_series_equal(full.equity[full.equity.index < end], run.equity)


def test_cache_fest_laedt_und_loescht_nie_und_bricht_ohne_datei_ab(monkeypatch, tmp_path):
    """--cache-fest: auch eine alte Datei gilt (kein Nachladen, kein Löschen); fehlt eine, bricht die Simulation ab."""
    monkeypatch.setattr(historie, "CACHE", tmp_path)
    monkeypatch.setitem(sys.modules, "ccxt", None)         # ohne Netz: jeder Versuch nachzuladen schlägt fehl
    datei = tmp_path / "bitstamp_BTC_1d.csv"
    _tage("2020-01-01", [100, 101, 102]).to_csv(datei)
    alt = time.time() - 30 * 86400
    os.utime(datei, (alt, alt))                            # älter als 7 Tage: ohne --cache-fest würde nachgeladen
    used = []
    df = historie.load_coin("BTC", "1d", fixed=True, used=used)
    assert list(df["close"]) == [100, 101, 102] and used == [datei]
    assert datei.exists() and datei.stat().st_mtime == pytest.approx(alt)
    with pytest.raises(ImportError):
        historie.load_coin("BTC", "1d")                    # zum Vergleich: ohne --cache-fest wird nachgeladen
    with pytest.raises(SystemExit, match="ETH 1d"):
        historie.load_coin("ETH", "1d", fixed=True)
    assert sorted(f.name for f in tmp_path.iterdir()) == ["bitstamp_BTC_1d.csv"]


class _Boerse:
    """ccxt-Börse ohne Netz: Tageskerzen BTC/USD vom 1.1. bis 28.2.2020, falls sie den Coin hat."""
    def __init__(self, hat: bool):
        self.hat = hat

    def load_markets(self):
        return {"BTC/USD": {}} if self.hat else {}

    def parse8601(self, text):
        return pd.Timestamp(text).value // 10**6

    def milliseconds(self):
        return pd.Timestamp("2020-03-01", tz="UTC").value // 10**6

    def iso8601(self, ms):
        return pd.Timestamp(ms, unit="ms", tz="UTC").isoformat()

    def fetch_ohlcv(self, symbol, timeframe, since=None, limit=1000):
        tage = pd.date_range("2020-01-01", "2020-02-28", freq="D", tz="UTC")
        return [[t.value // 10**6, 7.0, 7.0, 7.0, 7.0, 1.0] for t in tage if t.value // 10**6 >= since][:limit]


def test_quellen_mischen_sich_nie(monkeypatch, tmp_path):
    """Jede Börse hat eigene Cache-Dateien: Es zählen nur die der gewählten Quellen, und nur sie werden ersetzt."""
    monkeypatch.setattr(historie, "CACHE", tmp_path)
    assert historie.sources(None) == historie.SOURCES
    assert historie.sources(["coinbase", "Bitfinex:usdt"]) == (("coinbase", "USD"), ("bitfinex", "USDT"))
    with pytest.raises(SystemExit):
        historie.sources(["../coinbase"])
    alt = time.time() - 30 * 86400
    for name, preis in (("binance", 1.0), ("coinbase", 2.0)):
        _tage("2020-01-01", [preis] * 3).to_csv(tmp_path / f"{name}_BTC_1d.csv")
        os.utime(tmp_path / f"{name}_BTC_1d.csv", (alt, alt))
    used = []
    coinbase = historie.load_coin("BTC", "1d", sources=historie.sources(["coinbase"]), fixed=True, used=used)
    assert set(coinbase["close"]) == {2.0} and used == [tmp_path / "coinbase_BTC_1d.csv"]
    # Standardquellen, Datei von binance zu alt: neu laden (nur bitstamp hat den Coin) ersetzt sie, Coinbase bleibt
    monkeypatch.setitem(sys.modules, "ccxt", types.SimpleNamespace(
        **{name: (lambda cfg, hat=name == "bitstamp": _Boerse(hat)) for name, _ in historie.SOURCES}))
    used = []
    neu = historie.load_coin("BTC", "1d", used=used)
    assert set(neu["close"]) == {7.0} and used == [tmp_path / "bitstamp_BTC_1d.csv"]
    assert sorted(f.name for f in tmp_path.iterdir()) == ["bitstamp_BTC_1d.csv", "coinbase_BTC_1d.csv"]
    assert set(pd.read_csv(tmp_path / "coinbase_BTC_1d.csv")["close"]) == {2.0}


def test_fingerabdruck_ueber_name_und_inhalt(tmp_path):
    """Gleiche Kursdateien geben überall denselben Fingerabdruck (Reihenfolge und Ordner egal); jede Änderung am
    Inhalt oder am Namen gibt einen anderen."""
    a, b = tmp_path / "bitstamp_BTC_1h.csv", tmp_path / "kucoin_ETH_1h.csv"
    a.write_text("timestamp,close\n2020-01-01,7200.5\n")
    b.write_text("timestamp,close\n2020-01-01,130.1\n")
    fp = historie.cache_fingerprint([a, b])
    zeilen = "".join(f"{f.name} {hashlib.sha256(f.read_bytes()).hexdigest()}\n" for f in (a, b))
    assert fp == hashlib.sha256(zeilen.encode()).hexdigest()                  # von Hand nachrechenbar
    assert historie.cache_fingerprint([b, a, a]) == fp
    kopie = tmp_path / "kopie"
    kopie.mkdir()
    for f in (a, b):
        (kopie / f.name).write_bytes(f.read_bytes())
    assert historie.cache_fingerprint([kopie / a.name, kopie / b.name]) == fp
    ende = pd.Timestamp("2023-01-01", tz="UTC")
    kopf = historie.herkunft([a, b], historie.sources(["coinbase"]), fixed=True, end=ende)
    assert fp in kopf and "coinbase (USD)" in kopf and "eingefroren" in kopf and "31.12.2022" in kopf
    (kopie / a.name).rename(kopie / "binance_BTC_1h.csv")
    assert historie.cache_fingerprint([kopie / "binance_BTC_1h.csv", kopie / b.name]) != fp
    a.write_text("timestamp,close\n2020-01-01,7200.6\n")
    assert historie.cache_fingerprint([a, b]) != fp


# --- run_all: Coins je Bot, Chef nur mit den Stil-Bots

def test_run_all_gibt_jedem_bot_seine_coins_und_dem_chef_die_stil_bots(monkeypatch, tmp_path):
    monkeypatch.setattr(historie, "CACHE", tmp_path)
    kurse = {c: _welle("2020-01-01", 300, p) for c, p in (("BTC", 100.0), ("ETH", 10.0), ("SOL", 1.0))}
    monkeypatch.setattr(historie, "load_coin", _laden(kurse))
    coins, chef = {}, []

    def simulate(cfg, frames, *a, **k):
        coins[cfg.name] = list(frames)
        return historie.BotRun(cfg, frames[next(iter(frames))]["close"], pd.DataFrame(), 0, 0)
    monkeypatch.setattr(historie, "simulate", simulate)
    monkeypatch.setattr(historie, "simulate_chef", lambda runs, *a, **k: chef.append(list(runs)) or pd.Series([1.0]))
    bots = {"config_phasen": ("BTC/CHF", "ETH/CHF"), "config_risiko": ("SOL/CHF", "ETH/CHF"),
            "config_daytrading": ("BTC/CHF",), "config_langfrist": ("SOL/CHF", "BTC/CHF")}
    paths = {n: _bot(tmp_path, n, s) for n, s in bots.items()}
    g = historie.run_all(list(paths.values()), ["BTC", "ETH", "SOL"])
    assert coins == {"config_phasen": ["BTC/USD", "ETH/USD"], "config_risiko": ["ETH/USD", "SOL/USD"],
                     "config_daytrading": ["BTC/USD"], "config_langfrist": ["BTC/USD", "SOL/USD"]}
    assert chef == [["config_langfrist", "config_daytrading", "config_risiko"]] and g.chef is not None
    g = historie.run_all([paths[n] for n in ("config_phasen", "config_daytrading", "config_langfrist")],
                         ["BTC", "ETH", "SOL"])
    assert g.chef is None and len(chef) == 1                  # ohne Risiko-Bot kein Chef


# --- Kennzahlen: von Hand nachrechenbar

def test_broker_zaehlt_umschlag_gebuehren_und_slippage():
    from tradingbot.broker import PaperBroker
    b = PaperBroker(1000, fee_rate=0.01, slippage=0.001)
    b.buy("X", 2, 100.0)                       # zu 100,10: Slippage 2 × 0,10
    b.quotes["X"] = (99.0, 101.0)
    b.sell("X", 1, 100.0, market=True)         # zum Geldkurs 99: 1,00 unter dem Mittelkurs
    b.sell("X", 1, 100.0)                      # Stop oder Ziel: zu 99,90, Slippage 0,10
    assert b.turnover == pytest.approx(200.2 + 99 + 99.9)
    assert b.fees_paid == pytest.approx(0.01 * (200.2 + 99 + 99.9))
    assert b.slippage_paid == pytest.approx(0.2 + 1.0 + 0.1)


def test_kennzahlen_von_hand_nachgerechnet(monkeypatch):
    """1'000 Startkapital, BTC 100 bis zum 16.3.2021 und 110 ab dem 17.3., Handel ab dem 7.3. Kauf zur Eröffnung am
    12.3.: 5 BTC (Deckel 50 %) zu 100,05 (Slippage 0,05 %), Gebühr 1 % = 5,0025. Verkauf am 22.3. zu 109,945, Gebühr
    5,49725. Kapital: 5 Tage 1'000, 5 Tage 994,7475, 5 Tage 1'044,7475, 20 Tage 1'038,97525."""
    from tradingbot.config import RiskConfig
    kurse = _tage("2021-01-01", [100.0] * 75 + [110.0] * 25)
    _skript(monkeypatch, {"BTC": {"2021-03-11": 1, "2021-03-21": -1}})
    risk = RiskConfig(risk_per_trade=1.0, stop_loss_atr=50, take_profit_atr=1000, max_position_pct=0.5,
                      max_total_risk_pct=100, max_daily_loss_pct=1, max_drawdown_pct=0.99, loss_streak_pause=99,
                      max_trades_per_day=99, min_order_value=1)
    cfg = Config(symbols=["BTC/USD"], timeframe="1d", strategy="skript", fee_rate=0.01, slippage=0.0005,
                 starting_capital=1000, risk=risk)
    run = historie.simulate(cfg, {"BTC/USD": kurse}, pd.Timestamp("2021-03-07", tz="UTC"))
    kurve = [1000] * 5 + [994.7475] * 5 + [1044.7475] * 5 + [1038.97525] * 20
    assert list(run.equity) == pytest.approx(kurve)
    mittel, jahre = sum(kurve) / 35, 34 / 365.25
    kosten = 5.0025 + 5.49725 + 0.25 + 0.275             # Gebühren und Slippage; ohne Hebel keine Zinsen
    s = historie.segment(run, "2021-01-01", "2022-01-01")     # frischer Start: ab dem Startkapital
    assert s["Rendite %"] == 3.9 and s["Max. DD %"] == -0.6 and s["Trades"] == 1 and s["Not-Aus"] == 0
    assert s["Gebühren bezahlt"] == 10.5
    assert s["Kosten % pro Jahr"] == round(kosten / mittel / jahre * 100, 2) == 11.52
    assert s["Umschlag pro Jahr"] == round((500.25 + 549.725) / mittel / jahre, 2) == 10.97
    assert s["Ø investiert %"] == round((5 * 500 / 994.7475 + 5 * 550 / 1044.7475) / 35 * 100, 1) == 14.7
    assert s["Zeit im Markt %"] == round(10 / 35 * 100, 1)
    assert s["Kostenanteil am Bruttogewinn %"] == round(kosten / (38.97525 + kosten) * 100, 1) == 22.0
    assert s["Trades je Coin und Jahr"] == round(1 / (35 / 365.25), 2)
    teil = historie.segment(run, "2021-03-15", "2022-01-01")  # Ausschnitt: ab dem Kapital am 15.3.
    assert teil["Gebühren bezahlt"] == 5.5 and teil["Rendite %"] == round((1038.97525 / 994.7475 - 1) * 100, 1)
    ab_kauf = historie.simulate(cfg, {"BTC/USD": kurse}, pd.Timestamp("2021-03-12", tz="UTC"))
    s = historie.segment(ab_kauf, "2021-01-01", "2022-01-01")    # frischer Start: der Kauf am ersten Tag zählt mit
    assert ab_kauf.equity.iloc[0] == pytest.approx(994.7475) and s["Rendite %"] == 3.9 and s["Gebühren bezahlt"] == 10.5
    # Bitcoin halten nach Kosten: am 7.3. kaufen zu 100,05 mit 0,8 % Taker-Gebühr (unterste Kraken-Stufe)
    menge = 1000 / (100.05 * 1.008)
    halten = historie.hold_run(kurse["close"], 1000, 0.008, 0.0005, start="2021-03-07")
    h = historie.segment(halten, "2021-01-01", "2022-01-01")
    assert halten.equity.iloc[-1] == pytest.approx(menge * 110)
    assert h["Rendite %"] == round((menge * 110 / 1000 - 1) * 100, 1) == 9.1
    assert h["Gebühren bezahlt"] == round(menge * 100.05 * 0.008, 2) == 7.94
    assert h["Max. DD %"] == round((menge * 100 / 1000 - 1) * 100, 1) == -0.8
    assert h["Ø investiert %"] == 100 and h["Zeit im Markt %"] == 100 and h["Trades"] == 0
    assert h["Umschlag pro Jahr"] == round(menge * 100.05 / ((10 * menge * 100 + 25 * menge * 110) / 35) / jahre, 2)
    assert run.stats(kurse["close"])["B&H nach Kosten %"] == round((1.1 / (1.0005 * 1.008) - 1) * 100, 2) == 9.07


# --- --abschnitte: jeder Abschnitt ein frischer Start

def test_abschnitte_sind_frische_starts_mit_dem_startkapital(monkeypatch, tmp_path):
    monkeypatch.setattr(historie, "CACHE", tmp_path)
    monkeypatch.setattr(historie, "PERIODS", {"vorher": ("2011-01-01", "2020-09-01"),
                                              "nachher": ("2020-09-01", "2100-01-01")})
    kurse = _welle("2019-03-01", 900)
    monkeypatch.setattr(historie, "load_coin", _laden({"BTC": kurse}))
    path = _bot(tmp_path)
    assert historie.run_all([path], ["BTC"]).fresh == {}              # ohne --abschnitte wie bisher
    g = historie.run_all([path], ["BTC"], sections=True)
    lang, frisch = g.runs["config_test"], {k: v["config_test"] for k, v in g.fresh.items()}
    neu = historie.simulate(Config.load(path), {"BTC/USD": kurse}, pd.Timestamp("2020-09-01", tz="UTC"))
    pd.testing.assert_series_equal(frisch["nachher"].equity, neu.equity)
    pd.testing.assert_frame_equal(frisch["nachher"].trades, neu.trades)
    nachher = historie.PERIODS["nachher"]
    assert historie.segment(frisch["nachher"], *nachher) == historie.segment(neu, *nachher)
    # vor dem ersten Abschnitt gibt es keine Kurse: frischer Start = der lange Lauf bis zum Ende des Abschnitts
    pd.testing.assert_series_equal(frisch["vorher"].equity, lang.equity[lang.equity.index < "2020-09-01"])
    # der lange Lauf steht seit seinem Not-Aus still, der frische Start handelt mit neuem Kapital
    auszug, ab = historie.segment(lang, *nachher), historie.segment(frisch["nachher"], *nachher)
    assert auszug["Not-Aus"] == 1 and ab["Not-Aus"] == 0 and ab["Trades"] > auszug["Trades"]
    assert "frischer Start" in historie.report(g.runs, None, g.btc, fresh=g.fresh)
    assert "Ausschnitt aus dem Lauf" in historie.report(g.runs, None, g.btc)


# --- slot_cap: Deckel je Coin = max_invested_pct / Coins mit mindestens 200 Tageskerzen

def test_slot_cap_in_der_simulation(monkeypatch, tmp_path):
    """BTC ab 1.1.2020, ETH ab 10.4.2020 (200. Tageskerze am 26.10.). Kauf am 26.10.: ETH hat erst 199
    abgeschlossene Tageskerzen, also 75 % für BTC. Am 6.11. zählen beide: je 37,5 %. Ohne slot_cap 20 %."""
    kurse = {"BTC/USD": _tage("2020-01-01", [100.0] * 400), "ETH/USD": _tage("2020-04-10", [10.0] * 300)}
    _skript(monkeypatch, {"BTC": {"2020-10-25": 1, "2020-10-31": -1, "2020-11-05": 1, "2020-11-10": -1},
                          "ETH": {"2020-11-05": 1, "2020-11-10": -1}})
    groessen = {}
    for slot_cap in (True, False):
        path = tmp_path / f"slots_{slot_cap}.yaml"
        path.write_text(yaml.safe_dump({
            "symbols": ["BTC/CHF", "ETH/CHF"], "timeframe": "1d", "strategy": "skript", "starting_capital": 1000,
            "fee_rate": 0.0, "slippage": 0.0, "risk": {"max_position_pct": 0.2, "max_invested_pct": 0.75,
                                                       "slot_cap": slot_cap, "risk_per_trade": 0.1,
                                                       "max_total_risk_pct": 1.0}}), encoding="utf-8")
        run = historie.simulate(Config.load(path), kurse)
        groessen[slot_cap] = [(t.symbol, f"{t.opened:%d.%m.}", round(t.qty * t.entry / 1000, 4))
                              for t in run.trades.itertuples()]
    assert groessen[True] == [("BTC/USD", "26.10.", 0.75), ("BTC/USD", "06.11.", 0.375), ("ETH/USD", "06.11.", 0.375)]
    assert groessen[False] == [("BTC/USD", "26.10.", 0.2), ("BTC/USD", "06.11.", 0.2), ("ETH/USD", "06.11.", 0.2)]


def test_slot_cap_im_demo_betrieb(monkeypatch, tmp_path):
    """bot.py zählt wie die Simulation nur abgeschlossene Tageskerzen vor heute: BTC 400, ETH genau 200, SOL 199 (dazu
    je die offene Kerze von heute). Deckel 75 % / 2 = 37,5 % je Coin (statt max_position_pct 20 %); für SOL bleibt
    unter den 75 % nichts mehr übrig. Ein Coin ohne Tageskerzen zählt mit."""
    import json
    from datetime import datetime, timezone
    from test_core import ConstStrategy, MultiExchange, Uhr
    from tradingbot import bot, data
    from tradingbot.config import RiskConfig
    jetzt = datetime(2024, 1, 13, 13, 5, tzinfo=timezone.utc)
    tage = {"BTC/CHF": 400, "ETH/CHF": 200, "SOL/CHF": 199}

    class Boerse(MultiExchange):
        def fetch_ohlcv(self, symbol, timeframe, limit=300, since=None):
            if timeframe != "1d":
                return super().fetch_ohlcv(symbol, timeframe, limit, since)
            idx = pd.date_range(end=pd.Timestamp(jetzt).normalize(), periods=tage[symbol] + 1, freq="D")
            return [[t.value // 10**6, 1.0, 1.0, 1.0, 1.0, 1.0] for t in idx][-limit:]

    ex = Boerse(data.synthetic(bars=1500, seed=1))
    assert bot._slots(ex, list(tage), jetzt) == 2 and bot._slots(ex, ["BTC/CHF", "DOGE/CHF"], jetzt) == 2
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: ex)
    monkeypatch.setattr(bot, "build", lambda *a, **k: ConstStrategy(1))
    monkeypatch.setattr(bot, "datetime", Uhr)
    monkeypatch.setattr(Uhr, "t", jetzt)
    cfg = Config(symbols=list(tage), use_news=False, name="slots", poll_seconds=0, fee_rate=0.0, slippage=0.0,
                 risk=RiskConfig(max_position_pct=0.2, max_invested_pct=0.75, slot_cap=True, risk_per_trade=0.5,
                                 max_total_risk_pct=5, correlation_limit=1.01))
    bot.run(cfg, max_iterations=1)
    offen = json.loads(cfg.state_path.read_text())["open_trades"]
    assert {s: round(t["qty"] * t["entry"] / 1000, 4) for s, t in offen.items()} == {"BTC/CHF": 0.375, "ETH/CHF": 0.375}


# --- Befehl: alle neuen Optionen zusammen

def test_befehl_historie_blind_aus_dem_eingefrorenen_cache(monkeypatch, tmp_path):
    """historie --ende 2020-12-31 --cache-fest --quellen coinbase --abschnitte: ohne Netz nur aus der Coinbase-Datei,
    die Datei einer anderen Börse bleibt unberührt; der Bericht nennt Herkunft und Fingerabdruck."""
    from tradingbot import __main__ as cli
    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(sys.modules, "ccxt", None)
    cache = tmp_path / "data" / "historie"
    cache.mkdir(parents=True)
    coinbase, fremd = cache / "coinbase_BTC_1d.csv", cache / "bitstamp_BTC_1d.csv"
    _welle("2019-03-01", 900).to_csv(coinbase)
    _welle("2019-03-01", 900, 50.0).to_csv(fremd)
    alt = time.time() - 30 * 86400
    for f in (coinbase, fremd):
        os.utime(f, (alt, alt))
    inhalt = fremd.read_bytes()
    _bot(tmp_path, "bot")
    monkeypatch.setattr(sys, "argv", ["tradingbot", "historie", "--bots", "bot.yaml", "--ende", "2020-12-31",
                                      "--cache-fest", "--quellen", "coinbase", "--abschnitte"])
    cli.main()
    text = (tmp_path / "lernen" / "HISTORIE.md").read_text(encoding="utf-8")
    assert "Kurse von coinbase (USD), Cache eingefroren, nur bis 31.12.2020" in text
    assert historie.cache_fingerprint([coinbase]) in text and "frischer Start" in text
    kurven = pd.read_csv(cache / "kurven.csv", index_col=0, parse_dates=True)
    assert kurven.index[-1] == pd.Timestamp("2020-12-31", tz="UTC")
    assert fremd.read_bytes() == inhalt and fremd.stat().st_mtime == pytest.approx(alt)
