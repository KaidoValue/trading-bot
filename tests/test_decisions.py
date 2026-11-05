from datetime import datetime, timedelta, timezone

import pandas as pd
import pytest

from tradingbot import bot, data, events, news, state, web
from tradingbot.broker import PaperBroker
from tradingbot.config import Config, RiskConfig
from tradingbot.dashboard import Bot
from tradingbot.engine import Trader
from tradingbot.risk import RiskManager
from tradingbot.strategies import build

NOW = datetime(2026, 11, 4, 18, tzinfo=timezone.utc)


def headline(source, title, age=1):
    return news.Headline(source, title, NOW - timedelta(hours=age))


def test_unrelated_incidents_do_not_confirm_each_other():
    items = [headline("a", "Binance crypto hack, funds stolen"),
             headline("b", "GitBook crypto security breach, funds stolen")]
    assert news.score_headlines(items, "BTC", now=NOW) == (0, {})


def test_same_incident_needs_distinct_sources_and_rejects_future():
    title = "Acme crypto exchange hacked, funds stolen"
    items = [headline("a", title), headline("a", title)]
    assert news.score_headlines(items, "BTC", now=NOW) == (0, {})
    items.append(headline("b", title, age=-1))
    assert news.score_headlines(items, "BTC", now=NOW) == (0, {})
    items.append(headline("b", title))
    assert news.score_headlines(items, "BTC", now=NOW) == (-1, {"hack": ["a", "b"]})


def test_asset_specific_headlines_and_word_boundaries():
    items = [headline(s, "Solana protocol Acme crypto hack") for s in ("a", "b")]
    assert news.score_headlines(items, "BTC", now=NOW) == (0, {})
    assert news.score_headlines(items, "SOL", now=NOW)[0] == -1
    assert not news.matches("security corporate banking", ["sec", "rate", "ban "])


def test_name_mention_does_not_pause_but_announcement_does():
    commentary = headline("a", "Democrats to Target Trump's Crypto Ventures After Taking Congress", age=0.1)
    assert not events.detect_alerts([commentary], set(), NOW)
    action = headline("a", "Trump announces tariffs on China, Bitcoin drops", age=0.1)
    assert not news.MarketContext(alerts=events.detect_alerts([action], set(), NOW)).allows(1)


def test_conflicting_alerts_do_not_cancel_block_and_reason_is_actual_block():
    alerts = [events.Alert("a", "positive", "x", NOW, 1), events.Alert("b", "negative", "y", NOW, -0.6)]
    ctx = news.MarketContext(alerts=alerts)
    assert not ctx.allows(1) and not ctx.allows(-1)
    assert "negative" in ctx.block_reason(1)
    ctx = news.MarketContext(news_score=-1, confirmed={"hack": ["a", "b"]}, alerts=alerts[:1])
    assert "hack" in ctx.block_reason(1) and "positive" not in ctx.block_reason(1)


def test_coin_context_reuses_downloads(monkeypatch):
    import time
    monitor = news.NewsMonitor("BTC", events=False)
    monitor.context = news.MarketContext(fetched_at=time.time())
    monitor.headlines = [news.Headline(s, "Solana protocol Acme crypto hack", datetime.now(timezone.utc))
                         for s in ("a", "b")]
    monkeypatch.setattr(news, "fetch_headlines", lambda *a, **k: pytest.fail("unexpected download"))
    assert monitor.current("SOL").news_score == -1
    assert monitor.current("BTC").news_score == 0


def test_decisions_survive_restart_and_other_horizon(tmp_path):
    cfg = Config()
    trader = Trader(PaperBroker(100, 0, 0), RiskManager(cfg.risk, 100))
    h = cfg.horizon_list()[0]
    bot._decision(trader, "long:BTC/CHF", "BTC/CHF", h, NOW, NOW, 1, "News block")
    path = tmp_path / "state.json"
    state.save(path, trader, {})
    restored = Trader(PaperBroker(100, 0, 0), RiskManager(cfg.risk, 100))
    state.load(path, restored)
    bot._decision(restored, "short:BTC/CHF", "BTC/CHF", h, NOW, NOW, -1, "Cash")
    assert restored.decisions["long:BTC/CHF"]["reason"] == "News block"
    assert restored.decisions["long:BTC/CHF"]["checked"] == NOW


def test_rejected_order_does_not_keep_previous_success_note():
    class Reject(PaperBroker):
        def buy(self, *args, **kwargs):
            return None
    trader = Trader(Reject(1000, 0, 0), RiskManager(RiskConfig(), 1000))
    trader.note = "previously bought"
    trader.on_signal("BTC/CHF", 1, 100, 2, 1000, NOW)
    assert "nicht ausgeführt" in trader.note
    assert not trader.open_trades


def test_learning_distinguishes_no_executions_from_losses():
    frame = data.synthetic(bars=310, seed=1)
    strategy = build("adaptive", members=["trend"], execution_config=Config(starting_capital=1))
    strategy.signals(frame)
    assert "Keine simulierten Ausführungen" in strategy.last_diagnostic["reason"]
    strategy._pnl_cache = (frame, pd.DataFrame({"trend": -0.01}, index=frame.index))
    strategy._replay_activity = {"trend": {"closed": 2, "exposure": 0.5}}
    strategy.signals(frame)
    assert "Keine positiv gewichtete" in strategy.last_diagnostic["reason"]


def test_dashboard_escapes_decision_content_and_shows_time():
    cfg = Config(starting_capital=100)
    trader = Trader(PaperBroker(100, 0, 0), RiskManager(cfg.risk, 100))
    bot._decision(trader, "BTC/CHF", "BTC/CHF", cfg.horizon_list()[0], NOW, NOW, 1, "<script>alert(1)</script>")
    html = web.page([Bot(cfg, trader, 100, 0)], None, {}, {}, pd.DataFrame(), NOW)
    assert "Warum handelt der Bot" in html and "04.11. 19:00" in html
    assert "&lt;script&gt;alert(1)&lt;/script&gt;" in html
    assert "<script>alert(1)</script>" not in html


def test_paper_loop_uses_coin_context_and_retains_skipped_decisions(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    frame = data.synthetic(bars=300, seed=1)
    for column in ("open", "high", "low", "close"):
        frame[column] = pd.Series(range(100, 400), index=frame.index, dtype=float)
    frame["high"] += 2
    frame["low"] -= 2

    class Exchange:
        id = "test"
        def load_markets(self):
            return {"BTC/CHF": {}, "ETH/CHF": {}}
        def fetch_ticker(self, symbol):
            return {"last": 399}

    class Monitor:
        def __init__(self, *args, **kwargs):
            pass
        def current(self, asset=None):
            return news.MarketContext(news_score=-1 if asset in (None, "BTC") else 0)

    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: Exchange())
    monkeypatch.setattr(data, "fetch_recent", lambda *a, **k: frame)
    monkeypatch.setattr(bot, "NewsMonitor", Monitor)
    cfg = Config(symbols=["BTC/CHF", "ETH/CHF"], strategy="trend", starting_capital=1000,
                 poll_seconds=0, use_news=True, name="decisions")
    bot.run(cfg, max_iterations=1)
    first = state.read(cfg.state_path)
    assert "BTC/CHF" not in first["open_trades"]
    assert "ETH/CHF" in first["open_trades"]
    assert len(first["decisions"]) == 2
    bot.run(cfg, max_iterations=1)
    second = state.read(cfg.state_path)
    assert first["decisions"] == second["decisions"]
