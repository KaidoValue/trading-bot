"""Trading-Oberfläche als Webseite (wie bei einer Trading-Plattform): Kacheln, Kapitalkurven, Positionen, Live-Chart.

Wird bei jedem Lauf zusammen mit den Chart-Bildern in den Branch «charts» geschrieben und über GitHub Pages
angezeigt. Alles steckt in einer einzigen Datei (index.html); die Daten sind eingebettet.
"""
from __future__ import annotations

import csv
import json
from html import escape
from pathlib import Path

import pandas as pd

TZ = "Europe/Zurich"
COLORS = ["#f0b90b", "#3d8bfd", "#f6465d", "#0ecb81"]        # Langfrist, KI, Risiko, Chef
SHORT = {"config_langfrist": "Langfrist", "config_daytrading": "KI", "config_risiko": "Risiko"}


def _chf(x: float, d: int = 2) -> str:
    return f"{x:,.{d}f}".replace(",", "'")


def _local(ts) -> str:
    t = pd.Timestamp(ts)
    t = t.tz_localize("UTC") if t.tzinfo is None else t
    return t.tz_convert(TZ).strftime("%d.%m. %H:%M")


def _signed(x: float, pct: float | None = None, unit: str = " CHF") -> str:
    cls = "up" if x > 0 else "down" if x < 0 else ""
    txt = f"{'+' if x >= 0 else '−'}{_chf(abs(x))}{unit}"
    if pct is not None:
        txt += f" ({'+' if pct >= 0 else '−'}{abs(pct):.2f} %)"
    return f'<span class="{cls}">{txt}</span>'


def tv_symbol(symbol: str, exchange=None) -> str:
    symbol = getattr(exchange, "virtual", {}).get(symbol, symbol)
    return "KRAKEN:" + symbol.replace("/", "")


def record(path: Path, now, values: dict[str, float]) -> pd.DataFrame:
    """Hängt den aktuellen Kapitalstand aller Bots an den Verlauf an und gibt den ganzen Verlauf zurück."""
    path.parent.mkdir(parents=True, exist_ok=True)
    old = pd.read_csv(path) if path.exists() else pd.DataFrame(columns=["zeit"])
    row = pd.DataFrame([{"zeit": pd.Timestamp(now).isoformat(), **{k: round(v, 2) for k, v in values.items()}}])
    df = pd.concat([old, row], ignore_index=True)
    df.to_csv(path, index=False, quoting=csv.QUOTE_MINIMAL)
    return df


def page(bots, chef, tickers: dict, prices: dict, history: pd.DataFrame, now, exchange=None) -> str:
    names = [b.cfg.name for b in bots] + (["chef"] if chef else [])
    titles = {b.cfg.name: b.cfg.title or b.cfg.name for b in bots}
    titles["chef"] = "4️⃣ Chef-Bot (verteilt auf die Stile)"
    short = {b.cfg.name: SHORT.get(b.cfg.name, (b.cfg.title or b.cfg.name).split("(")[0].strip()) for b in bots}

    # --- Kacheln
    cards = []
    for i, b in enumerate(bots):
        start, eq = b.cfg.starting_capital, b.equity
        closed = b.trader.closed
        wins = sum(1 for t in closed if t["pnl"] > 0)
        rate = f"{wins / len(closed) * 100:.0f} %" if closed else "–"
        lev = f"Hebel {b.cfg.risk.leverage:g}×" if b.cfg.risk.leverage > 1 else "ohne Hebel"
        halt = '<div class="halt">⛔ Not-Aus aktiv</div>' if b.trader.risk.halted else ""
        cards.append(f"""<div class="card" style="--c:{COLORS[i % 4]}">
  <div class="card-title">{escape(titles[b.cfg.name])}</div>{halt}
  <div class="big">{_chf(eq)} <small>CHF</small></div>
  <div class="pnl">{_signed(eq - start, (eq / start - 1) * 100)}</div>
  <div class="kv"><span>Investiert</span><b>{_chf(b.invested, 0)} CHF ({b.invested / eq * 100:.0f} %)</b></div>
  <div class="kv"><span>Cash</span><b>{_chf(b.trader.broker.cash(), 0)} CHF</b></div>
  <div class="kv"><span>Offen / Abgeschlossen</span><b>{len(b.trader.open_trades)} / {len(closed)}</b></div>
  <div class="kv"><span>Trefferquote</span><b>{rate}</b></div>
  <div class="kv"><span>Strategie</span><b>{escape(b.cfg.strategy)} · {escape(b.cfg.timeframe)} · {lev}</b></div>
</div>""")
    if chef:
        alloc = "".join(f'<div class="seg" style="flex:{w * 100:.1f};background:{COLORS[j]}" title="{s}"></div>'
                        for j, (s, w) in enumerate(chef.weights.items()) if w > 0.001)
        cash = max(1 - sum(chef.weights.values()), 0)
        alloc += f'<div class="seg" style="flex:{cash * 100:.1f};background:#474d57" title="Cash"></div>'
        cards.append(f"""<div class="card" style="--c:{COLORS[3]}">
  <div class="card-title">{escape(titles['chef'])}</div>
  <div class="big">{_chf(chef.equity)} <small>CHF</small></div>
  <div class="pnl">{_signed(chef.equity - chef.start, (chef.equity / chef.start - 1) * 100)}</div>
  <div class="alloc">{alloc}</div>
  <div class="small">{escape(chef.allocation_text())}</div>
  <div class="kv"><span>Umschicht-Gebühren</span><b>{_chf(chef.fees)} CHF</b></div>
  <div class="kv"><span>Erfahrung</span><b>{len(chef.history)} Läufe</b></div>
  <div class="small muted">{escape(chef.reason)}</div>
</div>""")

    # --- Offene Positionen
    rows = []
    for i, b in enumerate(bots):
        for s, t in b.trader.open_trades.items():
            p = prices.get(s, t.entry)
            stake = t.entry * t.qty
            pnl = t.side * (p - t.entry) * t.qty
            side = '<span class="tag long">LONG</span>' if t.side > 0 else '<span class="tag short">SHORT</span>'
            rows.append(f"<tr><td><i class='dot' style='background:{COLORS[i % 4]}'></i>{escape(short[b.cfg.name])}</td>"
                        f"<td><b>{s.split('/')[0]}</b></td><td>{side}</td><td class='r'>{_chf(t.entry)}</td>"
                        f"<td class='r'>{_chf(p)}</td><td class='r'>{_chf(stake, 0)}</td>"
                        f"<td class='r'>{_signed(pnl, pnl / stake * 100, '')}</td>"
                        f"<td class='r muted'>{_chf(t.stop)}</td><td class='r muted'>{_chf(t.target) if t.target else '–'}</td>"
                        f"<td class='muted'>{_local(t.opened)}</td></tr>")
    positions = "".join(rows) or "<tr><td colspan='10' class='muted'>Keine offenen Positionen</td></tr>"

    # --- Letzte Trades
    closed = sorted(((b, t, i) for i, b in enumerate(bots) for t in b.trader.closed),
                    key=lambda x: pd.Timestamp(x[1]["closed"]), reverse=True)[:25]
    trades = "".join(
        f"<tr><td><i class='dot' style='background:{COLORS[i % 4]}'></i>{escape(short[b.cfg.name])}</td>"
        f"<td><b>{t['symbol'].split('/')[0]}</b></td>"
        f"<td><span class='tag {'long' if t['side'] == 'long' else 'short'}'>{t['side'].upper()}</span></td>"
        f"<td class='r'>{_chf(t['entry'])}</td><td class='r'>{_chf(t['exit'])}</td>"
        f"<td class='r'>{_signed(t['pnl'])}</td><td>{escape(str(t['reason']))}</td>"
        f"<td class='muted'>{_local(t['closed'])}</td></tr>" for b, t, i in closed) \
        or "<tr><td colspan='8' class='muted'>Noch keine abgeschlossenen Trades</td></tr>"

    # --- Marktübersicht
    market = []
    for s, tk in tickers.items():
        ch = tk.get("percentage")
        chtxt = _signed(ch, unit=" %") if ch is not None else "–"
        market.append(f"<tr class='sym' data-tv='{tv_symbol(s, exchange)}'><td><b>{s.split('/')[0]}</b>"
                      f"<span class='muted'>/CHF</span></td><td class='r'>{_chf(tk['last'])}</td><td class='r'>{chtxt}</td></tr>")

    # --- Kapitalkurven
    series = []
    if not history.empty:
        t = [pd.Timestamp(x).tz_convert(TZ).strftime("%d.%m. %H:%M") for x in history["zeit"]]
        for j, n in enumerate(names):
            if n in history:
                series.append({"label": short.get(n, "Chef"), "color": COLORS[j % 4],
                               "data": [None if pd.isna(v) else float(v) for v in history[n]]})
        curve = {"labels": t, "series": series}
    else:
        curve = {"labels": [], "series": []}
    first_tv = tv_symbol(next(iter(tickers)), exchange) if tickers else "KRAKEN:BTCCHF"
    stand = _local(now)

    return TEMPLATE.format(stand=stand, cards="\n".join(cards), positions=positions, trades=trades,
                           market="".join(market), curve=json.dumps(curve), first_tv=first_tv)


TEMPLATE = """<!doctype html>
<html lang="de"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="refresh" content="300">
<title>Trading-Bot Terminal</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<style>
:root{{--bg:#0b0e11;--panel:#161a1e;--line:#2b3139;--text:#eaecef;--muted:#848e9c;--up:#0ecb81;--down:#f6465d;--accent:#f0b90b}}
*{{box-sizing:border-box}}body{{margin:0;background:var(--bg);color:var(--text);font:14px/1.45 -apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif}}
header{{display:flex;flex-wrap:wrap;gap:12px;align-items:center;justify-content:space-between;padding:14px 20px;border-bottom:1px solid var(--line);background:var(--panel)}}
header h1{{margin:0;font-size:18px}}header h1 span{{color:var(--accent)}}
.badge{{background:#3c2f05;color:var(--accent);border:1px solid #6b5300;border-radius:4px;padding:2px 8px;font-size:12px;margin-left:8px}}
.stand{{color:var(--muted);font-size:13px}}
main{{padding:16px 20px;max-width:1500px;margin:0 auto}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:12px}}.grid>*,.two>*{{min-width:0}}
.card{{background:var(--panel);border:1px solid var(--line);border-top:3px solid var(--c);border-radius:6px;padding:14px}}
.card-title{{font-weight:600;margin-bottom:8px}}.big{{font-size:26px;font-weight:700;font-variant-numeric:tabular-nums}}.big small{{font-size:13px;color:var(--muted)}}
.pnl{{margin:2px 0 10px;font-weight:600}}.kv{{display:flex;justify-content:space-between;gap:8px;padding:4px 0;border-top:1px solid #1f242a;font-size:13px}}
.kv span{{color:var(--muted)}}.kv b{{font-weight:500;text-align:right}}.small{{font-size:12px;margin:6px 0}}.muted{{color:var(--muted)}}
.up{{color:var(--up)}}.down{{color:var(--down)}}.halt{{color:var(--down);font-weight:600}}
.alloc{{display:flex;height:10px;border-radius:5px;overflow:hidden;margin:6px 0}}
.panel{{background:var(--panel);border:1px solid var(--line);border-radius:6px;margin-top:12px}}
.panel h2{{font-size:14px;margin:0;padding:12px 14px;border-bottom:1px solid var(--line)}}
.two{{display:grid;grid-template-columns:minmax(0,3fr) minmax(260px,1fr);gap:12px}}
@media(max-width:900px){{.two{{grid-template-columns:1fr}}}}
@media(max-width:600px){{main,header,footer{{padding-left:16px;padding-right:16px}}.grid{{grid-template-columns:1fr}}#tv{{height:360px}}}}
.scroll{{overflow-x:auto}}table{{width:100%;border-collapse:collapse;font-variant-numeric:tabular-nums}}
th,td{{padding:8px 12px;text-align:left;white-space:nowrap;border-bottom:1px solid #1f242a}}th{{color:var(--muted);font-weight:500;font-size:12px}}
.r{{text-align:right}}tr.sym{{cursor:pointer}}tr.sym:hover,tr.sym.active{{background:#1e2329}}
.tag{{font-size:11px;font-weight:700;padding:2px 6px;border-radius:3px}}.tag.long{{background:#0e3a2a;color:var(--up)}}.tag.short{{background:#4a1820;color:var(--down)}}
.dot{{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:6px}}
#tv{{height:480px}}.chartbox{{height:300px;padding:10px}}
footer{{color:var(--muted);font-size:12px;padding:16px 20px 28px;max-width:1500px;margin:0 auto}}footer a{{color:var(--muted)}}
</style></head><body>
<header><h1><span>◆</span> Trading-Bot Terminal <span class="badge">DEMO · Spielgeld</span></h1>
<div class="stand">Stand {stand} Schweizer Zeit · aktualisiert sich alle 30 Min.</div></header>
<main>
<div class="grid">{cards}</div>

<div class="panel"><h2>Kapitalverlauf</h2><div class="chartbox"><canvas id="curve"></canvas></div></div>

<div class="two">
  <div class="panel"><h2>Live-Chart <span class="muted" id="tvname"></span></h2><div id="tv"></div></div>
  <div class="panel"><h2>Markt</h2><div class="scroll"><table><thead><tr><th>Coin</th><th class="r">Kurs</th><th class="r">24 Std.</th></tr></thead>
  <tbody>{market}</tbody></table></div><div class="small muted" style="padding:0 12px 10px">Coin anklicken für den Live-Chart</div></div>
</div>

<div class="panel"><h2>Offene Positionen</h2><div class="scroll"><table><thead><tr><th>Bot</th><th>Coin</th><th>Richtung</th>
<th class="r">Einstieg</th><th class="r">Kurs jetzt</th><th class="r">Einsatz CHF</th><th class="r">G/V CHF</th><th class="r">Stop-Loss</th><th class="r">Ziel</th><th>Eröffnet</th></tr></thead>
<tbody>{positions}</tbody></table></div></div>

<div class="panel"><h2>Letzte Trades</h2><div class="scroll"><table><thead><tr><th>Bot</th><th>Coin</th><th>Richtung</th>
<th class="r">Einstieg</th><th class="r">Ausstieg</th><th class="r">Ergebnis</th><th>Grund</th><th>Geschlossen</th></tr></thead>
<tbody>{trades}</tbody></table></div></div>
</main>
<footer>Demo-Handel mit Spielgeld, kein echtes Geld im Einsatz. Gewinne in der Vergangenheit sind keine Garantie für die Zukunft.
· <a href="https://github.com/KaidoValue/trading-bot/blob/main/STATUS.md">Ausführliche Übersicht</a>
· <a href="https://github.com/KaidoValue/trading-bot/tree/main/lernen/tagebuch">Lern-Tagebuch</a>
· <a href="https://github.com/KaidoValue/trading-bot/blob/main/lernen/LABOR.md">Strategie-Labor</a></footer>
<script>
const curve = {curve};
if (window.Chart && curve.labels.length) {{
  new Chart(document.getElementById('curve'), {{type:'line',
    data:{{labels:curve.labels, datasets:curve.series.map(s=>({{label:s.label,data:s.data,borderColor:s.color,backgroundColor:s.color,
      borderWidth:2,pointRadius:0,tension:.2,spanGaps:true}}))}},
    options:{{maintainAspectRatio:false,interaction:{{mode:'index',intersect:false}},
      plugins:{{legend:{{labels:{{color:'#eaecef',boxWidth:12}}}}}},
      scales:{{x:{{ticks:{{color:'#848e9c',maxTicksLimit:8}},grid:{{color:'#1f242a'}}}},
              y:{{ticks:{{color:'#848e9c',callback:v=>v+' CHF'}},grid:{{color:'#1f242a'}}}}}}}}}});
}} else {{ document.getElementById('curve').parentNode.innerHTML='<div class="muted" style="padding:20px">Der Verlauf wird ab jetzt bei jedem Lauf aufgezeichnet.</div>'; }}
function tv(sym) {{
  document.getElementById('tvname').textContent = sym;
  document.querySelectorAll('tr.sym').forEach(r=>r.classList.toggle('active', r.dataset.tv===sym));
  document.getElementById('tv').innerHTML = '<iframe style="width:100%;height:100%;border:0" src="https://s.tradingview.com/widgetembed/?symbol='
    + encodeURIComponent(sym) + '&interval=60&theme=dark&style=1&locale=de_DE&hide_side_toolbar=0&allow_symbol_change=1"></iframe>';
}}
document.querySelectorAll('tr.sym').forEach(r=>r.addEventListener('click',()=>tv(r.dataset.tv)));
tv('{first_tv}');
</script>
</body></html>
"""
