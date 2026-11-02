import json
from datetime import datetime, timezone
from pathlib import Path

import pytest

from scripts.reset_paper import reset
from tradingbot import state
from tradingbot.broker import paper_broker
from tradingbot.config import Config
from tradingbot.engine import Trader
from tradingbot.risk import RiskManager


def prepare(root):
    (root / 'bots').mkdir()
    (root / 'bots/config_daytrading.yaml').write_text('mode: paper\nstarting_capital: 1000\n', encoding='utf-8')
    (root / 'daten/state').mkdir(parents=True)
    (root / 'daten/logs').mkdir()
    old = root / 'daten/state/paper_config_daytrading.json'
    old.write_text('{"paper": {"cash": 23}, "closed": [{"pnl": -977}]}')
    (root / 'daten/logs/trades_config_daytrading.csv').write_text('pnl\n-977\n')
    memory = root / 'daten/state/ki_gedaechtnis_v2.json'
    memory.write_text('{"stats":{"up":{"trend":[1,10]}}}')
    return old, memory


def test_reset_archives_old_money_and_preserves_strategy_knowledge(tmp_path):
    old, memory = prepare(tmp_path)
    before, knowledge = old.read_bytes(), memory.read_bytes()
    archive = reset(100, tmp_path, datetime(2026, 11, 2, tzinfo=timezone.utc))
    assert (archive / old.relative_to(tmp_path)).read_bytes() == before
    assert memory.read_bytes() == knowledge
    cfg = Config.load(tmp_path / 'bots/config_daytrading.yaml')
    assert cfg.starting_capital == 100 and cfg.mode == 'paper'
    trader = Trader(paper_broker(cfg), RiskManager(cfg.risk, 100))
    state.load(old, trader)
    assert trader.broker.cash() == 100 and trader.closed == [] and trader.open_trades == {}
    assert trader.risk.peak_equity == 100 and not trader.risk.halted
    assert trader.broker.volume == 0 and trader.broker.interest_paid == 0
    chef = json.loads((tmp_path / 'daten/state/chef.json').read_text())
    assert chef['start'] == chef['equity'] == chef['peak'] == 100
    assert chef['history'] == [] and chef['fees'] == 0
    assert sum(chef['weights'].values()) <= 1 and chef['weights']['config_risiko'] <= .2


def test_reset_refuses_live_config_before_touching_accounts(tmp_path):
    old, _ = prepare(tmp_path)
    original = old.read_bytes()
    path = tmp_path / 'bots/config_daytrading.yaml'
    path.write_text('mode: live\nstarting_capital: 1000\n')
    with pytest.raises(ValueError, match='Paper-Modus'):
        reset(100, tmp_path)
    assert old.read_bytes() == original
    assert not (tmp_path / 'daten/archiv').exists()


def test_dashboard_shows_newly_reset_account_before_first_candle(tmp_path, monkeypatch):
    from tradingbot.dashboard import load_bot
    prepare(tmp_path)
    reset(100, tmp_path)
    monkeypatch.chdir(tmp_path)
    bot = load_bot('bots/config_daytrading.yaml', {})
    assert bot is not None
    assert bot.equity == 100 and bot.invested == 0


@pytest.mark.parametrize('amount', [0, -1, float('nan'), float('inf')])
def test_reset_rejects_invalid_capital(tmp_path, amount):
    old, _ = prepare(tmp_path)
    before = old.read_bytes()
    with pytest.raises(ValueError):
        reset(amount, tmp_path)
    assert old.read_bytes() == before
