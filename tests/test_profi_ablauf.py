"""Abläufe der Profi-Bot-Prüfung (lernen/PROFI_PLAN.md): Configs in bots/profi/, GitHub-Ablauf profi.yml, Pfadfilter
in historie.yml, profi --laden, das PC-Skript und der Bericht mit der eingefrorenen Fassung."""
import json
import os
import shutil
import subprocess
import sys
import types
from pathlib import Path

import pandas as pd
import pytest
import yaml

from test_auswertung import A, _ergebnis, _kz, _profi
from test_profi_werkzeug import _welle
from tradingbot import auswertung as aw
from tradingbot import historie

ROOT = Path(__file__).resolve().parent.parent
PROFI = ROOT / "bots" / "profi"
ABLAEUFE = ROOT / ".github" / "workflows"


def _ablauf(name: str) -> dict:
    wf = yaml.safe_load((ABLAEUFE / name).read_text(encoding="utf-8"))
    wf["on"] = wf.pop(True, wf.get("on"))           # YAML 1.1 liest «on» als True
    return wf


def test_profi_configs_nur_demo_mit_kraken_kosten_und_vorab_registriert(monkeypatch):
    """Jede Basis allein und jede Überlagerung auf den Kern, auch auf eine lange Kette früherer Sieger, so
    zusammengeführt wie in der Auswertung: dieselbe Prüfung wie Config.load, nur Demo, Kraken-Kosten, ohne Hebel und
    Short, Startkapital 100. Jede Datei steht im Plan."""
    monkeypatch.chdir(ROOT)
    basen = sorted(p.relative_to(ROOT).as_posix() for p in PROFI.glob("*.yaml"))
    varianten = sorted(p.relative_to(ROOT).as_posix() for p in (PROFI / "varianten").glob("*.yaml"))
    assert basen == ["bots/profi/e1_kb3.yaml", "bots/profi/k1.yaml", "bots/profi/p_minus_1.yaml"]
    assert {"e1_kb5", "e1_kbe", "e2_ohne_notaus", "e2_trail6", "e5_kostenstress"} <= {Path(v).stem for v in varianten}
    kette = [aw.E1_AMT, *(f"bots/profi/varianten/{n}.yaml" for n in ("e1_kb5", "e1_kbe", "e2_trail6"))]
    bots = [aw.bot(n) for n in (aw.K1, aw.P1)]
    for amt in ([aw.E1_AMT], kette):
        a, vs = aw.namen(amt, varianten)
        bots += [aw.bot(n, amt, varianten) for n in (a, *vs)]
    plan = (ROOT / "lernen" / "PROFI_PLAN.md").read_text(encoding="utf-8")
    for b in bots:
        c = b.cfg
        assert (c.mode, c.exchange, c.fee_model, c.starting_capital, c.risk.leverage) == ("paper", "kraken", "kraken",
                                                                                         100, 1.0), b.name
        assert not c.allow_short and not any(h.allow_short for h in c.horizon_list()), b.name
        assert not c.use_news and not c.use_events and c.fee_factor >= 1.0, b.name
        assert all(f"`{Path(d).name}`" in plan or d in plan for d in b.dateien), b.name
    stress = aw.bot(aw.namen(kette, varianten)[1][varianten.index("bots/profi/varianten/e5_kostenstress.yaml")],
                    kette, varianten)
    assert aw.ist_kostenstress(stress.ueberlagerung) and (stress.cfg.fee_factor, stress.cfg.slippage) == (1.5, 0.001)
    assert sum(aw.ist_kostenstress(b.ueberlagerung) for b in bots) == 2      # nur e5_kostenstress, je Kette einmal
    assert "**Eingefrorene Fassung:** Commit" in plan


def test_profi_yml_nur_von_hand_mit_eingefrorenem_cache_und_nie_auf_main(tmp_path):
    wf = _ablauf("profi.yml")
    assert list(wf["on"]) == ["workflow_dispatch"]
    schritte = {j: v["steps"] for j, v in wf["jobs"].items()}
    caches = [(j, s) for j, ss in schritte.items() for s in ss if s.get("uses", "").startswith("actions/cache")]
    assert {j for j, _ in caches} == {"vorbereiten", "rechnen", "chef"}
    assert all(s["with"]["key"] == "profi-2026-11-03" and "restore-keys" not in s["with"] for _, s in caches)
    assert "restore-keys" not in (ABLAEUFE / "profi.yml").read_text(encoding="utf-8")
    # nur der erste Job füllt den Cache (einmal), die Rechen-Jobs lesen ihn nur
    assert [s["uses"] for j, s in caches if j != "vorbereiten"] == ["actions/cache/restore@v4"] * 2
    assert all(s["with"]["fail-on-cache-miss"] for j, s in caches if j != "vorbereiten")
    assert wf["jobs"]["vorbereiten"]["concurrency"]["cancel-in-progress"] is False
    # zuerst die Tests, dann rechnen
    runs = [s.get("run", "") for s in schritte["vorbereiten"]]
    assert runs.index("python -m pytest -q") < min(i for i, r in enumerate(runs) if "tradingbot profi" in r)
    # Abbruch auf main: der erste Schritt bricht ab, der Sammel-Job läuft dort nie
    nie_main = schritte["vorbereiten"][0]["run"]
    for typ, name, code in (("branch", "main", 1), ("tag", "v1", 1), ("branch", "claude/project-thread-usz8e3", 0)):
        r = subprocess.run(["bash", "-c", nie_main], env={"PATH": os.environ["PATH"], "GITHUB_REF_TYPE": typ,
                                                          "GITHUB_REF_NAME": name}, capture_output=True, text=True)
        assert r.returncode == code, (typ, name)
    assert "github.ref != 'refs/heads/main'" in wf["jobs"]["sammeln"]["if"]
    # gespeichert werden nur die Profi-Ergebnisse, nie Bot-Stände
    speichern = " ".join(s.get("run", "") for s in schritte["sammeln"])
    assert "git add lernen/profi lernen/PROFI_ERGEBNISSE.md lernen/PROFI_PRUEFPROTOKOLL.md\n" in speichern
    assert "daten/" not in (ABLAEUFE / "profi.yml").read_text(encoding="utf-8")
    # der Eintrag im Prüfprotokoll kommt auch nach einem Fehler mit
    for j in ("rechnen", "chef"):
        assert [s.get("if") for s in schritte[j][-2:]] == ["always()", "always()"]
    assert wf["jobs"]["sammeln"]["if"].startswith("${{ always()")


def test_historie_rechnet_nie_profi_configs():
    paths = _ablauf("historie.yml")["on"]["push"]["paths"]
    assert paths[paths.index("bots/**") + 1] == "!bots/profi/**"
    assert "bots/profi" not in " ".join(s.get("run", "") for s in _ablauf("historie.yml")["jobs"]["historie"]["steps"])


def test_pc_skript_hat_windows_zeilenenden_und_die_standardquellen():
    roh = (ROOT / "scripts" / "profi_pc.bat").read_bytes()
    assert roh.endswith(b"\r\n") and roh.count(b"\n") == roh.count(b"\r\n")
    text = roh.decode("ascii")                       # nur ASCII wie die anderen PC-Skripte
    # Standardquellen wie auf GitHub (BTC von Bitstamp, Altcoins von Binance): so zählt der PC als Haupt-Cache
    assert "--quellen" not in text and "py -m tradingbot profi --schritt %SCHRITT% %REST% --cache-fest" in text
    assert "lernen/PROFI_PRUEFPROTOKOLL.md merge=union" in (ROOT / ".gitattributes").read_text(encoding="utf-8")
    # nach einem Abbruch kommen der Eintrag im Prüfprotokoll und die Teilergebnisse trotzdem hoch, wie auf GitHub
    assert "py -m tradingbot profi --schritt %SCHRITT% %REST% --cache-fest || goto abgebrochen\r\n" in text
    abbruch = text.split("\r\n:abgebrochen\r\n")[1].split("\r\n\r\n")[0]
    assert "set DANACH=fehler\r\n" in abbruch and abbruch.endswith("goto hochladen")
    assert "git add lernen/profi lernen/PROFI_ERGEBNISSE.md lernen/PROFI_PRUEFPROTOKOLL.md" in text.split(":hochladen")[1]


class _Boerse:
    """ccxt-Börse ohne Netz: Tageskerzen ab `ab` bis 28.2.2020 für jeden Coin, den sie führt. fehler: (Symbol,
    Zeitraster), bei denen die erste Anfrage scheitert (wie eine Zeitüberschreitung)."""
    def __init__(self, coins: set, quote: str, ab: str = "2020-01-01", fehler=()):
        self.coins, self.quote, self.ab, self.fehler = coins, quote, ab, set(fehler)

    def load_markets(self):
        return {f"{c}/{self.quote}": {} for c in self.coins}

    def parse8601(self, text):
        return pd.Timestamp(text).value // 10**6

    def milliseconds(self):
        return pd.Timestamp("2020-03-01", tz="UTC").value // 10**6

    def iso8601(self, ms):
        return pd.Timestamp(ms, unit="ms", tz="UTC").isoformat()

    def fetch_ohlcv(self, symbol, timeframe, since=None, limit=1000):
        if (symbol, timeframe) in self.fehler:
            self.fehler.discard((symbol, timeframe))
            raise TimeoutError(f"{symbol} {timeframe}: Zeitüberschreitung")
        tage = pd.date_range(self.ab, "2020-02-28", freq="D", tz="UTC")
        return [[t.value // 10**6, 7.0, 7.5, 6.5, 7.0, 1.0] for t in tage if t.value // 10**6 >= since][:limit]


def test_laden_holt_die_kurse_aller_jobs_und_rechnet_nichts(monkeypatch, tmp_path, capsys):
    monkeypatch.chdir(ROOT)                          # die echten Configs in bots/, die Kurse in tmp_path
    monkeypatch.setattr(historie, "CACHE", tmp_path / "historie")
    for name, mod in (("simulate", historie), ("simulate_chef", historie), ("hold_run", historie),
                      ("rechnen", aw), ("zusammenfassen", aw)):
        monkeypatch.setattr(mod, name, lambda *a, **k: pytest.fail("--laden rechnet nichts"))
    alle = {s.split("/")[0] for s in aw.bot("config_langfrist").cfg.symbols}
    boersen = {"bitstamp": {"BTC", "ETH"}, "binance": alle - {"HYPE"}, "binanceus": set(), "kucoin": alle,
               "coinbase": {"BTC", "ETH"}}
    monkeypatch.setitem(sys.modules, "ccxt", types.SimpleNamespace(**{n: (lambda cfg, n=n: _Boerse(
        boersen[n], historie.QUOTES[n], "2011-08-18" if n == "bitstamp" else "2020-01-01")) for n in boersen}))

    def datei(coin, tf, quellen=historie.SOURCES):    # die Börse mit der längsten Geschichte, bei Gleichstand die erste
        return tmp_path / "historie" / f"{next(n for n, _ in quellen if coin in boersen[n])}_{coin}_{tf}.csv"
    erwartet = {datei("BTC", "1d")}
    for n in aw.plan("E0"):
        if (cfg := aw.bot(n).cfg) is not None:
            tf = min((h.timeframe for h in cfg.horizon_list()), key=historie.TF_MS.get)
            erwartet |= {datei(s.split("/")[0], tf) for s in cfg.symbols}
    assert {p.name.split("_")[2] for p in erwartet} >= {"1h.csv", "1d.csv"} and datei("HYPE", "1d") in erwartet

    def laden(*args):
        _profi(monkeypatch, *args, "--laden")
        zeilen = capsys.readouterr().out.splitlines()
        return zeilen[:-1], zeilen[-1]
    dateien, finger = laden("--schritt", "E0")
    assert dateien == sorted(map(str, erwartet)) and set((tmp_path / "historie").iterdir()) == erwartet
    assert finger == f"Fingerabdruck des Kurs-Caches (bitstamp, binance, binanceus, kucoin): {aw.cache_id()}"
    # E1 mit ETH: dazu die ETH-Tageskerzen; die dritte Quelle bekommt eigene Dateien und ändert den Haupt-Cache nicht
    dateien, _ = laden("--schritt", "E1", "--varianten", "bots/profi/varianten/e1_kbe.yaml")
    assert dateien == sorted(map(str, {datei("BTC", "1d"), datei("ETH", "1d")}))
    haupt = aw.cache_id()
    dateien, finger = laden("--schritt", "E1", "--varianten", "bots/profi/varianten/e1_kbe.yaml", "--quellen", "coinbase")
    dritte = historie.sources(["coinbase"])
    assert dateien == sorted(map(str, {datei("BTC", "1d", dritte), datei("ETH", "1d", dritte)}))
    assert aw.cache_id() == haupt and finger.endswith(f"(coinbase): {aw.cache_id(dritte)}")
    # eingefroren: ohne Netz nur prüfen, ob alle Dateien da sind
    monkeypatch.setitem(sys.modules, "ccxt", None)
    vorher = {p: p.stat().st_mtime_ns for p in (tmp_path / "historie").iterdir()}
    assert laden("--schritt", "E0", "--cache-fest")[0] == sorted(map(str, erwartet))
    assert {p: p.stat().st_mtime_ns for p in (tmp_path / "historie").iterdir()} == vorher
    datei("SOL", "1d").unlink()
    with pytest.raises(SystemExit, match="Eingefrorener Cache"):
        laden("--schritt", "E0", "--cache-fest")


@pytest.mark.parametrize("bitstamp", [{"ab": "2011-08-18", "fehler": [("BTC/USD", "1h")]}, {"ab": "2014-01-01"}])
def test_laden_friert_bitcoin_nur_von_bitstamp_ab_2011_ein(monkeypatch, tmp_path, bitstamp):
    """Scheitert bei Bitstamp eine einzige Anfrage, nimmt load_coin still die nächste Börse (hier Binance ab 2020).
    --laden bricht dann ab, statt eine kürzere BTC-Geschichte einzufrieren; ebenso, wenn sie erst nach 2011 beginnt."""
    monkeypatch.chdir(ROOT)
    monkeypatch.setattr(historie, "CACHE", tmp_path / "historie")
    boersen = {"bitstamp": _Boerse({"BTC"}, "USD", **bitstamp), "binance": _Boerse({"BTC"}, "USDT"),
               "binanceus": _Boerse(set(), "USD"), "kucoin": _Boerse({"BTC"}, "USDT")}
    monkeypatch.setitem(sys.modules, "ccxt", types.SimpleNamespace(**{n: (lambda cfg, b=b: b) for n, b in boersen.items()}))
    geladen = "binance_BTC_1h.csv ab 2020-01-01" if "fehler" in bitstamp else "bitstamp_BTC_1h.csv ab 2014-01-01"
    with pytest.raises(SystemExit, match=f"BTC 1h: erwartet bitstamp_BTC_1h.csv ab 2011, geladen: {geladen}"):
        aw.laden("E0", nur_bot=["config_langfrist"])
    if "fehler" in bitstamp:                                                 # BTC 1d kam ohne Fehler von Bitstamp
        assert aw.laden("E0", nur_bot=["p_minus_1"]) == [tmp_path / "historie" / "bitstamp_BTC_1d.csv"]


@pytest.mark.skipif(shutil.which("jq") is None, reason="jq fehlt (auf GitHub vorhanden)")
def test_cache_pruefen_nur_fuer_die_gewaehlten_jobs(tmp_path):
    """E6 auf der dritten Quelle mit Auswahl (nur_bot, nur_fenster): Von coinbase liegen nur BTC und ETH im Cache.
    «Cache prüfen» bekommt die Auswahl aus dem Plan-Schritt und prüft nur die Kurse dieser Jobs."""
    schritte = {s.get("id"): s for s in _ablauf("profi.yml")["jobs"]["vorbereiten"]["steps"]}
    (tmp_path / "bots").symlink_to(ROOT / "bots")
    (tmp_path / "bin").mkdir()
    (tmp_path / "bin" / "python").symlink_to(sys.executable)
    (tmp_path / "data" / "historie").mkdir(parents=True)
    for coin in ("BTC", "ETH"):
        _welle("2015-07-20", 30).to_csv(tmp_path / "data" / "historie" / f"coinbase_{coin}_1d.csv")
    ausgabe = tmp_path / "ausgabe.txt"
    env = {"PATH": f"{tmp_path / 'bin'}:{os.environ['PATH']}", "HOME": str(tmp_path), "PYTHONPATH": str(ROOT),
           "GITHUB_OUTPUT": str(ausgabe), "SCHRITT": "E6", "CONFIG": "bots/profi/e1_kb3.yaml", "SIEGER": "",
           "VARIANTEN": "", "QUELLEN": "coinbase", "GEBUEHREN": "normiert", "PRUEFUNG": "true",
           "NUR_BOT": "e1_kb3 p_minus_1 bitcoin_halten", "NUR_FENSTER": "ab-2023Q1"}

    def lauf(schritt: str, **mehr) -> subprocess.CompletedProcess:
        return subprocess.run(["bash", "-e", "-c", schritte[schritt]["run"]], cwd=tmp_path, env=env | mehr,
                              capture_output=True, text=True)
    assert lauf("plan").returncode == 0
    outputs = dict(z.split("=", 1) for z in ausgabe.read_text(encoding="utf-8").splitlines())
    werte = {k: outputs[v.split("steps.plan.outputs.")[1].strip(" }")] for k, v in schritte["pruefen"]["env"].items()}
    r = lauf("pruefen", **werte)
    assert r.returncode == 0, r.stderr
    assert r.stdout.splitlines()[0] == "data/historie/coinbase_BTC_1d.csv" and "fingerabdruck=" in \
        ausgabe.read_text(encoding="utf-8")
    r = lauf("pruefen", **(werte | {"AUSWAHL": ""}))                       # ohne Auswahl: alle Bots von E6
    assert r.returncode != 0 and "Eingefrorener Cache (--cache-fest): keine Datei für" in r.stderr


def test_pruefprotokoll_behaelt_beim_zusammenfuehren_beide_eintraege(tmp_path, monkeypatch):
    """Zwei Läufe hängen an dieselbe Fassung an, mit gleichem Befehl und Commit (ein wiederholter Job): Beim
    «pull --rebase -X theirs» wie im Sammel-Job (merge=union aus .gitattributes) bleiben beide Einträge vollständig."""
    monkeypatch.chdir(tmp_path)

    def git(*args, ort=tmp_path):
        subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "-c", "commit.gpgsign=false", *args],
                       cwd=ort, check=True, capture_output=True)
    fern, a, b = tmp_path / "fern.git", tmp_path / "a", tmp_path / "b"
    git("init", "-q", "--bare", "-b", "main", str(fern))
    git("clone", "-q", str(fern), str(a))
    (a / "lernen").mkdir()
    for datei in (".gitattributes", "lernen/PROFI_PRUEFPROTOKOLL.md"):
        (a / datei).write_bytes((ROOT / datei).read_bytes())
    git("add", ".", ort=a)
    git("commit", "-q", "-m", "Kopf", ort=a)
    git("push", "-q", "origin", "HEAD:main", ort=a)
    git("clone", "-q", str(fern), str(b))
    jobs = {"e1_kb3": aw.gestaffelt_pruefung()[5:6]}
    for klon, lauf in ((a, "4711"), (b, "4712")):
        monkeypatch.setenv("GITHUB_RUN_ID", lauf)
        aw.protokoll("python -m tradingbot profi --schritt E6 --pruefung", historie.SOURCES, "f" * 64, True, jobs,
                     klon / "lernen" / "PROFI_PRUEFPROTOKOLL.md")
        git("commit", "-q", "-am", f"Lauf {lauf}", ort=klon)
    git("push", "-q", "origin", "HEAD:main", ort=a)
    git("pull", "-q", "--rebase", "-X", "theirs", "origin", "main", ort=b)
    text = (b / "lernen" / "PROFI_PRUEFPROTOKOLL.md").read_text(encoding="utf-8")
    eintraege = [z for z in text.splitlines() if z.startswith("- ")]
    assert text.startswith((ROOT / "lernen" / "PROFI_PRUEFPROTOKOLL.md").read_text(encoding="utf-8"))
    assert [z.split(" · ")[1] for z in eintraege] == ["GitHub-Lauf 4711", "GitHub-Lauf 4712"]
    assert all(z.endswith(f"`{'f' * 64}` (eingefroren, --cache-fest) · Befehl `python -m tradingbot profi --schritt E6 "
                          "--pruefung` · Läufe e1_kb3: ab-2024Q2") for z in eintraege)


def test_bericht_nennt_die_eingefrorene_fassung_und_die_commits(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    _ergebnis(A, "E0", "k1", aw.HAUPT, _kz(1.0))
    text = aw.zusammenfassen()
    assert "eingefrorene Fassung noch nicht eingetragen." in text and "| Entscheide | abc |" in text
    pfad = aw.datei("E0", A, "k1", aw.HAUPT, "normiert")
    pfad.write_text(json.dumps(json.loads(pfad.read_text(encoding="utf-8")) | {"sauber": False}), encoding="utf-8")
    plan = tmp_path / "lernen" / "PROFI_PLAN.md"
    plan.write_text("- **Eingefrorene Fassung:** Commit _(noch leer: wird vor dem ersten E0-Lauf eingetragen)_\n",
                    encoding="utf-8")
    assert aw.fassung() is None
    plan.write_text("- **Eingefrorene Fassung:** Commit `0123456789abcdef0123456789abcdef01234567`\n", encoding="utf-8")
    assert aw.fassung() == "0123456789abcdef0123456789abcdef01234567"
    text = aw.zusammenfassen()
    assert "eingefrorene Fassung Commit `0123456789abcdef0123456789abcdef01234567`." in text
    assert "| Entscheide | abc (mit Änderungen ohne Commit) |" in text
