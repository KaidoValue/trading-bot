"""Marktstruktur, Price Action, Chartmuster und Smart Money Concepts.

Alles wird so berechnet, dass zu jedem Zeitpunkt nur bekannte Kerzen verwendet werden. Ein Swing-Hoch ist
z.B. erst bestätigt, wenn danach `n` Kerzen tiefer geschlossen haben, und erscheint erst dann in den Daten.

`analyze(df)` liefert eine Tabelle mit allen Merkmalen; die Strategien greifen darauf zu.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

from . import indicators as ind


# ---------- Swings und Struktur ----------

def swings(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Bestätigte Swing Highs/Lows mit den letzten drei Niveaus (last, prev, prev2)."""
    w = 2 * n + 1
    is_sh = df["high"] == df["high"].rolling(w, center=True).max()
    is_sl = df["low"] == df["low"].rolling(w, center=True).min()
    # erst n Kerzen später bestätigt -> um n verschieben
    sh_conf = is_sh.shift(n, fill_value=False).astype(bool)
    sl_conf = is_sl.shift(n, fill_value=False).astype(bool)
    sh_level = df["high"].shift(n).where(sh_conf)
    sl_level = df["low"].shift(n).where(sl_conf)
    rsi = ind.rsi(df["close"]).shift(n)

    out = pd.DataFrame(index=df.index)
    out["sh_new"], out["sl_new"] = sh_conf, sl_conf
    for name, level, conf in (("sh", sh_level, sh_conf), ("sl", sl_level, sl_conf)):
        pts = level.dropna()
        out[f"{name}"] = pts.reindex(df.index).ffill()
        out[f"{name}_prev"] = pts.shift(1).reindex(df.index).ffill()
        out[f"{name}_prev2"] = pts.shift(2).reindex(df.index).ffill()
        r = rsi.where(conf).dropna()
        out[f"{name}_rsi"] = r.reindex(df.index).ffill()
        out[f"{name}_rsi_prev"] = r.shift(1).reindex(df.index).ffill()
    return out


def market_structure(df: pd.DataFrame, sw: pd.DataFrame) -> pd.DataFrame:
    """HH/HL/LH/LL, Trend (Auf/Ab/Seitwärts), Break of Structure und Change of Character."""
    out = pd.DataFrame(index=df.index)
    out["HH"] = sw["sh"] > sw["sh_prev"]
    out["LH"] = sw["sh"] < sw["sh_prev"]
    out["HL"] = sw["sl"] > sw["sl_prev"]
    out["LL"] = sw["sl"] < sw["sl_prev"]
    trend = pd.Series(0, index=df.index)
    trend[out["HH"] & out["HL"]] = 1
    trend[out["LH"] & out["LL"]] = -1
    out["trend"] = trend                                  # +1 Aufwärts, -1 Abwärts, 0 Seitwärts

    c, pc = df["close"], df["close"].shift()
    break_up = (c > sw["sh"]) & (pc <= sw["sh"].shift())
    break_dn = (c < sw["sl"]) & (pc >= sw["sl"].shift())
    prior = trend.shift().fillna(0)
    out["BOS_up"] = break_up & (prior >= 0)
    out["BOS_down"] = break_dn & (prior <= 0)
    out["CHoCH_up"] = break_up & (prior < 0)              # Abwärtstrend gebrochen -> möglicher Trendwechsel
    out["CHoCH_down"] = break_dn & (prior > 0)
    ev = pd.Series(np.nan, index=df.index)
    ev[break_up] = 1
    ev[break_dn] = -1
    out["bias"] = ev.ffill().fillna(0)                    # Richtung des letzten Strukturbruchs
    return out


# ---------- Support/Resistance, Breakouts, Retests ----------

def breakout_events(df: pd.DataFrame, sw: pd.DataFrame, k: int = 10, tol: float = 0.002) -> pd.DataFrame:
    """Ausbrüche über Widerstand/unter Unterstützung, Retests und Fehlausbrüche."""
    c, h, l = df["close"].to_numpy(), df["high"].to_numpy(), df["low"].to_numpy()
    res, sup = sw["sh"].to_numpy(), sw["sl"].to_numpy()
    n = len(df)
    retest_long, retest_short = np.zeros(n, bool), np.zeros(n, bool)
    false_up, false_dn = np.zeros(n, bool), np.zeros(n, bool)
    brk_up = brk_dn = None   # (Level, Index)
    for i in range(1, n):
        if not np.isnan(res[i - 1]) and c[i] > res[i - 1] >= c[i - 1]:
            brk_up = (res[i - 1], i)
            continue
        if not np.isnan(sup[i - 1]) and c[i] < sup[i - 1] <= c[i - 1]:
            brk_dn = (sup[i - 1], i)
            continue
        if brk_up:
            lvl, j = brk_up
            if i - j > k:
                brk_up = None
            elif c[i] < lvl:
                false_up[i], brk_up = True, None       # zurück unter das Niveau: Fehlausbruch
            elif l[i] <= lvl * (1 + tol):
                retest_long[i], brk_up = True, None    # Niveau von oben getestet und gehalten
        if brk_dn:
            lvl, j = brk_dn
            if i - j > k:
                brk_dn = None
            elif c[i] > lvl:
                false_dn[i], brk_dn = True, None
            elif h[i] >= lvl * (1 - tol):
                retest_short[i], brk_dn = True, None
    return pd.DataFrame({"retest_long": retest_long, "retest_short": retest_short,
                         "false_breakout_up": false_up, "false_breakout_down": false_dn}, index=df.index)


# ---------- Chartmuster ----------

def chart_patterns(df: pd.DataFrame, sw: pd.DataFrame, atr: pd.Series) -> pd.DataFrame:
    """Doppeltop/-boden, Kopf-Schulter (normal/invers), Dreiecke, Keile, Flaggen. Signal beim Ausbruch."""
    c, pc = df["close"], df["close"].shift()
    tol = 0.75 * atr

    def cross_below(level):
        return (c < level) & (pc >= level.shift())

    def cross_above(level):
        return (c > level) & (pc <= level.shift())

    out = pd.DataFrame(index=df.index)
    out["double_top"] = ((sw["sh"] - sw["sh_prev"]).abs() < tol) & cross_below(sw["sl"])
    out["double_bottom"] = ((sw["sl"] - sw["sl_prev"]).abs() < tol) & cross_above(sw["sh"])
    neck_dn = sw[["sl", "sl_prev"]].min(axis=1)
    neck_up = sw[["sh", "sh_prev"]].max(axis=1)
    out["head_shoulders"] = ((sw["sh_prev"] > sw["sh"]) & (sw["sh_prev"] > sw["sh_prev2"])
                             & ((sw["sh"] - sw["sh_prev2"]).abs() < 2 * tol) & cross_below(neck_dn))
    out["inv_head_shoulders"] = ((sw["sl_prev"] < sw["sl"]) & (sw["sl_prev"] < sw["sl_prev2"])
                                 & ((sw["sl"] - sw["sl_prev2"]).abs() < 2 * tol) & cross_above(neck_up))
    contracting = (sw["sh"] < sw["sh_prev"]) & (sw["sl"] > sw["sl_prev"])
    out["triangle_break_up"] = contracting & cross_above(sw["sh"])
    out["triangle_break_down"] = contracting & cross_below(sw["sl"])
    # Steigender Keil: Hochs und Tiefs steigen, Tiefs schneller (Konvergenz) -> bearish beim Bruch des Tiefs
    rising = (sw["sh"] > sw["sh_prev"]) & (sw["sl"] > sw["sl_prev"]) & \
             ((sw["sl"] - sw["sl_prev"]) > (sw["sh"] - sw["sh_prev"]))
    falling = (sw["sh"] < sw["sh_prev"]) & (sw["sl"] < sw["sl_prev"]) & \
              ((sw["sh_prev"] - sw["sh"]) > (sw["sl_prev"] - sw["sl"]))
    out["rising_wedge"] = rising & cross_below(sw["sl"])
    out["falling_wedge"] = falling & cross_above(sw["sh"])
    # Flagge/Wimpel: starker Impuls, danach enge Konsolidierung, dann Ausbruch in Impulsrichtung
    impulse = df["close"].shift(6) - df["close"].shift(16)
    cons_hi = df["high"].rolling(6).max().shift()
    cons_lo = df["low"].rolling(6).min().shift()
    tight = (cons_hi - cons_lo) < 2 * atr
    out["bull_flag"] = (impulse > 4 * atr) & tight & (c > cons_hi)
    out["bear_flag"] = (impulse < -4 * atr) & tight & (c < cons_lo)
    return out


def divergences(df: pd.DataFrame, sw: pd.DataFrame) -> pd.DataFrame:
    """RSI-Divergenzen: Preis macht neues Hoch, RSI nicht (bearish) und umgekehrt (bullish)."""
    return pd.DataFrame({
        "bearish_divergence": sw["sh_new"] & (sw["sh"] > sw["sh_prev"]) & (sw["sh_rsi"] < sw["sh_rsi_prev"]),
        "bullish_divergence": sw["sl_new"] & (sw["sl"] < sw["sl_prev"]) & (sw["sl_rsi"] > sw["sl_rsi_prev"]),
    }, index=df.index)


# ---------- Smart Money Concepts ----------

def smc(df: pd.DataFrame, sw: pd.DataFrame, ms: pd.DataFrame, max_age: int = 50) -> pd.DataFrame:
    """Fair Value Gaps, Order Blocks, Liquidity Sweeps, Premium/Discount."""
    o, h, l, c = (df[k].to_numpy() for k in ("open", "high", "low", "close"))
    n = len(df)
    out = pd.DataFrame(index=df.index)

    # Liquidity Sweep: Docht über das Swing-Hoch (Stops abgeholt), Schluss wieder darunter
    out["sweep_high"] = (df["high"] > sw["sh"].shift()) & (df["close"] < sw["sh"].shift())
    out["sweep_low"] = (df["low"] < sw["sl"].shift()) & (df["close"] > sw["sl"].shift())

    # Premium/Discount innerhalb der aktuellen Swing-Range
    rng = (sw["sh"] - sw["sl"]).where(lambda r: r > 0)
    out["range_pos"] = (df["close"] - sw["sl"]) / rng       # 0 = Range-Tief, 1 = Range-Hoch
    out["discount"] = out["range_pos"] < 0.5
    out["premium"] = out["range_pos"] > 0.5

    bull_fvg_tap, bear_fvg_tap = np.zeros(n, bool), np.zeros(n, bool)
    bull_ob_tap, bear_ob_tap = np.zeros(n, bool), np.zeros(n, bool)
    bull_fvg = bear_fvg = bull_ob = bear_ob = None  # (unten, oben, Index)
    up_break = (ms["BOS_up"] | ms["CHoCH_up"]).to_numpy()
    dn_break = (ms["BOS_down"] | ms["CHoCH_down"]).to_numpy()
    for i in range(2, n):
        # Rücklauf in bestehende Zonen prüfen (Zone entsteht erst nach ihrer Kerze)
        if bull_fvg and i - bull_fvg[2] <= max_age and l[i] <= bull_fvg[1] and c[i] > bull_fvg[0]:
            bull_fvg_tap[i], bull_fvg = True, None
        if bear_fvg and i - bear_fvg[2] <= max_age and h[i] >= bear_fvg[0] and c[i] < bear_fvg[1]:
            bear_fvg_tap[i], bear_fvg = True, None
        if bull_ob and i - bull_ob[2] <= max_age and l[i] <= bull_ob[1] and c[i] > bull_ob[0]:
            bull_ob_tap[i], bull_ob = True, None
        if bear_ob and i - bear_ob[2] <= max_age and h[i] >= bear_ob[0] and c[i] < bear_ob[1]:
            bear_ob_tap[i], bear_ob = True, None
        # Neue Fair Value Gaps: Lücke zwischen Kerze i-2 und i
        if l[i] > h[i - 2]:
            bull_fvg = (h[i - 2], l[i], i)
        if h[i] < l[i - 2]:
            bear_fvg = (h[i], l[i - 2], i)
        # Order Block: letzte Gegenkerze vor einem Strukturbruch
        if up_break[i]:
            for j in range(i - 1, max(i - 11, 0), -1):
                if c[j] < o[j]:
                    bull_ob = (l[j], h[j], i)
                    break
        if dn_break[i]:
            for j in range(i - 1, max(i - 11, 0), -1):
                if c[j] > o[j]:
                    bear_ob = (l[j], h[j], i)
                    break
    out["bull_fvg_tap"], out["bear_fvg_tap"] = bull_fvg_tap, bear_fvg_tap
    out["bull_ob_tap"], out["bear_ob_tap"] = bull_ob_tap, bear_ob_tap
    return out


# ---------- Multi-Timeframe ----------

def htf_trend(df: pd.DataFrame, rule: str = "4h", fast: int = 20, slow: int = 50) -> pd.Series:
    """Trend auf einer höheren Zeiteinheit (+1/-1), nur aus bereits abgeschlossenen höheren Kerzen."""
    step = df.index.to_series().diff().median()
    htf = df["close"].resample(rule).last().dropna()
    trend = np.sign(ind.ema(htf, fast) - ind.ema(htf, slow))
    # Eine höhere Kerze, die bei T beginnt, ist erst mit der letzten Kerze vor T+rule abgeschlossen
    trend.index = trend.index + pd.Timedelta(rule) - step
    return trend.reindex(df.index, method="ffill").fillna(0)


# ---------- Alles zusammen ----------

_CACHE: dict = {}


def analyze(df: pd.DataFrame, n: int = 3) -> pd.DataFrame:
    """Alle Merkmale. Ergebnis wird zwischengespeichert, da mehrere Strategien dieselben Daten auswerten."""
    key = (len(df), df.index[0], df.index[-1], float(df["close"].iloc[-1]), float(df["close"].sum()), n)
    if key not in _CACHE:
        if len(_CACHE) > 8:
            _CACHE.clear()
        _CACHE[key] = _analyze(df, n)
    return _CACHE[key]


def _analyze(df: pd.DataFrame, n: int) -> pd.DataFrame:
    atr = ind.atr(df)
    sw = swings(df, n)
    ms = market_structure(df, sw)
    return pd.concat([sw, ms, breakout_events(df, sw), chart_patterns(df, sw, atr),
                      divergences(df, sw), smc(df, sw, ms)], axis=1)
