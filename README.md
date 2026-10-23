# Krypto-Trading-Bot

Modularer, automatischer Krypto-Trading-Bot in Python. Er lädt laufend Kurse, wertet sie mit mehreren Strategien aus, eröffnet und schliesst Positionen und überwacht dabei strenge Risikoregeln.

> **Wichtig:** Kein Bot kann Gewinne garantieren. Teste jede Strategie zuerst im Backtest und danach mehrere Wochen im Paper-Modus (Demo), bevor du echtes Geld einsetzt. Setze nur Geld ein, dessen Verlust du verkraften kannst.

Welche Punkte aus deiner Trading-Wissensliste der Bot abdeckt, steht in **[WISSEN.md](WISSEN.md)**.

## Aufbau

| Modul | Aufgabe |
|---|---|
| `tradingbot/data.py` | Kursdaten von der Börse laden (über [ccxt](https://github.com/ccxt/ccxt), unterstützt über 100 Krypto-Börsen) |
| `tradingbot/indicators.py` | Indikatoren: EMA, SMA, RSI, MACD, ATR, Bollinger, VWAP, Momentum, Volumen, Volume Profile, Fibonacci |
| `tradingbot/patterns.py` | Kerzenmuster: Hammer, Shooting Star, Doji, Engulfing, Inside/Outside Bar |
| `tradingbot/structure.py` | Marktstruktur (Swings, HH/HL/LH/LL, BOS, CHoCH), Support/Resistance, Retests, Fehlausbrüche, Chartmuster, Divergenzen, Smart Money Concepts, Multi-Timeframe |
| `tradingbot/strategies.py` | 9 Strategien (Trendfolge, Mean Reversion, Breakout, Pullback, Momentum, Price Action, Smart Money, Umkehrmuster, Range) plus Ensemble und Adaptive (lernende Gewichtung aller 9, Standard) |
| `tradingbot/risk.py` | Positionsgrösse, Stop-Loss, Take-Profit, Gesamtrisiko, Overtrading- und Verlustserien-Sperre, Tageslimit, Not-Aus |
| `tradingbot/engine.py` | Gemeinsame Handelslogik für Backtest, Demo und Live |
| `tradingbot/backtest.py` | Backtest mit Gebühren und Slippage, Kennzahlen (Rendite, Drawdown, Sharpe, Trefferquote, CRV, Expectancy, Profit Factor), Walk-Forward-Analyse |
| `tradingbot/broker.py` | `PaperBroker` (simuliert) und `CCXTBroker` (echte Orders) |
| `tradingbot/news.py` | Infos aus dem Netz: Fear & Greed Index und News-Schlagzeilen, nur von mehreren Portalen bestätigte Themen zählen |
| `tradingbot/events.py` | Wichtige Ereignisse: Trump, Powell, Musk & Co., Fed, SEC, Wirtschaftskalender |
| `tradingbot/bot.py` | Laufender Bot: holt jede Minute neue Kurse, prüft Orderbuch und Nachrichtenlage und entscheidet |

## Installation

Python 3.10 bis 3.13 wird benötigt. Mit ganz neuen Versionen (z.B. 3.15) fehlen für einige Bausteine noch fertige Pakete, die Installation bricht dann mit „Microsoft Visual C++ 14.0 or greater is required" ab. Unter Windows: `py install 3.13`, danach alle Befehle mit `py -3.13` statt `python`.

```bash
pip install -r requirements.txt
python -m pytest            # Tests laufen lassen
```

## Benutzung

```bash
# 1. Strategien mit echten Kursdaten des letzten Jahres vergleichen
python -m tradingbot compare --days 365

# 1b. Schutz vor Overfitting: Strategie nur auf alten Daten wählen, auf neuen testen
python -m tradingbot walkforward --days 730

# 2. Eine Strategie im Detail testen
python -m tradingbot backtest --strategy adaptive --days 730

# 3. Demo-Betrieb: echte Live-Kurse, aber simulierte Orders (kein Konto nötig)
python -m tradingbot paper
#    Abgeschlossene Trades landen in logs/trades.csv

# 4. Echtes Geld (erst nach erfolgreichem Demo-Betrieb!)
export EXCHANGE_API_KEY=...
export EXCHANGE_API_SECRET=...
CONFIRM_LIVE=JA python -m tradingbot live

# 5. Lernbericht: In welcher Marktlage hat der Bot gewonnen oder verloren?
python -m tradingbot report
```

Alle Einstellungen (Börse, Handelspaar, Strategie, Risikoregeln) stehen in `config.yaml`.

## Börse wählen

Swissquote bietet für das eTrading-Konto (auch Krypto) nach meinem Kenntnisstand keine öffentliche Programmierschnittstelle. Ein Bot kann dort also nicht automatisch Orders platzieren. Vergleich (Stand Oktober 2026, Gebühren vor Kontoeröffnung auf der Website der Börse prüfen):

| Börse | API | Gebühr pro Order (kleinste Stufe) | Sicherheit / Regulierung | `exchange:` |
|---|---|---|---|---|
| Bitstamp | ja | 0,30–0,40 %, laut TradingView gebührenfrei unter 1'000 $ Monatsvolumen | EU-lizenziert, eine der ältesten Börsen | `bitstamp` |
| Kraken | ja | ca. 0,25–0,40 % (Quellen widersprechen sich) | MiCA-Lizenz, Proof of Reserves, CHF-Paare | `kraken` (voreingestellt) |
| Coinbase | ja | 0,40–0,60 % | US-reguliert, kein CHF | `coinbase` |
| Binance | ja | 0,10 % | keine FINMA-Lizenz, Probleme mit Behörden; nicht empfohlen | `binance` |
| Swissquote | nein | 0,5–1 % + Depotgebühr | FINMA | – |

Empfehlung: Bitstamp für den Start mit kleinem Betrag, Kraken wegen der CHF-Paare. `fee_rate` in `config.yaml` an die gewählte Börse anpassen.

Den Börsennamen in `config.yaml` unter `exchange` ändern. Beim API-Schlüssel **nur Handelsrechte, niemals Auszahlungsrechte** freigeben.

## Lernende Strategie (`adaptive`)

Die Standardstrategie lernt laufend aus den Ergebnissen: Für jede Teilstrategie (Trendfolge, Mean Reversion, Breakout) berechnet sie bei jeder neuen Kerze, wie viel Gewinn oder Verlust deren Signale in den letzten 200 Kerzen gebracht hätten, inklusive Gebühren. Strategien mit Verlust bekommen kein Stimmrecht, die übrigen werden nach ihrem Erfolg gewichtet. Im Trend setzt der Bot so automatisch mehr auf Trendfolge, im Seitwärtsmarkt mehr auf Mean Reversion.

Einstellbar über `strategy_params` in `config.yaml`:

```yaml
strategy_params:
  lookback: 200     # wie viele Kerzen zurück bewertet wird
  threshold: 0.5    # wie einig sich die Strategien sein müssen
```

Achtung: Auch eine lernende Strategie reagiert erst mit Verzögerung auf einen Marktwechsel und kann sich an Zufallsmuster anpassen. Deshalb immer mit `compare` über verschiedene Zeiträume prüfen (z.B. `--days 365` und `--days 730`).

## Infos aus dem Netz

Im Paper- und Live-Betrieb holt der Bot alle 15 Minuten die aktuelle Nachrichtenlage:

- **Crypto Fear & Greed Index** (alternative.me): misst die Stimmung von 0 (extreme Angst) bis 100 (extreme Gier).
- **Schlagzeilen** von CoinDesk, Cointelegraph, Decrypt und Bitcoin Magazine.

Damit nur bestätigte Informationen zählen, wird ein Thema (z.B. Hack, Verbot, ETF-Zulassung) erst berücksichtigt, wenn **mindestens zwei verschiedene Portale** in den letzten 24 Stunden darüber berichten. Einzelmeldungen und Gerüchte werden ignoriert.

So fliesst das in die Entscheidung ein:

- Bestätigte schlechte Nachrichten (z.B. Börsen-Hack): keine neuen Käufe.
- Bestätigte gute Nachrichten: keine neuen Shorts.
- Extreme Angst oder Gier (unter 15 bzw. über 85): Positionen nur halb so gross.

Die Stichwörter stehen in `THEMES` in `tradingbot/news.py` und lassen sich erweitern. Ist eine Quelle nicht erreichbar, läuft der Bot ohne sie weiter. Abschalten mit `use_news: false`.

Jeder Trade wird zusammen mit der Nachrichtenlage beim Einstieg in `logs/trades.csv` gespeichert (bei den anderen Configs `logs/trades_<name>.csv`, z.B. `logs/trades_config_langfrist.csv`). `python -m tradingbot report` zeigt dann, in welcher Lage der Bot gewinnt oder verliert. Nach einigen Wochen Paper-Betrieb ist das die Grundlage, um die Regeln anzupassen oder später ein Machine-Learning-Modell darauf zu trainieren.

Im Backtest gibt es keine historischen Nachrichten, dort entscheidet der Bot nur nach Kursen.

## Wichtige Ereignisse (Trump, Fed & Co.)

Alle 2 Minuten prüft der Bot:

- **Schlüsselpersonen** in allen Schlagzeilen: Trump, Powell (Fed), Musk, Saylor, SEC-Chef, US-Finanzminister, Lagarde (EZB), Larry Fink (BlackRock). Erwähnt eine Meldung eine dieser Personen zusammen mit einem Marktthema (Bitcoin, Zölle, Zinsen, Reserve, Verbot …), gibt es einen Ereignis-Alarm.
- **Offizielle Quellen**: Pressemitteilungen der Federal Reserve und der SEC. Eine Meldung direkt von der Quelle gilt sofort als bestätigt.
- **Wirtschaftskalender**: 30 Minuten vor und nach wichtigen US-Terminen (Zinsentscheid, Inflation, Arbeitsmarkt) keine neuen Trades.

Reaktion: Ist die Richtung eines Ereignisses unklar, pausiert der Bot neue Einstiege für 30 Minuten. Ist sie klar (z.B. neue Zölle = negativ, Bitcoin-Reserve = positiv), handelt er nur noch in diese Richtung. Offene Positionen bleiben durch ihren Stop-Loss geschützt.

**Posts direkt von X oder Truth Social:** X verlangt für seine API ein kostenpflichtiges Abo, Truth Social hat keine offizielle Schnittstelle. Du kannst aber jeden RSS-Feed eintragen, z.B. von einem RSS-Dienst, der ein Konto in einen Feed umwandelt. Posts aus diesen Feeds gelten als Primärquelle:

```yaml
event_feeds:
  trump_truthsocial: "https://<dein-rss-dienst>/truthsocial/realDonaldTrump.xml"
```

Ehrlich gesagt: Auf einen Tweet reagieren Profi-Firmen in Millisekunden. Ein privater Bot ist dafür zu langsam. Sein Vorteil ist, sich in solchen Momenten zu schützen statt hineinzuspringen.

## Fallende Kurse (Short)

Mit `allow_short: true` in `config.yaml` (oder `--short` beim Backtest) setzt der Bot bei Verkaufssignalen auch auf fallende Kurse. Ein Short hat einen Stop-Loss **über** dem Einstieg und ein Kursziel darunter, das Risiko pro Trade bleibt bei 1 %.

```bash
python -m tradingbot compare --short --days 365
```

Short-Handel läuft vorerst **nur im Backtest und im Paper-Modus**. Live braucht es dafür ein Margin- oder Futures-Konto, und Finanzierungskosten für offene Shorts sind im Backtest noch nicht eingerechnet. Bei Shorts sind die Verluste theoretisch unbegrenzt, wenn der Kurs stark steigt. Der Stop-Loss begrenzt das, aber bei Kurssprüngen kann er überrannt werden.

## Startkapital

Der Paper-Modus braucht gar kein Geld. Für echten Handel gilt: Börsen haben Mindestordergrössen (meist etwa 5 bis 10 CHF pro Order), und Gebühren von rund 0,1 bis 0,4 % pro Order fallen bei kleinen Beträgen stark ins Gewicht. Mit 1 CHF ist daher kein echter Handel möglich. Realistisch sind mindestens 50 bis 100 CHF.

## Risikoregeln (Standard)

- Pro Trade wird höchstens 1 % des Kapitals riskiert (Abstand zum Stop-Loss).
- Stop-Loss bei 2 × ATR unter dem Einstieg, Take-Profit bei 4 × ATR darüber.
- Höchstens 25 % des Kapitals in einer Position.
- Nach 3 % Tagesverlust werden für den Rest des Tages keine neuen Trades eröffnet.
- Fällt das Kapital 15 % unter den Höchststand, schliesst der Bot alles und stoppt (Not-Aus).
- Alle offenen Positionen zusammen riskieren höchstens 3 %, maximal 3 Positionen gleichzeitig.
- Höchstens 6 neue Trades pro Tag (gegen Overtrading).
- Nach 3 Verlusten in Folge 12 Stunden Pause (gegen "Revenge Trading").
- Kein Einstieg, wenn der Spread im Orderbuch grösser als 0,3 % ist.
- Stark korrelierte Positionen (z.B. BTC und ETH in gleicher Richtung) nur halb so gross.

## Langfrist-Variante (`config_langfrist.yaml`)

Die ersten echten Tests (Oktober 2026, BTC/USD) haben gezeigt: Kurzfristige Strategien auf 1h und 4h verloren nach Gebühren Geld (Walk-Forward −13 % bzw. −12 %), während Bitcoin selbst teils stark stieg. Die Langfrist-Variante handelt auf Tageskerzen mit dem 200-Tage-Trendfilter (`regime`): investiert, solange der Kurs über der Linie liegt, sonst Cash. Das ergibt wenige Trades und soll vor allem grosse Abstürze vermeiden.

```bash
python -m tradingbot compare --config config_langfrist.yaml --days 2500
python -m tradingbot walkforward --config config_langfrist.yaml --days 2500
```

Hier ist fast das ganze Kapital investiert, Rückgänge von 20–30 % sind möglich.

**Ergebnis der echten Tests (BTC/USD, Dez. 2019 bis Okt. 2026):** `regime` +837 % gegen +738 % beim Halten, grösster Rückgang −44 % statt −77 %, Walk-Forward 2022–2026 +195 % (Halten ca. +95 %). Vergangene Ergebnisse sind keine Garantie.

### Täglicher Demo-Betrieb

Der Bot speichert seinen Stand in `state/`. Er muss deshalb nicht ununterbrochen laufen, ein Durchlauf pro Tag genügt:

```bash
py -3.13 -m tradingbot paper --config config_langfrist.yaml --once     # einmal laufen lassen
py -3.13 -m tradingbot status --config config_langfrist.yaml           # Stand anzeigen
```

Automatisch jeden Tag um 02:30 (nach Schluss der Tageskerze um 00:00 UTC) mit der Windows-Aufgabenplanung, einmalig in PowerShell eingeben:

```
schtasks /create /tn "TradingBot" /tr "C:\trading-bot\bot_taeglich.bat" /sc daily /st 02:30
```

Der PC muss um diese Zeit eingeschaltet sein (sonst läuft der Bot beim nächsten Durchlauf). Protokoll: `logs\bot.log`. Entfernen: `schtasks /delete /tn "TradingBot"`.

Hinweis: Bei einem Durchlauf pro Tag wird der Notfall-Stop nur einmal täglich geprüft.

## Eigene Strategie hinzufügen

In `tradingbot/strategies.py` eine Klasse von `Strategy` ableiten, `signals()` implementieren (+1 kaufen, -1 verkaufen, 0 neutral) und in `STRATEGIES` eintragen. Der Test `test_no_lookahead` prüft automatisch, dass die Strategie nicht in die Zukunft schaut.

## Grenzen dieser Version

- Live nur Spot-Handel (kein Short, kein Hebel). Short nur im Backtest/Paper.
- News und Ereignisse werden über Stichwörter bewertet, nicht über ein Sprachmodell. Ironie oder komplexe Meldungen erkennt das nicht.
- Stops überwacht der Bot selbst (jede Minute); echte Stop-Orders an der Börse folgen später.
- Die Quellen-URLs (News, Fed, SEC, Kalender) konnten bei der Entwicklung nicht live getestet werden. Beim ersten `paper`-Lauf im Protokoll prüfen, ob sie ankommen.
- Backtest ohne historische News.
- Der Paper-Modus speichert seinen Stand nicht über einen Neustart hinweg.
