"""Forward-only research. Isolated spot trade experiments are NOT portfolio returns.

Features/predictions are frozen before future candles arrive. One experiment per
coin/horizon at a time; missing candles invalidate it. Models only filter new
paper entries after one frozen forward comparison. They never override exits.
"""
from __future__ import annotations

import hashlib
import json
import math
from copy import deepcopy
from dataclasses import asdict
from pathlib import Path

import numpy as np
import pandas as pd

from . import indicators as ind
from .broker import PaperBroker
from .engine import MINUTES, OpenTrade, Trader
from .risk import RiskManager

SCHEMA = 1
FEATURES = ["return_1", "return_6", "return_24", "volatility", "atr_pct", "trend_distance",
            "volume_ratio", "strategy_score", "news_score", "spread", "round_trip_cost"]


def stamp(value):
    t = pd.Timestamp(value)
    return t.tz_localize("UTC") if t.tzinfo is None else t.tz_convert("UTC")


def features(df, score, news, spread, cost):
    c = df.close
    if len(df) < 50 or not df.index.is_monotonic_increasing or df.index.has_duplicates:
        raise ValueError("Research needs 50 ordered unique closed candles")
    values = [c.iloc[-1] / c.iloc[-n-1] - 1 for n in (1, 6, 24)]
    values += [c.pct_change().tail(24).std(), ind.atr(df).iloc[-1] / c.iloc[-1],
               c.iloc[-1] / ind.ema(c, 50).iloc[-1] - 1,
               df.volume.iloc[-1] / max(df.volume.tail(24).mean(), 1e-9), score, news,
               spread if spread is not None else 0.01, cost]
    if not np.isfinite(values).all():
        raise ValueError("Non-finite research features")
    return [float(x) for x in values]


def predict(model, x):
    z = np.clip((np.asarray(x) - model["mean"]) / model["scale"], -8, 8)
    value = float(z @ np.asarray(model["weights"]) + model["bias"])
    return float(1 / (1 + np.exp(-np.clip(value, -30, 30))))


def supported(model, x):
    """Reject extrapolation far outside the training distribution."""
    return bool(np.max(np.abs((np.asarray(x)-model["mean"])/model["scale"])) <= 4)


def fit(rows, now):
    """Fixed regularized logistic model; no parameter search or future labels."""
    now = stamp(now)
    rows = [r for r in rows if r.get("outcome") and stamp(r["outcome"]["known_at"]) < now
            and stamp(r["observed"]) >= now - pd.Timedelta(days=180)]
    if len(rows) < 200:
        return None
    y = np.array([r["outcome"]["net_return"] > 0 for r in rows], dtype=float)
    if y.sum() < 30 or (1-y).sum() < 30:
        return None
    x = np.asarray([r["x"] for r in rows])
    mean, scale = x.mean(axis=0), np.maximum(x.std(axis=0), 1e-6)
    x = np.clip((x - mean) / scale, -8, 8)
    age = np.array([(now - stamp(r["observed"])).total_seconds() / 86400 for r in rows])
    counts = {b: sum(r["block"] == b for r in rows) for b in {r["block"] for r in rows}}
    weight = np.array([1 / counts[r["block"]] for r in rows]) * 0.5 ** (age / 90)
    weight /= weight.sum()
    base = float(np.clip(weight @ y, 0.01, 0.99))
    w, bias = np.zeros(x.shape[1]), math.log(base / (1-base))
    for _ in range(250):
        p = 1 / (1 + np.exp(-np.clip(x @ w + bias, -30, 30)))
        error = (p-y) * weight
        w -= 0.1 * (x.T @ error + 0.02 * w)
        bias -= 0.1 * error.sum()
    positive = [r["outcome"]["net_return"] for r in rows if r["outcome"]["net_return"] > 0]
    negative = [r["outcome"]["net_return"] for r in rows if r["outcome"]["net_return"] <= 0]
    model = {"mean": mean.tolist(), "scale": scale.tolist(), "weights": w.tolist(), "bias": float(bias),
             "base": base, "win": float(np.mean(positive)), "loss": float(np.mean(negative)),
             "trained": len(rows), "created": now.isoformat(), "status": "shadow"}
    model["id"] = hashlib.sha256(json.dumps(model, sort_keys=True).encode()).hexdigest()[:16]
    return model


def wilson_lower(wins, count):
    if not count:
        return 0.0
    p, z = wins/count, 1.96
    return (p + z*z/(2*count) - z*math.sqrt(p*(1-p)/count + z*z/(4*count*count))) / (1+z*z/count)


def review(model, rows, now):
    """One fixed forward test, clustered in non-overlapping time blocks.

    Comparisons use isolated, equal-notional cases, not compounded portfolios.
    A paired lower confidence bound is a screening heuristic, not a guarantee.
    """
    observations = [r for r in rows if r.get("model_id") == model["id"] and r.get("outcome")
                    and stamp(r["observed"]) > stamp(model["created"])
                    and stamp(r["outcome"]["known_at"]) <= stamp(now)]
    blocks = {}
    for r in observations:
        blocks.setdefault(r["block"], []).append(r)
    result = {"cases": len(observations), "blocks": len(blocks), "accepted": False,
              "reason": "Forward-Probe sammelt neue Ergebnisse"}
    if len(observations) < 200 or len(blocks) < 20 or stamp(now) < stamp(model["created"]) + pd.Timedelta(days=30):
        return result
    selected = [r for r in observations if r["candidate_buy"]]
    if len(selected) < 40:
        return result | {"reason": "Zu wenige simulierte Kandidaten-Einstiege"}
    differences, profits, baseline_brier, model_brier = [], [], [], []
    for b in sorted(blocks):
        items = blocks[b]
        profit = np.mean([r["outcome"]["net_return"] * r["candidate_buy"] for r in items])
        old = np.mean([r["outcome"]["net_return"] * r["baseline_buy"] for r in items])
        profits.append(profit)
        differences.append(profit-old)
        labels = np.array([r["outcome"]["net_return"] > 0 for r in items])
        model_brier.append(np.mean((np.array([r["probability"] for r in items])-labels)**2))
        baseline_brier.append(np.mean((model["base"]-labels)**2))
    def lower(xs):
        return float(np.mean(xs) - 2.58*np.std(xs, ddof=1)/math.sqrt(len(xs)))
    lower_p = wilson_lower(sum(r["outcome"]["net_return"] > 0 for r in selected), len(selected))
    edge = lower_p*model["win"] + (1-lower_p)*model["loss"]
    accepted = (lower(differences) > 0 and lower(profits) > 0 and edge > 0
                and np.mean(model_brier) < np.mean(baseline_brier) and min(profits) > -0.10)
    return result | {"accepted": bool(accepted), "reason": "Forward-Probe bestanden" if accepted else "Kein belastbarer Vorteil",
                     "paired_lower": lower(differences), "net_lower": lower(profits), "probability_lower": lower_p,
                     "edge_lower": edge, "brier": float(np.mean(model_brier)),
                     "baseline_brier": float(np.mean(baseline_brier))}


class Research:
    def __init__(self, cfg, horizon):
        if cfg.mode != "paper" or cfg.risk.leverage != 1 or cfg.allow_short or horizon.allow_short:
            raise ValueError("Research currently supports unleveraged long-only paper trading")
        self.cfg, self.h = cfg, horizon
        self.minutes = MINUTES[horizon.timeframe]
        self.hold = 12 if self.minutes < 1440 else 6
        # Wide blocks reduce dependence from overlapping coins/experiments.
        self.block_minutes = self.hold*self.minutes
        settings = {"schema": SCHEMA, "features": FEATURES, "horizon": asdict(horizon),
                    "risk": asdict(cfg.risk), "fee": cfg.fee_rate, "fee_model": cfg.fee_model,
                    "slippage": cfg.slippage, "capital": cfg.starting_capital, "hold": self.hold}
        self.signature = hashlib.sha256(json.dumps(settings, sort_keys=True).encode()).hexdigest()[:16]
        self.path = Path("daten/research") / f"{cfg.name}_{horizon.name or horizon.timeframe}_{self.signature}.json"
        self.raw = json.loads(self.path.read_text(encoding="utf-8")) if self.path.exists() else {
            "schema": SCHEMA, "signature": self.signature, "rows": [], "seen": {}, "candidate": None,
            "active": None, "history": [], "last_fit": None}
        if self.raw.get("signature") != self.signature or self.raw.get("schema") != SCHEMA:
            raise ValueError("Incompatible research state")

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.path.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.raw, ensure_ascii=False, allow_nan=False), encoding="utf-8")
        tmp.replace(self.path)

    def _archive(self, row):
        path = self.path.parent / "journal" / f"{self.cfg.name}_{stamp(row['observed']):%Y-%m}.jsonl"
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8") as f:
            kind = "outcome" if row.get("outcome") else "invalid" if row.get("invalid") else "observation"
            f.write(json.dumps({"type": kind} | row, ensure_ascii=False, allow_nan=False) + "\n")

    def _settle(self, row, df, now):
        if row.get("outcome") or row.get("invalid") or not row.get("experiment"):
            return
        eligible = df[(df.index >= stamp(row["entry_after"])) &
                      (df.index + pd.Timedelta(minutes=self.minutes) <= now)]
        if eligible.empty:
            return
        first = stamp(row["entry_after"])
        eligible = eligible.iloc[:self.hold]
        if eligible.index[0] != first or any((eligible.index[1:] - eligible.index[:-1]) != pd.Timedelta(minutes=self.minutes)):
            row["invalid"] = "Kerzenlücke: kein verlässliches Ergebnis"
            self._archive(row)
            return
        bars = eligible.iloc[:self.hold]
        capital = self.cfg.starting_capital
        broker = PaperBroker(capital, row["fee"], row["slippage"])
        trader = Trader(broker, RiskManager(self.cfg.risk, capital))
        price = float(bars.iloc[0].open)
        qty = min(capital*0.25, capital*self.cfg.risk.max_position_pct) / price
        if qty*price < self.cfg.risk.min_order_value:
            row["invalid"] = "Standard-Testposition unter Mindestorder"
            self._archive(row)
            return
        fill = broker.buy(row["symbol"], qty, price)
        atr = row["atr"]
        stop = self.h.stop_loss_atr or self.cfg.risk.stop_loss_atr
        target = self.h.take_profit_atr or self.cfg.risk.take_profit_atr
        trader.open_trades[row["symbol"]] = OpenTrade(
            1, fill.price, fill.qty, fill.price-stop*atr, fill.price+target*atr, first.to_pydatetime(), {},
            self.h.name, fee=fill.fee, partial=fill.price+self.h.partial_atr*atr if self.h.partial_atr else 0,
            partial_pct=self.h.partial_pct, trail=self.h.trail_atr*atr if self.h.trail_atr else 0, best=fill.price)
        for i, (when, bar) in enumerate(bars.iterrows()):
            known = when + pd.Timedelta(minutes=self.minutes)
            trader.check_stops(row["symbol"], float(bar.open), float(bar.high), float(bar.low), known.to_pydatetime())
            if i == self.hold-1:
                trader.close_all({row["symbol"]: float(bar.close)}, "Research-Zeitlimit", known.to_pydatetime())
            if trader.closed:
                row["outcome"] = {"net_return": trader.closed[-1]["pnl"]/(fill.qty*fill.price),
                                  "known_at": now.isoformat(), "exit_bar": known.isoformat(),
                                  "reason": trader.closed[-1]["reason"], "fees": trader.closed[-1]["fees"]}
                self._archive(row)
                return

    def advance(self, frames, now):
        now = stamp(now)
        for row in self.raw["rows"]:
            if row["symbol"] in frames:
                self._settle(row, frames[row["symbol"]], now)
        candidate = self.raw.get("candidate")
        if candidate:
            report = review(candidate, self.raw["rows"], now)
            candidate["report"] = report
            mature = report["cases"] >= 200 and report["blocks"] >= 20 and now >= stamp(candidate["created"])+pd.Timedelta(days=30)
            expired = now >= stamp(candidate["created"])+max(pd.Timedelta(days=90), pd.Timedelta(minutes=30*self.block_minutes))
            if mature or expired:
                candidate["status"] = "paper_filter" if report["accepted"] else "rejected"
                self.raw["history"].append(deepcopy(candidate))
                if report["accepted"]:
                    self.raw["active"] = deepcopy(candidate)
                self.raw["candidate"] = None
        active = self.raw.get("active")
        if active:
            recent = [r for r in self.raw["rows"] if r.get("active_id") == active["id"] and r.get("outcome")]
            blocks = sorted({r["block"] for r in recent})[-10:]
            profits = [np.mean([r["outcome"]["net_return"]*r["active_buy"] for r in recent if r["block"] == b]) for b in blocks]
            if (len(blocks) >= 10 and (np.mean(profits) < 0 or min(profits) < -0.10)
                    or now > stamp(active["created"])+pd.Timedelta(days=180)):
                active["status"] = "paused_drift"
                self.raw["history"].append(deepcopy(active))
                self.raw["active"] = None
                if self.raw.get("candidate"):
                    self.raw["candidate"]["status"] = "comparison_baseline_changed"
                    self.raw["history"].append(deepcopy(self.raw["candidate"]))
                    self.raw["candidate"] = None
        if not self.raw.get("candidate") and (
                not self.raw["last_fit"] or now >= stamp(self.raw["last_fit"])+pd.Timedelta(days=7)):
            self.raw["candidate"] = fit(self.raw["rows"], now)
            if self.raw["candidate"]:
                self.raw["candidate"]["baseline_id"] = (self.raw.get("active") or {}).get("id", "original")
            self.raw["last_fit"] = now.isoformat()
        # Keep a bounded working set; append-only journal retains the full evidence.
        self.raw["rows"] = [r for r in self.raw["rows"] if not r.get("outcome") and not r.get("invalid")
                            or stamp(r["observed"]) >= now-pd.Timedelta(days=365)]
        self.raw["history"] = self.raw["history"][-20:]

    def observe(self, symbol, df, signal, diagnostic, context, spread, fee, now):
        now = stamp(now)
        bar = stamp(df.index[-1])
        if bar+pd.Timedelta(minutes=self.minutes) > now:
            raise ValueError("Research must not observe an unfinished candle")
        seen = self.raw["seen"].get(symbol)
        if seen and bar <= stamp(seen):
            last = self.raw.get("latest", {}).get(symbol, {})
            active = self.raw.get("active")
            gate = (last.get("gate", False) if last.get("active") == active["id"] else False) if active else None
            return self.summary(), gate
        cost = 2*(fee+self.cfg.slippage)+(spread if spread is not None else 0.01)
        x = features(df, (diagnostic or {}).get("score", float(signal)),
                     context.news_score if context else 0, spread, cost)
        pending = any(r["symbol"] == symbol and r.get("experiment") and not r.get("outcome")
                      and not r.get("invalid") for r in self.raw["rows"])
        row = {"id": f"{self.signature}:{symbol}:{bar.isoformat()}", "symbol": symbol,
               "bar": bar.isoformat(), "observed": now.isoformat(), "x": x,
               "baseline_buy": signal > 0, "signal": signal, "experiment": not pending,
               "block": int(now.timestamp() // (self.block_minutes*60)),
               "atr": float(ind.atr(df).iloc[-1]), "fee": float(fee),
               "slippage": self.cfg.slippage + (spread if spread is not None else 0.01)/2,
               "entry_after": now.ceil(f"{self.minutes}min").isoformat()}
        for slot, prefix in (("candidate", ""), ("active", "active_")):
            model = self.raw.get(slot)
            if model:
                p = predict(model, x)
                # New model is a selective filter of the incumbent, not a risk bypass.
                buy = (signal > 0 and supported(model, x) and p >= 0.6
                       and p*model["win"]+(1-p)*model["loss"] > 0)
                row[prefix+"model_id" if not prefix else "active_id"] = model["id"]
                row[prefix+"probability"] = p
                row["candidate_buy" if not prefix else "active_buy"] = bool(buy)
        if self.raw.get("active"):
            row["baseline_buy"] = row["active_buy"]
        self.raw["seen"][symbol] = bar.isoformat()
        if row["experiment"]:
            self.raw["rows"].append(row)
        self._archive(row)
        active = self.raw.get("active")
        gate = None if not active else bool(row.get("active_buy"))
        self.raw.setdefault("latest", {})[symbol] = {"gate": gate, "active": active["id"] if active else None}
        return self.summary() | {"probability": row.get("probability"),
                                 "active_probability": row.get("active_probability")}, gate

    def decision(self, symbol, bar, reason, now):
        self._archive({"type": "decision", "symbol": symbol, "bar": stamp(bar).isoformat(),
                       "id": f"{self.signature}:{symbol}:{stamp(bar).isoformat()}",
                       "observed": stamp(now).isoformat(), "reason": reason, "signature": self.signature})

    def summary(self):
        rows = self.raw["rows"]
        candidate, active = self.raw.get("candidate"), self.raw.get("active")
        return {"status": "Geprüfter Paper-Filter" if active else "Modell in Forward-Probe" if candidate else "Sammelt Lernfälle",
                "completed": sum(bool(r.get("outcome")) for r in rows),
                "pending": sum(not r.get("outcome") and not r.get("invalid") for r in rows),
                "invalid": sum(bool(r.get("invalid")) for r in rows), "journal": str(self.path),
                "candidate": candidate["id"] if candidate else None,
                "active": active["id"] if active else None,
                "report": (candidate or active or {}).get("report", {})}
