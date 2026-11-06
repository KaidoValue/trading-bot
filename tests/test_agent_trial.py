from copy import deepcopy
from datetime import datetime, timedelta, timezone

import numpy as np
import pandas as pd
import pytest

from tradingbot import agent_trial as agent


def frame(now):
    index = pd.date_range(end=now-timedelta(days=1), periods=120, freq="D")
    prices = np.linspace(70, 100, len(index))
    return pd.DataFrame({"open": prices, "high": prices+1, "low": prices-1,
                         "close": prices, "volume": 1.0}, index=index)


def model_for(prices):
    wallet = agent.account()
    key = agent.state_key(agent.features(prices).iloc[-1].to_numpy(), wallet, 100)
    return {"q": {key: [0.0, 0.0, 0.0, 1.0]}}


def test_costs_and_long_only_allocations():
    wallet = agent.account()
    entry = agent.trade(wallet, 3, 100)
    assert 0 < wallet["qty"] < 0.5
    assert wallet["cash"] >= 0
    exit_fill = agent.trade(wallet, 1, 100)
    assert wallet["qty"] == 0
    assert wallet["cash"] == pytest.approx(
        100-wallet["fees"]+entry["qty"]*(exit_fill["price"]-entry["price"]))
    assert wallet["cash"] < 100


def test_daily_learning_frozen_control_and_atomic_retry(monkeypatch):
    monkeypatch.setattr(agent, "EPSILON", 0)
    now = datetime(2026, 11, 6, tzinfo=timezone.utc)
    data = frame(now)
    trial = agent.begin(model_for(data), now)
    agent.advance(trial, data, 100, now)
    frozen = deepcopy(trial["frozen_q"])
    first = deepcopy(trial)
    agent.advance(trial, data, 100, now)
    assert trial == first
    tomorrow = now+timedelta(days=1)
    agent.advance(trial, frame(tomorrow), 90, tomorrow)
    assert trial["learner"]["updates"] == 1
    assert trial["frozen_q"] == frozen
    assert trial["q"] != first["q"]
    assert trial["ends"] == first["ends"]


def test_expiry_liquidates_even_on_same_bar_and_never_restarts(monkeypatch):
    monkeypatch.setattr(agent, "EPSILON", 0)
    now = datetime(2026, 11, 6, tzinfo=timezone.utc)
    trial = agent.begin(model_for(frame(now)), now)
    agent.advance(trial, frame(now), 100, now)
    trial["ends"] = (now+timedelta(hours=1)).isoformat()
    agent.advance(trial, frame(now), 101, now+timedelta(hours=1))
    assert trial["status"] == "completed"
    assert trial["learner"]["qty"] == trial["frozen"]["qty"] == 0
    assert trial["learner"]["pending"] is None
    saved = deepcopy(trial)
    agent.advance(trial, frame(now), 900, now+timedelta(days=90))
    assert trial == saved


def test_features_are_causal_and_invalid_quotes_rejected():
    now = datetime(2026, 11, 6, tzinfo=timezone.utc)
    data = frame(now)
    pd.testing.assert_frame_equal(agent.features(data).iloc[:100], agent.features(data.iloc[:100]))
    trial = agent.begin(model_for(data), now)
    with pytest.raises(ValueError):
        agent.advance(trial, data, 100, now, (102, 99))


def test_stale_candles_never_create_new_orders():
    now = datetime(2026, 11, 6, tzinfo=timezone.utc)
    data = frame(now-timedelta(days=3))
    trial = agent.begin(model_for(data), now)
    agent.advance(trial, data, 100, now)
    assert trial["learner"]["fills"] == trial["frozen"]["fills"] == 0
