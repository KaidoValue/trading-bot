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
    rc = RiskConfig(leverage=3.0, max_position_pct=1.0, risk_per_trade=1.0, liquidation_margin=0.5,
                    max_total_risk_pct=1)
    plan = RiskManager(rc, 1000).plan(1000, 1000, 100, 1)
    assert plan.qty == pytest.approx(29.7)                 # 3 x 1000 CHF Kaufkraft (minus Reserve)
    b = PaperBroker(1000, 0.0, 0.0)
    b.leverage = 3.0
    t = Trader(b, RiskManager(rc, 1000))
    t.on_signal("BTC/CHF", 1, 100, atr=1, equity=1000, when=0)    # 2970 CHF Position, 1970 geliehen
    tr = t.open_trades["BTC/CHF"]
    assert tr.margin_value == pytest.approx(1970) and b.cash() == pytest.approx(-1970 * 1.0003)   # + Eröffnung
    t.charge_interest({"BTC/CHF": 100}, 24, 0.001)                 # Zinsen nur auf den geliehenen Teil
    assert tr.interest == pytest.approx(1970 * 0.0013) and b.interest_paid == pytest.approx(tr.interest)
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


def test_chef_cuts_risk_after_losses(tmp_path, monkeypatch):
    from datetime import datetime, timezone
    from tradingbot import chef as ch
    from tradingbot.chef import Chef, MAX_RISK
    monkeypatch.setattr(ch, "RISK_CUT", 0.10)            # Funktion bleibt einschaltbar (Standard: aus)
    chef = Chef(tmp_path / "chef.json")
    chef.equity, chef.peak = 850.0, 1000.0
    w, reason = chef.target("Seitwärts, ruhig", datetime(2026, 1, 1, tzinfo=timezone.utc))
    assert w["config_risiko"] <= MAX_RISK / 2 + 1e-9 and "halbiert" in reason


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
    html = (tmp_path / "daten" / "charts" / "index.html").read_text()
    assert "Trading-Bot Terminal" in html and "Chef-Bot" in html and "KRAKEN:BTCCHF" in html
    dashboard.render(["bot.yaml"], exchange=ex, chef_path="daten/state/chef.json")
    assert len(pd.read_csv(tmp_path / "daten" / "state" / "verlauf.csv")) == 2


def test_chef_emergency_brake(tmp_path):
    from datetime import datetime, timedelta, timezone
    from tradingbot.chef import Chef, DEFAULT
    path = tmp_path / "chef.json"
    t = datetime(2026, 1, 1, tzinfo=timezone.utc)
    eq = {"config_langfrist": 1000.0, "config_daytrading": 1000.0, "config_risiko": 1000.0}
    Chef(path).update(eq, "Aufwärtstrend, wild", t)
    for i in (1, 2):                                        # Risiko-Stil verliert 2 × 2.5 % in einer Stunde
        eq["config_risiko"] *= 0.975
        change = Chef(path).update(eq, "Aufwärtstrend, wild", t + timedelta(minutes=30 * i))
    chef = Chef(path)
    assert chef.weights["config_risiko"] <= DEFAULT["config_risiko"] * 0.1 + 0.001 and "Notbremse" in change["reason"]


def test_youtube_saves_new_videos(monkeypatch, tmp_path):
    from tradingbot import youtube
    monkeypatch.chdir(tmp_path)
    feed = """<feed xmlns="http://www.w3.org/2005/Atom" xmlns:yt="http://www.youtube.com/xml/schemas/2015"
      xmlns:media="http://search.yahoo.com/mrss/">
      <entry><yt:videoId>v2</yt:videoId><title>Bitcoin: Ausbruch über 100k?</title>
        <published>2026-10-24T08:00:00+00:00</published><media:group><media:description>Analyse</media:description></media:group></entry>
      <entry><yt:videoId>v1</yt:videoId><title>Elliott-Wellen Update</title>
        <published>2026-10-23T08:00:00+00:00</published><media:group><media:description></media:description></media:group></entry>
    </feed>"""
    page = '<link rel="canonical" href="https://www.youtube.com/channel/UCabcdefghijklmnopqrstuv">'
    get = lambda url: page if "/@" in url else feed
    files = youtube.update(["kanal"], get=get, fetch_transcript=lambda v: "Kaufen über der 200-Tage-Linie" if v == "v2" else None)
    assert len(files) == 2 and "Kaufen über der 200-Tage-Linie" in Path(files[-1]).read_text()
    assert "Keine Abschrift" in Path(files[0]).read_text()
    assert youtube.update(["kanal"], get=get, fetch_transcript=lambda v: "x") == []      # nichts doppelt


def test_youtube_retries_missing_transcript(monkeypatch, tmp_path):
    from tradingbot import youtube
    monkeypatch.chdir(tmp_path)
    now = pd.Timestamp.now(tz="UTC").isoformat()
    feed = f"""<feed xmlns="http://www.w3.org/2005/Atom" xmlns:yt="http://www.youtube.com/xml/schemas/2015">
      <entry><yt:videoId>v1</yt:videoId><title>Test</title><published>{now}</published></entry></feed>"""
    get = lambda url: '"channelId":"UCabcdefghijklmnopqrstuv"' if "/@" in url else feed
    [f] = youtube.update(["k"], get=get, fetch_transcript=lambda v: None)
    youtube.update(["k"], get=get, fetch_transcript=lambda v: "Jetzt mit Text")
    assert "Jetzt mit Text" in Path(f).read_text() and "Keine Abschrift" not in Path(f).read_text()


# --- Zeithorizonte: jeder Bot handelt kurz, mittel und lang auf einem Konto

def _horizon_trader():
    from tradingbot.config import Horizon
    t = Trader(PaperBroker(1000, 0, 0), RiskManager(RiskConfig(max_total_risk_pct=1, risk_per_trade=0.01), 1000),
               allow_short=True)
    t.horizons = {"kurz": Horizon("kurz", "1h", "trend", stop_loss_atr=1.0, take_profit_atr=2.0),
                  "lang": Horizon("lang", "1d", "regime", stop_loss_atr=8.0, take_profit_atr=20.0)}
    return t


def test_position_belongs_to_its_horizon():
    t = _horizon_trader()
    t.on_signal("X", 1, 100, atr=5, equity=1000, when=0, horizon="lang")
    assert t.open_trades["X"].horizon == "lang" and t.open_trades["X"].stop == pytest.approx(60)   # 8 × ATR
    t.on_signal("X", -1, 100, atr=5, equity=1000, when=1, horizon="kurz")     # fremder Horizont: bleibt offen
    assert "X" in t.open_trades and "lang" in t.note
    t.on_signal("X", -1, 100, atr=5, equity=1000, when=2, horizon="lang")     # eigener Horizont: schliessen, short
    assert t.closed[-1]["horizon"] == "lang" and t.open_trades["X"].side == -1


def test_each_horizon_can_short_with_own_stops():
    t = _horizon_trader()
    t.on_signal("X", -1, 100, atr=5, equity=1000, when=0, horizon="kurz")
    tr = t.open_trades["X"]
    assert tr.side == -1 and tr.stop == pytest.approx(105) and tr.target == pytest.approx(90)


def test_adaptive_shares_follow_winning_horizon():
    from tradingbot.engine import MIN_SHARE, MAX_SHARE, WEAK
    t = _horizon_trader()
    assert t.shares() == {"kurz": 0.5, "lang": 0.5}
    t.adaptive_shares = True
    t.closed = [{"pnl": 30.0, "horizon": "kurz"}] * 5 + [{"pnl": -20.0, "horizon": "lang"}] * 5
    w = t.shares()
    assert w["kurz"] > w["lang"] and sum(w.values()) == pytest.approx(1)
    assert MIN_SHARE - 1e-9 <= w["lang"] and w["kurz"] <= MAX_SHARE + 1e-9
    # ein Horizont, der klar verliert, wird praktisch abgeschaltet (5 % seines Startanteils), aber nicht ganz
    t.closed = [{"pnl": -20.0, "horizon": "lang"}] * 20
    w = t.shares()
    assert 0 < w["lang"] <= 0.5 * WEAK / (0.5 + 0.5 * WEAK) + 1e-9


def test_budget_share_limits_one_horizon():
    rm = RiskManager(RiskConfig(max_invested_pct=0.5, max_position_pct=1, risk_per_trade=1), 1000)
    assert rm.plan(1000, 1000, 100, 1, budget_share=0.5, exposure=0).qty == pytest.approx(2.5)    # 250 CHF
    assert rm.plan(1000, 1000, 100, 1, budget_share=0.5, exposure=250) is None


def test_bot_configs_trade_all_horizons_with_simulation_settings():
    for name in ("langfrist", "daytrading", "risiko"):
        cfg = Config.load(f"bots/config_{name}.yaml")
        # Risiko-Bot: «kurz» seit 29.10.2026 pausiert (verlor im Demo-Betrieb 64 % in 6 Tagen)
        assert {h.name for h in cfg.horizon_list()} == ({"mittel", "lang"} if name == "risiko" else {"kurz", "mittel", "lang"})
        assert all(h.trend_filter for h in cfg.horizon_list()) and cfg.horizon_priority
        assert cfg.short_probation                         # Shorts jederzeit einschaltbar, dann mit Probezeit
        assert cfg.strategy == cfg.horizon_list()[0].strategy
    assert Config.load("bots/config_langfrist.yaml").horizon_list()[0].name == "lang"
    assert Config.load("bots/config_daytrading.yaml").risk.halt_days > 0     # KI stoppt nicht für immer


def test_paper_loop_with_horizons(df, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: MultiExchange(df))
    cfg = Config(poll_seconds=0, symbols=["BTC/CHF", "ETH/CHF", "SOL/CHF"], use_news=False, name="hz",
                 allow_short=True, adaptive_shares=True,
                 horizons={"kurz": {"timeframe": "1h", "strategy": "breakout",
                                    "strategy_params": {"entry": 10, "exit": 5}},
                           "lang": {"timeframe": "1d", "strategy": "trend", "stop_loss_atr": 4.0}},
                 risk=RiskConfig(loss_streak_pause=99, max_total_risk_pct=1, max_open_positions=6,
                                 max_daily_loss_pct=1, max_trades_per_day=999))
    bot.run(cfg, max_iterations=300)
    trades = pd.read_csv(tmp_path / "daten" / "logs" / "trades_hz.csv")
    assert set(trades["horizon"]) == {"kurz", "lang"} and "short" in set(trades["side"])


def test_history_simulation_runs_whole_bots(df):
    from tradingbot.historie import simulate, simulate_chef, report, resample
    idx = pd.date_range("2020-01-01", periods=len(df), freq="1h", tz="UTC")
    btc = df.set_axis(idx)
    coins = {"BTC/USD": btc, "ETH/USD": btc.iloc[500:] * 0.05}          # ETH kommt später dazu
    runs = {}
    for name in ("config_langfrist", "config_daytrading", "config_risiko"):
        cfg = Config.load(f"bots/{name}.yaml")
        cfg.risk.max_drawdown_pct = 0.99
        for h in cfg.horizons.values():          # 62 Tage Testkurse: zu kurz für die 200-Tage-Linie
            h.update(trend_filter=False, min_edge=0)
        runs[name] = simulate(cfg, coins)
        assert len(runs[name].equity) > 50 and runs[name].equity.iloc[0] == pytest.approx(cfg.starting_capital, rel=0.05)
    assert {"kurz", "mittel"} <= set(runs["config_daytrading"].trades["horizon"])
    assert set(runs["config_risiko"].trades["horizon"]) <= {"mittel", "lang"}       # kurz pausiert
    chef = simulate_chef(runs, resample(btc, "1d"), Path(pytest.importorskip("tempfile").mkdtemp()) / "chef.json")
    assert len(chef) > 50
    text = report(runs, chef, resample(btc, "1d")["close"])
    assert "Jahr für Jahr" in text and "Nach Zeithorizont" in text and "Chef-Bot" in text


# --- Teilgewinn, Nachlauf-Stop, Trendfilter, Gebührenfilter

def _tool_trader(**h):
    from tradingbot.config import Horizon
    t = Trader(PaperBroker(10_000, 0.001, 0), RiskManager(RiskConfig(max_total_risk_pct=1, max_position_pct=1), 10_000),
               allow_short=True)
    t.horizons = {"kurz": Horizon("kurz", "1h", "trend", stop_loss_atr=2.0, take_profit_atr=10.0, **h)}
    return t


def test_trade_result_includes_buy_fee():
    t = _tool_trader()
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    t.exit("X", 100, "Signal", 1)
    assert t.closed[-1]["pnl"] < 0 and t.equity({}) == pytest.approx(10_000 + t.closed[-1]["pnl"])


def test_partial_profit_moves_stop_to_breakeven_and_counts_as_win():
    t = _tool_trader(partial_atr=1.0, partial_pct=0.5)
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    qty = t.open_trades["X"].qty
    t.check_stops("X", 100, 101.5, 99.5, 1)                    # Zwischenziel 101 erreicht
    tr = t.open_trades["X"]
    assert tr.qty == pytest.approx(qty / 2) and tr.stop > 100     # Rest mit Stop über dem Einstand
    t.check_stops("X", 100.5, 100.6, 99, 2)                     # Kurs fällt zurück: Rest ohne Verlust raus
    c = t.closed[-1]
    assert c["reason"] == "Stop auf Einstand" and c["pnl"] > 0 and c["qty"] == pytest.approx(qty) and c["partial"]
    assert t.equity({}) == pytest.approx(10_000 + c["pnl"])


def test_trailing_stop_follows_best_price_next_bar_only():
    t = _tool_trader(trail_atr=2.0)
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    t.check_stops("X", 100, 106, 99, 1)                        # bestes Hoch 106 -> Stop 104 ab nächster Kerze
    assert t.open_trades["X"].stop == pytest.approx(104)
    t.check_stops("X", 105, 105.5, 103, 2)
    assert t.closed[-1]["reason"] == "Nachlauf-Stop" and t.closed[-1]["exit"] == pytest.approx(104)
    s = _tool_trader(trail_atr=2.0)                              # Short spiegelbildlich
    s.on_signal("X", -1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    s.check_stops("X", 100, 101, 95, 1)
    assert s.open_trades["X"].stop == pytest.approx(97)


def test_trend_filter_blocks_entries_against_trend_but_allows_exits():
    t = _tool_trader()
    t.on_signal("X", -1, 100, atr=1, equity=10_000, when=0, horizon="kurz", trend=1)
    assert not t.open_trades and "Trend" in t.note                # kein Short im Aufwärtstrend
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=1, horizon="kurz", trend=1)
    t.on_signal("X", -1, 100, atr=1, equity=10_000, when=2, horizon="kurz", trend=1)
    assert not t.open_trades and t.closed[-1]["reason"] == "Signal"   # Long geschlossen, aber kein neuer Short
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=3, horizon="kurz", trend=0)
    assert not t.open_trades                                      # unbekannter Trend: kein Einstieg


def test_trend_direction_needs_200_days():
    from tradingbot.strategies import trend_direction
    idx = pd.date_range("2020-01-01", periods=400, freq="1D", tz="UTC")
    up = pd.DataFrame({"open": range(1, 401), "high": range(2, 402), "low": range(0, 400), "close": range(1, 401),
                       "volume": 1.0}, index=idx, dtype=float)
    d = trend_direction(up)
    assert d.iloc[150] == 0 and d.iloc[-1] == 1


def test_min_edge_skips_moves_too_small_for_fees():
    t = _tool_trader(partial_atr=1.0, min_edge=3.0)               # Kosten 0,2 %: erstes Ziel braucht 0,6 %
    t.on_signal("X", 1, 100, atr=0.5, equity=10_000, when=0, horizon="kurz")
    assert not t.open_trades and "Gebühren" in t.note
    t.on_signal("X", 1, 100, atr=1.0, equity=10_000, when=1, horizon="kurz")
    assert "X" in t.open_trades


def test_interest_is_part_of_the_trade_result():
    t = _tool_trader()
    t.on_signal("X", -1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    t.charge_interest({"X": 100}, 24 * 10, 0.0012)               # 10 Tage Leihzinsen für den Short
    t.exit("X", 100, "Signal", 1)
    c = t.closed[-1]
    assert c["pnl"] < -t.broker.interest_paid + 1e-9 and t.equity({}) == pytest.approx(10_000 + c["pnl"])


def test_longer_horizon_takes_over_or_turns_position():
    from tradingbot.config import Horizon
    t = _tool_trader()
    t.horizons["lang"] = Horizon("lang", "1d", "regime", stop_loss_atr=8.0, take_profit_atr=1000)
    t.priority = True
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    t.on_signal("X", 1, 100, atr=2, equity=10_000, when=1, horizon="lang")     # gleiche Richtung: übernehmen
    assert t.open_trades["X"].horizon == "lang" and t.open_trades["X"].stop == pytest.approx(84) and not t.closed
    t.on_signal("X", -1, 100, atr=1, equity=10_000, when=2, horizon="kurz")    # kürzerer Horizont: kein Zugriff
    assert t.open_trades["X"].horizon == "lang"
    t.horizons["kurz"].stop_loss_atr = 2.0
    t.exit("X", 100, "Signal", 3)
    t.on_signal("X", -1, 100, atr=1, equity=10_000, when=4, horizon="kurz")
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=5, horizon="lang")     # Gegenrichtung: drehen
    assert t.closed[-1]["reason"] == "Vorrang lang" and t.open_trades["X"].side == 1


def test_short_probation_keeps_shorts_small_until_proven():
    t = _tool_trader()
    t.short_probation = True
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    full = t.open_trades["X"].qty
    t.exit("X", 100, "Signal", 1)
    t.on_signal("X", -1, 100, atr=1, equity=10_000, when=2, horizon="kurz")
    assert t.open_trades["X"].qty == pytest.approx(full * 0.25, rel=0.01)     # Probezeit: Viertel
    t.exit("X", 100, "Signal", 3)
    t.closed += [{"side": "short", "pnl": 5.0}] * 10                           # Shorts haben sich bewährt
    t.on_signal("X", -1, 100, atr=1, equity=t.equity({}), when=4, horizon="kurz")
    assert t.open_trades["X"].qty == pytest.approx(full, rel=0.02)


def test_short_can_be_switched_per_horizon():
    t = _tool_trader(allow_short=False)
    t.on_signal("X", -1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    assert not t.open_trades


def test_history_simulation_can_start_later(df):
    from tradingbot.historie import simulate
    btc = df.set_axis(pd.date_range("2020-01-01", periods=len(df), freq="1h", tz="UTC"))
    cfg = Config(strategy="trend", symbols=["BTC/USD"], name="spaet")
    start = btc.index[800]
    run = simulate(cfg, {"BTC/USD": btc}, start=start)
    assert run.equity.index[0] >= start.normalize() and run.equity.iloc[0] == pytest.approx(cfg.starting_capital, rel=0.02)
    assert len(run.trades) == 0 or (pd.to_datetime(run.trades["opened"], utc=True) >= start).all()


# --- Marktphase je Coin: Horizont wählen, bester Einstieg, Ausstieg wenn die Phase kippt

def test_coin_phases_follow_200_day_line_without_lookahead():
    from tradingbot.phase import coin_phases
    idx = pd.date_range("2018-01-01", periods=500, freq="1D", tz="UTC")
    up = pd.Series(range(100, 600), index=idx, dtype=float)
    daily = pd.DataFrame({"open": up, "high": up * 1.01, "low": up * 0.99, "close": up, "volume": 1.0})
    ph = coin_phases(daily)
    assert ph.iloc[100].startswith("Seitwärts") and ph.iloc[-1].startswith("Aufwärtstrend")
    pd.testing.assert_series_equal(ph.iloc[:300], coin_phases(daily.iloc[:300]))
    down = daily.iloc[::-1].set_axis(idx)
    assert coin_phases(down).iloc[-1].startswith("Abwärtstrend")


def test_phase_gate_trades_full_only_where_horizon_has_proven_itself():
    from tradingbot.phase import PhaseBook
    t = _tool_trader()
    t.phase_book = PhaseBook(probation=0.25, loser=0.05)
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="kurz", phase="Aufwärtstrend, ruhig")
    small = t.open_trades["X"].qty
    assert "Probezeit" in t.note and t.open_trades["X"].context["phase"] == "Aufwärtstrend, ruhig"
    t.exit("X", 100, "Signal", 1)
    win = {"phase": "Aufwärtstrend, ruhig", "horizon": "kurz", "entry": 100, "qty": 1, "pnl": 2.0}
    t.closed += [win] * 8
    t.on_signal("X", 1, 100, atr=1, equity=t.equity({}), when=2, horizon="kurz")
    assert t.open_trades["X"].qty == pytest.approx(small * 4, rel=0.02) and "voll" in t.note
    t.exit("X", 100, "Signal", 3)
    t.closed += [dict(win, pnl=-5.0)] * 8                                   # jetzt verliert der Horizont dort
    t.on_signal("X", 1, 100, atr=1, equity=t.equity({}), when=4, horizon="kurz")
    assert t.open_trades["X"].qty == pytest.approx(small * 4 * 0.05, rel=0.02) and "verliert" in t.note


def test_phase_prior_counts_like_at_most_20_own_trades():
    from tradingbot.phase import PhaseBook
    book = PhaseBook({"Seitwärts, wild|kurz": [-10.0, 1000]})            # Geschichte: verliert (-1 % pro Trade)
    assert book.factor([], "Seitwärts, wild", "kurz")[0] == book.loser
    own = [{"phase": "Seitwärts, wild", "horizon": "kurz", "entry": 1, "qty": 100, "pnl": 3.0}] * 30   # +3 %
    assert book.factor(own, "Seitwärts, wild", "kurz")[0] == 1.0       # eigene neue Erfahrung setzt sich durch


def test_waits_for_pullback_and_exits_when_phase_turns():
    t = _tool_trader(max_stretch_atr=1.0)
    t.phase_exit = True
    t.on_signal("X", 1, 105, atr=2, equity=10_000, when=0, horizon="kurz", anchor=100)    # 2,5 ATR darüber
    assert not t.open_trades and "Rücksetzer" in t.note
    t.on_signal("X", 1, 101, atr=2, equity=10_000, when=1, horizon="kurz", anchor=100)
    assert "X" in t.open_trades
    t.check_phase("X", "Seitwärts, ruhig", 101, 2)
    assert "X" in t.open_trades
    t.check_phase("X", "Abwärtstrend, wild", 99, 3)
    assert not t.open_trades and t.closed[-1]["reason"] == "Phase gekippt"
    t.on_signal("X", 1, 99, atr=2, equity=t.equity({}), when=4, horizon="kurz", anchor=100)
    assert not t.open_trades and "Marktphase" in t.note


def test_phasen_bot_in_history_simulation(df, tmp_path):
    from tradingbot.historie import simulate, report, resample
    btc = df.set_axis(pd.date_range("2020-01-01", periods=len(df), freq="1h", tz="UTC"))
    cfg = Config.load("bots/config_phasen.yaml")
    cfg.risk.max_drawdown_pct = 0.99
    for h in cfg.horizons.values():
        h.update(trend_filter=False, min_edge=0)
    run = simulate(cfg, {"BTC/USD": btc})
    assert len(run.equity) > 50
    if len(run.trades):
        assert "phase" in run.trades
        assert "Nach Marktphase" in report({"p": run}, None, resample(btc, "1d")["close"])


def test_paper_loop_with_phase_gate(df, monkeypatch, tmp_path):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: MultiExchange(df))
    cfg = Config(poll_seconds=0, symbols=["BTC/CHF", "ETH/CHF"], use_news=False, name="ph",
                 phase_gate=True, phase_exit=True, phase_prior="fehlt.json",
                 horizons={"kurz": {"timeframe": "1h", "strategy": "trend", "max_stretch_atr": 2.0}},
                 risk=RiskConfig(loss_streak_pause=99, max_total_risk_pct=1, max_daily_loss_pct=1,
                                 max_trades_per_day=999))
    bot.run(cfg, max_iterations=200)
    trades = pd.read_csv(tmp_path / "daten" / "logs" / "trades_ph.csv")
    assert "phase" in trades and trades["phase"].notna().any()     # ohne Tageskerzen: ohne Phase


def test_phase_exit_can_be_switched_off_per_horizon():
    from tradingbot.config import Horizon
    t = _tool_trader()
    t.horizons["lang"] = Horizon("lang", "1d", "regime", stop_loss_atr=8.0, phase_exit=False)
    t.phase_exit = True
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="lang")
    t.check_phase("X", "Abwärtstrend, wild", 99, 1)
    assert "X" in t.open_trades


def test_close_positions_by_hand(df, monkeypatch, tmp_path):
    import json
    from tradingbot import state
    from tradingbot.__main__ import schliessen
    monkeypatch.chdir(tmp_path)
    ex = MultiExchange(df)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: ex)
    cfg = Config(symbols=["BTC/CHF", "ETH/CHF"], use_news=False, name="hand", allow_short=True,
                 risk=RiskConfig(max_total_risk_pct=1))
    t = bot.make_trader(cfg, None)
    price = ex.fetch_ticker("ETH/CHF")["last"]
    t.on_signal("ETH/CHF", -1, price, atr=price * 0.02, equity=1000.0, when=0)        # ein alter Short
    assert t.open_trades["ETH/CHF"].side == -1
    state.save(cfg.state_path, t, {"ETH/CHF": pd.Timestamp("2026-01-01", tz="UTC")})
    schliessen(cfg, ["ETH/CHF", "DOGE/CHF"])
    after = json.loads(cfg.state_path.read_text())
    assert "ETH/CHF" not in after["open_trades"] and after["closed"][-1]["reason"] == "Von Hand geschlossen"
    assert after["paper"]["positions"]["ETH/CHF"] == pytest.approx(0.0, abs=1e-12)
    assert "Von Hand geschlossen" in set(pd.read_csv(tmp_path / "daten" / "logs" / "trades_hand.csv")["reason"])


# --- Kapital nach Ausstieg, Hebel-Grenze über alle Horizonte, Korrelations-Sperre

class ConstStrategy:
    """Strategie mit immer demselben Signal, für Tests des Paper-Loops."""
    def __init__(self, sig):
        self.sig = sig

    def signals(self, frame):
        return pd.Series(self.sig, index=frame.index)


def test_turning_a_position_keeps_the_true_capital():
    """Dreht der längere Horizont eine Position, zählt danach das ganze Kapital (alle Coins), nicht nur Cash plus
    diesen Coin: sonst sperrt ein falsches «Tagesverlust-Limit» den Einstieg (Langfrist-Bot 28.10.)."""
    from tradingbot.config import Horizon
    rc = RiskConfig(risk_per_trade=0.05, max_position_pct=0.2, max_total_risk_pct=1, max_open_positions=8,
                    max_daily_loss_pct=0.15, max_trades_per_day=99)
    t = Trader(PaperBroker(1000, 0.0026, 0.0005), RiskManager(rc, 1000), allow_short=True)
    t.horizons = {"kurz": Horizon("kurz", "1h", "trend", share=0.1, stop_loss_atr=2.0),
                  "lang": Horizon("lang", "1d", "regime", share=0.9, stop_loss_atr=2.0)}
    t.priority = True
    px = {"A": 100.0, "B": 50.0, "C": 20.0, "D": 10.0}
    for s in "ABC":                                                 # drei Longs in anderen Coins
        t.on_signal(s, 1, px[s], atr=px[s] * 0.05, equity=t.equity(px), when=0, horizon="lang")
    t.on_signal("D", -1, px["D"], atr=0.5, equity=t.equity(px), when=0, horizon="kurz")
    assert len(t.open_trades) == 4 and t.broker.cash() < 500
    t.on_signal("D", 1, px["D"], atr=0.2, equity=t.equity(px), when=1, horizon="lang")     # «lang» dreht D
    assert t.closed[-1]["reason"] == "Vorrang lang" and "Tagesverlust" not in t.note
    d = t.open_trades["D"]
    true_equity = t.equity(px) + d.fee + d.qty * (d.entry - px["D"])     # Kapital vor dem neuen Kauf
    assert d.side == 1 and d.qty * px["D"] == pytest.approx(0.2 * true_equity)    # 20 % vom wahren Kapital


def test_leverage_after_turn_stays_within_limits():
    """Hebel 3 mit Shorts: das Cash enthält die Erlöse der Shorts. Nach dem Drehen einer Position darf es nicht als
    Kapital gelten, und alle Positionen zusammen bleiben unter Kapital × max_invested_pct × Hebel, auch wenn ein
    Horizont noch mehr hält, als sein Anteil heute erlaubt (Risiko-Bot 25.10.: Positionen von 8,7× Hebel)."""
    from tradingbot.config import Horizon
    rc = RiskConfig(leverage=3.0, risk_per_trade=0.05, max_position_pct=0.5, max_invested_pct=1.0,
                    max_total_risk_pct=1, max_open_positions=8, max_daily_loss_pct=0.5, max_trades_per_day=99)
    b = PaperBroker(1000, 0.0026, 0.0005)
    b.leverage = 3.0
    t = Trader(b, RiskManager(rc, 1000), allow_short=True)
    t.horizons = {"kurz": Horizon("kurz", "1h", "trend", share=1.0, stop_loss_atr=2.0),
                  "lang": Horizon("lang", "1d", "regime", share=0.0, stop_loss_atr=2.0)}
    t.priority = True
    px = {"A": 100.0, "B": 50.0, "C": 20.0}
    t.on_signal("A", -1, px["A"], atr=2.5, equity=t.equity(px), when=0, horizon="kurz")     # Short, ca. 1'000 CHF
    t.on_signal("B", -1, px["B"], atr=1.25, equity=t.equity(px), when=0, horizon="kurz")    # Short, ca. 1'000 CHF
    t.on_signal("C", 1, px["C"], atr=1.0, equity=t.equity(px), when=0, horizon="kurz")      # Long, ca. 500 CHF
    assert [tr.side for tr in t.open_trades.values()] == [-1, -1, 1] and b.cash() > 2000
    t.horizons["lang"].share = 1.0                  # Anteile verschoben: «kurz» hält mehr als seine Hälfte
    eq = t.equity(px)
    t.on_signal("C", -1, px["C"], atr=0.1, equity=eq, when=1, horizon="lang")              # «lang» dreht C
    assert t.closed[-1]["symbol"] == "C" and t.open_trades["C"].side == -1
    assert t.open_trades["C"].qty * px["C"] <= rc.max_position_pct * 3 * eq
    assert sum(tr.qty * px[s] for s, tr in t.open_trades.items()) <= eq * rc.max_invested_pct * 3


def test_correlation_sees_positions_of_later_coins(df, monkeypatch, tmp_path):
    """Korrelations-Sperre: Eine offene Position in einem Coin, der in der Liste später kommt, zählt auch."""
    import json
    from tradingbot import state
    monkeypatch.chdir(tmp_path)
    ex = MultiExchange(df)                                   # BTC und ETH: gleiche Kurse, nur anders skaliert
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: ex)
    monkeypatch.setattr(bot, "build", lambda *a, **k: ConstStrategy(1))
    factors, real = {}, bot._correlation_factor
    monkeypatch.setattr(bot, "_correlation_factor", lambda s, *a: factors.setdefault(s, real(s, *a)))
    cfg = Config(symbols=["BTC/CHF", "ETH/CHF"], use_news=False, name="korr", poll_seconds=0,
                 risk=RiskConfig(max_total_risk_pct=1))
    t = bot.make_trader(cfg, ex)
    price = ex.fetch_ticker("ETH/CHF")["last"]
    t.on_signal("ETH/CHF", 1, price, atr=price * 0.02, equity=1000.0, when=0)     # ETH long schon offen
    state.save(cfg.state_path, t, {})
    bot.run(cfg, max_iterations=1)
    assert factors["BTC/CHF"] == 0.5 and "BTC/CHF" in json.loads(cfg.state_path.read_text())["open_trades"]


def test_total_cap_over_all_horizons():
    """Alle Horizonte zusammen nie über Kapital × max_invested_pct × Hebel, auch wenn der Anteil des Horizonts
    noch Platz hätte."""
    from tradingbot.config import Horizon
    rm = RiskManager(RiskConfig(leverage=3.0, max_position_pct=1.0, risk_per_trade=1.0), 1000)
    short = dict(side=-1, exposure=0, budget_share=0.5)                   # Anteil des Horizonts: 1'500 CHF
    assert rm.plan(1000, 1000, 100, 1, **short).qty == pytest.approx(15)
    assert rm.plan(1000, 1000, 100, 1, **short, exposure_total=2900).qty == pytest.approx(1)    # alle: 3'000
    assert rm.plan(1000, 1000, 100, 1, **short, exposure_total=3000) is None
    assert rm.last_block == "Obergrenze für investiertes Kapital erreicht"
    # Übernahme durch den längeren Horizont: nach Verlusten passt nicht mehr die ganze Position unter die Grenze
    rc = RiskConfig(max_position_pct=0.5, risk_per_trade=0.5, max_total_risk_pct=1, max_open_positions=8)
    t = Trader(PaperBroker(1000, 0, 0), RiskManager(rc, 1000))
    t.horizons = {"kurz": Horizon("kurz", "1h", "trend", share=1.0), "lang": Horizon("lang", "1d", "regime", share=0.0)}
    t.priority = True
    t.on_signal("A", 1, 100, atr=1, equity=1000, when=0, horizon="kurz")             # 500 CHF
    t.on_signal("X", 1, 10, atr=0.1, equity=t.equity({"A": 100}), when=0, horizon="kurz")  # 495 CHF (Cash-Reserve)
    t.horizons["lang"].share = 1.0
    px = {"A": 80.0, "X": 10.0}                                                     # A verliert: Kapital 900
    t.on_signal("X", 1, 10, atr=0.1, equity=t.equity(px), when=1, horizon="lang")
    assert t.open_trades["X"].horizon == "lang"
    assert t.open_trades["X"].qty * 10 == pytest.approx(t.equity(px) - 500)          # 900 - 500 (A zum Einstieg)


def test_liquidation_checked_again_after_signals(df, monkeypatch, tmp_path):
    """Braucht eine neue Position schon beim Einstieg mehr Sicherheit als vorhanden, wird sie im selben Lauf
    zwangsweise geschlossen, nicht erst 30 Minuten später (hier mit knapp eingestellter Sicherheit)."""
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: MultiExchange(df))
    monkeypatch.setattr(bot, "build", lambda *a, **k: ConstStrategy(-1))
    cfg = Config(symbols=["BTC/CHF"], use_news=False, name="liq", poll_seconds=0, allow_short=True,
                 risk=RiskConfig(leverage=3.0, max_position_pct=1.0, risk_per_trade=1.0, max_total_risk_pct=1,
                                 liquidation_margin=1.0))
    bot.run(cfg, max_iterations=1)
    assert list(pd.read_csv(tmp_path / "daten" / "logs" / "trades_liq.csv")["reason"]) == ["Liquidation"]


def test_dashboard_shows_current_leverage():
    from tradingbot import dashboard
    def bot_(cfg, invested):
        return dashboard.Bot(cfg, Trader(PaperBroker(1000, 0, 0), RiskManager(cfg.risk, 1000)), 1000.0, invested)
    plain, lev = Config(title="Ohne"), Config(title="Mit Hebel", risk=RiskConfig(leverage=3.0))
    rows = dashboard.overview([bot_(plain, 500.0), bot_(lev, 1550.0)])
    assert "| Hebel aktuell | – | 1.55× (erlaubt 3×) |" in rows
    assert not any("Hebel aktuell" in row for row in dashboard.overview([bot_(plain, 500.0)]))


# --- Buchhaltung: Gebühren und Zinsen je Trade, Abgleich mit dem Kapital, einmalige Nachbuchung

class CountingBroker(PaperBroker):
    """PaperBroker, der alle verlangten Gebühren zusammenzählt."""
    charged = 0.0

    def buy(self, symbol, qty, price, **kw):
        fill = super().buy(symbol, qty, price, **kw)
        self.charged += fill.fee if fill else 0.0
        return fill

    def sell(self, symbol, qty, price, short=False, **kw):
        fill = super().sell(symbol, qty, price, short, **kw)
        self.charged += fill.fee if fill else 0.0
        return fill


def test_bookkeeping_reconciles_at_every_step():
    """Zufällige Trades mit Hebel 3, Shorts, Teilgewinnen, Übernahmen, Zinsen und Zwangsschliessung, mit
    Kraken-Gebührenstaffel, Geld-/Briefkurs und Margin-Gebühren: nach jedem Schritt ist Kapital = Start + alle
    Ergebnisse (offene zum aktuellen Kurs), und die Gebühren der Trades sind genau die, die der Broker verlangt hat."""
    import random
    from tradingbot.broker import KRAKEN_TIERS
    from tradingbot.config import Horizon
    rng = random.Random(3)
    # knapp eingestellte Sicherheit (liquidation_margin), damit auch Zwangsschliessungen vorkommen
    rc = RiskConfig(leverage=3.0, risk_per_trade=0.05, max_position_pct=0.5, max_total_risk_pct=1, max_open_positions=8,
                    max_daily_loss_pct=1, max_trades_per_day=10_000, loss_streak_pause=10_000, liquidation_margin=0.97)
    b = CountingBroker(1000, 0.0026, 0.0005, tiers=KRAKEN_TIERS)
    b.leverage, b.extra_fee = 3.0, {"C": 0.0026}
    t0, stufen = datetime(2026, 1, 1, tzinfo=timezone.utc), set()
    t = Trader(b, RiskManager(rc, 1000), allow_short=True)
    t.horizons = {"kurz": Horizon("kurz", "1h", "trend", stop_loss_atr=1.5, take_profit_atr=4.0, partial_atr=0.75),
                  "lang": Horizon("lang", "1d", "regime", stop_loss_atr=3.0, take_profit_atr=8.0, partial_atr=1.5)}
    t.priority = True
    px = {"A": 100.0, "B": 20.0, "C": 5.0}
    for step in range(600):
        s = rng.choice(list(px))
        old, px[s] = px[s], px[s] * (1 + rng.gauss(0, 0.015))
        high, low = max(old, px[s]) * (1 + rng.random() / 100), min(old, px[s]) * (1 - rng.random() / 100)
        b.now, b.quotes = t0 + timedelta(hours=4 * step), {k: (p * 0.9996, p * 1.0004) for k, p in px.items()}
        stufen.add(b.tier()[0])
        t.check_stops(s, old, high, low, step)
        if rng.random() < 0.5:
            t.on_signal(s, rng.choice((1, -1)), px[s], atr=px[s] / 100, equity=t.equity(px), when=step,
                        horizon=rng.choice(("kurz", "lang")))
        t.charge_interest(px, 4, 0.0012)
        if bot.liquidation(t, px, rc):
            t.close_all(px, "Liquidation", step)
        assert abs(t.abgleich(px, 1000)["differenz"]) < 0.01
    reasons = {c["reason"] for c in t.closed}
    assert len(t.closed) >= 50 and {c["side"] for c in t.closed} == {"long", "short"} and len(stufen) >= 2
    assert {"Vorrang lang", "Liquidation", "Stop auf Einstand"} <= reasons
    assert any(c["partial"] for c in t.closed) and all("fees" in c and "interest" in c for c in t.closed)
    assert t.gebuehren_bisher() == pytest.approx(b.charged)
    assert (sum(c["interest"] for c in t.closed) + sum(o.interest for o in t.open_trades.values())
            == pytest.approx(b.interest_paid))
    assert all(c["pnl"] == pytest.approx(c["qty"] * (c["exit"] - c["entry"]) * (1 if c["side"] == "long" else -1)
                                         - c["fees"] - c["interest"]) for c in t.closed)


def _old_style_trader():
    """Stand wie vor dem 28.10.2026: Ergebnisse ohne Kaufgebühr, eine offene Position ohne Kaufgebühr und Zinsen,
    die keinem Trade gehören. Gibt den Trader, die richtigen Kaufgebühren und die Zinsen zurück."""
    t0 = datetime(2026, 10, 25, 12, tzinfo=timezone.utc)
    b = PaperBroker(1000, 0.0026, 0.0005)
    b.extra_fee = {"SOL/CHF": 0.0026, "XRP/CHF": 0.0026}          # über USD umgerechnet: 0,52 % pro Order
    t = Trader(b, RiskManager(RiskConfig(max_total_risk_pct=1, max_position_pct=0.3, max_open_positions=8,
                                         margin_open_fee=0.0), 1000), allow_short=True)    # alter Code: ohne
    fees = []
    for i, (s, side, entry, exit_) in enumerate([("BTC/CHF", 1, 60_000, 61_000), ("SOL/CHF", -1, 80, 78),
                                                  ("ETH/CHF", 1, 2000, 1900)]):
        t.on_signal(s, side, entry, atr=entry * 0.02, equity=t.equity({}), when=t0 + timedelta(hours=i))
        fees.append(t.open_trades[s].fee)
        t.open_trades[s].fee = 0.0                                 # alter Code: Kaufgebühr nicht beim Trade gemerkt
        if side < 0:                                               # alter Code: Zinsen keinem Trade zugeordnet
            b.book_interest(t.open_trades[s].qty * entry * 0.0012 * 2)     # 2 Tage auf den geliehenen Short
        t.exit(s, exit_, "Signal", t0 + timedelta(hours=i, minutes=30))
        del t.closed[-1]["fees"], t.closed[-1]["interest"]
    t.on_signal("XRP/CHF", 1, 2.0, atr=0.04, equity=t.equity({}), when=t0 + timedelta(hours=5))
    fees.append(t.open_trades["XRP/CHF"].fee)
    t.open_trades["XRP/CHF"].fee = 0.0
    return t, fees, b.interest_paid


def test_nachbuchung_fixes_old_trades_once(tmp_path):
    """Nach der Nachbuchung enthält jedes Ergebnis die Kaufgebühr (alter Wert in pnl_alt), die offene Position hat
    ihre Kaufgebühr, die alten Zinsen sind Altlasten, die Buchhaltung stimmt und das Archiv hat den alten Stand.
    Ein zweiter Lauf ändert nichts."""
    from tradingbot import buchhaltung, state
    old, fees, interest = _old_style_trader()
    path = tmp_path / "daten" / "state" / "paper_alt.json"
    state.save(path, old, {})
    original = path.read_text()
    t = Trader(PaperBroker(1000, 0.0026, 0.0005), RiskManager(RiskConfig(), 1000))
    state.load(path, t)
    assert interest > 0 and abs(t.abgleich({}, 1000)["differenz"]) > 1          # vorher: Lücke
    pnl_alt = [c["pnl"] for c in t.closed]
    info = buchhaltung.nachbuchen(t, path, 1000)
    assert [c["pnl_alt"] for c in t.closed] == pnl_alt and all(c["nachgebucht"] for c in t.closed)
    assert [c["pnl"] for c in t.closed] == pytest.approx([p - f for p, f in zip(pnl_alt, fees)])
    assert all(c["interest"] == pytest.approx(0) for c in t.closed)
    assert t.open_trades["XRP/CHF"].fee == pytest.approx(fees[-1])
    assert info["trades_korrigiert"] == 3 and info["positionen_korrigiert"] == 1
    assert info["summe_korrektur"] == pytest.approx(-sum(fees), abs=0.01)
    assert t.altlasten == pytest.approx(interest) and info["zinsen_ohne_zuordnung"] == pytest.approx(interest, abs=0.01)
    assert info["rest"] == pytest.approx(0)
    assert abs(t.abgleich({"XRP/CHF": 2.5}, 1000)["differenz"]) < 0.005
    assert t.note.startswith("Buchhaltung nachgebucht: 3 Trades und 1 offene Position um die Kaufgebühr korrigiert")
    assert "(−" in t.note and "Zinsen ohne Trade-Zuordnung" in t.note
    archiv = path.parent / "archiv" / f"paper_alt_vor_nachbuchung_{datetime.now(timezone.utc):%Y-%m-%d}.json"
    assert archiv.read_text() == original
    state.save(path, t, {})                                         # gespeichert und neu geladen
    again = Trader(PaperBroker(1000, 0.0026, 0.0005), RiskManager(RiskConfig(), 1000))
    state.load(path, again)
    assert again.altlasten == pytest.approx(interest) and again.buchhaltung["trades_korrigiert"] == 3
    assert buchhaltung.nachbuchen(again, path, 1000) is None        # zweiter Lauf: nichts zu tun
    assert [c["pnl"] for c in again.closed] == pytest.approx([c["pnl"] for c in t.closed])
    assert abs(again.abgleich({}, 1000)["differenz"]) < 0.005


def test_bot_run_books_old_state_and_stores_reconciliation(df, monkeypatch, tmp_path):
    """Der Bot bucht beim Laden einmal nach, prüft bei jedem Lauf die Buchhaltung und speichert das Ergebnis;
    das Trade-Protokoll bekommt die Spalten für Gebühren und Zinsen."""
    import json
    from tradingbot import state
    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: MultiExchange(df))
    cfg = Config(strategy="trend", symbols=["BTC/CHF", "ETH/CHF"], use_news=False, name="alt", poll_seconds=0)
    t = bot.make_trader(cfg, None)
    t.on_signal("ETH/CHF", 1, 100.0, atr=2.0, equity=1000.0, when=datetime(2026, 10, 25, tzinfo=timezone.utc))
    t.open_trades["ETH/CHF"].fee = 0.0
    t.exit("ETH/CHF", 101.0, "Signal", datetime(2026, 10, 26, tzinfo=timezone.utc))
    del t.closed[-1]["fees"], t.closed[-1]["interest"]
    state.save(cfg.state_path, t, {})
    bot.run(cfg, max_iterations=1)
    st = json.loads(cfg.state_path.read_text())
    assert st["buchhaltung"]["trades_korrigiert"] == 1 and "Buchhaltung nachgebucht" in st["note"]
    assert set(st["abgleich"]) == {"kapital", "erwartet", "differenz"} and abs(st["abgleich"]["differenz"]) < 0.01
    assert {"fees", "interest", "pnl_alt", "nachgebucht"} <= set(pd.read_csv(cfg.trades_path).columns)
    assert len(list((tmp_path / "daten" / "state" / "archiv").glob("paper_alt_vor_nachbuchung_*.json"))) == 1


def test_dashboard_and_report_show_fees_and_bookkeeping(capsys):
    from tradingbot import dashboard
    from tradingbot.__main__ import report
    t = Trader(PaperBroker(1000, 0.0026, 0), RiskManager(RiskConfig(max_total_risk_pct=1), 1000))
    t.on_signal("X", 1, 100, atr=2, equity=1000, when=0)
    t.exit("X", 102, "Signal", 1)
    t.altlasten, t.broker._cash = 8.6, t.broker._cash - 8.6           # alte Zinsen ohne Trade
    rows = dashboard.overview([dashboard.Bot(Config(title="A"), t, t.equity({}), 0.0)])
    assert f"| Gebühren bisher | {dashboard.chf(t.closed[-1]['fees'])} CHF |" in rows
    assert "| Buchhaltung | ✅ stimmt (Abweichung 0.00 CHF) · Altlasten vor 28.10.: 8.60 CHF |" in rows
    t.broker._cash -= 12.34                                           # Geld fehlt, das kein Trade erklärt
    rows = dashboard.overview([dashboard.Bot(Config(title="A"), t, t.equity({}), 0.0)])
    assert any(r.startswith("| Buchhaltung | ⚠️ Abweichung -12.34 CHF") for r in rows)
    report(pd.DataFrame([{"pnl": -1.0, "side": "long", "reason": "Signal", "fees": 0.5, "interest": 0.1},
                         {"pnl": 2.0, "side": "short", "reason": "Signal"}]))      # alter Eintrag ohne Gebühren
    assert "Gebühren gesamt: 0.50, Zinsen gesamt: 0.10" in capsys.readouterr().out


# --- Echte Kraken-Kosten: Gebührenstaffel, Kauf zum Brief-/Verkauf zum Geldkurs, Margin-Kosten

def test_kraken_fee_tiers_follow_30_day_volume():
    """Gebühr = Taker-Satz der Stufe, die der Umsatz der letzten 30 Tage in USD vor der Order erreicht hat."""
    from tradingbot.broker import KRAKEN_TIERS
    t0 = datetime(2026, 10, 1, tzinfo=timezone.utc)
    b = PaperBroker(10_000, 0.0026, 0.0, tiers=KRAKEN_TIERS)
    b.now, b.quote_usd = t0, 1.25                                  # CHF-Konto: 1 CHF = 1.25 USD
    b.load_volume([(t0, 1999.2)])                                  # 2'499 USD
    assert b.tier()[0] == 1 and b.fee("SOL/CHF") == 0.008
    b.load_volume([(t0, 2000.0)])                                  # 2'500 USD
    assert b.tier() == (2, 0.003, 0.006, 2000.0) and b.fee("SOL/CHF") == 0.006
    b.quote_usd = 1.0                                              # dieselben 2'000 als USD-Konto: noch Stufe 1
    assert b.tier()[0] == 1
    b.quote_usd = 1.25
    b.load_volume([])
    first = b.buy("BTC/CHF", 1, 2000.0)                            # Umsatz vorher 0: 0,80 %
    b.now = t0 + timedelta(days=29)
    second = b.sell("BTC/CHF", 1, 2000.0)                          # vorher 2'000 CHF = 2'500 USD: 0,60 %
    assert first.fee == pytest.approx(16.0) and second.fee == pytest.approx(12.0) and b.volume == 4000.0
    b.now = t0 + timedelta(days=31)                                # der erste Fill ist älter als 30 Tage
    assert b.tier() == (2, 0.003, 0.006, 2000.0) and len(b.volume_log) == 1
    b.now = t0 + timedelta(days=60)
    assert b.tier() == (1, 0.004, 0.008, 0.0) and not b.volume_log
    flat = PaperBroker(1000, 0.0026, 0.0)                          # ohne Staffel: fester Satz wie bisher
    flat.load_volume([(t0, 1e9)])
    assert flat.tier()[:3] == (0, 0.0026, 0.0026) and flat.fee("BTC/CHF") == 0.0026


def test_volume_log_is_saved_and_rebuilt_from_trades(tmp_path):
    """Alte Stände haben kein Umsatz-Protokoll: beim Laden aus den Trades der letzten 30 Tage nachbilden
    (abgeschlossene: Kauf und Verkauf, offene: Kauf der ganzen Menge); danach wird es mitgespeichert."""
    import json
    from tradingbot import state
    from tradingbot.broker import KRAKEN_TIERS
    from tradingbot.engine import OpenTrade
    now = datetime.now(timezone.utc)
    old = Trader(PaperBroker(1000, 0.0026, 0.0), RiskManager(RiskConfig(), 1000))
    old.closed = [dict(symbol="BTC/CHF", side="long", opened=now - timedelta(days=40), closed=now - timedelta(days=20),
                       entry=100.0, exit=110.0, qty=10.0, pnl=0.0),            # Kauf zu alt, Verkauf zählt
                  dict(symbol="ETH/CHF", side="short", opened=now - timedelta(days=5), closed=now - timedelta(days=4),
                       entry=50.0, exit=40.0, qty=20.0, pnl=0.0)]
    old.open_trades = {"SOL/CHF": OpenTrade(1, 20.0, 5.0, 15.0, 30.0, now - timedelta(days=2), sold=5.0)}
    path = tmp_path / "paper_alt.json"
    state.save(path, old, {})
    raw = json.loads(path.read_text())
    del raw["paper"]["volume"], raw["paper"]["quote_usd"]          # Stand von vor der Gebührenstaffel
    path.write_text(json.dumps(raw))
    b = PaperBroker(1000, 0.0026, 0.0, tiers=KRAKEN_TIERS)
    t = Trader(b, RiskManager(RiskConfig(), 1000))
    state.load(path, t)
    assert [v for _, v in b.volume_log] == [1100.0, 1000.0, 800.0, 200.0]        # SOL: (5 + 5 verkauft) × 20
    assert b.volume == 3100.0 and b.tier()[0] == 2 and b.quote_usd == 1.0
    b.now, b.quote_usd = now + timedelta(days=15), 1.25            # der BTC-Verkauf ist jetzt älter als 30 Tage
    state.save(path, t, {})
    saved = json.loads(path.read_text())["paper"]
    assert [v for _, v in saved["volume"]] == [1000.0, 800.0, 200.0] and saved["quote_usd"] == 1.25
    again = PaperBroker(1000, 0.0026, 0.0, tiers=KRAKEN_TIERS)
    state.load(path, Trader(again, RiskManager(RiskConfig(), 1000)))
    assert again.volume == 2000.0 and again.volume_log[0][0] == now - timedelta(days=5) and again.quote_usd == 1.25


def test_market_orders_fill_at_bid_and_ask_stops_at_level():
    """Market-Orders (Einstieg, Ausstieg per Signal, Not-Aus) zum Brief- bzw. Geldkurs ohne Slippage; Stop-Loss und
    Teilgewinn zur Marke plus/minus Slippage. Der Spread beim Einstieg steht beim Trade."""
    from tradingbot.config import Horizon
    b = PaperBroker(10_000, 0.001, 0.001)
    b.quotes = {"X": (99.0, 101.0)}
    t = Trader(b, RiskManager(RiskConfig(max_total_risk_pct=1, max_position_pct=0.5), 10_000), allow_short=True)
    t.horizons = {"kurz": Horizon("kurz", "1h", "trend", stop_loss_atr=2.0, take_profit_atr=10.0, partial_atr=1.0)}
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="kurz")
    tr = t.open_trades["X"]
    assert tr.entry == 101.0 and tr.context["spread"] == 0.02                  # Kauf zum Briefkurs
    t.check_stops("X", 101, 102.5, 100.5, 1)                                   # Teilgewinn bei 102 = Einstieg + 1 ATR
    assert tr.sold_value / tr.sold == pytest.approx(102 * 0.999)              # zur Marke minus Slippage
    t.on_signal("X", -1, 100, atr=1, equity=t.equity({"X": 100}), when=2, horizon="kurz")   # Rest zum Geldkurs, Short
    c, s = t.closed[-1], t.open_trades["X"]
    assert c["exit"] == pytest.approx((tr.sold_value + 99.0 * tr.qty) / c["qty"]) and c["spread"] == 0.02
    assert s.side == -1 and s.entry == 99.0                                    # Leerverkauf zum Geldkurs
    t.check_stops("X", 99, s.stop + 1, 98, 3)                                   # Stop-Loss: Marke plus Slippage
    assert t.closed[-1]["reason"] == "Stop-Loss" and t.closed[-1]["exit"] == pytest.approx(s.stop * 1.001)
    t.on_signal("X", 1, 100, atr=1, equity=t.equity({}), when=4, horizon="kurz")
    t.close_all({"X": 100}, "Not-Aus", 5)                                       # Not-Aus: Market-Order zum Geldkurs
    assert t.closed[-1]["reason"] == "Not-Aus" and t.closed[-1]["exit"] == 99.0
    plain = Trader(PaperBroker(10_000, 0.001, 0.001), RiskManager(RiskConfig(max_total_risk_pct=1), 10_000))
    plain.on_signal("X", 1, 100, atr=1, equity=10_000, when=0)                 # ohne Geld-/Briefkurs: Slippage
    assert plain.open_trades["X"].entry == pytest.approx(100.1) and "spread" not in plain.open_trades["X"].context


def test_takeover_and_phase_exit_are_market_orders():
    """Auch die Übernahme durch den längeren Horizont (Überschuss verkaufen) und der Ausstieg, wenn die Phase kippt,
    sind Market-Orders zum Geldkurs."""
    from tradingbot.config import Horizon
    b = PaperBroker(10_000, 0.0, 0.001)
    t = Trader(b, RiskManager(RiskConfig(max_total_risk_pct=1, max_position_pct=0.5), 10_000))
    t.horizons = {"kurz": Horizon("kurz", "1h", "trend", stop_loss_atr=2.0),
                  "lang": Horizon("lang", "1d", "regime", stop_loss_atr=8.0)}
    t.priority, t.phase_exit = True, True
    t.on_signal("X", 1, 100, atr=1, equity=10_000, when=0, horizon="kurz")             # 50 Stück
    b.quotes = {"X": (99.0, 101.0)}
    t.on_signal("X", 1, 100, atr=2, equity=t.equity({"X": 100}), when=1, horizon="lang")    # behält gut 6 Stück
    tr = t.open_trades["X"]
    assert tr.horizon == "lang" and tr.sold > 40 and tr.sold_value / tr.sold == 99.0
    t.check_phase("X", "Abwärtstrend, wild", 100, 2)
    assert t.closed[-1]["reason"] == "Phase gekippt" and t.closed[-1]["exit"] == 99.0


def test_converted_ticker_converts_bid_and_ask():
    class Ex:
        id = "fake"

        def load_markets(self):
            return {"BTC/CHF": {}, "SOL/USD": {"spot": True}, "USD/CHF": {"spot": True}}

        def fetch_ticker(self, s):
            return {"SOL/USD": {"last": 100.0, "bid": 99.5, "ask": 100.5, "percentage": 2.0}, "USD/CHF": {"last": 0.8},
                    "BTC/CHF": {"last": 50_000.0, "bid": 49_990.0, "ask": 50_010.0}}[s]
    ex = data.Converted(Ex(), "CHF")
    t = ex.fetch_ticker("SOL/CHF")
    assert (t["last"], t["bid"], t["ask"], t["percentage"]) == pytest.approx((80.0, 79.6, 80.4, 2.0))
    assert ex.fetch_ticker("BTC/CHF")["bid"] == 49_990.0                      # echtes CHF-Paar unverändert
    assert ex.usd_value() == pytest.approx(1.25)                              # 1 CHF = 1 / 0.80 USD


def _margin_trader():
    """Hebel 3 ohne Gebühren: A (600 CHF) zahlt das Cash ganz, B (800 CHF) nur zur Hälfte, dazu ein Short C."""
    rc = RiskConfig(leverage=3.0, max_position_pct=1.0, risk_per_trade=0.12, max_total_risk_pct=1, max_open_positions=8)
    b = PaperBroker(1000, 0.0, 0.0)
    b.leverage = 3.0
    t = Trader(b, RiskManager(rc, 1000), allow_short=True)
    px = {"A": 100.0, "B": 10.0, "C": 50.0}
    t.on_signal("A", 1, 100, atr=10, equity=1000, when=0)           # 1000 × 12 % / (2 × 10) = 6 Stück = 600 CHF
    t.on_signal("B", 1, 10, atr=0.75, equity=t.equity(px), when=0)  # 80 Stück = 800 CHF, 400 davon geliehen
    return t, px


def test_margin_costs_only_on_the_borrowed_part():
    """Eröffnungsgebühr und Rollover nur auf den geliehenen Teil: bei Longs, was das Cash beim Kauf nicht deckte
    (bleibt bis zum Schliessen gleich, nach Teilverkäufen anteilig), bei Shorts auf den Wert der geliehenen Coins.
    Die Buchhaltung geht dabei auf."""
    t, px = _margin_trader()
    a, b = t.open_trades["A"], t.open_trades["B"]
    assert a.margin_value == 0 and a.interest == 0                              # ganz mit Cash bezahlt
    assert b.margin_value == pytest.approx(400) and b.interest == pytest.approx(400 * 0.0003)   # Eröffnungsgebühr
    t.on_signal("C", -1, 50, atr=6, equity=t.equity(px), when=0)               # Short, ca. 500 CHF
    c = t.open_trades["C"]
    assert c.margin_value == pytest.approx(c.qty * 50) and c.interest == pytest.approx(c.qty * 50 * 0.0003)
    before = {s: tr.interest for s, tr in t.open_trades.items()}
    t.charge_interest(px, 24, 0.0018)                                           # ein Tag Rollover
    assert t.open_trades["A"].interest == 0
    assert b.interest - before["B"] == pytest.approx(400 * 0.0018)
    assert c.interest - before["C"] == pytest.approx(c.qty * 50 * 0.0018)
    t._reduce("B", b, 40, 10)                                                   # halb verkauft: halber Zins
    px["C"] = 60.0                                                              # Short: Zins auf den Wert jetzt
    before = {s: tr.interest for s, tr in t.open_trades.items()}
    t.charge_interest(px, 24, 0.0018)
    assert b.margin_value == pytest.approx(400) and b.interest - before["B"] == pytest.approx(200 * 0.0018)
    assert c.interest - before["C"] == pytest.approx(c.qty * 60 * 0.0018)
    assert t.broker.interest_paid == pytest.approx(sum(tr.interest for tr in t.open_trades.values()))
    assert abs(t.abgleich(px, 1000)["differenz"]) < 1e-9


def test_old_positions_share_the_borrowed_cash(tmp_path):
    """Stände von vor der Margin-Rechnung (ohne margin_value): Longs teilen sich das geliehene Cash nach ihrem Wert,
    Shorts sind ganz geliehen; so zahlen alte Hebel-Positionen weiter Zinsen."""
    import json
    from tradingbot import state
    t, px = _margin_trader()
    t.on_signal("C", -1, 50, atr=30, equity=t.equity(px), when=0)              # kleiner Short, ca. 100 CHF
    path = tmp_path / "paper_alt.json"
    state.save(path, t, {})
    raw = json.loads(path.read_text())
    for tr in raw["open_trades"].values():
        del tr["margin_value"]
    path.write_text(json.dumps(raw))
    again = Trader(PaperBroker(1000, 0.0, 0.0), RiskManager(RiskConfig(leverage=3.0), 1000))
    again.broker.leverage = 3.0
    state.load(path, again)
    o, debt = again.open_trades, -again.broker.cash()
    assert debt == pytest.approx(-t.broker.cash()) and debt > 200
    assert o["A"].margin_value == pytest.approx(debt * 600 / 1400)
    assert o["B"].margin_value == pytest.approx(debt * 800 / 1400)
    assert o["C"].margin_value == pytest.approx(o["C"].qty * o["C"].entry)


def test_liquidation_pays_two_percent_instead_of_the_trading_fee():
    from tradingbot.broker import KRAKEN_TIERS
    rc = RiskConfig(leverage=3.0, max_position_pct=1.0, risk_per_trade=1.0, max_total_risk_pct=1, max_daily_loss_pct=1)
    b = PaperBroker(1000, 0.0026, 0.0, tiers=KRAKEN_TIERS)
    b.leverage = 3.0
    t = Trader(b, RiskManager(rc, 1000))
    t.on_signal("X", 1, 100, atr=1, equity=1000, when=0)
    tr = t.open_trades["X"]
    assert tr.fee == pytest.approx(tr.qty * 100 * 0.008)                       # Kauf: Taker der kleinsten Stufe
    assert bot.liquidation(t, {"X": 79}, rc)
    t.close_all({"X": 79}, "Liquidation", 1)
    c = t.closed[-1]
    assert c["fees"] == pytest.approx(tr.fee + 0.02 * tr.qty * 79) and b.fee_override is None
    assert t.equity({}) == pytest.approx(1000 + c["pnl"])
    t.on_signal("X", 1, 100, atr=1, equity=t.equity({}), when=2)
    tr = t.open_trades["X"]
    t.close_all({"X": 100}, "Not-Aus", 3)                                       # Not-Aus: normale Gebühr
    assert t.closed[-1]["fees"] == pytest.approx(tr.fee + tr.qty * 100 * 0.006)   # Umsatz jetzt über 2'500 USD


def test_history_simulation_with_kraken_fees_costs_more(df):
    """Die Geschichts-Simulation rechnet mit der Kraken-Staffel: mit 1'000 USD Kapital deutlich teurer als 0,26 %."""
    from tradingbot.historie import simulate
    btc = df.set_axis(pd.date_range("2020-01-01", periods=len(df), freq="1h", tz="UTC"))
    runs = {}
    for model in ("fix", "kraken"):
        cfg = Config(strategy="trend", symbols=["BTC/USD"], name=model, fee_model=model, fee_rate=0.0026)
        cfg.risk.max_drawdown_pct = 0.99
        runs[model] = simulate(cfg, {"BTC/USD": btc})
    fix, kraken = runs["fix"].trades, runs["kraken"].trades
    rate = lambda tr: tr["fees"].sum() / (tr["qty"] * (tr["entry"] + tr["exit"])).sum()      # Gebühr je Umsatz
    assert len(kraken) >= 10 and len(runs["kraken"].equity) > 50
    assert rate(fix) == pytest.approx(0.0026) and rate(kraken) > 0.0059
    assert kraken["fees"].sum() > 2 * fix["fees"].sum()


class QuoteExchange(MultiExchange):
    """Börse mit Geld- und Briefkurs im Ticker und USD-Wert der Kontowährung (wie data.Converted)."""

    def fetch_ticker(self, symbol):
        t = super().fetch_ticker(symbol)
        return {**t, "bid": t["last"] * 0.999, "ask": t["last"] * 1.001}

    def usd_value(self):
        return 1.25


def test_sync_paper_sets_clock_and_quotes_and_keeps_last_usd_rate():
    class Offline:
        def usd_value(self):
            raise OSError("offline")
    now = datetime(2026, 10, 30, 12, tzinfo=timezone.utc)
    b = PaperBroker(1000, 0.0, 0.0)
    b.quote_usd = 1.2
    bot.sync_paper(b, Offline(), {"X": {"last": 1.0, "bid": 0.99, "ask": 1.01}, "Y": {"last": 2.0}}, now)
    assert b.now == now and b.quotes == {"X": (0.99, 1.01)} and b.quote_usd == 1.2     # letzter Kurs bleibt


def test_bot_run_buys_at_ask_with_kraken_fee_and_keeps_the_volume(df, monkeypatch, tmp_path):
    import json
    monkeypatch.chdir(tmp_path)
    ex = QuoteExchange(df)
    monkeypatch.setattr(data, "make_exchange", lambda *a, **k: ex)
    monkeypatch.setattr(bot, "build", lambda *a, **k: ConstStrategy(1))
    cfg = Config(symbols=["BTC/CHF"], use_news=False, name="kosten", poll_seconds=0, fee_model="kraken",
                 risk=RiskConfig(max_total_risk_pct=1))
    bot.run(cfg, max_iterations=1)
    st = json.loads(cfg.state_path.read_text())
    tr = st["open_trades"]["BTC/CHF"]
    assert tr["entry"] == pytest.approx(df["close"].iloc[ex.i] * 1.001)       # Kauf zum Briefkurs
    assert tr["context"]["spread"] == pytest.approx(0.002) and tr["margin_value"] == 0
    assert tr["fee"] == pytest.approx(tr["qty"] * tr["entry"] * 0.008)         # Stufe 1: 0,80 %
    assert st["paper"]["quote_usd"] == 1.25
    assert [v for _, v in st["paper"]["volume"]] == [pytest.approx(tr["qty"] * tr["entry"], abs=0.01)]


def test_dashboard_shows_fee_tier():
    from tradingbot import dashboard
    from tradingbot.broker import KRAKEN_TIERS
    b = PaperBroker(1000, 0.006, 0, tiers=KRAKEN_TIERS)
    b.quote_usd = 1.25
    b.load_volume([(datetime.now(timezone.utc), 3420.0)])                     # 4'275 USD: Stufe 2
    kraken = dashboard.Bot(Config(title="K"), Trader(b, RiskManager(RiskConfig(), 1000)), 1000.0, 0.0)
    fix = dashboard.Bot(Config(title="F"), Trader(PaperBroker(1000, 0.0026, 0), RiskManager(RiskConfig(), 1000)),
                        1000.0, 0.0)
    assert ("| Gebührenstufe | Stufe 2: 0.60 % je Market-Order (30-Tage-Umsatz 3'420 CHF) "
            "| fest 0.26 % je Order (30-Tage-Umsatz 0 CHF) |") in dashboard.overview([kraken, fix])


def test_bot_configs_use_kraken_costs():
    from tradingbot.broker import KRAKEN_TIERS, CCXTBroker, paper_broker
    from tradingbot.chef import FEE
    for name in ("config", "config_langfrist", "config_daytrading", "config_risiko", "config_phasen"):
        cfg = Config.load(f"bots/{name}.yaml")
        assert cfg.fee_model == "kraken" and cfg.fee_rate == 0.006 and paper_broker(cfg).tiers is KRAKEN_TIERS
    risk = Config.load("bots/config_risiko.yaml").risk
    assert (risk.margin_interest_per_day, risk.margin_open_fee, paper_broker(Config()).tiers) == (0.0018, 0.0003, None)
    assert FEE == 0.008
    with pytest.raises(ValueError):
        paper_broker(Config(fee_model="Kraken"))

    class Live:                                     # echte Börse: market wird angenommen und nicht gebraucht
        def amount_to_precision(self, s, q):
            return q

        def create_order(self, s, kind, side, qty):
            return {"average": 100.0, "filled": qty, "fee": {"cost": 0.1}}

        def fetch_balance(self):
            return {"free": {"CHF": 1000.0, "BTC": 1.0}}
    live = CCXTBroker(Live(), "CHF")
    assert live.buy("BTC/CHF", 0.5, 99.0, market=True).price == 100.0
    assert live.sell("BTC/CHF", 2.0, 99.0, market=True).qty == 1.0
