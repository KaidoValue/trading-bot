# Krypto-Trading-Bot

## 🖥️ [Zur Trading-Oberfläche: kaidovalue.github.io/trading-bot](https://kaidovalue.github.io/trading-bot/)

Modularer, automatischer Krypto-Trading-Bot in Python. Er lädt laufend Kurse, wertet sie mit mehreren Strategien aus, eröffnet und schliesst Positionen und überwacht dabei strenge Risikoregeln.

> **Wichtig:** Kein Bot kann Gewinne garantieren. Teste jede Strategie zuerst im Backtest und danach mehrere Wochen im Paper-Modus (Demo), bevor du echtes Geld einsetzt. Setze nur Geld ein, dessen Verlust du verkraften kannst.

## Wegweiser: Was liegt wo?

| Ordner / Datei | Inhalt |
|---|---|
| **[STATUS.md](STATUS.md)** | 📈 Aktueller Stand aller 3 Demo-Bots: Kapital, Positionen, Kurse, Charts (alle 30 Min. neu) |
| **[lernen/](lernen)** | 📚 Alles zum Lernen: Lern-Tagebuch jedes Trades, Trading-Wissen, Strategie-Vergleich, Strategie-Labor der KI, Auswertung von YouTube-Videos (`YOUTUBE.md`) und Trading-Büchern (`BUECHER.md`) |
| **[bots/](bots)** | ⚙️ Einstellungen der Bots: `config_langfrist.yaml` (1️⃣ Langfrist-Bot), `config_daytrading.yaml` (2️⃣ KI-Bot), `config_risiko.yaml` (3️⃣ Risiko-/Hebel-Bot), `config.yaml` (Vorlage). Jeder Bot handelt kurz-, mittel- und langfristig, long und short (siehe [Zeithorizonte](#zeithorizonte-gleiche-bedingungen-für-alle-bots)) |
| **[tradingbot/chef.py](tradingbot/chef.py)** | 4️⃣ Chef-Bot: verteilt eigene 1'000 CHF auf die drei Bots, alle starten mit gleichem Anteil; er bewertet sie kurz- (1 Tag), mittel- (7 Tage) und langfristig (30 Tage) (höchstens 20 % Hebel-Stil, Notbremse bei −3 % in 3 Stunden). Stand in `daten/state/chef.json`, Gedächtnis in `daten/state/chef_gedaechtnis.json` |
| **[daten/](daten)** | 🗂️ Automatisch gespeichert: Stand der Bots (`state/`), Trade-Tabellen für Excel und Fehler-Protokolle (`logs/`), Chart-Bilder (`charts/`); Aufträge von Hand an die Bots (`auftraege/`, siehe [Positionen von Hand schliessen](#positionen-von-hand-schliessen)) |
| `tradingbot/` | 🧠 Der Programmcode |
| `tests/` | ✅ Automatische Tests |
| `scripts/` | ▶️ Startskripte (GitHub und Windows) |
| `.github/workflows/` | ☁️ Automatischer Betrieb auf GitHub |

Welche Punkte aus deiner Trading-Wissensliste der Bot abdeckt, steht in **[lernen/WISSEN.md](lernen/WISSEN.md)**.

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
| `tradingbot/broker.py` | `PaperBroker` (simuliert, mit Kraken-Gebührenstaffel, Geld-/Briefkurs und Margin-Kosten) und `CCXTBroker` (echte Orders) |
| `tradingbot/news.py` | Infos aus dem Netz: Fear & Greed Index und News-Schlagzeilen, nur von mehreren Portalen bestätigte Themen zählen |
| `tradingbot/events.py` | Wichtige Ereignisse: Trump, Powell, Musk & Co., Fed, SEC, Wirtschaftskalender |
| `tradingbot/bot.py` | Laufender Bot (auf GitHub ein Durchlauf alle 30 Minuten, kurz nach Kerzenschluss): holt Kurse, prüft die Stops mit den Minutenkerzen seit dem letzten Lauf, dazu Orderbuch und Nachrichtenlage, und entscheidet |
| `tradingbot/historie.py` | Geschichts-Simulation der kompletten Bots über 2011-2026 inkl. Chef, Kursgeschichte mit Cache |

## Zeithorizonte: gleiche Bedingungen für alle Bots

Jeder Bot hat seine eigene Aufgabe, aber alle haben die gleichen Möglichkeiten: Sie dürfen **kurzfristig
(Daytrading), mittelfristig und langfristig** handeln. Alle drei starten mit 1'000 CHF, denselben 8 Coins und
denselben Gebühren. Die Einstellungen stammen aus der [Geschichts-Simulation](#geschichts-simulation-2011-2026).

| Bot | Aufgabe / Charakter | kurz | mittel | lang |
|---|---|---|---|---|
| 1️⃣ Langfrist | Schwerpunkt Trend, bis 100 % investiert, je Coin bis 20 % | `adaptive` 1h | `buch_triple_screen` 4h | `regime` (200-Tage-Linie) 1d, Startanteil 50 % |
| 2️⃣ KI | lernt mit Gedächtnis, je Horizont ein eigenes Gedächtnis | `adaptive_memory` 1h | `adaptive_memory` 4h | `adaptive_memory` 1d, Startanteil 50 % |
| 3️⃣ Risiko | Hebel 3×, ignoriert News, grosse Trends voll mitnehmen | `breakout` 30m | `trend` 4h | `regime` 1d |
| 4️⃣ Chef | verteilt Kapital auf die drei Bots | Rendite letzter Tag | letzte 7 Tage | letzte 30 Tage + Gedächtnis |

So funktioniert es (Einstellung `horizons:` in den Configs):

- Alle Horizonte eines Bots teilen sich **ein Konto** und die gemeinsamen Risikoregeln (Not-Aus, Tageslimit, max. Positionen).
  Alle Positionen zusammen sind höchstens `max_invested_pct` × Hebel des Kapitals gross, auch wenn ein Horizont mehr
  hält, als sein Anteil heute erlaubt (Anteile wandern, Übernahmen).
- Jeder Horizont hat eigene Kerzen, eigene Strategie und eigene Stops (`stop_loss_atr`, `take_profit_atr`, `risk_per_trade`).
- Pro Coin gibt es eine Position. Sie gehört dem Horizont, der sie eröffnet hat; nur er schliesst sie per Signal
  (Stops gelten immer). Mit `horizon_priority: true` darf ein **längerer** Horizont eine Position eines kürzeren
  übernehmen (gleiche Richtung) oder drehen (Gegenrichtung), damit der gewinnstärkste Stil nicht ausgesperrt wird.
- **Hauptsache Gewinn:** Mit `adaptive_shares: true` bekommt der Horizont mehr Kapital, dessen letzte 20 Trades mehr
  verdient haben (je Horizont zwischen 10 und 70 %). Die Anteile stehen in der Übersicht.
- `backtest`, `compare` und `status` nutzen den Haupthorizont (der erste in `horizons:` oder `main_horizon`).
- Das KI-Gedächtnis für 4h und 1d (`ki_gedaechtnis_mittel.json`, `ki_gedaechtnis_lang.json`) wird beim ersten Lauf
  automatisch mit Kursgeschichte vorgefüllt.
- Positionen aus der Zeit vor den Horizonten gehören automatisch dem Haupthorizont des Bots.

Werkzeuge je Horizont (alle optional):

| Einstellung | Wirkung |
|---|---|
| `trend_filter: true` | Neue Positionen nur in Richtung der 200-Tage-Linie des Coins (darüber nur long, darunter nur short). Ausstiege sind immer erlaubt. |
| `min_edge: 5` | **Gebührenfilter:** kein Einstieg, wenn das erste Ziel weniger als 5× die Kosten (Gebühren + Slippage für Kauf und Verkauf) bringt. |
| `partial_atr: 0.75`, `partial_pct: 0.5` | **Teilgewinn:** die Hälfte bei +0,75 × ATR verkaufen, danach Stop auf den Einstand (plus Kosten). Hebt die Trefferquote stark. |
| `trail_atr: 3` | Nachlauf-Stop im Abstand 3 × ATR zum besten Kurs (in der Simulation ohne Vorteil, daher aus). |
| `allow_short: false` | Shorts nur in diesem Horizont aus- oder einschalten (leer = Einstellung des Bots). |

Für den ganzen Bot: `short_probation: true` (Short-Probezeit) lässt Shorts nur mit einem Viertel der Grösse zu, bis
die letzten 20 eigenen Shorts zusammen Gewinn gebracht haben (mindestens 10 Shorts). Trade-Ergebnisse enthalten
**alle Kosten**: Kauf- und Verkaufsgebühr, Spread bzw. Slippage und Margin-Kosten (Eröffnung, Zinsen) für Shorts oder
Hebel (siehe [Realistische Kosten](#realistische-kosten-wie-bei-kraken)).

**Buchhaltung** (`tradingbot/buchhaltung.py`): Jeder abgeschlossene Trade speichert `fees` (Kaufgebühr und alle
Verkaufsgebühren, auch von Teilverkäufen) und `interest` (Zinsen); das Ergebnis `pnl` ist der Kursgewinn minus beides.
Bei jedem Lauf prüft der Bot: Kapital = Startkapital + Ergebnisse aller Trades (offene zum aktuellen Kurs) − Altlasten.
Mehr als 1 CHF Abweichung kommt als Fehler ins Protokoll; die Übersicht zeigt «Gebühren bisher» und «Buchhaltung»
(✅ stimmt oder ⚠️ Abweichung). Bis zum 28.10.2026 21:26 UTC fehlte in den Ergebnissen die Kaufgebühr (das Cash
stimmte). Der erste Lauf danach bucht einmal nach: alte Ergebnisse um die Kaufgebühr korrigiert (alter Wert in
`pnl_alt`, Spalte `nachgebucht`), alte offene Positionen bekommen ihre Kaufgebühr, der alte Stand liegt in
`daten/state/archiv/<Name>_vor_nachbuchung_<Datum>.json`. Was dann noch fehlt (Zinsen von vor dem 28.10., die keinem
Trade gehören), zeigt die Übersicht als «Altlasten».

## Realistische Kosten (wie bei Kraken)

Demo-Betrieb und Geschichts-Simulation rechnen mit den Kosten eines echten Kraken-Kontos (`fee_model: kraken` in den
Bot-Configs, `tradingbot/broker.py`):

- **Gebührenstaffel** (gültig seit 9.7.2026): Der Satz hängt vom Handelsvolumen der letzten 30 Tage in USD ab (beim
  CHF-Konto mit dem USD/CHF-Kurs umgerechnet). Der Bot sendet nur Market-Orders und zahlt deshalb immer die
  Taker-Gebühr. Die aktuelle Stufe jedes Bots steht in der Übersicht («Gebührenstufe»).

  | 30-Tage-Umsatz | Maker | Taker |
  |---|---|---|
  | ab 0 $ | 0,40 % | 0,80 % |
  | ab 2'500 $ | 0,30 % | 0,60 % |
  | ab 10'000 $ | 0,22 % | 0,38 % |
  | ab 25'000 $ | 0,20 % | 0,35 % |
  | ab 50'000 $ | 0,15 % | 0,30 % |
  | ab 100'000 $ | 0,12 % | 0,25 % |
  | … ab 10 Mio. $ | 0,00 % | 0,10 % |

- **Kauf zum Brief-, Verkauf zum Geldkurs:** Market-Orders (Einstieg, Ausstieg per Signal oder Phase, Übernahme durch
  einen längeren Horizont, Not-Aus, Zwangsschliessung, von Hand) laufen zum Ask bzw. Bid des Tickers, ohne zusätzliche
  Slippage. Stop-Loss, Take-Profit, Nachlauf-Stop und Teilgewinn laufen zur Marke plus/minus Slippage. Den Spread beim
  Einstieg zeigt das Trade-Protokoll (Spalte `spread`); bewertet wird weiterhin zum letzten Kurs.
- **Hebel und Shorts (Margin):** Eröffnungsgebühr `margin_open_fee` (0,03 %) und Rollover `margin_interest_per_day`
  (0,18 % pro Tag, also 0,03 % alle 4 Std., Mitte von Krakens 0,02-0,04 %; BTC kostet dort 0,01-0,02 %, vereinfacht
  ein Satz für alle) nur auf den geliehenen Teil: bei Longs, was das Cash beim Kauf nicht deckte (bleibt bis zum
  Schliessen gleich, nach Teilverkäufen anteilig), bei Shorts der Wert der geliehenen Coins. Beides zählt zu den
  Zinsen des Trades. Offene Positionen von vor dieser Rechnung teilen sich das geliehene Cash nach ihrem Wert.
- **Zwangsschliessung:** 2 % des Positionswerts statt der Handelsgebühr.
- **Chef-Bot:** Umschichten kostet 0,8 % (Taker der kleinsten Stufe).

Vereinfachungen: Coins ohne CHF-Paar (z.B. SOL) handelt ein echtes Konto über ein USD-Guthaben; den einmaligen Umtausch
CHF → USD rechnet der Bot nicht ein. Maker-Gebühren nutzt er nicht, weil er nur Market-Orders sendet. Die
Geschichts-Simulation kennt keinen Geld-/Briefkurs (dort Slippage) und rechnet in USD. Ältere Stände ohne
Umsatz-Protokoll bilden es beim ersten Laden aus den Trades der letzten 30 Tage nach. `fee_rate` (0,6 %) ist nur noch
ein Schätzwert für das Strategie-Labor und einzelne Backtests (`backtest`, `compare`, `walkforward`); mit
`fee_model: fix` rechnet ein Bot wie früher mit diesem festen Satz. Die Simulationszahlen unten (Oktober 2026) wurden
noch mit 0,26 % je Order gerechnet; die nächste Geschichts-Simulation rechnet mit der Staffel.

## Läufe kurz nach Kerzenschluss

Signale entstehen beim Schluss einer Kerze (um :00 oder :30 UTC); die noch offene Kerze zählt nicht. Vorher startete
jeder Durchlauf 30 Minuten nach dem vorherigen, ohne Bezug zur Uhr: Einstiege und Ausstiege per Signal kamen 0 bis 30
Minuten nach dem Signal, im Mittel rund 15 Minuten (221 Einstiege vom 23. bis 30.10.2026). Die Geschichts-Simulation
handelt dagegen zum Eröffnungskurs der nächsten Kerze, also gleich beim Kerzenschluss, wie ein echter Bot, der innert
einer Minute reagiert.

Jetzt wartet `.github/workflows/bot.yml` vor jedem Durchlauf (auch vor dem ersten, z.B. nach einem Start von Hand)
bis zur nächsten vollen oder halben Stunde plus 90 Sekunden, damit die Börse die Kerze sicher abgeschlossen hat: Die
Bots laufen um ca. **:01:30 und :31:30 UTC**, nacheinander (Langfrist-, KI-, Risiko-Bot). Ein Block hat 9 Durchläufe
(ca. 4½ Stunden) und startet dann den nächsten.

Jeder Einstieg speichert **`delay_min`**: die Minuten vom Schluss der Signalkerze (Beginn der letzten abgeschlossenen
Kerze plus ihre Länge) bis zum Durchlauf, zu dessen Kurs der Bot einsteigt. Der Wert steht im Trade-Protokoll (Spalte
`delay_min`) und bei offenen Positionen im Stand unter `context`. Erwartet sind etwa 2 bis 4 Minuten (90 Sekunden
Wartezeit, dazu die Laufzeit der Bots, die vorher drankommen). Deutlich mehr heisst, dass ein Durchlauf ausgefallen ist
oder zu spät kam (z.B. Kette abgerissen) oder dass ein Einstieg nachgeholt wurde, etwa beim Langfrist-Bot
(`reevaluate: true`) nach einer Pause wegen der Nachrichtenlage. Ältere Trades haben in dieser Spalte keinen Wert.

## Stops minutengenau (Demo-Betrieb)

Der Demo-Bot läuft alle 30 Minuten. Bei jedem Lauf spielt er für jede offene Position die **1-Minuten-Kerzen seit
dem letzten Lauf** der Reihe nach durch, so als läge der Stop als Stop-Order an der Börse (`replay_stops` in
`tradingbot/bot.py`):

- Berührt eine Minute den Stop, das Ziel oder den Teilgewinn, wird zu diesem Zeitpunkt (Ende der Minute) an der Marke
  ausgeführt, minus Slippage. Auch wenn der Kurs beim Lauf schon wieder auf der sicheren Seite liegt.
- **«Stop-Loss (Gap)»** heisst jetzt nur noch: Eine Minute hat schon jenseits des Stops eröffnet (echter Kurssprung),
  ausgeführt zu ihrem Eröffnungskurs.
- Danach prüft er die laufende Minute mit dem aktuellen Kurs. Liegt dieser schon jenseits des Stops, schliesst er zu
  diesem Kurs und schreibt das in den Grund: **«Stop-Loss (Ticker)»**. Gleich, wenn die Minutenkerzen nicht abrufbar
  sind (dann wie früher nur mit dem Kurs beim Lauf); der nächste Lauf spielt die fehlenden Minuten nach.
- Liegt die letzte Prüfung mehr als 12 Stunden zurück, nimmt er 5-Minuten-Kerzen (mehr als 720 Kerzen liefert Kraken
  nicht), nach mehr als 60 Stunden nur den aktuellen Kurs.
- Wie oft die alte Prüfung nur mit dem Kurs beim Lauf einen Treffer verpasst hätte, zählt der Stand unter `zaehler`
  (`minutenkerze_getroffen`).

Bis zum 30.10.2026 prüfte der Bot nur den Kurs beim Lauf: Jeder Stop-Treffer wurde als Gap zum Kurs in diesem Moment
gebucht (z.B. «Stop-Loss (Gap)», schlechter als der Stop), und Stops oder Ziele, die zwischen zwei Läufen berührt
wurden, während der Kurs danach wieder zurückkam, wurden gar nicht ausgelöst. Trefferquote, Ergebnis je
Ausstiegsgrund und Stop-Verluste vor und nach dem 30.10.2026 sind deshalb nicht direkt vergleichbar. Live (echtes
Geld) prüft der Bot weiterhin nur zum Kurs beim Lauf, weil eine echte Order nicht rückwirkend ausgeführt werden kann.

## Wächter für stille Fehler

Vorher blieb ein fehlgeschlagener Durchlauf unsichtbar: Der Bot fing den Fehler ab und endete normal, der Stand wurde
nicht gespeichert, und STATUS.md zeigte trotzdem eine frische Zeit. Ein einziger fehlender Kurs (am 29.10.2026 08:01
UTC Kraken «EGeneral:No data») brach den ganzen Durchlauf ab, auch die Stops aller anderen Coins, und liess die
Übersicht abstürzen. Jetzt (`tradingbot/waechter.py`):

- **Kurse je Coin:** Fällt der Ticker eines Coins aus, laufen die anderen normal weiter. Für diesen Coin setzt der Bot
  Signale und Stops aus; der nächste Lauf mit Kurs spielt die Minutenkerzen nach. Eine offene Position zählt für
  Kapital, Drawdown und Hebel zum letzten gespeicherten Kurs (im Stand unter `prices`: Coin → [Kurs, Zeit]; ohne einen
  zum Einstiegskurs), die Notiz sagt es. Orders gibt es nur zum aktuellen Kurs: Auch Not-Aus und Zwangsschliessung
  schliessen diesen Coin erst im nächsten Lauf. Fehlen nur die Kerzen eines Coins, setzt nur sein Signal aus. Fehlen
  alle Kurse, gilt der Durchlauf als fehlgeschlagen.
- **Fehler-Protokoll:** Jeder Fehler kommt als Zeile «Zeit UTC | Fehlerart | Meldung» nach
  `daten/logs/fehler_<Config>.txt` (z.B. `fehler_config_risiko.txt`, die letzten 100 Zeilen), auch ein Fehler schon
  beim Start. `scripts/zyklus.sh` schreibt Fehler des ganzen Laufs (Bot mit Fehler beendet, Übersicht, Charts,
  Speichern) nach `daten/logs/fehler_zyklus.txt`.
- **Exit-Code:** `paper --once` endet nach einem fehlgeschlagenen Durchlauf mit Exit-Code 1, damit `zyklus.sh` es
  merkt. Im Dauerbetrieb (ohne `--once`) läuft der Bot weiter.
- **Übersicht:** Die Zeile «Letzter Durchlauf» zeigt, wann jeder Bot zuletzt gespeichert hat. Ist ein Stand älter als
  90 Minuten oder kam in den letzten 2 Stunden ein Fehler, steht oben in STATUS.md eine Warnung, z.B. «⚠️ **3️⃣
  Risiko-Bot:** seit 3 Std. kein neuer Stand gespeichert (letzter Fehler …)», und dieselbe auf der Kachel der
  Trading-Oberfläche. Ohne Ticker zeigt die Übersicht den letzten bekannten Kurs (gespeicherter Kurs der Bots oder
  Schluss der letzten Kerze) mit «Kurs vom …», ein Coin ganz ohne Kurs steht als «kein Kurs abrufbar» da. Die
  Nachrichtenlage kommt nur noch an eine neu geschriebene STATUS.md (früher stand sie nach einem Absturz doppelt da).

## Positionen von Hand schliessen

Auf GitHub: Actions → «Position schliessen» → Run workflow, Bot-Datei (z.B. `bots/config_daytrading.yaml`) und Coins
(z.B. `TRX/CHF HYPE/CHF`) angeben. Das geht jederzeit: Der Workflow legt nur einen **Auftrag** in `daten/auftraege/` ab
(z.B. `20261030T201500_config_daytrading.txt` mit der Zeile `schliessen TRX/CHF HYPE/CHF`, Format in
[daten/auftraege/README.md](daten/auftraege/README.md)). Der nächste Durchlauf dieses Bots (normalerweise innert 30
Minuten) führt ihn vor den Stops aus:

- Jede offene Position dieser Coins wird zum dann aktuellen Kurs geschlossen (Market-Order zum Geld- bzw. Briefkurs,
  Grund «Von Hand geschlossen»), mit Eintrag im Trade-Protokoll und im Lern-Tagebuch. Ein Coin ohne Position wird
  übersprungen.
- Hat ein Coin mit Position gerade keinen Kurs, wartet der ganze Auftrag auf den nächsten Lauf.
- Danach liegt der Auftrag in `daten/auftraege/erledigt/`, und STATUS.md zeigt unter «Letzte Entscheidung», was
  passiert ist (z.B. «Auftrag vom 30.10. 20:15 UTC: TRX/CHF geschlossen @ 0.2712 (Ergebnis -1.38)»).

Warum ein Auftrag: Die Bots speichern ihren Stand nach jedem Durchlauf mit `git pull --rebase -X theirs`. Schrieb der
Workflow früher selbst in `daten/state/`, während ein Bot-Durchlauf lief (4-5 Minuten), mischte git die beiden
Fassungen Zeile für Zeile: Eine geschlossene Position konnte wieder auftauchen, Cash und Positionen aus verschiedenen
Ständen stammen oder die Datei kaputt sein. Jetzt schreibt nur noch der Bot selbst in seinen Stand.

Lokal legt `python -m tradingbot schliessen --config bots/config_daytrading.yaml --symbols TRX/CHF` denselben Auftrag
ab (für die Bots auf GitHub die Datei hochladen: `git add`, `git commit`, `git push`). Mit `--sofort` schliesst der
Befehl direkt wie früher, nur für einen Bot auf dem eigenen PC und nur, wenn er gerade nicht läuft.

> **Regel:** Dateien unter `daten/state/` nie von Hand ändern, solange die Bots laufen. Für eine Änderung zuerst den
> Workflow «Trading-Bot stündlich» abschalten (Disable workflow) und den laufenden Lauf abbrechen (Cancel workflow
> run), dann ändern, hochladen und den Workflow wieder einschalten.

## Geschichts-Simulation (2011-2026)

```bash
python -m tradingbot historie --bots bots/config_langfrist.yaml bots/config_daytrading.yaml bots/config_risiko.yaml
```

Spielt die **kompletten Bots** über die ganze verfügbare Kursgeschichte durch: alle Horizonte, alle Coins (sobald es
sie gibt), Risikoregeln, Not-Aus, Hebel, Zinsen und Zwangsschliessung, dazu den Chef-Bot. Bitcoin kommt von Bitstamp
ab August 2011, die meisten anderen Coins von Binance ab 2017. Die Kurse werden beim ersten Lauf geladen (ca. 10 Minuten)
und in `data/historie/` zwischengespeichert. Ergebnis: [lernen/HISTORIE.md](lernen/HISTORIE.md).

**So wurden die heutigen Einstellungen gefunden (Oktober 2026):** Rund 500 Varianten (Trendfilter, Gebührenfilter,
Teilgewinn, Nachlauf-Stop, Vorrang, Shorts, Strategien je Horizont, Investitionsgrad, Risiko pro Trade, Hebel,
Grenzen des Chefs) wurden simuliert. **Gewählt wurde nur nach den Jahren 2011-2022**; die Jahre 2023-2026 waren dabei
weggesperrt und dienen als unabhängige Prüfung. Ziel: **möglichst viel Gewinn**. Regel: höchster Gewinn pro Jahr
2011-2022; eine Einstellung wird nur geändert, wenn sie mindestens 1 Prozentpunkt pro Jahr mehr bringt (kleinere
Unterschiede sind Zufall); Leitplanke: kein Rückgang über 75 %.

| Bot | vorher 2011-2026 | nachher 2011-2026 | 2011-2022 pro Jahr | 2023-2026 pro Jahr (Prüfung) | Start erst 2022 |
|---|---|---|---|---|---|
| 1️⃣ Langfrist | 1'000 → 4'937, Rückgang bis −80 % | 1'000 → 649'516, Rückgang bis −51 % | +58,0 % | +39,6 % (max. −35 %) | 1'000 → 1'834 |
| 2️⃣ KI | 1'000 → 850 (2011 für immer gestoppt) | 1'000 → 10'522, Rückgang bis −26 % | +17,6 % | +14,4 % (max. −19 %) | 1'000 → 1'259 |
| 3️⃣ Risiko | 1'000 → 18 (2011 fast alles verloren) | 1'000 → 1'796'269, Rückgang bis −62 % | +65,5 % | +58,6 % (max. −49 %) | 1'000 → 2'767 |
| 4️⃣ Chef | 1'000 → 1'971 | 1'000 → 78'182, Rückgang bis −40 % | +35,8 % | +25,9 % (max. −31 %) | 1'000 → 1'471 |
| Bitcoin halten | | | +90,4 % (max. −85 %) | +51,3 % (max. −53 %) | 1'000 → 1'691 (max. −67 %) |

„Start erst 2022“: frische 1'000 am 1. Januar 2022 (Beginn eines Crashs, Bitcoin −65 % im Jahr 2022), bis Oktober 2026.
Selbst ausprobieren: `python -m tradingbot historie --bots ... --start 2022-01-01`.

Was die Simulation gezeigt hat:

- **Trendfilter** war die wichtigste Verbesserung (+18 % pro Jahr beim Langfrist-Bot im Schnitt aller Varianten).
- **Kurzfristiger Handel verliert ohne Gebührenfilter**: Kauf und Verkauf kosteten in der Simulation zusammen rund
  0,6 % (0,26 % Gebühr je Order plus Slippage; mit der Kraken-Staffel in der kleinsten Stufe rund 1,7 %), die meisten
  Stunden-Bewegungen sind kleiner. Mit `min_edge: 5` handeln die Bots seltener, aber nur, wenn es sich lohnen kann.
  Auch mit 0,4 % Gebühr und doppelter Slippage bleiben die Ergebnisse fast gleich.
- **Mehr investieren bringt mehr:** Der Langfrist-Bot darf jetzt bis 100 % statt 50 % investieren (je Coin bis 20 %),
  der KI-Bot riskiert 2 % statt 1 % pro Trade, der Chef darf bis 20 % in den Risiko-Bot legen (in der Simulation 50 %; im Demo-Betrieb verlor der Risiko-Bot aber 64 % in 6 Tagen) und hält keine feste
  Cash-Reserve mehr. Der Preis dafür sind grössere Rückgänge.
- **Shorts verloren in jeder Variante** Geld, auch mit Trendfilter und Probezeit: Leihzinsen (bei Kraken 0,02-0,04 %
  alle 4 Std., also 0,12-0,24 % pro Tag) und Krypto steigt langfristig. Deshalb ist `allow_short` bei allen Bots aus,
  die Funktion bleibt aber erhalten (mit Short-Probezeit).
- **Teilgewinne** heben die Trefferquote auf über 70 %, verkaufen aber in grossen Aufschwüngen zu früh und kosten
  bei Trendfolgern viel Gewinn. Weil Gewinn das Ziel ist, gibt es Teilgewinne nur bei «kurz» und «mittel». Für eine
  hohe Trefferquote: `partial_atr: 0.75` auch beim Horizont `lang` eintragen.
- **Bitcoin einfach halten** brachte bis 2022 mehr Rendite, aber mit Abstürzen bis −85 %. In der Prüfung 2023-2026
  liegt der Risiko-Bot vor Bitcoin halten, mit Start 2022 auch der Langfrist-Bot.
- **Hebel 4 oder 5** brachte bis 2022 nicht mehr als Hebel 3 (nur Zinsen und Risiko), deshalb bleibt es bei 3.

Grenzen: keine historischen News und Ereignisse, kein Orderbuch-Spread, keine Korrelationsprüfung, Kurse in USD.
Die Jahre 2011-2013 hatten sehr wenig Handel an den Börsen. Kleine Details (z.B. welcher Coin bei gleichzeitigen
Signalen zuerst Kapital bekommt) verschieben das Ergebnis um einige Prozent pro Jahr: Die Zahlen sind
Grössenordnungen, keine Vorhersage. Vergangene Ergebnisse sind keine Garantie.

## Marktphasen: der Bot wählt kurz, mittel oder lang selbst (Test: `bots/config_phasen.yaml`)

Der 5️⃣ Phasen-Bot (vorerst nur in der Simulation) bestimmt für jeden Coin aus den Tageskerzen die **Marktphase**:
Aufwärtstrend, Abwärtstrend oder Seitwärts (50- und 200-Tage-Linie), jeweils ruhig oder wild (`tradingbot/phase.py`).

- **Horizont wählen** (`phase_gate`): Für jede Phase merkt er sich, was die Trades jedes Horizonts dort gebracht
  haben. Nur ein Horizont, der in der aktuellen Phase bewiesen Geld verdient (mindestens 8 Trades, im Schnitt im
  Plus), handelt mit voller Grösse. Fehlt die Erfahrung, handelt er klein (`phase_probation`, ein Viertel); verliert
  er dort bewiesen, nur noch winzig (`phase_loser`, 5 %), damit er merkt, wenn sich das ändert. Vorwissen aus der Geschichts-Simulation liegt in `daten/state/phasen_wissen.json`
  und zählt höchstens wie 20 eigene Trades; eigene Trades setzen sich also durch.
- **Bester Einstieg**: Rücksetzer im Trend statt Ausbruch (`pullback` bei «kurz»), und mit `max_stretch_atr`
  kein Kauf, wenn der Kurs der 20er-Linie davongelaufen ist.
- **Bester Ausstieg**: Nachlauf-Stop und Teilgewinn sichern Gewinne; `phase_exit` schliesst eine Position, sobald
  die Phase des Coins gegen sie kippt (Long im Abwärtstrend; nicht bei «lang», der über die 200-Tage-Linie aussteigt).

In der Simulation lernt er ohne Vorwissen Trade für Trade (kein Blick in die Zukunft). Die Simulation läuft
automatisch auf GitHub (`.github/workflows/historie.yml`) und schreibt das Ergebnis nach `lernen/HISTORIE.md`.

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
#    Abgeschlossene Trades landen in daten/logs/trades.csv

# 4. Echtes Geld (erst nach erfolgreichem Demo-Betrieb!)
export EXCHANGE_API_KEY=...
export EXCHANGE_API_SECRET=...
CONFIRM_LIVE=JA python -m tradingbot live

# 5. Lernbericht: In welcher Marktlage hat der Bot gewonnen oder verloren?
python -m tradingbot report
```

Alle Einstellungen (Börse, Handelspaar, Strategie, Risikoregeln) stehen in `bots/config.yaml`.

## Börse wählen

Swissquote bietet für das eTrading-Konto (auch Krypto) nach meinem Kenntnisstand keine öffentliche Programmierschnittstelle. Ein Bot kann dort also nicht automatisch Orders platzieren. Vergleich (Stand Oktober 2026, Gebühren vor Kontoeröffnung auf der Website der Börse prüfen):

| Börse | API | Gebühr pro Order (kleinste Stufe) | Sicherheit / Regulierung | `exchange:` |
|---|---|---|---|---|
| Bitstamp | ja | 0,30–0,40 %, laut TradingView gebührenfrei unter 1'000 $ Monatsvolumen | EU-lizenziert, eine der ältesten Börsen | `bitstamp` |
| Kraken | ja | 0,80 % Taker, 0,40 % Maker unter 2'500 $ Monatsumsatz (Staffel seit 9.7.2026, siehe [Realistische Kosten](#realistische-kosten-wie-bei-kraken)) | MiCA-Lizenz, Proof of Reserves, CHF-Paare | `kraken` (voreingestellt) |
| Coinbase | ja | 0,40–0,60 % | US-reguliert, kein CHF | `coinbase` |
| Binance | ja | 0,10 % | keine FINMA-Lizenz, Probleme mit Behörden; nicht empfohlen | `binance` |
| Swissquote | nein | 0,5–1 % + Depotgebühr | FINMA | – |

Empfehlung: Bitstamp für den Start mit kleinem Betrag, Kraken wegen der CHF-Paare. Für Kraken rechnet `fee_model: kraken` mit der Staffel; für eine andere Börse in `bots/config.yaml` `fee_model: fix` setzen und `fee_rate` anpassen.

Den Börsennamen in `bots/config.yaml` unter `exchange` ändern. Beim API-Schlüssel **nur Handelsrechte, niemals Auszahlungsrechte** freigeben.

## Lernende Strategie (`adaptive`)

Die Standardstrategie lernt laufend aus den Ergebnissen: Für jede Teilstrategie (Trendfolge, Mean Reversion, Breakout) berechnet sie bei jeder neuen Kerze, wie viel Gewinn oder Verlust deren Signale in den letzten 200 Kerzen gebracht hätten, inklusive Gebühren. Strategien mit Verlust bekommen kein Stimmrecht, die übrigen werden nach ihrem Erfolg gewichtet. Im Trend setzt der Bot so automatisch mehr auf Trendfolge, im Seitwärtsmarkt mehr auf Mean Reversion.

Einstellbar über `strategy_params` in `bots/config.yaml`:

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

Jeder Trade wird zusammen mit der Nachrichtenlage beim Einstieg in `daten/logs/trades.csv` gespeichert (bei den anderen Configs `daten/logs/trades_<name>.csv`, z.B. `daten/logs/trades_config_langfrist.csv`). `python -m tradingbot report` zeigt dann, in welcher Lage der Bot gewinnt oder verliert, dazu die Gebühren und Zinsen aller Trades zusammen. Nach einigen Wochen Paper-Betrieb ist das die Grundlage, um die Regeln anzupassen oder später ein Machine-Learning-Modell darauf zu trainieren.

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

Mit `allow_short: true` in `bots/config.yaml` (oder `--short` beim Backtest) setzt der Bot bei Verkaufssignalen auch auf fallende Kurse. Ein Short hat einen Stop-Loss **über** dem Einstieg und ein Kursziel darunter, das Risiko pro Trade bleibt bei 1 %.

```bash
python -m tradingbot compare --short --days 365
```

Short-Handel läuft vorerst **nur im Backtest und im Paper-Modus**. Live braucht es dafür ein Margin- oder Futures-Konto. Im Paper-Modus und in der Geschichts-Simulation werden Leihzinsen berechnet (`margin_interest_per_day`) und dem Trade zugerechnet; in der Simulation 2011-2026 haben Shorts deshalb in keiner Variante Geld gebracht (siehe oben). Mit `short_probation: true` starten Shorts klein, bis sie sich bewährt haben. Bei Shorts sind die Verluste theoretisch unbegrenzt, wenn der Kurs stark steigt. Der Stop-Loss begrenzt das, aber bei Kurssprüngen kann er überrannt werden.

## Startkapital

Der Paper-Modus braucht gar kein Geld. Für echten Handel gilt: Börsen haben Mindestordergrössen (meist etwa 5 bis 10 CHF pro Order), und Gebühren von rund 0,1 bis 0,8 % pro Order (Kraken: 0,8 % unter 2'500 $ Monatsumsatz) fallen bei kleinen Beträgen stark ins Gewicht. Mit 1 CHF ist daher kein echter Handel möglich. Realistisch sind mindestens 50 bis 100 CHF.

## Risikoregeln (Standard)

- Pro Trade wird höchstens 1 % des Kapitals riskiert (Abstand zum Stop-Loss).
- Stop-Loss bei 2 × ATR unter dem Einstieg, Take-Profit bei 4 × ATR darüber.
- Höchstens 25 % des Kapitals in einer Position, alle zusammen höchstens `max_invested_pct` (long und short, alle
  Horizonte; mit Hebel entsprechend mehr). Die Grösse richtet sich immer nach dem ganzen Kapital (alle Coins zum
  aktuellen Kurs), auch direkt nachdem der Bot eine Position gedreht hat.
- Nach 3 % Tagesverlust werden für den Rest des Tages keine neuen Trades eröffnet.
- Fällt das Kapital 15 % unter den Höchststand, schliesst der Bot alles und stoppt (Not-Aus).
- Alle offenen Positionen zusammen riskieren höchstens 3 %, maximal 3 Positionen gleichzeitig.
- Höchstens 6 neue Trades pro Tag (gegen Overtrading).
- Nach 3 Verlusten in Folge 12 Stunden Pause (gegen "Revenge Trading").
- Kein Einstieg, wenn der Spread im Orderbuch grösser als 0,3 % ist.
- Stark korrelierte Positionen (z.B. BTC und ETH in gleicher Richtung) nur halb so gross; verglichen wird mit allen
  offenen Positionen, egal in welcher Reihenfolge die Coins geprüft werden.
- Mit Hebel (nur Demo): Zwangsschliessung wie an der Börse (Gebühr 2 % des Positionswerts), wenn das Kapital unter
  `liquidation_margin` der hinterlegten Sicherheit fällt, geprüft vor und nach den neuen Signalen. Den tatsächlichen
  Hebel (Wert aller Positionen geteilt durch das Kapital) zeigt die Übersicht als «Hebel aktuell».

## Langfrist-Variante (`bots/config_langfrist.yaml`)

Die ersten echten Tests (Oktober 2026, BTC/USD) haben gezeigt: Kurzfristige Strategien auf 1h und 4h verloren nach Gebühren Geld (Walk-Forward −13 % bzw. −12 %), während Bitcoin selbst teils stark stieg. Die Langfrist-Variante handelt auf Tageskerzen mit dem 200-Tage-Trendfilter (`regime`): investiert, solange der Kurs über der Linie liegt, sonst Cash. Das ergibt wenige Trades und soll vor allem grosse Abstürze vermeiden.

```bash
python -m tradingbot compare --config bots/config_langfrist.yaml --days 2500
python -m tradingbot walkforward --config bots/config_langfrist.yaml --days 2500
```

Hier ist fast das ganze Kapital investiert, Rückgänge von 20–30 % sind möglich.

**Ergebnis der echten Tests (BTC/USD, Dez. 2019 bis Okt. 2026):** `regime` +837 % gegen +738 % beim Halten, grösster Rückgang −44 % statt −77 %, Walk-Forward 2022–2026 +195 % (Halten ca. +95 %). Vergangene Ergebnisse sind keine Garantie.

### Täglicher Demo-Betrieb

Der Bot speichert seinen Stand in `daten/state/`. Er muss deshalb nicht ununterbrochen laufen, ein Durchlauf pro Tag genügt:

```bash
py -3.13 -m tradingbot paper --config bots/config_langfrist.yaml --once     # einmal laufen lassen
py -3.13 -m tradingbot status --config bots/config_langfrist.yaml           # Stand anzeigen
```

Automatisch jeden Tag um 02:30 (nach Schluss der Tageskerze um 00:00 UTC) mit der Windows-Aufgabenplanung, einmalig in PowerShell eingeben:

```
schtasks /create /tn "TradingBot" /tr "C:\trading-bot\scripts\bot_taeglich.bat" /sc daily /st 02:30
```

Der PC muss um diese Zeit eingeschaltet sein (sonst läuft der Bot beim nächsten Durchlauf). Protokoll: `logs\bot.log`. Entfernen: `schtasks /delete /tn "TradingBot"`.

Hinweis: Bei einem Durchlauf pro Tag spielt der Demo-Bot die Stops rückwirkend mit 5-Minuten-Kerzen nach (siehe
[Stops minutengenau](#stops-minutengenau-demo-betrieb)); Signale und Not-Aus prüft er aber nur einmal täglich, und mit
echtem Geld würde auch ein Stop nur dann greifen.

## KI-Gedächtnis und Strategie-Labor

Der KI-Bot (`bots/config_daytrading.yaml`, Strategie `adaptive_memory`) hat ein dauerhaftes Gedächtnis
(`daten/state/ki_gedaechtnis.json`): Für jede Marktphase (Trend auf/ab/seitwärts, ruhig/wild) merkt er sich, wie viel
jede Strategie dort gebracht hätte. Es startet mit einem Jahr Kursgeschichte und wächst bei jedem Lauf. Je mehr
Erfahrung, desto stärker verlässt er sich darauf statt nur auf die letzten Wochen.

Das Strategie-Labor (`python -m tradingbot labor`, auf GitHub jeden Sonntag) erfindet aus den vorhandenen Bausteinen
neue Regeln, entwickelt sie auf älteren Kursen weiter und prüft sie auf den neuesten, unbekannten Kursen. Nur bestandene
kommen in die Bibliothek (`daten/state/strategie_bibliothek.json`) und werden vom KI-Bot mitbenutzt. Bericht:
[lernen/LABOR.md](lernen/LABOR.md). Die KI kombiniert dabei nur geprüfte Bausteine und schreibt keinen freien Code.

## Eigene Strategie hinzufügen

In `tradingbot/strategies.py` eine Klasse von `Strategy` ableiten, `signals()` implementieren (+1 kaufen, -1 verkaufen, 0 neutral) und in `STRATEGIES` eintragen. Der Test `test_no_lookahead` prüft automatisch, dass die Strategie nicht in die Zukunft schaut.

## Grenzen dieser Version

- Live nur Spot-Handel (kein Short, kein Hebel). Short nur im Backtest/Paper.
- News und Ereignisse werden über Stichwörter bewertet, nicht über ein Sprachmodell. Ironie oder komplexe Meldungen erkennt das nicht.
- Stops überwacht der Bot selbst: im Demo-Betrieb alle 30 Minuten rückwirkend mit den Minutenkerzen, live nur zum Kurs
  beim Lauf. Echte Stop-Orders an der Börse folgen später.
- Die Quellen-URLs (News, Fed, SEC, Kalender) konnten bei der Entwicklung nicht live getestet werden. Beim ersten `paper`-Lauf im Protokoll prüfen, ob sie ankommen.
- Backtest ohne historische News.
- Der Paper-Modus speichert seinen Stand nicht über einen Neustart hinweg.
