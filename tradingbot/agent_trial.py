"""Thirty-day, isolated Q-learning paper experiment. No live-order interface."""
from __future__ import annotations

import argparse
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import pandas as pd

from .broker import PaperBroker

ROOT = Path("daten/agent_trial")
MODEL = Path("bots/agent_trial_model.json")
SYMBOL = "BTC/CHF"
FEE = 0.008
SLIPPAGE = 0.0015
ACTIONS = ("hold", "cash", "target_25", "target_50")
ALPHA = 0.08
GAMMA = 0.95
EPSILON = 0.05


def account():
    return {"cash": 100.0, "qty": 0.0, "peak": 100.0, "equity": 100.0,
            "max_drawdown": 0.0, "fees": 0.0, "fills": 0, "updates": 0,
            "pending": None, "stopped": False}


def features(frame):
    close = frame.close
    output = pd.DataFrame({
        "momentum": close.pct_change(7, fill_method=None),
        "trend": close / close.rolling(50).mean() - 1,
        "volatility": close.pct_change(fill_method=None).rolling(20).std(),
    })
    return output


def mark(wallet, price):
    value = wallet["cash"] + wallet["qty"] * price
    wallet["equity"] = value
    wallet["peak"] = max(wallet["peak"], value)
    wallet["max_drawdown"] = max(wallet["max_drawdown"], 1 - value / wallet["peak"])
    return value


def state_key(observation, wallet, price):
    value = mark(wallet, price)
    if not np.isfinite(observation).all() or not math.isfinite(value):
        raise ValueError("Non-finite agent input")
    position = wallet["qty"] * price / max(value, 0.01)
    drawdown = 1 - value / wallet["peak"]
    parts = (
        np.digitize(observation[0], [-0.02, 0.02]),
        np.digitize(observation[1], [-0.02, 0.02]),
        np.digitize(observation[2], [0.02, 0.04]),
        np.digitize(position, [0.10, 0.35]),
        np.digitize(drawdown, [0.05, 0.15]),
    )
    return ",".join(str(int(part)) for part in parts)


def choose(table, key, rng, epsilon):
    values = table.get(key, [0.0] * len(ACTIONS))
    if rng.random() < epsilon:
        return int(rng.integers(len(ACTIONS)))
    return int(np.argmax(values))


def learn(table, key, action, reward, next_key, terminal=False):
    current = table.setdefault(key, [0.0] * len(ACTIONS))
    future = 0.0 if terminal else max(table.get(next_key, [0.0] * len(ACTIONS)))
    current[action] += ALPHA * (reward + GAMMA * future - current[action])


def trade(wallet, action, price, quotes=None):
    """Target orders capped at 50% of marked capital; hold never rebalances."""
    before = mark(wallet, price)
    if action == 0 or wallet["stopped"]:
        return None
    target = (0.0, 0.0, 0.25, 0.50)[action]
    difference = target * before - wallet["qty"] * price
    if abs(difference) < 10 and target != 0:
        return None
    broker = PaperBroker(wallet["cash"], FEE, SLIPPAGE)
    broker.positions[SYMBOL] = wallet["qty"]
    if quotes:
        bid, ask = quotes
        broker.quotes[SYMBOL] = (bid * (1-SLIPPAGE), ask * (1+SLIPPAGE))
    if difference > 0:
        purchase_price = quotes[1] * (1+SLIPPAGE) if quotes else price * (1+SLIPPAGE)
        fill = broker.buy(SYMBOL, difference / (purchase_price * (1+FEE)), price, market=bool(quotes))
    elif wallet["qty"] > 0:
        quantity = wallet["qty"] if target == 0 else min(wallet["qty"], -difference / price)
        fill = broker.sell(SYMBOL, quantity, price, market=bool(quotes))
    else:
        return None
    if not fill:
        return None
    wallet["cash"], wallet["qty"] = broker.cash(), broker.position(SYMBOL)
    wallet["fees"] += fill.fee
    wallet["fills"] += 1
    mark(wallet, price)
    assert wallet["cash"] >= -1e-8 and wallet["qty"] >= -1e-8
    return vars(fill)


def reward(previous, current):
    # Multiplicative capital growth penalizes approaching ruin increasingly.
    return math.log(max(current, 0.01) / max(previous, 0.01))


def historical(frame, table, learning, seed=7, start=None):
    """Close-t observations, next-open execution and next-open valuation."""
    table = deepcopy(table)
    observations = features(frame).to_numpy()
    wallet = account()
    rng = np.random.default_rng(seed)
    first = max(60, frame.index.searchsorted(start) if start is not None else 60)
    for index in range(first, len(frame)-1):
        price = float(frame.open.iloc[index])
        key = state_key(observations[index-1], wallet, price)
        action = choose(table, key, rng, 0.15 if learning else 0.0)
        before = wallet["equity"]
        trade(wallet, action, price)
        next_price = float(frame.open.iloc[index+1])
        terminal = index == len(frame)-2
        if terminal:
            trade(wallet, 1, next_price)
        next_key = state_key(observations[index], wallet, next_price)
        if learning:
            learn(table, key, action, reward(before, wallet["equity"]), next_key, terminal)
        if wallet["equity"] <= 0.01:
            break
    return table, wallet


def train(csv, destination=MODEL):
    frame = pd.read_csv(csv, index_col=0, parse_dates=True).sort_index()
    if frame.index.has_duplicates or not np.isfinite(frame[["open", "close"]]).all().all():
        raise ValueError("Invalid historical candles")
    training = frame.loc[frame.index < pd.Timestamp("2023-01-01", tz="UTC")]
    table = {}
    for episode in range(200):
        rng = np.random.default_rng(episode)
        first = int(rng.integers(0, len(training)-425))
        segment = training.iloc[first:first+425]
        table, _ = historical(segment, table, True, seed=episode)
    _, validation = historical(frame, table, False, start=pd.Timestamp("2023-01-01", tz="UTC"))
    model = {"schema": 1, "method": "tabular_q_learning", "actions": ACTIONS,
             "trained_until": str(training.index[-1]), "episodes": 200,
             "source_sha256": hashlib.sha256(Path(csv).read_bytes()).hexdigest(),
             "validation_end": str(frame.index[-2]), "validation": validation, "q": table}
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(model, indent=2), encoding="utf-8")
    print(json.dumps({k:v for k,v in model.items() if k != "q"}, indent=2))


def begin(model, now):
    return {"schema": 1, "started": now.isoformat(), "ends": (now+timedelta(days=30)).isoformat(),
            "status": "running", "model_sha256": hashlib.sha256(json.dumps(model, sort_keys=True).encode()).hexdigest(),
            "q": deepcopy(model["q"]), "frozen_q": deepcopy(model["q"]),
            "learner": account(), "frozen": account(), "last_bar": None, "history": []}


def advance(trial, frame, price, now, quotes=None):
    if trial["status"] != "running":
        return trial
    frame = frame.loc[frame.index + pd.Timedelta(days=1) <= now]
    if len(frame) < 60 or frame.index.has_duplicates or not frame.index.is_monotonic_increasing:
        raise ValueError("Agent needs ordered, closed daily candles")
    bar = frame.index[-1].isoformat()
    terminal = now >= datetime.fromisoformat(trial["ends"])
    if not math.isfinite(price) or price <= 0:
        raise ValueError("Invalid current market price")
    if quotes and (not all(math.isfinite(x) and x > 0 for x in quotes) or quotes[0] > quotes[1]):
        raise ValueError("Invalid bid/ask")
    observation = features(frame).iloc[-1].to_numpy()
    # Always mark holdings; process each closed candle once.
    for name in ("learner", "frozen"):
        mark(trial[name], price)
    if trial["last_bar"] == bar and not terminal:
        trial["updated"] = now.isoformat()
        return trial
    fresh = now - frame.index[-1].to_pydatetime() < timedelta(days=2)
    record = {"at": now.isoformat(), "bar": bar, "price": price}
    for name, table in (("learner", trial["q"]), ("frozen", trial["frozen_q"])):
        wallet = trial[name]
        key = state_key(observation, wallet, price)
        previous = wallet["pending"]
        if terminal:
            record[name+"_fill"] = trade(wallet, 1, price, quotes)
        if previous and name == "learner":
            learn(table, previous["state"], previous["action"],
                  reward(previous["equity"], wallet["equity"]), key, terminal or wallet["equity"] <= 0.01)
            wallet["updates"] += 1
        wallet["pending"] = None
        if wallet["equity"] <= 0.01:
            wallet["stopped"] = True
        if not terminal and fresh and not wallet["stopped"]:
            # Common random draws for both agents make exploration comparable.
            rng = np.random.default_rng(int(frame.index[-1].timestamp()))
            action = choose(table, key, rng, EPSILON)
            wallet["pending"] = {"state": key, "action": action, "equity": wallet["equity"]}
            record[name+"_fill"] = trade(wallet, action, price, quotes)
            record[name+"_action"] = ACTIONS[action]
        record[name] = wallet["equity"]
    trial["last_bar"], trial["updated"] = bar, now.isoformat()
    trial["history"].append(record)
    if terminal:
        trial["status"] = "completed"
        trial["completed_at"] = now.isoformat()
        trial["objective_met"] = trial["learner"]["equity"] > 100
    return trial


def run():
    from . import data
    path = ROOT / "trial.json"
    trial = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
    if trial and trial["status"] != "running":
        return
    exchange = data.make_exchange("kraken")
    frame = data.fetch_recent(exchange, SYMBOL, "1d", 120)
    ticker = exchange.fetch_ticker(SYMBOL)
    now = datetime.now(timezone.utc)
    price = float(ticker["last"])
    timestamp = ticker.get("timestamp")
    if timestamp and abs(now.timestamp()*1000 - timestamp) > 900_000:
        raise ValueError("Stale market quote")
    quotes = (float(ticker["bid"]), float(ticker["ask"]))
    if trial is None:
        trial = begin(json.loads(MODEL.read_text(encoding="utf-8")), now)
    advance(trial, frame, price, now, quotes)
    ROOT.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(".tmp")
    temporary.write_text(json.dumps(trial, indent=2, allow_nan=False), encoding="utf-8")
    temporary.replace(path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--train")
    args = parser.parse_args()
    if args.train:
        train(args.train)
    else:
        run()
