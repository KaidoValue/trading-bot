"""Regressions for execution-aware learning and temporal validation."""
import json
from dataclasses import replace

import pandas as pd
import pytest

from tradingbot import backtest, data, labor
from tradingbot.broker import KRAKEN_TIERS
from tradingbot.config import Config, Horizon, RiskConfig
from tradingbot.evaluation import replay, evaluation_params
from tradingbot.memory import Memory
from tradingbot.strategies import build


def candles(n=310):
    idx = pd.date_range("2025-01-01", periods=n, freq="h", tz="UTC")
    return pd.DataFrame({"open": 100., "high": 101., "low": 99., "close": 100., "volume": 10.}, index=idx)


def config():
    return Config(fee_rate=.001, slippage=0,
                  risk=RiskConfig(max_total_risk_pct=1, max_position_pct=.5, max_trades_per_day=100,
                                  loss_streak_pause=99, max_drawdown_pct=.99, max_daily_loss_pct=.99))


def test_replay_uses_partial_stops_and_accounts_for_all_fees():
    df = candles()
    df.iloc[251, df.columns.get_loc("high")] = 104
    df.iloc[252, df.columns.get_loc("low")] = 80
    sig = pd.Series(0, index=df.index)
    sig.iloc[250] = 1
    h = Horizon("short", "1h", "trend", partial_atr=.5, stop_loss_atr=4, take_profit_atr=100)
    result = replay(df, sig, config(), h)
    assert len(result.trades) == 1
    trade = result.trades[0]
    assert trade["partial"] and trade["fees"] > 0
    assert result.equity.iloc[-1] == pytest.approx(config().starting_capital + trade["pnl"])
    assert trade["opened"] == df.index[251]


def test_higher_fees_reduce_the_same_flat_trade_return():
    df = candles()
    sig = pd.Series(0, index=df.index)
    sig.iloc[250], sig.iloc[260] = 1, -1
    cfg = config()
    cheap = replay(df, sig, cfg)
    expensive = replay(df, sig, replace(cfg, fee_rate=.008))
    assert expensive.equity.iloc[-1] < cheap.equity.iloc[-1] < cfg.starting_capital


def test_kraken_replay_uses_configured_tiers():
    cfg, df = replace(config(), fee_model="kraken"), candles()
    sig = pd.Series(0, index=df.index)
    sig.iloc[250], sig.iloc[260] = 1, -1
    result = replay(df, sig, cfg)
    trade = result.trades[0]
    assert trade["fees"] == pytest.approx(trade["qty"] * (trade["entry"] + trade["exit"]) * KRAKEN_TIERS[0][2])


def test_member_returns_are_production_replay_returns():
    df = data.synthetic(bars=700, seed=8)
    cfg = config()
    strategy = build("adaptive", members=["trend"], **evaluation_params(cfg))
    expected = replay(df, strategy.members[0].signals(df), cfg).returns
    pd.testing.assert_series_equal(strategy.member_pnl(df)["trend"], expected, check_names=False)


def test_observed_strategies_learn_without_changing_votes(tmp_path):
    df = data.synthetic(bars=500, seed=7)
    params = dict(members=["trend"], **evaluation_params(config()))
    original = build("adaptive_memory", **params)
    path = tmp_path / "memory.json"
    trial = build("adaptive_memory", observe_members=["trend_recovery", "time_series_momentum"],
                  memory_file=path, **params)
    comparison = build("adaptive_memory", memory_file=tmp_path / "baseline.json", **params)
    pd.testing.assert_series_equal(comparison.signals(df), trial.signals(df))
    assert list(original.weights(df)) == list(trial.weights(df)) == ["trend"]
    trial.learn("BTC", df)
    comparison.learn("BTC", df)
    assert any("trend_recovery" in bucket and "time_series_momentum" in bucket
               for bucket in Memory(path).stats.values())
    pd.testing.assert_series_equal(comparison.signals(df), trial.signals(df))


def test_future_prices_do_not_change_replay_or_adaptive_signals():
    df = data.synthetic(bars=700, seed=3)
    strategy = build("adaptive_memory", **evaluation_params(config()))
    full, prefix = strategy.signals(df), strategy.signals(df.iloc[:550])
    pd.testing.assert_series_equal(full.iloc[:550], prefix)


def test_memory_halves_old_evidence_and_deduplicates(tmp_path):
    idx = pd.to_datetime(["2025-01-01", "2025-04-01"], utc=True)
    pnl = pd.DataFrame({"trend": [.1, 0]}, index=idx)
    phase = pd.Series("up", index=idx)
    path = tmp_path / "memory.json"
    mem = Memory(path, half_life_days=90)
    assert mem.learn(pnl, phase, key="BTC") == 2
    total, count = mem.prior("up", "trend")
    assert total == pytest.approx(.05)
    assert count == pytest.approx(1.5)
    assert mem.learn(pnl, phase, key="BTC") == 0
    mem.save()
    assert Memory(path, half_life_days=90).prior("up", "trend") == pytest.approx((total, count))


def test_memory_decay_is_independent_of_coin_processing_order():
    idx = pd.to_datetime(["2025-01-01", "2025-04-01"], utc=True)
    memories = [Memory(half_life_days=90), Memory(half_life_days=90)]
    for memory, order in zip(memories, [[0, 1], [1, 0]]):
        for i in order:
            memory.learn(pd.DataFrame({"s": [.1]}, index=idx[i:i+1]),
                         pd.Series("up", index=idx[i:i+1]), key=str(i))
    assert memories[0].prior("up", "s") == pytest.approx(memories[1].prior("up", "s"))


def test_legacy_evidence_is_archived_before_reset(tmp_path):
    path = tmp_path / "memory.json"
    original = json.dumps({"stats": {"up": {"s": [99, 100]}}, "pretrained": True})
    path.write_text(original)
    memory = Memory(path, half_life_days=90)
    assert memory.experience() == 0 and not memory.pretrained
    assert path.with_suffix(".json.legacy").read_text() == original


def test_backtest_does_not_read_or_mutate_persisted_future_knowledge(tmp_path):
    path = tmp_path / "future.json"
    memory = Memory(path, half_life_days=90)
    memory.stats = {"Aufwärtstrend, ruhig": {"trend": [9999., 10000.]}}
    memory.save()
    before = path.read_bytes()
    cfg, df = config(), data.synthetic(bars=600, seed=4)
    result = backtest.run(df, build("adaptive_memory", memory_file=str(path)), cfg)
    fresh = backtest.run(df, build("adaptive_memory"), cfg)
    pd.testing.assert_series_equal(result.equity, fresh.equity)
    assert path.read_bytes() == before


def test_test_account_has_no_training_positions():
    df = candles()
    sig = pd.Series(0, index=df.index)
    sig.iloc[250] = 1
    result = replay(df, sig, config(), start=df.index[280], liquidate=True)
    assert result.trades == []
    assert result.equity.iloc[-1] == config().starting_capital


def test_labor_uses_disjoint_folds_and_requires_more_than_ten_trades():
    df = data.synthetic(bars=700, seed=5)
    found = labor.evolve(df, cfg=config(), population=5, generations=1, seed=2, log=lambda *_: None)
    assert found
    for candidate in found:
        folds = candidate["folds"]
        assert len(folds) == 3
        assert pd.Timestamp(folds[0]["start"]) >= df.index[350]
        assert all(pd.Timestamp(a["end"]) < pd.Timestamp(b["start"]) for a, b in zip(folds, folds[1:]))
        if candidate["accepted"]:
            assert candidate["test_trades"] >= 30
            assert all(f["return"] > 0 and f["profit_factor"] >= 1.2 for f in folds)


def test_library_keeps_unproven_and_legacy_rules_out_of_trading(tmp_path):
    path = tmp_path / "library.json"
    rule = {"entry": ["rsi_oversold"], "exit": ["rsi_overbought"], "test_return": .2,
            "accepted": True, "validation_version": 2}
    lib = labor.update_library([rule], candles(), path, cfg=config())
    assert lib[0]["status"] == "probation"
    assert labor.library_strategies(path) == []
    lib[0]["status"] = "active"
    path.write_text(json.dumps(lib))
    assert len(labor.library_strategies(path)) == 1
    lib[0].pop("validation_version")
    path.write_text(json.dumps(lib))
    assert labor.library_strategies(path) == []


def test_probe_cannot_use_pre_discovery_data_or_changed_execution_rules(tmp_path):
    df = candles(1000)
    path = tmp_path / "library.json"
    rule = {"name": "labor_1", "entry": ["rsi_oversold"], "exit": ["rsi_overbought"],
            "status": "probation", "validation_version": 2, "discovered_at": df.index[800].isoformat(),
            "probe_config": labor.probe_signature(config())}
    path.write_text(json.dumps([rule]))
    reviewed = labor.review_probation(df, config(), path, now=df.index[810])
    assert reviewed[0]["status"] == "probation"
    assert reviewed[0]["paper_forward"]["days"] < 1
    reviewed = labor.review_probation(df, replace(config(), slippage=.01), path, now=df.index[-1])
    assert reviewed[0]["status"] == "rejected"


def test_probe_promotes_only_after_both_time_and_trade_requirements(tmp_path, monkeypatch):
    from tradingbot import evaluation
    df, cfg = candles(1200), config()
    discovery = df.index[400]
    path = tmp_path / "library.json"
    rule = {"name": "labor_1", "entry": ["rsi_oversold"], "exit": ["rsi_overbought"],
            "status": "probation", "validation_version": 2, "discovered_at": discovery.isoformat()}
    path.write_text(json.dumps([rule]))
    trades = [{"pnl": 1., "reason": "Signal"} for _ in range(20)]
    def simulated(segment, signal, bound_cfg, start=None, **kwargs):
        assert start == discovery and segment.index[-1] <= df.index[-1]
        equity = pd.Series(1020., index=segment.index)
        return evaluation.Replay(equity, equity.pct_change().fillna(0), trades)
    monkeypatch.setattr(evaluation, "replay", simulated)
    assert labor.review_probation(df, cfg, path, now=discovery + pd.Timedelta(days=13))[0]["status"] == "probation"
    assert labor.review_probation(df, cfg, path, now=discovery + pd.Timedelta(days=15))[0]["status"] == "active"


def test_daily_trend_filter_cannot_see_later_days():
    df = candles(600)
    daily = candles(400)
    daily.index = pd.date_range("2024-06-01", periods=400, freq="D", tz="UTC")
    daily["close"] = [50 + i * .25 for i in range(400)]
    h = Horizon("short", "1h", "trend", trend_filter=True)
    sig = pd.Series(1, index=df.index)
    first = replay(df, sig, config(), h, daily_history=daily)
    assert first.equity.iloc[-1] < config().starting_capital  # the known uptrend actually permits an entry
    changed = daily.copy()
    changed.loc[changed.index > df.index[-1].normalize(), "close"] = 100000
    assert not changed.equals(daily)  # there really are future daily candles in this fixture
    second = replay(df, sig, config(), h, daily_history=changed)
    pd.testing.assert_series_equal(first.equity, second.equity)
