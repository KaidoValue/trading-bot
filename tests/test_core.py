from pathlib import Path
import pandas as pd
import pytest

from tradingbot import backtest, bot, data
from tradingbot.broker import PaperBroker
from tradingbot.config import Config, RiskConfig
from tradingbot.engine import Trader
from tradingbot.risk import RiskManager
from tradingbot.strategies import STRATEGIES, build


@pytest.fixture(scope="module")
def df():
    return data.synthetic(bars=1500, seed=1)


@pytest.mark.parametrize("name", list(STRATEGIES))
def test_no_lookahead(df, name):
    """Signale bis Kerze i dürfen sich nicht ändern, wenn spätere Kerzen dazukommen."""
    s = build(name)
    full = s.signals(df)
    partial = s.signals(df.iloc[:1000])
    pd.testing.assert_series_equal(full.iloc[:1000], partial, check_names=False)


def test_position_size_respects_risk():
    rm = RiskManager(RiskConfig(risk_per_trade=0.01, stop_loss_atr=2, max_position_pct=1.0), 1000)
    plan = rm.plan(equity=1000, cash=1000, price=100, atr=1)
    assert plan.qty == pytest.approx(5)          # 10 CHF Risiko / 2 CHF Stop-Abstand
    assert plan.stop == pytest.approx(98)


def test_too_small_order_rejected():
    rm = RiskManager(RiskConfig(min_order_value=10), 1)
    assert rm.plan(equity=1, cash=1, price=50_000, atr=500) is None


def test_paper_broker_charges_fees():
    b = PaperBroker(1000, fee_rate=0.01, slippage=0)
    b.buy("X", 5, 100)
    b.sell("X", 5, 100)
    assert b.cash() == pytest.approx(1000 - 5 - 5)


def test_stop_loss_and_kill_switch():
    cfg = RiskConfig(max_drawdown_pct=0.05, max_position_pct=1.0, risk_per_trade=0.5, max_total_risk_pct=1.0)
    t = Trader(PaperBroker(1000, 0, 0), RiskManager(cfg, 1000))
    t.on_signal("X", 1, 100, atr=5, equity=1000, when=0)
    stop = t.open_trades["X"].stop
    t.check_stops("X", 100, 101, stop - 1, when=1)
    assert "X" not in t.open_trades and t.closed[0]["reason"] == "Stop-Loss"
    t.risk.update(t.equity({}), day=1)
    assert t.risk.halted
    t.on_signal("X", 1, 100, atr=5, equity=t.equity({}), when=2)
    assert "X" not in t.open_trades


def test_backtest_runs(df):
    res = backtest.run(df, build("trend"), Config())
    st = res.stats()
    assert st["Trades"] > 0 and st["Endkapital"] > 0


class FakeExchange:
    """Simuliert eine Börse für den Paper-Loop ohne Netzwerk."""
    id = "fake"

    def __init__(self, df):
        self.df, self.i = df, 300

    def fetch_ticker(self, symbol):
        self.i += 1
        return {"last": self.df["close"].iloc[self.i]}

    def fetch_ohlcv(self, symbol, timeframe, limit=300, since=None):
        part = self.df.iloc[self.i - limit:self.i + 1]
        ts = (part.index.astype("int64") // 1_000_000).tolist()
        return [[t, *row] for t, row in zip(ts, part[["open", "high", "low", "close", "volume"]].values.tolist())]


def test_paper_loop(df, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: FakeExchange(df))
    cfg = Config(strategy="trend", poll_seconds=0, symbols=["BTC/CHF"], use_news=False)
    bot.run(cfg, max_iterations=200)


def test_short_trade_profits_when_price_falls():
    cfg = RiskConfig(max_position_pct=1.0, risk_per_trade=0.5, max_total_risk_pct=1.0)
    t = Trader(PaperBroker(1000, 0, 0), RiskManager(cfg, 1000), allow_short=True)
    t.on_signal("X", -1, 100, atr=5, equity=1000, when=0)
    tr = t.open_trades["X"]
    assert tr.side == -1 and tr.stop > 100 and tr.target < 100
    t.check_stops("X", 95, 96, tr.target - 1, when=1)
    assert t.closed[0]["reason"] == "Take-Profit" and t.closed[0]["pnl"] > 0
    assert t.broker.position("X") == pytest.approx(0)
    assert t.equity({"X": 50}) == pytest.approx(1000 + t.closed[0]["pnl"])


def test_short_disabled_by_default():
    t = Trader(PaperBroker(1000, 0, 0), RiskManager(RiskConfig(), 1000))
    t.on_signal("X", -1, 100, atr=5, equity=1000, when=0)
    assert not t.open_trades


def test_short_stop_loss():
    cfg = RiskConfig(max_position_pct=1.0, risk_per_trade=0.5, max_total_risk_pct=1.0)
    t = Trader(PaperBroker(1000, 0, 0), RiskManager(cfg, 1000), allow_short=True)
    t.on_signal("X", -1, 100, atr=5, equity=1000, when=0)
    t.check_stops("X", 101, t.open_trades["X"].stop + 1, 100, when=1)
    assert t.closed[0]["reason"] == "Stop-Loss" and t.closed[0]["pnl"] < 0


def test_adaptive_prefers_trend_in_trending_market():
    """In einem stetigen Aufwärtstrend soll die lernende Gewichtung die Trendfolge bevorzugen."""
    import numpy as np
    n = 1200
    close = 100 * np.exp(np.linspace(0, 1.5, n) + 0.002 * np.random.default_rng(0).standard_normal(n))
    idx = pd.date_range("2024-01-01", periods=n, freq="h", tz="UTC")
    df = pd.DataFrame({"open": close, "high": close * 1.002, "low": close * 0.998, "close": close, "volume": 1.0}, index=idx)
    w = build("adaptive").weights(df).iloc[-1]
    assert w["trend"] > w["mean_reversion"]


@pytest.mark.parametrize("name", list(STRATEGIES))
def test_no_lookahead_with_short(df, name):
    s = build(name, allow_short=True)
    pd.testing.assert_series_equal(s.signals(df).iloc[:1000], s.signals(df.iloc[:1000]), check_names=False)


# ---------- Nachrichten ----------
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime

from tradingbot import news
from tradingbot.news import Headline, MarketContext

NOW = datetime(2026, 10, 22, 12, tzinfo=timezone.utc)


def _h(source, title, hours_ago=1):
    return Headline(source, title, NOW - timedelta(hours=hours_ago))


def test_single_source_is_not_confirmed():
    score, confirmed = news.score_headlines([_h("a", "Bitcoin exchange hack: $100M stolen")], "BTC", now=NOW)
    assert score == 0 and not confirmed


def test_confirmed_negative_news():
    hs = [_h("a", "Bitcoin exchange hacked, funds stolen"), _h("b", "Major crypto exchange hack drains wallets")]
    score, confirmed = news.score_headlines(hs, "BTC", now=NOW)
    assert score <= -0.8 and confirmed["hack"] == ["a", "b"]


def test_old_and_irrelevant_news_ignored():
    hs = [_h("a", "Bitcoin rally continues", hours_ago=48), _h("b", "Bitcoin rally continues", hours_ago=48),
          _h("a", "Football club hacked"), _h("b", "Football club hack")]
    assert news.score_headlines(hs, "BTC", now=NOW) == (0.0, {})


def test_context_blocks_and_sizes():
    bad = MarketContext(fear_greed=10, news_score=-0.9)
    assert not bad.allows(1) and bad.allows(-1) and bad.size_factor() == 0.5
    assert MarketContext(fear_greed=50).size_factor() == 1.0


def test_trader_respects_news():
    t = Trader(PaperBroker(1000, 0, 0), RiskManager(RiskConfig(), 1000))
    t.context = MarketContext(news_score=-1.0)
    t.on_signal("X", 1, 100, atr=5, equity=1000, when=0)
    assert not t.open_trades


def test_news_monitor_with_fake_web():
    pub = format_datetime(datetime.now(timezone.utc))
    rss = f"<rss><channel><item><title>Bitcoin ETF inflows hit record inflows</title><pubDate>{pub}</pubDate></item></channel></rss>".encode()

    def fake_get(url, timeout=10):
        return b'{"data":[{"value":"72"}]}' if "alternative.me" in url else rss

    ctx = news.NewsMonitor("BTC", get=fake_get).current()
    assert ctx.fear_greed == 72 and ctx.news_score > 0 and "etf_zulassung" in ctx.confirmed


def test_news_monitor_survives_offline():
    def broken(url, timeout=10):
        raise OSError("offline")
    ctx = news.NewsMonitor("BTC", get=broken).current()
    assert ctx.fear_greed is None and ctx.news_score == 0


# ---------- Kerzenmuster, Struktur, SMC ----------
from tradingbot import patterns, structure, events
from tradingbot.backtest import walk_forward


def _candles(rows):
    idx = pd.date_range("2024-01-01", periods=len(rows), freq="h", tz="UTC")
    return pd.DataFrame(rows, columns=["open", "high", "low", "close"], index=idx).assign(volume=1.0)


def test_candlestick_patterns():
    falling = [[110 - i, 111 - i, 108 - i, 109 - i] for i in range(6)]
    df = _candles(falling + [[104, 105, 98, 104.8],        # Hammer
                              [104.8, 105, 102, 102.5],     # rot
                              [102.3, 106, 102, 105.5],    # Bullish Engulfing
                              [105, 105.8, 103, 104]])     # Inside Bar
    assert patterns.hammer(df).iloc[6]
    assert patterns.bullish_engulfing(df).iloc[8]
    assert patterns.inside_bar(df).iloc[9]
    assert patterns.doji(_candles([[100, 105, 95, 100.2]])).iloc[0]


def test_structure_has_no_lookahead(df):
    full, part = structure.analyze(df), structure.analyze(df.iloc[:1000])
    pd.testing.assert_frame_equal(full.iloc[:1000], part, check_dtype=False)
    pd.testing.assert_series_equal(structure.htf_trend(df).iloc[:1001], structure.htf_trend(df.iloc[:1001]))


def test_swings_and_break_of_structure():
    # Auf und ab mit steigenden Hochs und Tiefs, dann Ausbruch über das letzte Hoch
    path = [100, 104, 108, 104, 101, 106, 111, 107, 104, 109, 114, 110, 107, 112, 118, 122, 125]
    df = _candles([[p, p + 1, p - 1, p] for p in path])
    a = structure.analyze(df, n=2)
    assert a["sh"].dropna().iloc[-1] == 115 and a["trend"].iloc[-1] == 1
    assert a["BOS_up"].any()


def test_fair_value_gap_detected_and_tapped():
    df = _candles([[100, 101, 99, 100.5], [100.5, 106, 100.4, 105.8], [105.8, 108, 103, 107],
                   [107, 107.5, 102.5, 104], [104, 106, 103.5, 105.5]])
    sm = structure.analyze(df, n=1)
    assert sm["bull_fvg_tap"].iloc[3]


# ---------- Risikoregeln ----------

def test_overtrading_and_loss_streak_pause():
    from datetime import datetime as dt
    cfg = RiskConfig(max_trades_per_day=2, loss_streak_pause=2, pause_hours=5, max_total_risk_pct=1.0)
    rm = RiskManager(cfg, 1000)
    t0 = dt(2026, 1, 1, 10, tzinfo=timezone.utc)
    rm.update(1000, t0.date())
    rm.record_open(); rm.record_open()
    assert not rm.can_open(1000, t0) and rm.last_block == "max. Trades pro Tag"
    rm.update(1000, (t0 + timedelta(days=1)).date())
    rm.record_close(-5, t0 + timedelta(days=1)); rm.record_close(-5, t0 + timedelta(days=1))
    assert not rm.can_open(1000, t0 + timedelta(days=1, hours=1))
    assert rm.can_open(1000, t0 + timedelta(days=1, hours=6))


def test_total_risk_limit():
    cfg = RiskConfig(risk_per_trade=0.01, max_total_risk_pct=0.02, max_position_pct=1.0)
    t = Trader(PaperBroker(10_000, 0, 0), RiskManager(cfg, 10_000))
    for s in ("A", "B", "C"):
        t.on_signal(s, 1, 100, atr=1, equity=t.equity({k: 100 for k in t.open_trades} | {s: 100}), when=0)
    assert len(t.open_trades) == 2


def test_stats_and_walk_forward(df):
    st = backtest.run(df, build("trend"), Config()).stats()
    assert {"CRV", "Expectancy", "Profit Factor", "Max. Verlustserie"} <= set(st)
    wf = walk_forward(df, Config(), {"trend": lambda: build("trend"), "breakout": lambda: build("breakout")},
                      train_bars=600, test_bars=300)
    assert len(wf) == 3 and set(wf["Gewählt"]) <= {"trend", "breakout"}


# ---------- Ereignisse ----------

def test_trump_tariff_alert_blocks_longs():
    hs = [_h("cointelegraph", "Trump announces new tariffs on China, Bitcoin drops", hours_ago=0.2)]
    alerts = events.detect_alerts(hs, set(), NOW, window_minutes=30)
    assert alerts and alerts[0].who == "trump" and alerts[0].impact < 0
    ctx = MarketContext(alerts=alerts)
    assert not ctx.allows(1) and ctx.allows(-1)


def test_unclear_alert_pauses_everything_and_old_alert_expires():
    hs = [_h("sec", "SEC statement on crypto market structure", hours_ago=0.1),
          _h("x", "Musk talks about Bitcoin", hours_ago=2)]
    alerts = events.detect_alerts(hs, {"sec"}, NOW, window_minutes=30)
    assert len(alerts) == 1 and alerts[0].impact == 0
    ctx = MarketContext(alerts=alerts)
    assert not ctx.allows(1) and not ctx.allows(-1)


def test_economic_calendar_blackout():
    raw = b'[{"title":"FOMC Statement","country":"USD","impact":"High","date":"2026-10-22T14:00:00-04:00"},' \
          b'{"title":"Minor","country":"USD","impact":"Low","date":"2026-10-22T08:00:00-04:00"}]'
    cal = events.parse_calendar(raw)
    assert len(cal) == 1
    assert events.blackout(cal, datetime(2026, 10, 22, 18, 10, tzinfo=timezone.utc)) .startswith("FOMC")
    assert events.blackout(cal, datetime(2026, 10, 22, 20, 0, tzinfo=timezone.utc)) is None
    assert not MarketContext(blackout="FOMC").allows(1)


def test_halt_days_resumes_after_pause():
    from datetime import date
    rm = RiskManager(RiskConfig(max_drawdown_pct=0.1, halt_days=3), 1000)
    rm.update(1000, date(2026, 1, 1))
    rm.update(850, date(2026, 1, 2))
    assert rm.halted
    rm.update(850, date(2026, 1, 4))
    assert rm.halted
    rm.update(850, date(2026, 1, 5))
    assert not rm.halted and rm.peak_equity == 850


def test_state_survives_restart(df, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    ex = FakeExchange(df)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: ex)
    cfg = Config(strategy="trend", poll_seconds=0, use_news=False)
    bot.run(cfg, max_iterations=150)
    from tradingbot import state
    t1 = bot.make_trader(cfg, ex)
    last = state.load(cfg.state_path, t1)
    assert last and cfg.state_path.exists()
    n_closed, cash = len(t1.closed), t1.broker.cash()
    assert n_closed > 0
    bot.run(cfg, max_iterations=50)          # macht weiter statt neu anzufangen
    t2 = bot.make_trader(cfg, ex)
    state.load(cfg.state_path, t2)
    assert len(t2.closed) >= n_closed


def test_news_briefing_lists_sources_and_links():
    hs = [Headline("coindesk", "SEC sues crypto exchange over listings", NOW - timedelta(hours=2), "https://x/1"),
          Headline("decrypt", "Crypto exchange faces SEC lawsuit", NOW - timedelta(hours=1), "https://x/2")]
    score, confirmed = news.score_headlines(hs, "BTC", now=NOW)
    ctx = MarketContext(fear_greed=30, news_score=score, confirmed=confirmed,
                        evidence=news.evidence(hs, "BTC", confirmed, now=NOW))
    md = news.briefing(ctx.to_dict())
    assert "klage" in md and "[Crypto exchange faces SEC lawsuit](https://x/2)" in md and "decrypt" in md
    assert md.index("decrypt") < md.index("coindesk**")


def test_lawsuit_alone_does_not_block():
    hs = [_h("a", "Shareholder sues Trump over crypto deals"), _h("b", "Crypto lawsuit filed against Trump")]
    score, confirmed = news.score_headlines(hs, "BTC", now=NOW)
    assert "klage" in confirmed and MarketContext(news_score=score, confirmed=confirmed).allows(1)
    alerts = events.detect_alerts(hs, set(), NOW, window_minutes=120)
    assert MarketContext(alerts=alerts).allows(1)


class MultiExchange(FakeExchange):
    """Börse mit mehreren Coins (gleiche Kurse, je anders skaliert); DOGE/CHF gibt es nicht."""
    markets = {"BTC/CHF": {}, "ETH/CHF": {}, "SOL/CHF": {}}

    def load_markets(self):
        return self.markets

    def fetch_ticker(self, symbol):
        if symbol == "BTC/CHF":
            self.i += 1
        return {"last": self.df["close"].iloc[self.i] * self.scale(symbol)}

    def fetch_ohlcv(self, symbol, timeframe, limit=300, since=None):
        return [[t, *(v * self.scale(symbol) for v in row[:4]), row[4]]
                for t, *row in super().fetch_ohlcv(symbol, timeframe, limit, since)]

    @staticmethod
    def scale(symbol):
        return {"BTC/CHF": 1.0, "ETH/CHF": 0.05, "SOL/CHF": 0.002}[symbol]


def test_several_coins_and_unknown_coin_skipped(df, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: MultiExchange(df))
    cfg = Config(strategy="trend", poll_seconds=0, symbols=["BTC/CHF", "ETH/CHF", "SOL/CHF", "DOGE/CHF"],
                 use_news=False, name="multi")
    bot.run(cfg, max_iterations=300)
    assert cfg.symbols == ["BTC/CHF", "ETH/CHF", "SOL/CHF"]
    trades = pd.read_csv(tmp_path / "daten" / "logs" / "trades_multi.csv")
    assert {"BTC/CHF", "ETH/CHF"} <= set(trades["symbol"])


def test_dashboard_tables_and_charts(df, monkeypatch, tmp_path):
    from tradingbot import dashboard
    monkeypatch.chdir(tmp_path)
    ex = MultiExchange(df)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: ex)
    Path("bot.yaml").write_text('strategy: trend\ntitle: "Test-Bot"\nsymbols: ["BTC/CHF", "ETH/CHF"]\n'
                                'use_news: false\npoll_seconds: 0\ntimeframe: 1h\n')
    bot.run(Config.load("bot.yaml"), max_iterations=300)
    text = dashboard.render(["bot.yaml"], exchange=ex)
    assert "Test-Bot" in text and "Kapital jetzt" in text and "Im Einsatz" in text
    assert (tmp_path / "daten" / "charts" / "BTC-CHF.png").exists()


def test_converted_chf_pairs():
    class Ex:
        id = "fake"
        def load_markets(self):
            return {"BTC/CHF": {}, "SOL/USD": {"spot": True}, "USD/CHF": {"spot": True}, "BTC/USD": {"spot": True}}
        def fetch_ticker(self, s):
            return {"last": {"SOL/USD": 100.0, "USD/CHF": 0.8, "BTC/CHF": 50_000.0}[s]}
        def fetch_ohlcv(self, s, tf, since=None, limit=None):
            if s == "USD/CHF":
                return [[1, 0.9, 0.9, 0.9, 0.9, 1], [3, 0.8, 0.8, 0.8, 0.8, 1]]
            return [[t, 100, 110, 90, 100, 5] for t in (1, 2, 3)]
    ex = data.Converted(Ex(), "CHF")
    assert "SOL/CHF" in ex.load_markets() and "BTC/CHF" not in ex.virtual
    assert ex.fetch_ticker("SOL/CHF")["last"] == pytest.approx(80.0)
    rows = ex.fetch_ohlcv("SOL/CHF", "1h")
    assert [r[4] for r in rows] == pytest.approx([90.0, 90.0, 80.0])       # Lücke mit letztem Kurs gefüllt
    assert ex.fetch_ticker("BTC/CHF")["last"] == 50_000.0


def test_total_invested_cap():
    rm = RiskManager(RiskConfig(max_position_pct=0.5, max_invested_pct=0.5, risk_per_trade=1.0), 1000)
    assert rm.plan(1000, 1000, 100, 1).qty == pytest.approx(5.0)       # 500 CHF frei bis zur Grenze
    assert rm.plan(1000, 600, 100, 1).qty == pytest.approx(1.0)        # 400 schon investiert: noch 100
    assert rm.plan(1000, 500, 100, 1) is None                          # Grenze erreicht


def test_learning_journal(df, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: FakeExchange(df))
    cfg = Config(strategy="trend", poll_seconds=0, symbols=["BTC/CHF"], use_news=False, title="Test-Bot")
    bot.run(cfg, max_iterations=300)
    text = "".join(p.read_text() for p in (tmp_path / "lernen" / "tagebuch").glob("*.md"))
    assert "Kauf" in text and "Verkauf" in text and "Was man daraus lernt" in text and "Test-Bot" in text


def test_breakout_hold_has_no_lookahead_and_stays_in_market(df):
    s = build("breakout", entry=10, exit=5, hold=True)
    full = s.signals(df)
    pd.testing.assert_series_equal(full.iloc[:1000], s.signals(df.iloc[:1000]), check_names=False)
    assert (full.iloc[100:] != 0).all()


def test_leverage_sizing_interest_and_liquidation():
    from tradingbot.broker import PaperBroker
    from tradingbot.engine import Trader
    rc = RiskConfig(leverage=3.0, max_position_pct=1.0, risk_per_trade=1.0, liquidation_margin=0.5)
    plan = RiskManager(rc, 1000).plan(1000, 1000, 100, 1)
    assert plan.qty == pytest.approx(29.7)                 # 3 x 1000 CHF Kaufkraft (minus Reserve)
    b = PaperBroker(1000, 0.0, 0.0)
    b.leverage = 3.0
    t = Trader(b, RiskManager(rc, 1000))
    b.buy("BTC/CHF", 30, 100)                               # 3000 CHF Position, 2000 geliehen
    assert b.cash() == pytest.approx(-2000)
    assert b.charge_interest({"BTC/CHF": 100}, 24, 0.001) == pytest.approx(2.0)
    assert not bot.liquidation(t, {"BTC/CHF": 95}, rc)     # -5 % Kurs = -15 % Konto
    assert bot.liquidation(t, {"BTC/CHF": 79}, rc)         # -21 % Kurs: Kapital < 50 % der Sicherheit -> zu


def test_leverage_refused_in_live_mode():
    cfg = Config(mode="live", risk=RiskConfig(leverage=2.0))
    with pytest.raises(SystemExit):
        bot.make_trader(cfg, None)


def test_leverage_caps_total_exposure_including_shorts():
    rm = RiskManager(RiskConfig(leverage=3.0, max_position_pct=0.5, risk_per_trade=1.0), 1000)
    assert rm.plan(1000, 1000, 100, 1, side=-1, exposure=2900).qty == pytest.approx(1.0)   # nur noch 100 CHF Platz
    assert rm.plan(1000, 1000, 100, 1, side=-1, exposure=3000) is None


def test_memory_grows_and_is_remembered(df, tmp_path):
    path = tmp_path / "ki.json"
    s = build("adaptive_memory", memory_file=str(path))
    assert s.pretrain([df.iloc[:800]]) > 0
    first = s.memory.experience()
    assert s.learn("BTC/CHF", df.iloc[700:1000]) > 0
    assert s.learn("BTC/CHF", df.iloc[700:1000]) == 0            # dieselben Kerzen nicht doppelt lernen
    again = build("adaptive_memory", memory_file=str(path))      # neu laden: nichts vergessen
    assert again.memory.experience() > first and again.memory.pretrained
    assert set(again.signals(df.iloc[-300:]).unique()) <= {-1, 0, 1}


def test_labor_invents_rules_without_lookahead(df, tmp_path):
    from tradingbot import labor
    s = labor.Evolved(["rsi_oversold", "above_sma200"], ["macd_neg"])
    pd.testing.assert_series_equal(s.signals(df).iloc[:1000], s.signals(df.iloc[:1000]), check_names=False)
    found = labor.evolve(df, population=12, generations=2, seed=1, log=lambda *_: None)
    assert found and all({"entry", "exit", "test_return", "accepted"} <= set(f) for f in found)
    path = tmp_path / "lib.json"
    lib = labor.update_library([{**found[0], "accepted": True}], df, path)
    assert lib[0]["name"] == "labor_1" and "Kaufen, wenn" in lib[0]["text"]
    ki = build("adaptive_memory", library_file=str(path))
    assert "labor_1" in [m.name for m in ki.members]


def test_chef_follows_winner_with_limits(tmp_path):
    from datetime import datetime, timedelta, timezone
    from tradingbot.chef import Chef, MAX_RISK, MIN_CASH
    path = tmp_path / "chef.json"
    t = datetime(2026, 1, 1, tzinfo=timezone.utc)
    eq = {"config_langfrist": 1000.0, "config_daytrading": 1000.0, "config_risiko": 1000.0}
    for i in range(60):                     # Risiko-Stil läuft stark, Langfrist verliert
        eq = {"config_langfrist": eq["config_langfrist"] * 0.998, "config_daytrading": eq["config_daytrading"],
              "config_risiko": eq["config_risiko"] * 1.01}
        Chef(path).update(eq, "Aufwärtstrend, wild", t + timedelta(minutes=30 * i))
    chef = Chef(path)
    assert chef.weights["config_risiko"] <= MAX_RISK + 1e-9
    assert sum(chef.weights.values()) <= 1 - MIN_CASH + 1e-9
    assert chef.weights["config_langfrist"] < 0.5           # vom Verlierer weg umgeschichtet
    assert chef.equity > 1000 and chef.fees > 0
    assert chef.memory.best("Aufwärtstrend, wild")[0][0] == "config_risiko"


def test_chef_cuts_risk_after_losses(tmp_path):
    from datetime import datetime, timezone
    from tradingbot.chef import Chef
    chef = Chef(tmp_path / "chef.json")
    chef.equity, chef.peak = 850.0, 1000.0
    w, reason = chef.target("Seitwärts, ruhig", datetime(2026, 1, 1, tzinfo=timezone.utc))
    assert w["config_risiko"] <= 0.05 + 1e-9 and "halbiert" in reason


def test_dashboard_shows_chef(df, monkeypatch, tmp_path):
    from tradingbot import dashboard
    monkeypatch.chdir(tmp_path)
    ex = MultiExchange(df)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: ex)
    Path("bot.yaml").write_text('strategy: trend\nsymbols: ["BTC/CHF"]\nuse_news: false\npoll_seconds: 0\ntimeframe: 1h\n')
    bot.run(Config.load("bot.yaml"), max_iterations=200)
    text = dashboard.render(["bot.yaml"], exchange=ex, chef_path="daten/state/chef.json")
    assert "4️⃣ Chef-Bot" in text and "Aktuelle Verteilung" in text
    assert (tmp_path / "daten" / "state" / "chef.json").exists()
