"""Auswertung für den Profi-Bot (python -m tradingbot profi): Überlagerungen, Fenster, Sperre ab 2023, Prüfprotokoll,
gepaarter Block-Bootstrap, Regel G, Tor, E5-Kriterien, Go-Regeln und Zusammenfassen über zwei Caches."""
import json
import shutil
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest
import yaml

from test_profi_werkzeug import _welle
from tradingbot import auswertung as aw
from tradingbot import historie
from tradingbot.config import Config

BOTS = Path(__file__).resolve().parent.parent / "bots"
KERN = {"symbols": ["BTC/CHF"], "starting_capital": 100, "fee_model": "kraken", "use_news": False, "use_events": False,
        "horizons": {"kern": {"timeframe": "1d", "strategy": "regime",
                              "strategy_params": {"period": 200, "band": 0.03}}},
        "risk": {"risk_per_trade": 0.12, "stop_loss_atr": 8.0, "take_profit_atr": 1000, "max_position_pct": 0.75,
                 "max_invested_pct": 0.75, "max_drawdown_pct": 0.35, "halt_days": 30, "max_total_risk_pct": 1.0,
                 "loss_streak_pause": 99, "correlation_limit": 1.01}}


# --- Überlagerungen und Config-Prüfung

def test_ueberlagerung_ist_ein_deep_merge_und_geht_durch_die_config_pruefung(tmp_path):
    neu = aw.ueberlagern(KERN, {"symbols": ["BTC/CHF", "ETH/CHF"], "risk": {"max_drawdown_pct": 0.99},
                                "horizons": {"kern": {"strategy_params": {"band": 0.05}, "trail_atr": 6}}})
    assert neu["symbols"] == ["BTC/CHF", "ETH/CHF"]                         # Listen ersetzen
    assert neu["horizons"]["kern"] == {"timeframe": "1d", "strategy": "regime", "trail_atr": 6,
                                       "strategy_params": {"period": 200, "band": 0.05}}
    assert neu["risk"] == KERN["risk"] | {"max_drawdown_pct": 0.99}
    neu["horizons"]["kern"]["strategy_params"]["period"] = 150
    assert KERN["horizons"]["kern"]["strategy_params"] == {"period": 200, "band": 0.03}     # Basis unverändert
    cfg = aw.pruefen(neu, "kern+trail")
    assert (cfg.name, cfg.risk.max_drawdown_pct, cfg.horizon_list()[0].trail_atr) == ("kern+trail", 0.99, 6)
    for falsch in ({"risk": {"max_drawdown": 0.9}}, {"horizons": {"kern": {"trail": 6}}}, {"fee_faktor": 1.5},
                   {"horizons": {"kernn": {"strategy_params": {"band": 0.05}}}}):
        with pytest.raises(SystemExit, match="ungültige Config"):
            aw.pruefen(aw.ueberlagern(KERN, falsch), "falsch")
    # Config.from_dict ist dieselbe Prüfung wie Config.load
    for name in ("config_langfrist", "config_daytrading", "config_risiko", "config_phasen"):
        raw = yaml.safe_load((BOTS / f"{name}.yaml").read_text(encoding="utf-8"))
        assert Config.from_dict(raw, name) == Config.load(BOTS / f"{name}.yaml")
    # Dateien: Amtsinhaber = Basis + Sieger, Herausforderer = Amtsinhaber + eigene Überlagerung
    (tmp_path / "kb3.yaml").write_text(yaml.safe_dump(KERN), encoding="utf-8")
    (tmp_path / "kb5.yaml").write_text("horizons: {kern: {strategy_params: {band: 0.05}}}\n", encoding="utf-8")
    (tmp_path / "ohne.yaml").write_text("risk: {max_drawdown_pct: 0.99}\n", encoding="utf-8")
    amt, var = [tmp_path / "kb3.yaml", tmp_path / "kb5.yaml"], [tmp_path / "ohne.yaml"]
    assert aw.namen(amt, var) == ("kb3+kb5", ["kb3+kb5+ohne"])
    b = aw.bot("kb3+kb5+ohne", amt, var)
    assert (b.rolle, b.nr, b.ueberlagerung, b.dateien) == ("herausforderer", 1, {"risk": {"max_drawdown_pct": 0.99}},
                                                          tuple(map(str, amt + var)))
    assert b.config["horizons"]["kern"]["strategy_params"]["band"] == 0.05 and b.cfg.risk.max_drawdown_pct == 0.99
    assert aw.bot("kb3+kb5", amt, var).rolle == "amtsinhaber"
    assert aw.ist_kostenstress({"fee_factor": 1.5, "slippage": 0.001}) and not aw.ist_kostenstress(b.ueberlagerung)


def test_kostenstress_fee_factor():
    from tradingbot.broker import KRAKEN_TIERS, paper_broker
    assert paper_broker(Config(fee_model="kraken")).tiers is KRAKEN_TIERS                    # Standard unverändert
    stress = paper_broker(Config(fee_model="kraken", fee_factor=1.5))
    assert [t[2] for t in stress.tiers] == pytest.approx([t[2] * 1.5 for t in KRAKEN_TIERS])
    assert paper_broker(Config(fee_rate=0.002, fee_factor=1.5)).fee_rate == pytest.approx(0.003)


# --- Fenster, Plan und Auswahl

def test_fensterlisten_und_plan():
    g = aw.gestaffelt()
    assert len(g) == 28 and g[0] == aw.Fenster("3J-2013Q1", "2013-01-01", "2015-12-31")
    assert g[-1] == aw.Fenster("3J-2019Q4", "2019-10-01", "2022-09-30")
    assert [f.start for f in g[:5]] == ["2013-01-01", "2013-04-01", "2013-07-01", "2013-10-01", "2014-01-01"]
    assert not any(f.gesperrt for f in [*g, *aw.STANDARD, *aw.CRASH])
    p = aw.gestaffelt_pruefung()
    assert len(p) == 12 and p[0] == aw.Fenster(aw.PRUEFUNG, "2023-01-01") and p[-1].start == "2025-10-01"
    assert all(f.ende is None and f.gesperrt for f in p) and aw.CRASH_2022.gesperrt
    assert [tuple(f) for f in aw.STANDARD] == [("2012-2022", "2012-01-01", "2022-12-31"),
                                                ("2012-2019", "2012-01-01", "2019-12-31"),
                                                ("2020-2022", "2020-01-01", "2022-12-31")]
    assert [tuple(f) for f in aw.CRASH] == [("Crash-2014", "2014-01-01", "2022-12-31"),
                                             ("Crash-2018", "2018-01-01", "2022-12-31")]
    assert aw.STANDARD[0].bis == aw.SPERRE and aw.STANDARD[0].von == pd.Timestamp("2012-01-01", tz="UTC")
    e0 = aw.plan("E0")
    assert list(e0) == [*aw.PFADE, "chef", "bitcoin_halten"] and all(fs == [aw.STANDARD[0]] for fs in e0.values())
    e1 = aw.plan("E1", "a", ["a+b"])
    assert list(e1) == ["a", "a+b", "p_minus_1", "bitcoin_halten"] and all(fs == list(aw.STANDARD) for fs in e1.values())
    e5 = aw.plan("E5", "a", ["a+n"])
    assert len(e5["a"]) == 1 + 1 + 28 + 2 and e5["a+n"] == [aw.STANDARD[0]] and e5["bitcoin_halten"] == e5["a"]
    assert e5["p_minus_1"] == [aw.Fenster("2016-2022", "2016-01-01", "2022-12-31")]
    e6 = aw.plan("E6", "a", ["a+o"])
    assert e6["a"] == [*p, aw.CRASH_2022] and e6["a+o"] == [p[0], aw.CRASH_2022] and e6["config_daytrading"] == p
    assert e6["k1"] == p[:1] and e6["p_minus_1"] == [p[0], aw.CRASH_2022] and list(e6)[-2:] == ["chef", "bitcoin_halten"]
    assert aw.plan("E6", "p_minus_1")["p_minus_1"] == [*p, aw.CRASH_2022]      # P−1 als Kandidat: alle Fenster
    for falsch in (("E1",), ("E7", "a"), ("E0", None, ["x"])):
        with pytest.raises(SystemExit):
            aw.plan(*falsch)
    assert aw.eigenes_fenster("2016-01-01", "2022-12-31") == aw.Fenster("2016-2022", "2016-01-01", "2022-12-31")
    assert aw.eigenes_fenster(None, "2022-12-31") == aw.STANDARD[0]
    assert aw.eigenes_fenster("2022-06-01", None) == aw.Fenster("2022-06-01-bis-Ende", "2022-06-01")
    with pytest.raises(SystemExit):
        aw.eigenes_fenster("2020-01-01", "2019-12-31")
    assert aw.plan("E1", "a", eigenes=aw.eigenes_fenster("2016-01-01", "2022-12-31"))["a"][0].name == "2016-2022"
    assert aw.auswahl(e6, ["a", "chef"], ["ab-2023Q2"]) == {"chef": [p[1]], "a": [p[1]]}
    with pytest.raises(SystemExit, match="Bot nicht im Plan: k2"):
        aw.auswahl(e0, ["k2"])
    with pytest.raises(SystemExit, match="Fenster nicht im Plan: 2013-2022"):
        aw.auswahl(e0, None, ["2013-2022"])


# --- Befehl: Ergebnisdateien, Sperre ab 2023 und Prüfprotokoll

@pytest.fixture
def ordner(tmp_path, monkeypatch):
    """Arbeitsordner ohne Netz: BTC-Tageskerzen vom 1.1.2021 bis 19.6.2023 im eingefrorenen Cache, ein Kern-Bot, eine
    Variante (Puffer 5 %) und P−1."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setitem(sys.modules, "ccxt", None)
    (tmp_path / "data" / "historie").mkdir(parents=True)
    _welle("2021-01-01", 900).to_csv(tmp_path / "data" / "historie" / "bitstamp_BTC_1d.csv")
    (tmp_path / "bots" / "profi" / "varianten").mkdir(parents=True)
    (tmp_path / "bots" / "profi" / "kern.yaml").write_text(yaml.safe_dump(KERN), encoding="utf-8")
    (tmp_path / "bots" / "profi" / "varianten" / "band5.yaml").write_text(
        "horizons: {kern: {strategy_params: {band: 0.05}}}\n", encoding="utf-8")
    p1 = aw.ueberlagern(KERN, {"risk": {"risk_per_trade": 100, "max_position_pct": 1.0, "max_invested_pct": 1.0,
                                        "max_drawdown_pct": 0.99}})
    (tmp_path / "bots" / "profi" / "p_minus_1.yaml").write_text(yaml.safe_dump(p1), encoding="utf-8")
    return tmp_path


def _profi(monkeypatch, *args):
    from tradingbot import __main__ as cli
    monkeypatch.setattr(sys, "argv", ["tradingbot", "profi", *args])
    cli.main()


def test_befehl_profi_schreibt_je_lauf_eine_ergebnisdatei(ordner, monkeypatch, capsys):
    gesehen = []
    echt = historie.simulate

    def spion(cfg, coins, *a, **k):
        gesehen.append(max(df.index[-1] for df in coins.values()))
        return echt(cfg, coins, *a, **k)
    monkeypatch.setattr(historie, "simulate", spion)
    args = ["--schritt", "E1", "--config", "bots/profi/kern.yaml", "--varianten", "bots/profi/varianten/band5.yaml",
            "--start", "2022-01-01", "--ende", "2022-12-31", "--cache-fest"]
    _profi(monkeypatch, *args, "--liste")
    jobs = json.loads(capsys.readouterr().out)["include"]
    assert jobs == [{"bot": b, "fenster": "2022"} for b in ("kern", "kern+band5", "p_minus_1", "bitcoin_halten")]
    _profi(monkeypatch, *args)
    csv = ordner / "data" / "historie" / "bitstamp_BTC_1d.csv"
    cache = historie.cache_fingerprint([csv])
    assert aw.cache_id() == cache and gesehen and max(gesehen) < aw.SPERRE   # Kurse ab 2023 abgeschnitten
    dateien = sorted(p.name for p in (ordner / "lernen" / "profi" / "E1" / cache[:12]).iterdir())
    assert dateien == [f"{b}__2022__normiert.json" for b in ("bitcoin_halten", "kern+band5", "kern", "p_minus_1")]
    e = json.loads(aw.datei("E1", cache, "kern+band5", "2022", "normiert").read_text(encoding="utf-8"))
    assert (e["schritt"], e["rolle"], e["amtsinhaber"], e["nr"], e["gebuehren"]) == ("E1", "herausforderer", "kern",
                                                                                    1, "normiert")
    assert e["fenster"] == {"name": "2022", "start": "2022-01-01", "ende": "2022-12-31"} and not e["pruefung"]
    assert e["config"] == aw.ueberlagern(KERN, {"horizons": {"kern": {"strategy_params": {"band": 0.05}}}})
    assert e["ueberlagerung"] == {"horizons": {"kern": {"strategy_params": {"band": 0.05}}}}
    assert e["dateien"] == ["bots/profi/kern.yaml", "bots/profi/varianten/band5.yaml"]
    assert e["quellen"] == [list(q) for q in historie.SOURCES] and e["cache"] == cache and e["cache_fest"]
    assert e["kursdateien"] == ["bitstamp_BTC_1d.csv"] and e["kurs_fingerabdruck"] == cache
    assert e["commit"] == "unbekannt" and e["befehl"] == "python -m tradingbot profi " + " ".join(args)
    # dieselben Zahlen wie ein frischer Start mit historie.simulate und segment
    kurse = pd.read_csv(csv, index_col=0, parse_dates=True)
    von, bis = pd.Timestamp("2022-01-01", tz="UTC"), pd.Timestamp("2023-01-01", tz="UTC")
    run = echt(Config.from_dict(e["config"], "kern+band5"), {"BTC/USD": kurse[kurse.index < bis]}, von, end=bis)
    assert e["kennzahlen"] == historie.segment(run, von, bis) and e["startkapital"] == 100
    assert list(e["kurve"])[0] == "2022-01-01" and list(e["kurve"])[-1] == "2022-12-31" == e["letzter_tag"]
    assert list(e["kurve"].values()) == pytest.approx(list(run.equity), abs=1e-4)
    halten = json.loads(aw.datei("E1", cache, "bitcoin_halten", "2022", "normiert").read_text(encoding="utf-8"))
    assert halten["rolle"] == "benchmark" and halten["config"] == {"startkapital": 100, "gebuehr": 0.008,
                                                                   "slippage": 0.0005}
    text = (ordner / "lernen" / "PROFI_ERGEBNISSE.md").read_text(encoding="utf-8")
    assert "### Regel G gegen den Amtsinhaber kern" in text and "**Sieger von E1:" in text
    assert not (ordner / "lernen" / "HISTORIE.md").exists() and not (ordner / "lernen" / "PROFI_PRUEFPROTOKOLL.md").exists()
    neu = (ordner / "lernen" / "PROFI_ERGEBNISSE.md").stat().st_mtime_ns
    monkeypatch.setattr(historie, "simulate", lambda *a, **k: pytest.fail("zusammenfassen simuliert nie"))
    _profi(monkeypatch, "--zusammenfassen")
    assert (ordner / "lernen" / "PROFI_ERGEBNISSE.md").read_text(encoding="utf-8") == text
    assert (ordner / "lernen" / "PROFI_ERGEBNISSE.md").stat().st_mtime_ns >= neu


@pytest.mark.parametrize("fenster", [["--schritt", "E6", "--config", "bots/profi/kern.yaml"],
                                     ["--schritt", "E1", "--config", "bots/profi/kern.yaml", "--start", "2022-06-01"],
                                     ["--schritt", "E1", "--config", "bots/profi/kern.yaml", "--ende", "2023-01-01"],
                                     ["--schritt", "E5", "--config", "bots/profi/kern.yaml", "--start", "2023-02-01",
                                      "--ende", "2023-03-31"]])
def test_sperre_verweigert_kurse_ab_2023_ohne_pruefung(ordner, monkeypatch, fenster):
    """Auch ein offenes Ende (bis Datenende) berührt die weggesperrten Jahre."""
    monkeypatch.setattr(historie, "simulate", lambda *a, **k: pytest.fail("gesperrt: nichts rechnen"))
    with pytest.raises(SystemExit, match="Gesperrt"):
        _profi(monkeypatch, *fenster)
    with pytest.raises(SystemExit, match="Gesperrt"):
        _profi(monkeypatch, *fenster, "--liste")
    assert not (ordner / "lernen").exists()


def test_pruefung_haengt_jeden_lauf_ans_protokoll(ordner, monkeypatch):
    args = ["--schritt", "E1", "--config", "bots/profi/kern.yaml", "--start", "2023-01-01", "--cache-fest",
            "--nur-bot", "kern", "--pruefung"]
    protokoll = ordner / "lernen" / "PROFI_PRUEFPROTOKOLL.md"
    _profi(monkeypatch, *args)
    erst = protokoll.read_text(encoding="utf-8")
    cache = historie.cache_fingerprint([ordner / "data" / "historie" / "bitstamp_BTC_1d.csv"])
    eintrag = erst.splitlines()[-1]                                          # ein Eintrag ist genau eine Zeile
    assert erst.startswith("# Profi-Bot: Prüfprotokoll") and erst.count("\n- ") == 1 and eintrag.startswith("- **20")
    assert f" · Cache-Fingerabdruck `{cache}` (eingefroren, --cache-fest) · " in eintrag
    assert " · Befehl `python -m tradingbot profi " + " ".join(args) + "` · " in eintrag
    assert " UTC** · Commit `unbekannt` (tradingbot/ oder bots/ mit Änderungen ohne Commit) · Quellen bitstamp (USD), " \
           "binance (USDT)" in eintrag and eintrag.endswith(" · Läufe kern: 2023-01-01-bis-Ende")
    e = json.loads(aw.datei("E1", cache, "kern", "2023-01-01-bis-Ende", "normiert").read_text(encoding="utf-8"))
    assert e["pruefung"] and e["letzter_tag"] == "2023-06-19"                 # bis Datenende
    monkeypatch.setenv("GITHUB_RUN_ID", "4711")
    _profi(monkeypatch, *args)
    zweit = protokoll.read_text(encoding="utf-8")
    assert zweit.startswith(erst) and zweit.count("\n- ") == 2               # nur angehängt
    assert " UTC** · GitHub-Lauf 4711 · Commit `unbekannt`" in zweit.splitlines()[-1]


def test_chef_rechnet_aus_den_ergebnisdateien_der_stil_bots(ordner, monkeypatch):
    """Der Chef als eigener Job (GitHub-Matrix): Er liest die Kurven der drei Stil-Bots aus ihren Ergebnisdateien."""
    from tradingbot.chef import STYLES
    args = ["--schritt", "E0", "--start", "2022-01-01", "--ende", "2022-12-31", "--cache-fest", "--nur-bot", "chef"]
    with pytest.raises(SystemExit, match="Chef: Lauf von config_langfrist im Fenster 2022 fehlt"):
        _profi(monkeypatch, *args)
    stunden = ordner / "data" / "historie" / "bitstamp_BTC_1h.csv"            # die Kurse eines Stil-Bots
    stunden.write_text("x\n", encoding="utf-8")
    cache = aw.cache_id()
    tage = pd.date_range("2022-01-01", "2022-12-31", tz="UTC")
    for i, s in enumerate(STYLES):
        kurve = {f"{t:%Y-%m-%d}": round(100 * (1 + 0.001 * i) ** j, 4) for j, t in enumerate(tage)}
        _ergebnis(cache, "E0", s, "2022", _kz(1.0), kurve=kurve)
    zweiter = list(STYLES)[1]
    pfad = aw.datei("E0", cache, zweiter, "2022", "normiert")
    alt = json.loads(pfad.read_text(encoding="utf-8"))
    pfad.write_text(json.dumps(alt | {"commit": "def", "sauber": False, "kursdateien": [stunden.name]}), encoding="utf-8")
    _profi(monkeypatch, *args)
    e = json.loads(aw.datei("E0", cache, "chef", "2022", "normiert").read_text(encoding="utf-8"))
    assert e["rolle"] == "chef" and e["config"] == {"stil_bots": list(STYLES), "startkapital": 100}
    assert (e["erster_tag"], e["letzter_tag"], e["startkapital"]) == ("2022-01-01", "2022-12-31", 100)
    assert 100 < e["kurve"]["2022-12-31"] < 100 * 1.002 ** 364 and e["kennzahlen"]["Calmar"] > 0
    # woher er rechnet: Commit und Kurse jedes Stil-Laufs; einer mit Änderungen ohne Commit macht ihn ebenso unsauber
    btc = ordner / "data" / "historie" / "bitstamp_BTC_1d.csv"
    assert e["kursdateien"] == [btc.name, stunden.name] and e["kurs_fingerabdruck"] == historie.cache_fingerprint(
        [btc, stunden])
    assert e["stil_laeufe"] == {s: {"commit": "def" if s == zweiter else "abc", "sauber": s != zweiter,
                                    "erstellt": "x", "kurs_fingerabdruck": "x"} for s in STYLES}
    assert not e["sauber"] and "| abc, def, unbekannt (mit Änderungen ohne Commit) |" in aw.zusammenfassen()


def _schein(monkeypatch):
    """historie.simulate ohne Simulation: feste Tagesrendite je Config (Puffer 5 % besser, mit ETH schlechter), für
    alle dieselbe Schwankung, keine Kosten."""
    def simulate(cfg, coins, start=None, fees="normiert", end=None):
        tage = pd.date_range(start, end - pd.Timedelta(days=1), freq="D", tz="UTC")
        r = 0.0005 + 0.0003 * (cfg.horizon_list()[0].strategy_params["band"] == 0.05) - 0.0002 * (len(cfg.symbols) > 1)
        eq = pd.Series(cfg.starting_capital * np.cumprod(1 + r + 0.02 * np.sin(np.arange(len(tage)) / 5)), tage)
        daily = pd.DataFrame(0.0, index=tage, columns=historie.DAILY).assign(invested=eq, open=1, coins=1)
        return historie.BotRun(cfg, eq, pd.DataFrame(), 0, 0, daily)
    monkeypatch.setattr(historie, "simulate", simulate)


def test_e1b_behaelt_die_rolle_des_e1a_siegers(ordner, monkeypatch):
    """E1a, dann E1b mit dem Sieger von E1a als Amtsinhaber (Befehle wie im Plan): Dessen Ergebnisdateien werden neu
    geschrieben und behalten die Rolle aus E1a. Der Bericht nennt den richtigen E1-Sieger und rechnet das Tor für ihn."""
    _schein(monkeypatch)
    _welle("2021-01-01", 900, 10.0).to_csv(ordner / "data" / "historie" / "bitstamp_ETH_1d.csv")
    (ordner / "bots" / "profi" / "varianten" / "eth.yaml").write_text("symbols: [BTC/CHF, ETH/CHF]\n", encoding="utf-8")
    cache = aw.cache_id()
    for n, c in zip(aw.L_DEV, (0.5, 0.2, 0.9, 1.5, 0.4, 0.6, 0.8, 0.3)):     # L_dev 1,5: das Tor verlangt 1,275
        _ergebnis(cache, "E0", n, aw.HAUPT, _kz(c), "chef" if n == "chef" else "vergleich")
    e1 = ["--schritt", "E1", "--config", "bots/profi/kern.yaml", "--cache-fest", "--varianten"]
    _profi(monkeypatch, *e1, "bots/profi/varianten/band5.yaml")                                       # E1a
    assert "**Sieger von E1: kern+band5**" in aw.zusammenfassen()
    e1b = [*e1, "bots/profi/varianten/eth.yaml", "--sieger", "bots/profi/varianten/band5.yaml"]
    _profi(monkeypatch, *e1b)
    text = (ordner / "lernen" / "PROFI_ERGEBNISSE.md").read_text(encoding="utf-8")
    assert f"| **kern+band5 · Cache {cache[:12]}** | ✓ 1.71 gegen 0.91 |" in text                 # Regel G aus E1a
    assert f"| **kern+band5+eth · Cache {cache[:12]}** | ✗ 1.16 gegen 1.71 |" in text
    assert "**Sieger von E1: kern+band5**" in text and "überholt" not in text
    assert f"| **Cache {cache[:12]}** | ✓ 1.71 gegen 1.27 | ✓ 0.00 % | ✓ |" in text and "**Tor bestanden:**" in text
    pfad = aw.datei("E1", cache, "kern+band5", aw.HAUPT, "normiert")
    e = json.loads(pfad.read_text(encoding="utf-8"))
    rollen = [{"rolle": "herausforderer", "amtsinhaber": "kern", "nr": 1},
              {"rolle": "amtsinhaber", "amtsinhaber": "kern+band5", "nr": 0}]
    assert (e["rolle"], e["amtsinhaber"], e["nr"]) == ("amtsinhaber", "kern+band5", 0) and e["rollen"] == rollen
    _profi(monkeypatch, *e1b)                                                     # wiederholt: keine Rolle doppelt
    assert json.loads(pfad.read_text(encoding="utf-8"))["rollen"] == rollen


# --- Gepaarter Block-Bootstrap

def test_bootstrap_auf_synthetischen_kurven_mit_bekanntem_ergebnis():
    rng = np.random.default_rng(1)
    tage = pd.date_range("2012-01-01", periods=1200, freq="D", tz="UTC")
    r = rng.normal(0.0005, 0.03, len(tage))
    basis = pd.Series(100 * np.cumprod(1 + r), tage)
    besser = pd.Series(100 * np.cumprod(1 + r + 0.0005), tage)       # dieselben Tage, jeden Tag 0,05 % mehr
    assert aw.bootstrap(besser, basis) > 0.95 and aw.bootstrap(basis, besser) < 0.05
    assert aw.bootstrap(besser, basis) == aw.bootstrap(besser, basis)        # Seed 2026: immer gleich
    assert aw.bootstrap(basis, basis) == 0.0                                 # gleich gut ist nicht besser
    a = pd.Series(100 * np.cumprod(1 + rng.normal(0.001, 0.03, len(tage))), tage)
    mitte = aw.bootstrap(a, basis)
    assert 0.0 < mitte < 1.0 and aw.bootstrap(a, basis, seed=2026) == mitte
    assert aw.bootstrap(a.iloc[:600], basis) == aw.bootstrap(a.iloc[:600], basis.iloc[:600])   # nur gemeinsame Tage
    assert aw.bootstrap(a.iloc[:20], basis) is None


# --- Entscheide auf Kennzahl-Tabellen (von Hand gebaut)

def _kz(calmar, dd=-40.0, cagr=None, kosten=1.0, umschlag=1.0, anteil=10.0, notaus=0, rendite=None):
    cagr = round(calmar * abs(dd), 1) if cagr is None else cagr
    return {"Rendite %": cagr * 3 if rendite is None else rendite, "pro Jahr %": cagr, "Max. DD %": dd,
            "Calmar": calmar, "Kosten % pro Jahr": kosten, "Umschlag pro Jahr": umschlag,
            "Kostenanteil am Bruttogewinn %": anteil, "Not-Aus": notaus, "Trades": 10}


def _g(amt=(0.30, 0.25, 0.40), her=(0.35, 0.25, 0.40), kosten=3.0, umschlag=4.0):
    """Amtsinhaber und Herausforderer mit Calmar (2012-2022, 2012-2019, 2020-2022)."""
    fenster = (aw.HAUPT, *aw.HAELFTEN)
    return {"amt": {f: _kz(c) for f, c in zip(fenster, amt)},
            "her": {f: _kz(c, kosten=kosten, umschlag=umschlag) for f, c in zip(fenster, her)}}


def test_regel_g():
    assert all(aw.regel_g(_g(), "amt", "her", 0.65).values())                # genau auf allen Grenzen
    g = aw.regel_g(_g(her=(0.34, 0.25, 0.40)), "amt", "her", 0.9)
    assert not g["G1"] and g["G2"] and not g["besteht"] and g["G1"].text == "0.34 gegen 0.30"
    assert not aw.regel_g(_g(her=(0.50, 0.24, 0.60)), "amt", "her", 0.9)["G2"]          # eine Hälfte schlechter
    assert not aw.regel_g(_g(her=(0.50, 0.30, 0.39)), "amt", "her", 0.9)["G2"]
    assert not aw.regel_g(_g(), "amt", "her", 0.649)["G3"] and not aw.regel_g(_g(), "amt", "her", None)["G3"]
    assert not aw.regel_g(_g(kosten=3.01), "amt", "her", 0.9)["G4"]
    assert not aw.regel_g(_g(umschlag=4.01), "amt", "her", 0.9)["G4"]
    ohne_haelfte = _g()
    del ohne_haelfte["her"]["2020-2022"]
    assert not aw.regel_g(ohne_haelfte, "amt", "her", 0.9)["G2"]             # fehlende Zahl: nicht erfüllt


def test_sieger_ueber_zwei_caches_und_einfachere_variante():
    p = lambda cache, a, b: 0.9
    ks = {"A": _g(), "B": _g()}
    assert aw.ersetzt(ks, "amt", "her", p) and aw.sieger(ks, "amt", ["her"], p) == "her"
    ks["B"] = _g(her=(0.40, 0.20, 0.50))                                     # Cache B: eine Hälfte schlechter
    assert aw.sieger(ks, "amt", ["her"], p) == "amt"                          # Caches uneinig: Amtsinhaber bleibt
    assert aw.sieger({}, "amt", ["her"], p) == "amt"
    assert aw.sieger(ks, "amt", ["her"], lambda c, a, b: 0.6 if c == "B" else 0.9) == "amt"
    # zwei Herausforderer bestehen: der zweite (komplexere) muss auch die einfachere Variante schlagen
    zwei = lambda c2: {"amt": _g()["amt"],
                       "her": _g()["her"], "her2": {f: _kz(c) for f, c in zip((aw.HAUPT, *aw.HAELFTEN), c2)}}
    ks = {"A": zwei((0.38, 0.25, 0.40)), "B": zwei((0.38, 0.25, 0.40))}
    assert aw.sieger(ks, "amt", ["her", "her2"], p) == "her"                  # nur +0,03 gegen «her»: Gleichstand
    ks = {"A": zwei((0.41, 0.26, 0.45)), "B": zwei((0.41, 0.26, 0.45))}
    assert aw.sieger(ks, "amt", ["her", "her2"], p) == "her2"
    assert aw.sieger(ks, "amt", ["her2", "her"], p) == "her2"                 # «her» schlägt «her2» nicht


def test_tor_nach_e1_und_l_dev():
    k0 = {n: {aw.HAUPT: _kz(c)} for n, c in zip(aw.L_DEV, (0.5, 0.2, 0.9, 1.0, 0.4, 0.6, 0.8, 0.3))}
    assert aw.l_dev(k0) == (1.0, "config_phasen")
    del k0["chef"]
    assert aw.l_dev(k0) == (None, None)                                      # E0 unvollständig: kein L_dev
    assert aw.tor({"kern": {aw.HAUPT: _kz(0.85, kosten=3.0)}}, "kern", 1.0)["besteht"]
    assert not aw.tor({"kern": {aw.HAUPT: _kz(0.84)}}, "kern", 1.0)["besteht"]
    assert not aw.tor({"kern": {aw.HAUPT: _kz(0.9, kosten=3.2)}}, "kern", 1.0)["besteht"]
    assert not aw.tor({"kern": {aw.HAUPT: _kz(0.9)}}, "kern", None)["besteht"]


def test_e2_flagge():
    k = lambda n: {"amt": {aw.HAUPT: _kz(1.0, notaus=n)}}
    assert aw.e2_flagge({"A": k(3), "B": k(2)}, "amt", "amt")                # in einem Cache höchstens 2 Not-Aus
    assert not aw.e2_flagge({"A": k(3), "B": k(4)}, "amt", "amt")
    assert not aw.e2_flagge({"A": k(1)}, "amt", "amt+ohne")                   # Not-Aus nicht behalten: keine Flagge


def _e5():
    gestaffelt = [f.name for f in aw.gestaffelt()]
    k = {"kand": {aw.HAUPT: _kz(1.0), aw.DRITTE: _kz(0.9), "Crash-2014": _kz(0.7, dd=-51.0),
                  "Crash-2018": _kz(0.7, dd=-45.0), **{f: _kz(0.8, dd=-30.0) for f in gestaffelt}},
         "nah1": {aw.HAUPT: _kz(0.75)}, "nah2": {aw.HAUPT: _kz(1.2)}, "stress": {aw.HAUPT: _kz(0.5)},
         "bitcoin_halten": {aw.HAUPT: _kz(0.5), aw.DRITTE: _kz(0.4), "Crash-2014": _kz(0.5, dd=-85.0),
                            "Crash-2018": _kz(0.5, dd=-80.0), **{f: _kz(0.5, dd=-80.0) for f in gestaffelt}},
         "p_minus_1": {aw.DRITTE: _kz(1.0)}}
    dritte = {"kand": {aw.DRITTE: _kz(0.7)}, "bitcoin_halten": {aw.DRITTE: _kz(0.3)}, "p_minus_1": {aw.DRITTE: _kz(0.8)}}
    return k, dritte, gestaffelt


def test_e5_kriterien():
    k, dritte, gestaffelt = _e5()
    r = aw.e5(k, "kand", ["nah1", "nah2"], ["stress"], [dritte])
    assert all(r.values())                                                   # alle Grenzen genau erreicht
    k["nah1"][aw.HAUPT]["Calmar"] = 0.74
    assert not aw.e5(k, "kand", ["nah1", "nah2"], ["stress"], [dritte])["(a)"]
    assert not aw.e5(k, "kand", [], ["stress"], [dritte])["(a)"]               # ohne Nachbarwerte nicht bewiesen
    k, dritte, gestaffelt = _e5()
    k["stress"][aw.HAUPT]["Calmar"] = 0.49
    assert not aw.e5(k, "kand", ["nah1"], ["stress"], [dritte])["(b)"]
    k, dritte, gestaffelt = _e5()
    assert not aw.e5(k, "kand", ["nah1"], ["stress"], [])["(c)"]              # dritte Quelle fehlt
    dritte["p_minus_1"][aw.DRITTE]["Calmar"] = 0.6                            # dort ist der Kandidat besser als P−1
    assert not aw.e5(k, "kand", ["nah1"], ["stress"], [dritte])["(c)"]
    k, dritte, gestaffelt = _e5()
    for f in gestaffelt[:11]:                                                # 17 von 28 über halten: genau 60 %
        k["kand"][f]["Calmar"] = 0.5
    assert aw.e5(k, "kand", ["nah1"], ["stress"], [dritte])["(d)"]
    k["kand"][gestaffelt[11]]["Calmar"] = 0.4
    assert not aw.e5(k, "kand", ["nah1"], ["stress"], [dritte])["(d)"]
    k, dritte, gestaffelt = _e5()
    for f in gestaffelt[:7]:                                                 # 21 von 28 mit DD ≤ 0,6 × halten
        k["kand"][f]["Max. DD %"] = -49.0
    assert aw.e5(k, "kand", ["nah1"], ["stress"], [dritte])["(d)"]
    k["kand"][gestaffelt[7]]["Max. DD %"] = -48.1
    assert not aw.e5(k, "kand", ["nah1"], ["stress"], [dritte])["(d)"]
    k, dritte, gestaffelt = _e5()
    k["kand"]["Crash-2014"]["Max. DD %"] = -51.1                             # über 0,6 × 85 %
    r = aw.e5(k, "kand", ["nah1"], ["stress"], [dritte])
    assert not r["(e)"] and not r["bestanden"]


def _go():
    """Kandidat erfüllt alle Go-Regeln genau auf den Grenzen."""
    p = [f.name for f in aw.gestaffelt_pruefung()]
    k = {"kand": {p[0]: _kz(1.5, dd=-30.0, cagr=20.0, kosten=3.0, anteil=25.0),
                  "Crash-2022": _kz(1.0, dd=-42.0), **{f: _kz(1.2) for f in p[1:]}},
         "bitcoin_halten": {p[0]: _kz(1.2, dd=-50.0, cagr=60.0), "Crash-2022": _kz(0.5, dd=-70.0)},
         "p_minus_1": {p[0]: _kz(1.55, dd=-60.0), "Crash-2022": _kz(0.6, dd=-50.0)},
         "k1": {p[0]: _kz(1.4)}}
    for b in aw.HEUTIGE:
        k[b] = {p[0]: _kz(1.4 if b == "config_risiko" else 1.0), **{f: _kz(1.0) for f in p[1:]}}
    for f in p[8:]:                                                          # nur in 8 von 12 Fenstern besser
        k["kand"][f] = _kz(0.9)
    return k, p


def test_go_regeln():
    k, p = _go()
    r = aw.go(k, "kand")
    assert all(r.values()) and r["6"].text == "8 von 12" and r["1"].text == "1.50 gegen 1.50"
    k["k1"][p[0]]["Calmar"] = 1.41
    assert not aw.go(k, "kand")["1"]                                         # K1 + 0,10 über dem Kandidaten
    k, p = _go()
    del k["config_phasen"][p[0]]
    assert not aw.go(k, "kand")["1"]                                         # Vergleichs-Bot fehlt
    k, p = _go()
    k["p_minus_1"][p[0]]["Calmar"] = 1.56
    assert not aw.go(k, "kand")["2"]
    k, p = _go()
    k["bitcoin_halten"][p[0]]["Calmar"] = 1.51
    assert not aw.go(k, "kand")["2"]
    k, p = _go()
    k["kand"]["Crash-2022"]["Max. DD %"] = -42.1                             # Crash-Start 2022: über 0,6 × 70 %
    assert not aw.go(k, "kand")["3"]
    k, p = _go()
    k["kand"][p[0]]["pro Jahr %"] = 19.9                                     # unter ⅓ von 60 %
    assert not aw.go(k, "kand")["4"]
    for feld, wert in (("Kosten % pro Jahr", 3.01), ("Kostenanteil am Bruttogewinn %", 25.1),
                       ("Kostenanteil am Bruttogewinn %", None)):
        k, p = _go()
        k["kand"][p[0]][feld] = wert
        assert not aw.go(k, "kand")["5"]
    k, p = _go()
    k["kand"][p[7]] = _kz(0.9)
    assert not aw.go(k, "kand")["6"]                                         # 7 von 12
    # beide Renditen negativ: die höhere Rendite zählt, nicht der Calmar
    k["kand"][p[7]] = _kz(-0.5, rendite=-10.0)
    for b in aw.HEUTIGE:
        k[b][p[7]] = _kz(-0.2 if b == "chef" else -0.3, rendite=-15.0 if b == "chef" else -5.0)
    assert aw.go(k, "kand")["6"]
    k["kand"][p[7]]["Rendite %"] = -16.0
    assert not aw.go(k, "kand")["6"]


def test_go_regel_7_und_sonderfall_p1():
    k, p = _go()
    assert not aw.go(k, "kand", flagge=True)["7"]                            # Flagge, aber Variante fehlt
    k["ohne"] = {p[0]: dict(k["kand"][p[0]]), "Crash-2022": dict(k["kand"]["Crash-2022"])}
    assert aw.go(k, "kand", flagge=True, ohne_notaus=["ohne"])["7"]
    k["ohne"]["Crash-2022"]["Max. DD %"] = -45.0                             # ohne Not-Aus: Regel 3 verletzt
    r = aw.go(k, "kand", flagge=True, ohne_notaus=["ohne"])
    assert not r["7"] and not r["Go"] and aw.go(k, "kand")["Go"]
    s = aw.sonderfall_p1(k, "kand")
    assert not s["P−1 besser um mehr als 0,05"] and not s["P−1 erfüllt die Regeln 1 und 3-5"]
    k["p_minus_1"][p[0]] = _kz(1.56, dd=-29.0, cagr=45.2, kosten=2.0, anteil=5.0)
    k["p_minus_1"]["Crash-2022"]["Max. DD %"] = -40.0
    s = aw.sonderfall_p1(k, "kand")
    assert s["P−1 besser um mehr als 0,05"] and s["P−1 erfüllt die Regeln 1 und 3-5"]
    assert not aw.go(k, "kand")["2"]


# --- Zusammenfassen über zwei Caches (Ergebnisdateien von Hand, ohne Simulation)

A, B, C = "a" * 64, "b" * 64, "c" * 64          # zwei Haupt-Caches (Standardquellen) und eine dritte Quelle
FENSTER = {f.name: f for f in (*aw.STANDARD, *aw.CRASH, aw.CRASH_2022, *aw.gestaffelt(), *aw.gestaffelt_pruefung(),
                               aw.Fenster(aw.DRITTE, "2016-01-01", "2022-12-31"),
                               aw.eigenes_fenster("2022-01-01", "2022-12-31"))}


def _kurve(seed: int, plus: float = 0.0) -> dict:
    tage = pd.date_range("2012-01-01", periods=400, freq="D", tz="UTC")
    r = np.random.default_rng(seed).normal(0.001, 0.03, len(tage)) + plus
    return {f"{t:%Y-%m-%d}": v for t, v in zip(tage, 100 * np.cumprod(1 + r))}


def _ergebnis(cache, schritt, name, fenster, kz, rolle="vergleich", amt=None, nr=0, kurve=None, gebuehren="normiert",
              ueberlagerung=None, notaus=()):
    f = FENSTER[fenster]
    quellen = [["coinbase", "USD"]] if cache == C else [list(q) for q in historie.SOURCES]
    e = {"schritt": schritt, "gebuehren": gebuehren, "quellen": quellen, "cache": cache, "cache_fest": True,
         "commit": "abc", "sauber": True, "befehl": "test", "pruefung": schritt == "E6", "erstellt": "x", "name": name,
         "rolle": rolle, "amtsinhaber": amt, "nr": nr, "rollen": [{"rolle": rolle, "amtsinhaber": amt, "nr": nr}],
         "fenster": f._asdict(), "erster_tag": f.start,
         "letzter_tag": f.ende or "2026-11-03", "startkapital": 100, "dateien": [], "ueberlagerung": ueberlagerung,
         "config": {}, "kursdateien": ["bitstamp_BTC_1d.csv"], "kurs_fingerabdruck": "x", "kennzahlen": kz,
         "notaus": list(notaus), "kurve": kurve or {}}
    pfad = aw.datei(schritt, cache, name, fenster, gebuehren)
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text(json.dumps(e), encoding="utf-8")


def _leiter(cache, her_haelfte=0.30):
    """E0 (L_dev 1.0) und E1: «kern+band5» schlägt «kern» klar, ausser die erste Hälfte ist schlechter."""
    for n, c in zip(aw.L_DEV, (0.5, 0.2, 0.9, 1.0, 0.4, 0.6, 0.8, 0.3)):
        _ergebnis(cache, "E0", n, aw.HAUPT, _kz(c), "chef" if n == "chef" else "vergleich")
    for n, w in (("kern", (0.80, 0.30, 1.0)), ("kern+band5", (0.90, her_haelfte, 1.1))):
        rolle, nr = ("amtsinhaber", 0) if n == "kern" else ("herausforderer", 1)
        for f, c in zip((aw.HAUPT, *aw.HAELFTEN), w):
            _ergebnis(cache, "E1", n, f, _kz(c), rolle, "kern", nr,
                      kurve=_kurve(1, 0.002 if n == "kern+band5" else 0.0) if f == aw.HAUPT else None)


def test_zusammenfassen_ueber_zwei_caches(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(historie, "simulate", lambda *a, **k: pytest.fail("zusammenfassen simuliert nie"))
    _leiter(A)
    _leiter(B, her_haelfte=0.29)                         # in Cache B ist «kern+band5» 2012-2019 schlechter
    _leiter(C, her_haelfte=0.10)                         # dritte Quelle zählt nicht für Entscheide
    _ergebnis(A, "E0", "config_risiko", aw.HAUPT, _kz(5.0), gebuehren="alt")    # Kontrolle: zählt nicht für L_dev
    text = aw.zusammenfassen()
    assert (tmp_path / "lernen" / "PROFI_ERGEBNISSE.md").read_text(encoding="utf-8") == text + "\n"
    assert f"| **Cache {C[:12]}** | coinbase (USD) | bitstamp | ja | 14 | nur Information |" in text
    assert f"| **Cache {A[:12]}** | 1.00 | Phasen |" in text and "Gebühren alt" in text
    assert f"### Alte (fest 0,26 %) gegen normierte Kosten: Cache {A[:12]}, 2012-2022" in text
    assert "| **Risiko** | 200 | 36 | 5 | 0.90 | 1 | 1 |" in text and "normierte Kosten: Cache bbb" not in text
    assert "**Sieger von E1: kern**" in text and "der Amtsinhaber bleibt" in text
    assert f"| **kern+band5 · Cache {B[:12]}** | ✓ 0.90 gegen 0.80 | ✗ 0.29 gegen 0.30" in text
    assert "### Tor nach E1" in text and "**Tor nicht bestanden:**" in text    # 0,80 < 0,85 × 1,0
    _leiter(B)                                           # jetzt besteht «kern+band5» auch in Cache B
    text = aw.zusammenfassen()
    assert "**Sieger von E1: kern+band5**" in text and "**Tor bestanden:** weiter mit E2." in text
    assert f"| **kern+band5 · Cache {A[:12]}** | ✓ 0.90 gegen 0.80 | ✓ 0.30 gegen 0.30 · 1.10 gegen 1.00 | ✓ P = 1.00" \
           in text
    for cache in (A, B):                                 # zweiter Herausforderer: muss auch «kern+band5» schlagen
        for f, c in zip((aw.HAUPT, *aw.HAELFTEN), (0.96, 0.31, 1.2)):
            _ergebnis(cache, "E1", "kern+band8", f, _kz(c), "herausforderer", "kern", 2,
                      kurve=_kurve(1, 0.003) if f == aw.HAUPT else None)
    text = aw.zusammenfassen()
    assert "**Sieger von E1: kern+band8**" in text
    assert f"| **kern+band8 gegen kern+band5 · Cache {B[:12]}** | ✓ 0.96 gegen 0.90 | ✓ 0.31 gegen 0.30 · 1.20 gegen " \
           "1.10 | ✓ P = 1.00" in text


def test_zusammenfassen_e2_e5_e6(tmp_path, monkeypatch):
    """Not-Aus-Tabelle und Flagge (E2), E5-Kriterien mit dritter Quelle, Go-Regeln mit Regel 7 und Entscheid (E6)."""
    monkeypatch.chdir(tmp_path)
    ereignis = {"tag": "2018-11-15", "coin": "BTC/USD", "kurs": 5600.0, "rendite_90_tage_pct": 4.9,
                "linie_verkauft": "2019-02-15", "linie_kurs": 3700.0}
    k, dritte, gestaffelt = _e5()
    g, p = _go()
    for cache in (A, B):
        _ergebnis(cache, "E2", "kern", aw.HAUPT, _kz(1.0, notaus=1), "amtsinhaber", "kern", notaus=[ereignis],
                  kurve=_kurve(1))
        _ergebnis(cache, "E2", "kern+ohne", aw.HAUPT, _kz(1.02), "herausforderer", "kern", 1, kurve=_kurve(1, 0.0001))
        for n, fs in k.items():
            rolle = {"kand": "amtsinhaber", "nah1": "herausforderer", "nah2": "herausforderer",
                     "stress": "herausforderer"}.get(n, "benchmark" if n == "bitcoin_halten" else "vergleich")
            nr = {"nah1": 1, "nah2": 2, "stress": 3}.get(n, 0)
            ueber = {"fee_factor": 1.5} if n == "stress" else {"risk": {"stop_loss_atr": 6}} if nr else None
            for f, kz in fs.items():
                _ergebnis(cache, "E5", n, f, kz, rolle, "kand" if rolle != "vergleich" and n != "bitcoin_halten"
                          else None, nr, ueberlagerung=ueber)
        g["ohne"] = {p[0]: dict(g["kand"][p[0]]), "Crash-2022": dict(g["kand"]["Crash-2022"])}
        for n, fs in g.items():
            rolle = {"kand": "amtsinhaber", "ohne": "herausforderer", "chef": "chef",
                     "bitcoin_halten": "benchmark"}.get(n, "vergleich")
            for f, kz in fs.items():
                _ergebnis(cache, "E6", n, f, kz, rolle, "kand" if n in ("kand", "ohne") else None,
                          1 if n == "ohne" else 0)
    for n, fs in dritte.items():
        for f, kz in fs.items():
            _ergebnis(C, "E5", n, f, kz, "amtsinhaber" if n == "kand" else "vergleich", "kand" if n == "kand" else None)
    for n, c in (("kand", 1.1), ("bitcoin_halten", 1.2), ("p_minus_1", 1.0)):     # dritte Quelle: unter halten
        _ergebnis(C, "E6", n, aw.PRUEFUNG, _kz(c), "amtsinhaber" if n == "kand" else "vergleich",
                  "kand" if n == "kand" else None)
    text = aw.zusammenfassen()
    assert f"| **Cache {A[:12]} · 2018-11-15 BTC/USD** | 5'600 | 4.90 | 2019-02-15 | 3'700 |" in text
    assert "**E2-Flagge: gesetzt** (Not-Aus 2012-2022: 1, 1)." in text
    assert "### E5-Kriterien für kand" in text and "**E5 bestanden**" in text
    assert "| **(b) Kostenstress ≥ Bitcoin halten** | ✓ 0.50 gegen 0.50 | ✓ 0.50 gegen 0.50 |" in text
    assert "✓ gegen halten/P−1 hier +/−, dritte Quelle +/− |" in text
    assert "### Go-Regeln für kand" in text and "**Entscheid: Go**" in text
    assert "| **7. bei E2-Flagge: ohne Not-Aus erfüllt 1-4** | ✓ ohne ✓ | ✓ ohne ✓ |" in text
    assert f"Regel 2 mit anderem Vorzeichen als Cache {A[:12]}, Cache {B[:12]}" in text
    _ergebnis(B, "E6", "p_minus_1", aw.PRUEFUNG, _kz(1.56, dd=-29.0, cagr=45.2, kosten=2.0, anteil=5.0))
    _ergebnis(B, "E6", "p_minus_1", "Crash-2022", _kz(0.6, dd=-40.0))
    assert "**Entscheid: No-Go für den Kandidaten, Vorschlag P−1**" not in aw.zusammenfassen()   # nur in Cache B
    for cache in (A, B):
        _ergebnis(cache, "E6", "p_minus_1", aw.PRUEFUNG, _kz(1.56, dd=-29.0, cagr=45.2, kosten=2.0, anteil=5.0))
        _ergebnis(cache, "E6", "p_minus_1", "Crash-2022", _kz(0.6, dd=-40.0))
    assert "**Entscheid: No-Go für den Kandidaten, Vorschlag P−1**" in aw.zusammenfassen()


def test_jede_stufe_geht_vom_sieger_der_vorigen_aus(tmp_path, monkeypatch):
    """E2 nach einem geänderten E1-Ergebnis neu gerechnet: Die alte Gruppe (Amtsinhaber kern) bleibt liegen, zählt aber
    weder für den Sieger von E2 noch für die E2-Flagge; Wurzel ist der Sieger von E1."""
    monkeypatch.chdir(tmp_path)
    _leiter(A)                                                               # Sieger von E1: kern+band5
    for amt, hers in (("kern", ["kern+ohne"]), ("kern+band5", ["kern+band5+ohne", "kern+band5+trail6"])):
        for f in (aw.HAUPT, *aw.HAELFTEN):
            _ergebnis(A, "E2", amt, f, _kz(0.9, notaus=1), "amtsinhaber", amt, kurve=_kurve(1) if f == aw.HAUPT else None)
            for nr, her in enumerate(hers, 1):                               # nur trail6 schlägt den Amtsinhaber
                plus = 0.002 if her.endswith("trail6") else -0.001
                _ergebnis(A, "E2", her, f, _kz(1.0 if plus > 0 else 0.8), "herausforderer", amt, nr,
                          kurve=_kurve(1, plus) if f == aw.HAUPT else None)
    text = aw.zusammenfassen()
    assert "**Sieger von E2: kern+band5+trail6**" in text and "**E2-Flagge: nicht gesetzt**" in text
    assert "### Regel G gegen den Amtsinhaber kern (überholt)" in text
    assert "Zählt nicht: kern ist nicht der Sieger von E1 (kern+band5)." in text
    assert "### Regel G gegen den Amtsinhaber kern+band5\n" in text
    for p in (tmp_path / "lernen" / "profi" / "E2").rglob("kern+band5*.json"):  # E2 noch nicht mit dem E1-Sieger
        p.unlink()
    text = aw.zusammenfassen()
    assert "**Sieger von E2: –** (E2 ist noch nicht mit dem Sieger von E1 gerechnet: kern+band5 als Amtsinhaber)" in text
    assert "**E2-Flagge: nicht gesetzt** (E2 nicht mit dem Sieger von E1 gerechnet)." in text


def test_vorlaeufig_solange_einem_haupt_cache_laeufe_fehlen(tmp_path, monkeypatch):
    """Cache B (z.B. der PC) hat E1 noch nicht oder nur zum Teil: Sieger und Tor sind vorläufig, bis E1 in jedem
    Haupt-Cache gerechnet ist."""
    monkeypatch.chdir(tmp_path)
    _leiter(A)
    _leiter(B)
    shutil.rmtree(tmp_path / "lernen" / "profi" / "E1" / B[:12])               # B: nur E0
    text = aw.zusammenfassen()
    assert f"**Vorläufig:** Cache {B[:12]} hat noch keine Läufe von E1, entschieden ist ohne diesen Cache. Der nächste " \
           "Schritt startet erst, wenn E1 in jedem Haupt-Cache gerechnet ist" in text
    assert "**Sieger von E1: kern+band5** (vorläufig)" in text and "**Tor bestanden (vorläufig):**" in text
    assert "Nur ein Haupt-Cache" not in text and text.count("**Vorläufig:**") == 1    # E0 ist in beiden vollständig
    _leiter(B)
    aw.datei("E1", B, "kern+band5", "2020-2022", "normiert").unlink()           # B: ein Job fehlt
    text = aw.zusammenfassen()
    assert f"**Vorläufig:** In Cache {B[:12]} fehlen 1 von 6 Läufen von E1 (fehlende Zahlen gelten als nicht " \
           "erfüllt)." in text and "**Sieger von E1: kern** (vorläufig)" in text
    _leiter(B)
    text = aw.zusammenfassen()
    assert "orläufig" not in text and "**Sieger von E1: kern+band5**\n" in text


def test_e5_des_e1_siegers_verfehlt_ist_ein_no_go(tmp_path, monkeypatch):
    """Verfehlt der E1-Sieger E5, gibt es kein E6 für den Kern: No-Go statt «zurück zum E1-Sieger», auch in E6."""
    monkeypatch.chdir(tmp_path)
    k, _, _ = _e5()
    g, p = _go()
    for cache in (A, B):
        _leiter(cache)                                                       # Sieger von E1: kern+band5
        for n, fs in k.items():                                              # Kandidat kern, (c) ohne dritte Quelle
            rolle = {"kand": "amtsinhaber", "nah1": "herausforderer"}.get(n, "vergleich")
            for f, kz in fs.items():
                _ergebnis(cache, "E5", n.replace("kand", "kern"), f, kz, rolle, "kern" if rolle != "vergleich" else None,
                          int(n == "nah1"), ueberlagerung={"risk": {"stop_loss_atr": 6}} if n == "nah1" else None)
        for n, fs in g.items():
            for f, kz in fs.items():
                _ergebnis(cache, "E6", n.replace("kand", "kern"), f, kz, "amtsinhaber" if n == "kand" else "vergleich",
                          "kern" if n == "kand" else None)
    text = aw.zusammenfassen()
    assert "**E5 nicht bestanden**: zurück zum E1-Sieger und nur diesen prüfen, keine neuen Varianten." in text
    assert "**Entscheid: No-Go (E5 nicht bestanden: kein E6 für den Kern)**" in text     # die Go-Regeln allein: Go
    for cache in (A, B):
        _leiter(cache, her_haelfte=0.29)                                     # jetzt bleibt kern Sieger von E1
    text = aw.zusammenfassen()
    assert "**E5 nicht bestanden**: Der Kandidat ist der E1-Sieger, darum kein E6 für den Kern, sondern ein No-Go mit " \
           "Begründung." in text and "**Entscheid: No-Go (E5 nicht bestanden: kein E6 für den Kern)**" in text
