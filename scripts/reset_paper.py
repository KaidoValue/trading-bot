"""Archive and restart paper accounts. Never connects to an exchange.

Stop the bot workflow before calling this module. The GitHub reset workflow
uses the same concurrency group as the bot and rejects concurrent bot runs.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import shutil
from datetime import datetime, timezone
from pathlib import Path

from tradingbot import state
from tradingbot.broker import paper_broker
from tradingbot.chef import STYLES
from tradingbot.config import Config
from tradingbot.engine import Trader
from tradingbot.risk import RiskManager


def reset(capital: float, root: Path = Path('.'), now: datetime | None = None) -> Path:
    if not math.isfinite(capital) or capital <= 0:
        raise ValueError('Startkapital muss endlich und positiv sein')
    root = root.resolve()
    # All validation precedes the first change to the existing accounts.
    configs = sorted((root / 'bots').glob('config*.yaml'))
    if not configs:
        raise ValueError('Keine Bot-Konfigurationen gefunden')
    for path in configs:
        cfg = Config.load(path)
        if cfg.mode != 'paper':
            raise ValueError(f'Neustart verweigert: {path.name} ist nicht im Paper-Modus')
        if not re.search(r'^starting_capital:\s*[^\r\n]+', path.read_text(encoding='utf-8'), re.M):
            raise ValueError(f'Explizites starting_capital fehlt: {path.name}')
    now = now or datetime.now(timezone.utc)
    if now.tzinfo is None:
        raise ValueError('Neustart-Zeit benötigt eine Zeitzone')
    archive = root / 'daten' / 'archiv' / f'neustart_{now:%Y%m%dT%H%M%S%fZ}'
    archive.mkdir(parents=True, exist_ok=False)
    files = list(configs)
    financial = [root / 'daten/state' / f'paper_{p.stem}.json' for p in configs]
    files += [p for p in financial if p.exists()]
    files += [root / p for p in ['daten/state/chef.json', 'daten/state/chef_gedaechtnis.json',
                                 'daten/state/verlauf.csv', 'STATUS.md', 'daten/index.html'] if (root / p).exists()]
    files += list((root / 'daten/logs').glob('trades*.csv'))
    files += list((root / 'daten/logs').glob('*fehler*.txt'))
    pending = list((root / 'daten/auftraege').glob('*.txt'))
    files += pending
    manifest = {'reset_at': now.isoformat(), 'starting_capital': capital, 'mode': 'paper',
                'strategy_memory_preserved': True, 'files': {}}
    for path in dict.fromkeys(files):
        relative = path.relative_to(root)
        target = archive / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, target)
        manifest['files'][relative.as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    # Verify the archive before resetting even one balance.
    for relative, digest in manifest['files'].items():
        if hashlib.sha256((archive / relative).read_bytes()).hexdigest() != digest:
            raise RuntimeError(f'Archivprüfung fehlgeschlagen: {relative}')
    (archive / 'manifest.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    for path in configs:
        text = path.read_text(encoding='utf-8')
        text = re.sub(r'^starting_capital:\s*[^\r\n]+', f'starting_capital: {capital:g}', text, flags=re.M)
        path.write_text(text, encoding='utf-8')
        cfg = Config.load(path)
        trader = Trader(paper_broker(cfg), RiskManager(cfg.risk, capital), allow_short=cfg.allow_short)
        trader.note = f'Paper-Neustart am {now.isoformat()} mit {capital:.2f} CHF; bisherige Ergebnisse archiviert'
        balance = trader.abgleich({}, capital)
        state.save(root / 'daten/state' / f'paper_{path.stem}.json', trader, {}, balance)
    for path in (root / 'daten/logs').glob('trades*.csv'):
        with path.open('w', encoding='utf-8', newline='') as f:
            csv.writer(f).writerow(['symbol', 'side', 'opened', 'closed', 'entry', 'exit', 'qty', 'pnl',
                                    'fees', 'interest', 'reason', 'horizon', 'partial'])
    for path in (root / 'daten/logs').glob('*fehler*.txt'):
        path.write_text('', encoding='utf-8')
    # Stale manual close orders must not act on new positions. They have
    # already been copied and verified in the reset archive.
    for path in pending:
        path.write_text('# Beim Paper-Neustart archiviert; nicht mehr ausführen\n', encoding='utf-8')
    chef = {'start': capital, 'equity': capital, 'peak': capital,
            'weights': {'config_langfrist': .3, 'config_daytrading': .3, 'config_risiko': .2},
            'last': {name: capital for name in STYLES}, 'history': [], 'fees': 0.,
            'reason': f'Paper-Neustart mit {capital:.2f} CHF am {now.isoformat()}'}
    folder = root / 'daten/state'
    folder.mkdir(parents=True, exist_ok=True)
    (folder / 'chef.json').write_text(json.dumps(chef, indent=2), encoding='utf-8')
    (folder / 'chef_gedaechtnis.json').write_text(json.dumps({'stats': {}, 'seen': {}, 'pretrained': False}), encoding='utf-8')
    with (folder / 'verlauf.csv').open('w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['zeit', *STYLES, 'chef'])
        writer.writerow([now.isoformat(), *([capital] * 4)])
    summary = '\n'.join(f'- {p.stem}: {capital:.2f} CHF, keine Positionen, keine alten Trades' for p in configs)
    (root / 'STATUS.md').write_text(f'# Paper-Neustart\n\n{now.isoformat()}\n\n{summary}\n'
                                  f'- Chef: {capital:.2f} CHF\n\nArchiv: `{archive.relative_to(root).as_posix()}`\n'
                                  '\nDie Handelsstrategien behalten ihr Wissen.\n', encoding='utf-8')
    return archive


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--capital', type=float, required=True)
    args = parser.parse_args()
    print(reset(args.capital))
