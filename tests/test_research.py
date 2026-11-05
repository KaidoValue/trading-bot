import json
from copy import deepcopy
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import pytest

from tradingbot import data, news_analysis
from tradingbot.config import Config, Horizon
from tradingbot.news import Headline
from tradingbot.research import Research, features, fit, predict, review, supported

NOW = pd.Timestamp("2026-11-04T12:02Z")


def frame():
    idx = pd.date_range(end="2026-11-04T11:00Z", periods=60, freq="h")
    return pd.DataFrame({"open": 100., "high": 101., "low": 99., "close": 100., "volume": 10.}, index=idx)


def study(tmp_path, monkeypatch, **kwargs):
    monkeypatch.chdir(tmp_path)
    cfg = Config(starting_capital=100, fee_rate=.01, slippage=.001, name="test", **kwargs)
    return Research(cfg, Horizon("kurz", "1h", "adaptive", stop_loss_atr=2, take_profit_atr=4))


def test_decision_is_frozen_and_never_learns_current_candle(tmp_path, monkeypatch):
    r = study(tmp_path, monkeypatch)
    df = frame()
    r.observe("BTC/CHF", df, 1, {"score": .8}, None, .002, .01, NOW)
    row = deepcopy(r.raw["rows"][0])
    assert row["entry_after"] == "2026-11-04T13:00:00+00:00"
    r.advance({"BTC/CHF": df}, NOW)
    assert r.raw["rows"][0] == row
    r.observe("BTC/CHF", df, -1, {"score": 0}, None, .002, .01, NOW)
    assert len(r.raw["rows"]) == 1 and r.raw["rows"][0] == row
    r.save()
    restored = Research(r.cfg, r.h)
    assert restored.raw == r.raw


def test_flat_future_loses_fees_and_slippage_after_timeout(tmp_path, monkeypatch):
    r = study(tmp_path, monkeypatch)
    df = frame()
    r.observe("BTC/CHF", df, 0, {"score": 0}, None, .002, .01, NOW)
    future = pd.DataFrame({"open": 100., "high": 101., "low": 99., "close": 100., "volume": 10.},
                          index=pd.date_range("2026-11-04T13:00Z", periods=12, freq="h"))
    r.advance({"BTC/CHF": future}, NOW+pd.Timedelta(hours=13))
    outcome = r.raw["rows"][0]["outcome"]
    assert outcome["net_return"] < -.02 and outcome["fees"] > 0
    assert outcome["reason"] == "Research-Zeitlimit"


def test_stop_precedes_target_and_gap_invalidates_case(tmp_path, monkeypatch):
    r = study(tmp_path, monkeypatch)
    r.observe("BTC/CHF", frame(), 1, {}, None, 0, 0, NOW)
    future = pd.DataFrame({"open": [100.], "high": [115.], "low": [85.], "close": [110.], "volume": [10.]},
                          index=pd.DatetimeIndex(["2026-11-04T13:00Z"]))
    r.advance({"BTC/CHF": future}, NOW+pd.Timedelta(hours=2))
    assert r.raw["rows"][0]["outcome"]["net_return"] < 0
    other = study(tmp_path, monkeypatch)
    other.observe("ETH/CHF", frame(), 1, {}, None, 0, 0, NOW)
    other.advance({"ETH/CHF": future.set_axis(future.index+pd.Timedelta(hours=1))}, NOW+pd.Timedelta(hours=3))
    assert other.raw["rows"][0].get("invalid") and not other.raw["rows"][0].get("outcome")


def training_rows(n=240):
    rows = []
    for i in range(n):
        good = i % 2 == 0
        observed = NOW-pd.Timedelta(days=60)+pd.Timedelta(hours=i)
        rows.append({"x": [float(good), *([0.]*10)], "block": i//8, "observed": observed.isoformat(),
                     "outcome": {"net_return": .03 if good else -.02,
                                 "known_at": (observed+pd.Timedelta(hours=12)).isoformat()}})
    return rows


def test_model_trains_only_on_mature_labels_and_has_uncertainty():
    rows = training_rows()
    model = fit(rows, NOW)
    assert model and model["trained"] == 240
    assert predict(model, [1., *([0.]*10)]) > predict(model, [0., *([0.]*10)])
    poison = deepcopy(rows[0])
    poison["outcome"]["known_at"] = (NOW+pd.Timedelta(days=1)).isoformat()
    assert fit(rows+[poison], NOW) == model
    assert not supported(model, [1000., *([0.]*10)])
    assert fit(rows[:199], NOW) is None


def test_review_rejects_same_data_wrong_version_and_accepts_forward_improvement():
    model = fit(training_rows(), NOW)
    rows = []
    for i in range(240):
        good = i % 2 == 0
        rows.append({"model_id": model["id"], "block": i//10,
                     "observed": (NOW+pd.Timedelta(days=1+i//8)).isoformat(),
                     "probability": .9 if good else .1, "candidate_buy": good, "baseline_buy": True,
                     "outcome": {"net_return": .03 if good else -.02,
                                 "known_at": (NOW+pd.Timedelta(days=32)).isoformat()}})
    report = review(model, rows, NOW+pd.Timedelta(days=40))
    assert report["accepted"] and report["paired_lower"] > 0 and report["brier"] < report["baseline_brier"]
    assert not review(model, rows, NOW+pd.Timedelta(days=10))["accepted"]
    assert not review(model | {"id": "other"}, rows, NOW+pd.Timedelta(days=40))["accepted"]
    for row in rows:
        row["candidate_buy"] = True
    assert not review(model, rows, NOW+pd.Timedelta(days=40))["accepted"]


def test_regime_change_pauses_active_filter(tmp_path, monkeypatch):
    r = study(tmp_path, monkeypatch)
    model = fit(training_rows(), NOW)
    r.raw["active"] = model
    r.raw["last_fit"] = NOW.isoformat()
    r.raw["rows"] = [dict(symbol="BTC/CHF", active_id=model["id"], active_buy=True, block=i,
                          observed=NOW.isoformat(), outcome={"net_return": -.02, "known_at": NOW.isoformat()}) for i in range(10)]
    r.advance({}, NOW)
    assert r.raw["active"] is None and r.raw["history"][-1]["status"] == "paused_drift"


def test_changed_execution_settings_have_separate_evidence(tmp_path, monkeypatch):
    r = study(tmp_path, monkeypatch)
    r.save()
    other_cfg = deepcopy(r.cfg)
    other_cfg.slippage *= 2
    other = Research(other_cfg, r.h)
    assert other.path != r.path and not other.raw["rows"]


def test_incomplete_candles_and_nonfinite_features_rejected(tmp_path, monkeypatch):
    r = study(tmp_path, monkeypatch)
    with pytest.raises(ValueError, match="unfinished"):
        r.observe("BTC/CHF", frame(), 1, {}, None, 0, 0, NOW-pd.Timedelta(hours=2))
    with pytest.raises(ValueError, match="Non-finite"):
        features(frame(), float("nan"), 0, 0, 0)


def test_llm_default_off_and_bounded_cached_calls(tmp_path, monkeypatch):
    monkeypatch.delenv("NEWS_LLM_ENABLED", raising=False)
    assert "ausgeschaltet" in news_analysis.analyze([], request=lambda *a: pytest.fail())["status"]
    monkeypatch.setenv("NEWS_LLM_ENABLED", "1")
    monkeypatch.setenv("NEWS_LLM_MODEL", "configured-model")
    monkeypatch.setenv("OPENAI_API_KEY", "test-key")
    monkeypatch.setenv("NEWS_LLM_MAX_CALLS_PER_DAY", "1")
    headlines = [Headline("source", "Crypto example", NOW.to_pydatetime(), "https://example.org/source")]
    calls = []
    def fake(payload, key):
        calls.append(payload)
        assert payload["store"] is False and "test-key" not in json.dumps(payload)
        result = {"items": [{"id": 0, "event_key": "example", "kind": "uncertain", "assets": ["UNKNOWN"],
                             "confidence": .2, "explanation": "Unklar"}]}
        return {"status": "completed", "output": [{"content": [{"type": "output_text", "text": json.dumps(result)}]}]}
    path = tmp_path / "news.json"
    first = news_analysis.analyze(headlines, path, fake, NOW.to_pydatetime())
    assert first["items"][0]["link"] == headlines[0].link
    assert news_analysis.analyze(headlines, path, fake, NOW.to_pydatetime()) == first
    headlines[0].title = "Changed news"
    assert "Tageslimit" in news_analysis.analyze(headlines, path, fake, NOW.to_pydatetime())["status"]
    assert len(calls) == 1 and "test-key" not in path.read_text()


@pytest.mark.parametrize("change", [{"id": 999}, {"confidence": float("nan")}, {"assets": ["FAKE"]}, {"link": "https://evil"}])
def test_llm_rejects_hallucinated_sources_and_invalid_output(change):
    item = {"id": 0, "event_key": "example", "kind": "uncertain", "assets": ["UNKNOWN"],
            "confidence": .2, "explanation": "Unklar"}
    with pytest.raises(ValueError):
        news_analysis.validate({"items": [item | change]}, [{"title": "x", "source": "s", "link": "https://good"}])


def test_paper_integration_filter_blocks_entries_but_never_exits(tmp_path, monkeypatch):
    from tradingbot import bot, state
    from tradingbot.broker import PaperBroker
    from tradingbot.engine import Trader
    from tradingbot.risk import RiskManager
    monkeypatch.chdir(tmp_path)
    now = pd.Timestamp.now(tz="UTC")
    df = frame()
    df.index = pd.date_range(end=now.floor("h")-pd.Timedelta(hours=1), periods=len(df), freq="h")

    class Exchange:
        id = "fake"
        def load_markets(self):
            return {"BTC/CHF": {}}
        def fetch_ticker(self, s):
            return {"last": 100.}

    class Strategy:
        signal = 1
        params = {}
        last_diagnostic = {"score": .8, "threshold": .5, "reason": "Test"}
        def member_pnl(self, df):
            return None
        def signals(self, df):
            return pd.Series(self.signal, index=df.index)

    cfg = Config(starting_capital=100, use_news=False, research_enabled=True, reevaluate=True,
                 symbols=["BTC/CHF"], poll_seconds=0, name="integration")
    r = Research(cfg, cfg.horizon_list()[0])
    r.raw["active"] = {"id": "active-test", "created": now.isoformat(), "mean": [0.]*11,
                       "scale": [1.]*11, "weights": [0.]*11, "bias": -10, "win": .03, "loss": -.02}
    r.raw["last_fit"] = now.isoformat()
    r.save()
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: Exchange())
    monkeypatch.setattr(data, "fetch_recent", lambda *a, **k: df)
    monkeypatch.setattr(bot, "build", lambda *a, **k: Strategy())
    monkeypatch.setattr(bot, "_spread", lambda *a: .001)
    bot.run(cfg, max_iterations=1)
    snapshot = state.read(cfg.state_path)
    assert not snapshot["open_trades"] and "KI-Filter" in snapshot["note"]
    assert snapshot["research"][""]["pending"] == 1
    trader = Trader(PaperBroker(100, 0, 0), RiskManager(cfg.risk, 100))
    trader.on_signal("BTC/CHF", 1, 100, 2, 100, now.to_pydatetime())
    assert trader.open_trades
    state.save(cfg.state_path, trader, {})
    Strategy.signal = -1
    bot.run(cfg, max_iterations=1)
    snapshot = state.read(cfg.state_path)
    assert not snapshot["open_trades"] and len(snapshot["closed"]) == 1
    assert len(Research(cfg, cfg.horizon_list()[0]).raw["rows"]) == 1


def test_leverage_and_live_research_refused(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    cfg = Config(mode="live")
    with pytest.raises(ValueError, match="paper"):
        Research(cfg, cfg.horizon_list()[0])
    cfg.mode = "paper"
    cfg.risk.leverage = 3
    with pytest.raises(ValueError, match="unleveraged"):
        Research(cfg, cfg.horizon_list()[0])
