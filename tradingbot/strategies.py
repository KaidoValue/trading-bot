"""Handelsstrategien.

Jede Strategie liefert pro Kerze ein Signal: +1 = kaufen/halten, -1 = verkaufen/flat, 0 = keine Meinung.
Die Signale werden nur aus Daten bis einschliesslich der aktuellen Kerze berechnet (kein Blick in die Zukunft).
Neue Strategien: Klasse von Strategy ableiten, `signals()` implementieren und in STRATEGIES eintragen.
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd

from . import indicators as ind
from . import patterns as pat
from . import structure as st


class Strategy:
    name = "base"

    def __init__(self, **params):
        self.params = params

    def signals(self, df: pd.DataFrame) -> pd.Series:
        raise NotImplementedError


class TrendFollowing(Strategy):
    """Trendfolge: kaufen, wenn der schnelle EMA über dem langsamen liegt."""
    name = "trend"

    def signals(self, df):
        fast = ind.ema(df["close"], self.params.get("fast", 20))
        slow = ind.ema(df["close"], self.params.get("slow", 50))
        sig = pd.Series(0, index=df.index)
        sig[fast > slow] = 1
        sig[fast < slow] = -1
        return sig


class MeanReversion(Strategy):
    """Mean Reversion: kaufen bei überverkauftem RSI unter dem unteren Bollinger-Band, verkaufen bei Rückkehr zur Mitte."""
    name = "mean_reversion"

    def signals(self, df):
        r = ind.rsi(df["close"], self.params.get("rsi_period", 14))
        lower, mid, _ = ind.bollinger(df["close"], self.params.get("bb_period", 20))
        sig = pd.Series(0, index=df.index)
        sig[(r < self.params.get("oversold", 30)) & (df["close"] < lower)] = 1
        sig[(r > self.params.get("overbought", 70)) | (df["close"] > mid * 1.02)] = -1
        return sig


class Breakout(Strategy):
    """Donchian-Breakout: kaufen beim Ausbruch über das N-Perioden-Hoch, verkaufen beim Bruch des M-Perioden-Tiefs.
    Mit hold=True bleibt das Signal bis zum Gegensignal bestehen (nach einem Stop-Loss sofort wieder einsteigen)."""
    name = "breakout"

    def signals(self, df):
        hi = df["high"].rolling(self.params.get("entry", 20)).max().shift()
        lo = df["low"].rolling(self.params.get("exit", 10)).min().shift()
        sig = pd.Series(0, index=df.index)
        sig[df["close"] > hi] = 1
        sig[df["close"] < lo] = -1
        if self.params.get("hold"):      # Richtung halten bis zum Gegensignal: immer im Markt, viele Trades
            sig = sig.replace(0, float("nan")).ffill().fillna(0).astype(int)
        return sig


class Regime(Strategy):
    """Langfristiger Trendfilter (klassische 200-Tage-Linie): investiert, solange der Kurs über dem
    gleitenden Durchschnitt liegt, sonst in Cash (bzw. short, falls erlaubt). Wenige Trades, wenig Gebühren.
    Ziel ist nicht, Bitcoin zu schlagen, sondern grosse Abstürze zu vermeiden."""
    name = "regime"

    def signals(self, df):
        ma = ind.sma(df["close"], self.params.get("period", 200))
        band = self.params.get("band", 0.03)        # Puffer gegen ständiges Hin und Her an der Linie
        sig = pd.Series(0, index=df.index)
        sig[df["close"] > ma * (1 + band / 3)] = 1
        sig[df["close"] < ma * (1 - band)] = -1
        return sig


class TrendRecovery(Strategy):
    """Enter on recovery of the 20-bar mean in a long trend, exit below the prior ten-bar low."""
    name = "trend_recovery"

    def signals(self, df):
        close = df["close"]
        short_mean = close.rolling(20).mean()
        long_mean = close.rolling(200).mean()
        recovered = (close.shift() <= short_mean.shift()) & (close > short_mean)
        signal = pd.Series(0, index=df.index)
        signal[recovered & (close > long_mean)] = 1
        signal[(close < long_mean) | (close < df["low"].shift().rolling(10).min())] = -1
        return signal


class TimeSeriesMomentum(Strategy):
    """Directional price momentum across three horizons; intended for daily spot data."""
    name = "time_series_momentum"

    def signals(self, df):
        close = df["close"]
        returns = pd.concat([close.pct_change(n, fill_method=None) for n in (30, 90, 180)], axis=1)
        ready = returns.notna().all(axis=1)
        signal = pd.Series(0, index=df.index)
        signal[ready & returns.gt(0).all(axis=1)] = 1
        signal[ready & (returns.lt(0).sum(axis=1) >= 2)] = -1
        return signal


class Ensemble(Strategy):
    """Mehrheitsentscheid mehrerer Strategien. Kauf erst, wenn `min_votes` Strategien zustimmen."""
    name = "ensemble"

    def __init__(self, **params):
        super().__init__(**params)
        self.members = [TrendFollowing(), MeanReversion(), Breakout()]

    def signals(self, df):
        total = sum(m.signals(df) for m in self.members)
        need = self.params.get("min_votes", 2)
        sig = pd.Series(0, index=df.index)
        sig[total >= need] = 1
        sig[total <= -need] = -1
        return sig


class Pullback(Strategy):
    """Pullback/Retracement: im Aufwärtstrend (auch auf höherer Zeiteinheit) Rücksetzer in den Discount-Bereich
    bzw. die Fibonacci-Zone 50-78,6 % kaufen, wenn eine bullishe Kerze bestätigt. Short spiegelbildlich."""
    name = "pullback"

    def signals(self, df):
        a = st.analyze(df)
        htf = st.htf_trend(df, self.params.get("htf", "4h"))
        pos = a["range_pos"]
        long_zone = (pos >= 0.214) & (pos <= 0.5)        # 50-78,6 % Retracement vom Swing-Hoch
        short_zone = (pos <= 0.786) & (pos >= 0.5)
        sig = pd.Series(0, index=df.index)
        sig[(a["bias"] > 0) & (htf > 0) & long_zone & pat.bullish_candle_signal(df)] = 1
        sig[(a["bias"] < 0) & (htf < 0) & short_zone & pat.bearish_candle_signal(df)] = -1
        sig[(sig == 0) & a["CHoCH_down"]] = -1             # Trendwechsel: raus
        sig[(sig == 0) & a["CHoCH_up"]] = 1 if self.params.get("allow_short") else 0
        return sig


class Momentum(Strategy):
    """Momentum: MACD positiv und steigend, positiver Rate of Change, Kurs über VWAP, erhöhtes Volumen."""
    name = "momentum"

    def signals(self, df):
        _, _, hist = ind.macd(df["close"])
        roc = ind.momentum(df["close"], self.params.get("roc", 10))
        vw = ind.vwap(df)
        vol = df["volume"] > df["volume"].rolling(20).mean()
        sig = pd.Series(0, index=df.index)
        sig[(hist > 0) & (hist > hist.shift()) & (roc > 0) & (df["close"] > vw) & vol] = 1
        sig[(hist < 0) & (hist < hist.shift()) & (roc < 0) & (df["close"] < vw) & vol] = -1
        return sig


class PriceAction(Strategy):
    """Price Action: Ausbruch mit bestätigtem Retest handeln (Fehlausbrüche werden so gefiltert),
    Fehlausbrüche selbst als Gegensignal nutzen, Kerzenmuster an Unterstützung/Widerstand im Trend."""
    name = "price_action"

    def signals(self, df):
        a = st.analyze(df)
        atr = ind.atr(df)
        near_support = (df["low"] - a["sl"]).abs() < 0.5 * atr
        near_resist = (df["high"] - a["sh"]).abs() < 0.5 * atr
        sig = pd.Series(0, index=df.index)
        sig[a["retest_long"] | a["false_breakout_down"] | (near_support & (a["trend"] >= 0) & pat.bullish_candle_signal(df))] = 1
        sig[a["retest_short"] | a["false_breakout_up"] | (near_resist & (a["trend"] <= 0) & pat.bearish_candle_signal(df))] = -1
        return sig


class SmartMoney(Strategy):
    """Smart Money Concepts: nach Strukturbruch (BOS/CHoCH) in Richtung Bias einsteigen, wenn der Kurs im
    Discount (bzw. Premium) in ein Fair Value Gap oder einen Order Block zurückläuft. Liquidity Sweeps gegen
    den Bias gelten als Einstiegsbestätigung."""
    name = "smc"

    def signals(self, df):
        a = st.analyze(df)
        recent_sweep_low = a["sweep_low"].rolling(10).max().fillna(0).astype(bool)
        recent_sweep_high = a["sweep_high"].rolling(10).max().fillna(0).astype(bool)
        tap_long = a["bull_fvg_tap"] | a["bull_ob_tap"]
        tap_short = a["bear_fvg_tap"] | a["bear_ob_tap"]
        sig = pd.Series(0, index=df.index)
        sig[(a["bias"] > 0) & a["discount"] & (tap_long | recent_sweep_low & a["sweep_low"])] = 1
        sig[(a["bias"] < 0) & a["premium"] & (tap_short | recent_sweep_high & a["sweep_high"])] = -1
        sig[(sig == 0) & a["CHoCH_down"]] = -1
        return sig


class Reversal(Strategy):
    """Umkehrmuster: Doppelboden/-top, (inverse) Kopf-Schulter, Keile, Dreiecks- und Flaggenausbrüche,
    RSI-Divergenzen."""
    name = "reversal"

    def signals(self, df):
        a = st.analyze(df)
        bull = (a["double_bottom"] | a["inv_head_shoulders"] | a["falling_wedge"] | a["triangle_break_up"]
                | a["bull_flag"] | a["bullish_divergence"])
        bear = (a["double_top"] | a["head_shoulders"] | a["rising_wedge"] | a["triangle_break_down"]
                | a["bear_flag"] | a["bearish_divergence"])
        sig = pd.Series(0, index=df.index)
        sig[bull & ~bear] = 1
        sig[bear & ~bull] = -1
        return sig


class RangeTrading(Strategy):
    """Range-Trading: nur im Seitwärtsmarkt (keine HH/HL- oder LH/LL-Folge) an der Range-Unterkante kaufen
    und an der Oberkante verkaufen."""
    name = "range"

    def signals(self, df):
        a = st.analyze(df)
        ranging = a["trend"] == 0
        sig = pd.Series(0, index=df.index)
        sig[ranging & (a["range_pos"] < 0.15) & (df["close"] > df["open"])] = 1
        sig[(a["range_pos"] > 0.85) | a["BOS_down"]] = -1
        return sig


class Adaptive(Strategy):
    """Lernende Gewichtung: bewertet laufend, wie gut jede Strategie zuletzt war, und gewichtet sie danach.

    Für jede Teilstrategie wird die Rendite berechnet, die man erzielt hätte, wenn man ihren Signalen gefolgt
    wäre (abzüglich Gebühren bei jedem Wechsel). Über die letzten `lookback` Kerzen ergibt das eine Punktzahl.
    Nur Strategien mit positiver Punktzahl stimmen mit, und zwar proportional zu ihrer Punktzahl.
    So passt sich der Bot an die Marktphase an: im Trend gewinnt die Trendfolge, seitwärts Range und Mean Reversion.
    Alles wird nur aus vergangenen Daten berechnet.
    """
    name = "adaptive"

    def __init__(self, **params):
        super().__init__(**params)
        names = params.get("members") or ["trend", "mean_reversion", "breakout", "pullback", "momentum",
                                            "price_action", "smc", "reversal", "range"]
        self.members = [STRATEGIES[n](allow_short=params.get("allow_short", False)) for n in names]
        self.observers = [STRATEGIES[n](allow_short=params.get("allow_short", False))
                          for n in dict.fromkeys(params.get("observe_members", [])) if n not in names]

    def member_pnl(self, df) -> pd.DataFrame:
        """Rendite pro Kerze, die jede Teilstrategie gebracht hätte (abzüglich Gebühren bei jedem Wechsel)."""
        from .config import Config
        from .evaluation import replay
        cfg = self.params.get("execution_config") or Config(
            fee_rate=self.params.get("fee", 0.0026),
            slippage=self.params.get("slippage", 0.0005),
            allow_short=self.params.get("allow_short", False))
        # signals() and learn() use the identical frame within a bot iteration.
        cached = getattr(self, "_pnl_cache", None)
        if cached is not None and cached[0] is df:
            return cached[1]
        results = {m.name: replay(df, m.signals(df), cfg,
                              self.params.get("execution_horizon"),
                              daily_history=self.params.get("daily_history")) for m in self.members + self.observers}
        self._replay_activity = {name: {"closed": len(r.trades), "exposure": r.exposure}
                                 for name, r in results.items() if name in {m.name for m in self.members}}
        result = pd.DataFrame({name: r.returns for name, r in results.items()})
        self._pnl_cache = (df, result)
        return result

    def weights(self, df) -> pd.DataFrame:
        lookback = self.params.get("lookback", 200)
        pnl = self.member_pnl(df)[[m.name for m in self.members]]
        raw = pnl.rolling(lookback, min_periods=lookback // 2).sum()
        if self.params.get("memory"):
            mem, trust = self._memory_scores(df, pnl, lookback)
            raw = raw.fillna(0).mul(1 - trust, axis=0) + mem.mul(trust, axis=0)
        w = raw.clip(lower=0).fillna(0)
        total = w.sum(axis=1).replace(0, float("nan"))
        return w.div(total, axis=0).fillna(0)

    def signals(self, df):
        allow_short = self.params.get("allow_short", False)
        w = self.weights(df)
        score = sum(w[m.name] * _holding(m.signals(df), allow_short) for m in self.members)
        threshold = self.params.get("threshold", 0.5)
        active = int((w.iloc[-1] > 0).sum()) if len(w) else 0
        activity = getattr(self, "_replay_activity", {})
        traded = any(x["closed"] or x["exposure"] for x in activity.values())
        reason = ("Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen"
                  if not active and activity and not traded else
                  "Keine positiv gewichtete Strategie nach Kosten" if not active else
                  f"{active}/{len(self.members)} Strategien positiv gewichtet")
        self.last_diagnostic = {"reason": reason, "score": float(score.iloc[-1]),
                                "threshold": float(threshold), "active_members": active,
                                "simulated_closed": sum(x["closed"] for x in activity.values())}
        sig = pd.Series(0, index=df.index)
        sig[score >= threshold] = 1
        sig[score <= -threshold if allow_short else score < threshold / 2] = -1
        return sig


class AdaptiveMemory(Adaptive):
    """Lernende Gewichtung mit dauerhaftem Gedächtnis (siehe memory.py): merkt sich für jede Marktphase, welche
    Strategie dort funktioniert hat, und vertraut diesem Wissen umso mehr, je mehr Erfahrung es hat.
    Mit `memory_file` wird das Gedächtnis gespeichert und wächst bei jedem Lauf (Paper/Live);
    im Backtest lernt es Kerze für Kerze nur aus der Vergangenheit."""
    name = "adaptive_memory"

    def __init__(self, **params):
        params.setdefault("memory", True)
        super().__init__(**params)
        if params.get("library_file"):
            # Vom Strategie-Labor erfundene und geprüfte Strategien als zusätzliche Mitglieder
            from .labor import library_strategies
            self.members += library_strategies(Path(params["library_file"]))
        from .memory import Memory
        self.memory = Memory(params["memory_file"], half_life_days=params.get("memory_half_life_days", 90)) if params.get("memory_file") else None

    def _memory_scores(self, df, pnl: pd.DataFrame, lookback: int):
        import numpy as np
        from .memory import phases
        ph = phases(df).to_numpy()
        half_life = self.params.get("memory_half_life_days", 90)
        if half_life <= 0:
            raise ValueError("memory_half_life_days must be positive")
        mem = np.zeros((len(df), len(pnl.columns)))
        counts = np.zeros(len(df))
        if self.memory is not None:
            # Persisted priors are used only by online callers, never backtests.
            for i, p in enumerate(ph):
                for j, name in enumerate(pnl.columns):
                    total, n = self.memory.prior(p, name)
                    mem[i, j] = total / n * lookback if n else 0.0
                counts[i] = self.memory.prior(p, pnl.columns[0])[1]
        else:
            totals = {p: np.zeros(len(pnl.columns)) for p in set(ph)}
            count = dict.fromkeys(totals, 0.0)
            values = pnl.to_numpy()
            for i, stamp in enumerate(df.index):
                decay = 0.5 ** ((stamp - df.index[i - 1]).total_seconds() / (86400 * half_life)) if i else 1.0
                for p in totals:
                    totals[p] *= decay
                    count[p] *= decay
                # The regime at t is observable at t's close. Evidence uses
                # only earlier outcomes; outcome t belongs to regime t-1.
                p = ph[i]
                counts[i] = count[p]
                if count[p]:
                    mem[i] = totals[p] / count[p] * lookback
                if i >= 250:
                    source = ph[i - 1]
                    totals[source] += values[i]
                    count[source] += 1
        n = pd.Series(counts, index=df.index)
        trust = n / (n + self.params.get("memory_trust", 2000))
        return pd.DataFrame(mem, index=df.index, columns=pnl.columns), trust

    def learn(self, key: str, df) -> int:
        """Nach jedem Lauf: neue Kerzen ins Gedächtnis aufnehmen und speichern."""
        if self.memory is None:
            return 0
        from .memory import phases
        added = self.memory.learn(self.member_pnl(df).iloc[250:],
                                  phases(df).shift().iloc[250:], key=key)
        self.memory.save()
        return added

    def pretrain(self, frames: list) -> int:
        """Vorwissen aus mehreren Jahren Kursgeschichte, bevor der Bot zum ersten Mal handelt."""
        from .memory import phases
        added = sum(self.memory.learn(self.member_pnl(df).iloc[250:], phases(df).shift().iloc[250:],
                                     key=f"pretrain:{i}") for i, df in enumerate(frames))
        self.memory.pretrained = True
        self.memory.save()
        return added


# --- Regeln aus YouTube-Videos (lernen/YOUTUBE.md). Werden nur getestet, nicht automatisch gehandelt. ---

def fib_retracement(df: pd.DataFrame, lookback: int = 120) -> tuple[pd.Series, pd.Series]:
    """Wie weit der Kurs vom letzten Aufwärtsimpuls (Tief -> Hoch der letzten `lookback` Kerzen) zurückgesetzt hat
    (0 = am Hoch, 1 = am Tief), und ob das Hoch nach dem Tief kam (also ein Aufwärtsimpuls vorliegt)."""
    hi = df["high"].rolling(lookback).max()
    lo = df["low"].rolling(lookback).min()
    retr = (hi - df["close"]) / (hi - lo).replace(0, float("nan"))
    hi_pos = df["high"].rolling(lookback).apply(lambda x: x.argmax(), raw=True)
    lo_pos = df["low"].rolling(lookback).apply(lambda x: x.argmin(), raw=True)
    return retr, hi_pos > lo_pos


class YtFibWave(Strategy):
    """HKCM (Elliott-Wellen): Nach einem Aufwärtsimpuls die Korrektur (Welle 2/4) in der Fibonacci-Zone
    38,2-61,8 % kaufen, sobald der Kurs wieder dreht. Ungültig, wenn das 78,6-%-Retracement unterschritten wird;
    Teilgewinn/Ausstieg in die Stärke (RSI über 75)."""
    name = "yt_fib_welle"

    def signals(self, df):
        c = df["close"]
        retr, impulse = fib_retracement(df, self.params.get("lookback", 120))
        r = ind.rsi(c)
        trend = c > ind.sma(c, 200)
        sig = pd.Series(0, index=df.index)
        sig[impulse & trend & (retr >= 0.382) & (retr <= 0.618) & (c > c.shift()) & (r < 50)] = 1
        sig[(retr > 0.786) | (r > 75)] = -1
        return sig


class YtCycle(Strategy):
    """STA Solutions (Zyklen, «im Einkauf liegt der Gewinn»): kaufen, wenn nach einem tiefen Rückgang (über 40 %
    unter dem Jahreshoch) der RSI aus dem überverkauften Bereich dreht oder der Kurs die 200er-Linie zurückerobert
    (Ende des Bärenmarkts). Gewinne in die Euphorie mitnehmen: Kurs mehr als 60 % über der 200er-Linie."""
    name = "yt_zyklus"

    def signals(self, df):
        c = df["close"]
        ma = ind.sma(c, 200)
        r = ind.rsi(c)
        dd = 1 - c / c.rolling(self.params.get("year", 365), min_periods=50).max()
        sig = pd.Series(0, index=df.index)
        rsi_turn = (r > 30) & (r.shift() <= 30)
        reclaim = (c > ma) & (c.shift() <= ma.shift())
        sig[(dd > 0.4) & rsi_turn | (dd > 0.2) & reclaim] = 1
        sig[(c > ma * 1.6) | (r > 85)] = -1
        return sig


class YtDivergence(Strategy):
    """HKCM/STA («Trendwendesignale»): bullishe RSI-Divergenz (tieferes Tief im Kurs, höheres Tief im RSI) kaufen,
    bei bearisher Divergenz (höheres Hoch im Kurs, tieferes Hoch im RSI) verkaufen."""
    name = "yt_divergenz"

    def signals(self, df):
        n = self.params.get("window", 20)
        r = ind.rsi(df["close"])
        low_now, low_prev = df["low"].rolling(n).min(), df["low"].shift(n).rolling(n).min()
        rl_now, rl_prev = r.rolling(n).min(), r.shift(n).rolling(n).min()
        high_now, high_prev = df["high"].rolling(n).max(), df["high"].shift(n).rolling(n).max()
        rh_now, rh_prev = r.rolling(n).max(), r.shift(n).rolling(n).max()
        sig = pd.Series(0, index=df.index)
        sig[(df["low"] == low_now) & (low_now < low_prev) & (rl_now > rl_prev) & (r < 40)] = 1
        sig[(df["high"] == high_now) & (high_now > high_prev) & (rh_now < rh_prev) & (r > 60)] = -1
        return sig


# --- Regeln aus klassischen Trading-Büchern (lernen/BUECHER.md). Werden nur getestet, nicht automatisch gehandelt. ---

class BookTurtle(Strategy):
    """Turtle Trading (Richard Dennis, beschrieben von Curtis Faith), System 2: kaufen beim Ausbruch über das
    55-Kerzen-Hoch, verkaufen beim Bruch des 20-Kerzen-Tiefs. Short spiegelbildlich, falls erlaubt."""
    name = "buch_turtle"

    def signals(self, df):
        hi = df["high"].rolling(self.params.get("entry", 55)).max().shift()
        lo = df["low"].rolling(self.params.get("exit", 20)).min().shift()
        sig = pd.Series(0, index=df.index)
        sig[df["close"] > hi] = 1
        sig[df["close"] < lo] = -1
        return sig


class BookTripleScreen(Strategy):
    """Triple Screen (Alexander Elder, «Trading for a Living»): 1. Bildschirm: Trend der höheren Zeiteinheit
    (13er-EMA auf 5-fachem Zeitraster, hier EMA 65, steigt). 2. Bildschirm: Rücksetzer gegen den Trend
    (Force Index, 2er-EMA, unter null). 3. Bildschirm: Einstieg, wenn der Kurs über das Hoch der Vorkerze steigt.
    Raus, sobald der übergeordnete Trend dreht."""
    name = "buch_triple_screen"

    def signals(self, df):
        c = df["close"]
        long_ema = ind.ema(c, self.params.get("trend", 65))
        trend_up = long_ema > long_ema.shift()
        force = ind.ema(c.diff() * df["volume"], 2)
        sig = pd.Series(0, index=df.index)
        sig[trend_up & (force.shift() < 0) & (df["high"] > df["high"].shift())] = 1
        sig[~trend_up] = -1
        return sig


class BookGoldenCross(Strategy):
    """John Murphy («Technische Analyse der Finanzmärkte»): Golden Cross. Investiert, solange die 50er-Linie
    über der 200er-Linie liegt und das MACD-Histogramm den Trend bestätigt; raus beim Death Cross."""
    name = "buch_golden_cross"

    def signals(self, df):
        c = df["close"]
        fast, slow = ind.sma(c, 50), ind.sma(c, 200)
        _, _, hist = ind.macd(c)
        sig = pd.Series(0, index=df.index)
        sig[(fast > slow) & (hist > 0)] = 1
        sig[fast < slow] = -1
        return sig


class BookLivermore(Strategy):
    """Jesse Livermore («Reminiscences of a Stock Operator» / «How to Trade in Stocks»): nur mit dem Trend handeln
    und am «Pivotal Point» kaufen, also beim Ausbruch aus einer engen Seitwärtsphase auf ein neues Hoch. Verlierer
    schnell schliessen: raus, wenn der Kurs 10 % unter das letzte Hoch fällt."""
    name = "buch_livermore"

    def signals(self, df):
        c = df["close"]
        n = self.params.get("base", 20)
        hi = df["high"].rolling(n).max().shift()
        lo = df["low"].rolling(n).min().shift()
        tight = (hi - lo) / c < self.params.get("tight", 0.12)          # enge Basis vor dem Ausbruch
        sig = pd.Series(0, index=df.index)
        sig[(c > hi) & tight & (c > ind.sma(c, 200))] = 1
        sig[c < df["high"].rolling(n).max() * 0.9] = -1
        return sig


def _holding(sig: pd.Series, allow_short: bool) -> pd.Series:
    """Wandelt Kauf-/Verkaufssignale in die gehaltene Position um (+1 long, 0 flat, -1 short)."""
    pos = sig.replace(0, float("nan")).ffill().fillna(0)
    return pos if allow_short else pos.clip(lower=0)


def trend_direction(daily: pd.DataFrame, period: int = 200) -> pd.Series:
    """Langfristige Richtung eines Coins je Tageskerze für den Trendfilter: +1 über der 200-Tage-Linie, -1 darunter
    (mit Puffer wie bei Regime, damit es an der Linie nicht ständig hin und her springt), 0 solange es noch keine
    200 Tage gibt."""
    return _holding(Regime(period=period).signals(daily), allow_short=True).astype(int)


STRATEGIES = {cls.name: cls for cls in (TrendFollowing, MeanReversion, Breakout, Regime, Pullback, Momentum, PriceAction,
                                        SmartMoney, Reversal, RangeTrading, TrendRecovery, TimeSeriesMomentum, Ensemble, Adaptive,
                                        AdaptiveMemory, YtFibWave, YtCycle, YtDivergence,
                                        BookTurtle, BookTripleScreen, BookGoldenCross, BookLivermore)}


def build(name: str, **params) -> Strategy:
    if name not in STRATEGIES:
        raise ValueError(f"Unbekannte Strategie '{name}'. Verfügbar: {', '.join(STRATEGIES)}")
    return STRATEGIES[name](**params)
