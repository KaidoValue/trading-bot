# Profi-Bot «Kern zuerst»: Vorab-Registrierung

- **Eingefrorene Fassung:** Commit _(noch leer: wird vor dem ersten E0-Lauf eingetragen)_
- **Fassung mit Stufe 2 (E3/E4):** _(nur falls gebaut: Commit, ab dem E3 rechnet)_
- **E6-Kandidat:** _(offen: nach E5 eintragen, mit `--config`, `--sieger` und Commit)_
- **Massstab:** Calmar. Bestätigung durch Hiran: _(offen, vor E0)_
- **Registriert:** 5.11.2026, bevor eine einzige Profi-Zahl mit echten Kursen gerechnet ist. Bis hier liefen alle
  Profi-Tests nur mit synthetischen Kursen.

Dieser Plan legt vor der ersten Rechnung fest, was geprüft wird, mit welchen Configs, Fenstern und Zahlen, und nach
welchen Regeln entschieden wird. Grundlage ist der Entwurf «Kern zuerst» (Fassung 2) vom 31.10.2026. Wo der Entwurf
von «1'000er-Starts» spricht, gilt seit Hirans Neustart vom 2.11.2026 ein Startkapital von 100 für alle Bots.

## Worum es geht

Der Profi-Bot ist eine Bewährungsleiter. Die unterste Sprosse ist P−1: nur Bitcoin, über der 200-Tage-Linie ganz
investiert, darunter ganz in Cash. Der Kern handelt BTC/CHF (und ETH/CHF nur, wenn ETH sich beweist) nach der
200-Tage-Linie, mit Grösse nach Schwankung, höchstens 75 % investiert, ohne Hebel, ohne Short und ohne News-Pausen.
Jede weitere Schicht (ETH, Not-Aus, Wochentakt, Grösse nachführen) muss sich nach Kraken-Kosten gegen die einfachere
Stufe darunter beweisen, sonst bleibt die einfachere. Die eingefrorene Fassung wird genau einmal auf den Jahren ab
2023 geprüft und startet nur bei Go und nur nach Hirans Zustimmung als 5. Demo-Bot.

## Spielregeln

1. **Vorab festgelegt.** Regeln, Zahlen, Configs, Überlagerungen und Fenster in dieser Datei ändern sich nach dem
   Eintrag der eingefrorenen Fassung nicht mehr. Danach werden nur die Felder oben ausgefüllt (Massstab, Commits,
   E6-Kandidat). Jede andere Änderung wäre ein neuer Plan: neu registrieren und alle Schritte neu rechnen.
2. **Derselbe Code.** Jeder Lauf rechnet mit einem Commit, dessen `tradingbot/` und `bots/` gleich sind wie in der
   eingefrorenen Fassung (`git diff <Fassung> <Commit des Laufs> -- tradingbot bots` ist leer). Die Ergebnisdateien
   nennen den Commit, der Bericht nennt die eingefrorene Fassung. Einzige Ausnahme ist der Code der Stufe 2 für
   E3/E4: eigener Commit, hier eingetragen, mit grünem Test, dass die vier Bots und Configs ohne die neuen Schlüssel
   genau gleich rechnen; sonst werden E0 bis E2 neu gerechnet.
3. **Blind auswählen.** Ausgewählt wird nur mit den Jahren 2012 bis 2022. Ohne `--pruefung` schneidet `profi` alle
   Kurse ab 2023 vor jeder Berechnung ab und verweigert jedes Fenster, das Tage ab 2023-01-01 berührt (auch ein
   offenes Ende). Die Jahre ab 2023 werden genau einmal geöffnet: in E6, je Quelle ein Lauf mit `--pruefung`, und
   jeder solche Lauf steht vor der Rechnung im Prüfprotokoll. An 2023-2026 wird nichts nachjustiert.
4. **Kein Nachbessern.** Durchgefallen heisst zurück zur einfacheren Stufe, nie neue Varianten.
5. **Frische Starts.** Jedes Fenster ist ein eigener Start mit `starting_capital` der Config (100 wie bei den
   Demo-Bots seit dem Neustart am 2.11.2026). Kein Dauerlauf ab 2011.
6. **Gleiche Kosten für alle.** Entschieden wird nur mit `--gebuehren normiert`: Kraken-Stufe wie für ein Konto mit
   dem Startkapital (30-Tage-Umsatz × Startkapital / Kapital), also Taker 0,80 % je Order, dazu Slippage 0,05 % je
   Seite; eine Rundreise kostet rund 1,7 %. Die heutigen Bots, K1, P−1 und Bitcoin halten werden genau gleich
   gerechnet. `--gebuehren alt` (fest 0,26 %) gibt es nur als Kontrolle in E0, `staffel` nie für Entscheide.
7. **Die vier Demo-Bots bleiben unverändert** (Langfrist, KI, Risiko und Chef; Test «die vier Bots bleiben
   unverändert»). Profi-Configs laufen nie als Demo-Bot und nie in `historie.yml`.

## Massstab

Calmar = Rendite pro Jahr (CAGR) geteilt durch den grössten Rückgang (|Max. DD|), wie `historie.segment` ihn rechnet
(zwei Nachkommastellen). Er belohnt weniger Rückgang bei etwas weniger Rendite. Hiran bestätigt den Massstab vor E0
(Feld oben); bis dahin gilt Calmar. Ein anderer Massstab, zum Beispiel die reine Rendite, darf nur vor der ersten
Rechnung festgelegt werden: Dann werden diese Datei und die Auswertung angepasst und neu registriert, bevor E0 läuft.
Nach der ersten Rechnung gilt der eingetragene Massstab bis zum Entscheid.

## Daten und Caches

| Cache | Quellen | Eingefroren | zählt für |
|---|---|---|---|
| GitHub (Haupt-Cache) | Standardquellen bitstamp, binance, binanceus, kucoin. Binance sperrt GitHub-Server, darum kommen die Altcoins von binanceus bzw. kucoin; Bitcoin kommt von Bitstamp ab 2011 | GitHub-Cache mit festem Schlüssel `profi-2026-11-03`, ohne restore-keys; Fingerabdruck in `lernen/profi/cache_github.txt` | Entscheide |
| Hirans PC (Haupt-Cache) | dieselben Standardquellen, dort ist Binance erreichbar (Altcoins von Binance, Bitcoin von Bitstamp) | Zip `%USERPROFILE%\trading-bot-profi\data\profi_cache.zip`; Fingerabdruck in `lernen/profi/cache_pc.txt` | Entscheide |
| Dritte Quelle | coinbase mit eigenem BTC und ETH, sonst bitfinex (`--quellen`) | eigene Dateien im GitHub-Cache | nur E5 (c) und die Warnung in E6 |

- Der erste GitHub-Lauf auf dem Profi-Zweig lädt alle Kurse für E0 bis E6 und die dritte Quelle (`profi --laden`) und
  speichert den Cache. Danach wird er nur gelesen (`--cache-fest`), und jeder Job prüft den Fingerabdruck. Auf dem PC
  lädt der erste Lauf die Kurse und friert sie als Zip ein; danach rechnet jeder Lauf nur mit dem Zip.
- Vor dem Einfrieren prüft `profi --laden`, dass jede BTC-Datei der Haupt-Caches von Bitstamp kommt und spätestens am
  31.12.2011 beginnt. Sonst bricht es ab, und nichts wird eingefroren (eine einzige gescheiterte Anfrage bei Bitstamp
  liesse sonst still eine andere Börse mit kürzerer Geschichte einspringen); später nochmals laden.
- Datenende ist die letzte Kerze im eingefrorenen Cache; «bis Datenende» heisst bis dorthin.
- BTC kommt in beiden Haupt-Caches von Bitstamp. Unabhängig prüft nur die dritte Quelle, und die beginnt erst
  2015/2016.
- **Haupt-Caches** sind Ergebnisse mit den Standardquellen. Nur sie und nur mit normierten Gebühren zählen für
  Entscheide; jede Regel muss in jedem Haupt-Cache gelten. Ein Schritt ist erst entschieden, wenn er in jedem
  Haupt-Cache gerechnet ist: Bis dahin zeigt der Bericht seine Entscheide als vorläufig, und der nächste Schritt startet
  erst danach (sein Amtsinhaber hängt am Sieger). Fehlt der PC-Lauf, zählt der GitHub-Cache allein; das entscheidet
  Hiran ausdrücklich vor dem nächsten Schritt, und der Bericht zeigt es als Schwäche.
- **Cache verloren** (GitHub löscht einen Cache nach 7 Tagen ohne Zugriff und gibt ihn nur dem Zweig, auf dem er
  entstand; das Zip auf dem PC gelöscht): nicht neu laden, der Ablauf bricht ab. Hiran entscheidet; neu einfrieren
  heisst neuer Cache und alle Schritte auf diesem Cache neu rechnen. Darum laufen alle Profi-Läufe auf dem Zweig
  `claude/project-thread-usz8e3`, mit höchstens 7 Tagen zwischen zwei GitHub-Läufen.

## Fenster

Jedes Fenster ist ein frischer Start mit dem Startkapital. «Bitcoin halten nach Kosten» rechnet in jedem Fenster mit.

| Schritt | Bot | Fenster |
|---|---|---|
| E0 | Langfrist, KI, Risiko, Phasen, Chef, K1, P−1 | 2012-2022 (2012-01-01 bis 2022-12-31) |
| E1 bis E4 | Amtsinhaber, Herausforderer, P−1 | 2012-2022, 2012-2019 (bis 2019-12-31), 2020-2022 (ab 2020-01-01) |
| E5 | Kandidat | 2012-2022, 2016-2022, die 28 3-Jahres-Fenster, Crash-2014 und Crash-2018 (ab 2014-01-01 bzw. 2018-01-01, je bis 2022-12-31) |
| E5 | Nachbarwerte und Kostenstress | 2012-2022 |
| E5 | P−1 | 2016-2022 |
| E6 | Kandidat | die 12 gestaffelten Starts ab-2023Q1 bis ab-2025Q4 und Crash-2022 (ab 2022-01-01), alle bis Datenende |
| E6 | Variante ohne Not-Aus (nur bei E2-Flagge) | ab-2023Q1, Crash-2022 |
| E6 | K1 | ab-2023Q1 |
| E6 | P−1 | ab-2023Q1, Crash-2022 |
| E6 | Langfrist, KI, Risiko, Phasen, Chef | die 12 gestaffelten Starts |

- **28 3-Jahres-Fenster (E5 d),** Start vierteljährlich, je drei Jahre: 3J-2013Q1 (2013-01 bis 2015-12),
  3J-2013Q2 (2013-04 bis 2016-03), 3J-2013Q3 (2013-07 bis 2016-06), 3J-2013Q4 (2013-10 bis 2016-09), 3J-2014Q1
  (2014-01 bis 2016-12), 3J-2014Q2 (2014-04 bis 2017-03), 3J-2014Q3 (2014-07 bis 2017-06), 3J-2014Q4 (2014-10 bis
  2017-09), 3J-2015Q1 (2015-01 bis 2017-12), 3J-2015Q2 (2015-04 bis 2018-03), 3J-2015Q3 (2015-07 bis 2018-06),
  3J-2015Q4 (2015-10 bis 2018-09), 3J-2016Q1 (2016-01 bis 2018-12), 3J-2016Q2 (2016-04 bis 2019-03), 3J-2016Q3
  (2016-07 bis 2019-06), 3J-2016Q4 (2016-10 bis 2019-09), 3J-2017Q1 (2017-01 bis 2019-12), 3J-2017Q2 (2017-04 bis
  2020-03), 3J-2017Q3 (2017-07 bis 2020-06), 3J-2017Q4 (2017-10 bis 2020-09), 3J-2018Q1 (2018-01 bis 2020-12),
  3J-2018Q2 (2018-04 bis 2021-03), 3J-2018Q3 (2018-07 bis 2021-06), 3J-2018Q4 (2018-10 bis 2021-09), 3J-2019Q1
  (2019-01 bis 2021-12), 3J-2019Q2 (2019-04 bis 2022-03), 3J-2019Q3 (2019-07 bis 2022-06), 3J-2019Q4 (2019-10 bis
  2022-09). Jedes beginnt am ersten Tag des Startmonats und endet am letzten Tag des Endmonats.
- **12 gestaffelte Starts (E6),** jeweils bis Datenende: ab-2023Q1 (ab 2023-01-01, das Prüffenster), ab-2023Q2,
  ab-2023Q3, ab-2023Q4, ab-2024Q1, ab-2024Q2, ab-2024Q3, ab-2024Q4, ab-2025Q1, ab-2025Q2, ab-2025Q3, ab-2025Q4 (ab
  2025-10-01).

## Kennzahlen und Bootstrap

- **Je Lauf** (aus `historie.segment`): Rendite %, CAGR (pro Jahr %), Max. DD %, Calmar, Trades, Treffer %, Profit
  Factor, Gebühren bezahlt, Kosten in % pro Jahr (Gebühren + Slippage + Zinsen, pro Jahr im Verhältnis zum
  Ø Kapital), Umschlag pro Jahr (gehandelter Wert im Verhältnis zum Ø Kapital), Ø investiert %, Zeit im Markt %,
  Kostenanteil am Bruttogewinn %, Trades je Coin und Jahr, Zahl der Not-Aus. Dazu die Kapitalkurve je Tag.
- **Bitcoin halten nach Kosten:** ein Kauf am ersten Tag zum Schlusskurs mit Taker-Gebühr 0,80 % (mit
  `--gebuehren alt` 0,26 %) und Slippage 0,05 %, danach nur halten.
- **Bootstrap:** gepaarter Block-Bootstrap auf den Tagesrenditen beider Kapitalkurven über dieselben Tage,
  30-Tage-Blöcke, 1'000 Ziehungen, Seed 2026. Ergebnis: P(Calmar A > Calmar B). In Regel G (G3) der Herausforderer
  gegen den Amtsinhaber 2012-2022, in E6 der Kandidat gegen Bitcoin halten (nur zur Information).

## Configs

Alle Configs: `mode: paper`, `fee_model: kraken`, `slippage: 0.0005`, `starting_capital: 100`, `leverage: 1.0`,
`allow_short: false`, keine News- und Ereignis-Pausen. Sie liegen in `bots/profi/` und laufen nur in der Simulation
(`scripts/reset_paper.py` und die Bot-Läufe lesen nur `bots/config*.yaml`).

| Name | Datei | Inhalt |
|---|---|---|
| P−1 | `bots/profi/p_minus_1.yaml` | nur BTC/CHF; Horizont `kern` wie im Kern (regime, period 200, band 0.03, share 1.0, trend_filter false); risk: risk_per_trade 100, stop_loss_atr 100, take_profit_atr 1000, max_position_pct 1.0, max_invested_pct 1.0, max_daily_loss_pct 1.0, max_drawdown_pct 0.99, halt_days 0, max_total_risk_pct 1000, max_open_positions 1, loss_streak_pause 99, correlation_limit 1.01, leverage 1.0. Über der Linie rund 99 % investiert (Cash × 0,99), darunter 0 % |
| K1 | `bots/profi/k1.yaml` | Kopie von `bots/config_langfrist.yaml` nur mit dem Horizont `lang` (share 1.0), `use_news: false`, `use_events: false`; alles andere wie beim Langfrist-Bot |
| Kern, Amtsinhaber von E1 | `bots/profi/e1_kb3.yaml` | symbols [BTC/CHF]; Horizont `kern`: timeframe 1d, regime, period 200, band 0.03 (Kauf über Linie +1 %, Verkauf unter Linie −3 %), share 1.0, trend_filter false; reevaluate true, adaptive_shares false, horizon_priority false, phase_gate false, phase_exit false; risk: risk_per_trade 0.12, stop_loss_atr 8.0, take_profit_atr 1000, max_position_pct 0.75, slot_cap true, max_invested_pct 0.75, max_daily_loss_pct 0.15, max_drawdown_pct 0.35, halt_days 30, min_order_value 10, max_total_risk_pct 1.0, max_open_positions 2, max_trades_per_day 6, loss_streak_pause 99, pause_hours 0, max_spread_pct 0.003, correlation_limit 1.01, leverage 1.0 |

Grösse im Kern: 12 % Risiko bis zum Notfall-Stop bei 8 ATR, also Gewicht ≈ 1,5 % / ATR %; mit `slot_cap` ist der
Deckel je Coin 75 % geteilt durch die Zahl der Coins mit mindestens 200 Tageskerzen (BTC allein 75 %, mit ETH je
37,5 %). Not-Aus bei 35 % Rückgang vom Höchststand: alles verkaufen, 30 Tage Pause, danach gilt ein neuer Höchststand.

### Herausforderer der Leiter

Überlagerungen (deep merge) auf den jeweiligen Amtsinhaber in `bots/profi/varianten/`: nur die geänderten Schlüssel;
Listen ersetzen den Wert. Nr. = Platz in `--varianten`, die einfachere Variante zuerst.

| Schritt | Nr. | Datei | Überlagerung |
|---|---|---|---|
| E1a | 1 | `e1_kb5.yaml` | `horizons.kern.strategy_params.band: 0.05` (Kauf über Linie +1,67 %, Verkauf unter Linie −5 %) |
| E1b | 1 | `e1_kbe.yaml` | `symbols: [BTC/CHF, ETH/CHF]` |
| E2 | 1 | `e2_ohne_notaus.yaml` | `risk.max_drawdown_pct: 0.99` |
| E2 | 2 | `e2_trail6.yaml` | `horizons.kern.trail_atr: 6`, `risk.max_drawdown_pct: 0.99` |
| E3 | 1 | `e3_kauf_woche.yaml` (Stufe 2) | `horizons.kern.entry_weekday: 6` |
| E3 | 2 | `e3_beides_woche.yaml` (Stufe 2) | `horizons.kern.entry_weekday: 6`, `horizons.kern.exit_weekly: true` |
| E4 | 1 | `e4_nur_kleiner.yaml` (Stufe 2) | `horizons.kern.resize: nur_kleiner`, `horizons.kern.resize_band: 0.05` |
| E4 | 2 | `e4_beides.yaml` (Stufe 2) | `horizons.kern.resize: beides`, `horizons.kern.resize_band: 0.05` |

Die Schlüssel für E3 und E4 kommen erst mit dem Code der Stufe 2 (`config.load` bricht bei unbekannten Schlüsseln ab).
Die vier Dateien entstehen erst dann, mit genau diesem Inhalt:

```yaml
# bots/profi/varianten/e3_kauf_woche.yaml
horizons:
  kern:
    entry_weekday: 6
```

```yaml
# bots/profi/varianten/e3_beides_woche.yaml
horizons:
  kern:
    entry_weekday: 6
    exit_weekly: true
```

```yaml
# bots/profi/varianten/e4_nur_kleiner.yaml
horizons:
  kern:
    resize: nur_kleiner
    resize_band: 0.05
```

```yaml
# bots/profi/varianten/e4_beides.yaml
horizons:
  kern:
    resize: beides
    resize_band: 0.05
```

Bedeutung (Stufe 2, Standardwerte ändern nichts): `entry_weekday` 0-6 (0 = Montag, 6 = Sonntag, leer = täglich):
gekauft wird nur, wenn die Signalkerze dieser Wochentag ist, gemessen an der Kerzenzeit und nicht an der Laufzeit;
der Kaufentscheid der Sonntagskerze (UTC) gilt bis Dienstag 00:00 UTC, die Simulation kauft zum Eröffnungskurs am
Montag. Verkauft wird täglich, ausser mit `exit_weekly: true`; Stops greifen immer. Nach einem Verkauf oder Stop
wird frühestens mit der nächsten Kaufkerze gekauft. `resize` (aus | nur_kleiner | beides, Standard aus) mit
`resize_band` (Standard 0.05): Ziel = Kapital × min(Deckel, 1,5 % / ATR %) mit aktuellem Kapital und Kurswert;
täglich verkleinern, wenn die Position mehr als 5 Prozentpunkte über dem Ziel liegt; mit `beides` zusätzlich an
Kauftagen vergrössern, wenn sie mehr als 5 Prozentpunkte darunter liegt.

### Robustheit E5: Nachbarwerte und Kostenstress

Überlagerungen auf den Leiter-Sieger, jeweils einzeln; keine Auswahl.

| Kriterium | Dateien in `bots/profi/varianten/` | Überlagerung | gilt |
|---|---|---|---|
| (a) Linie 150/250 | `e5_linie150.yaml`, `e5_linie250.yaml` | `horizons.kern.strategy_params.period: 150` bzw. `250` | immer |
| (a) Puffer ±0,01 | `e5_puffer002.yaml` und `e5_puffer004.yaml` | `horizons.kern.strategy_params.band: 0.02` bzw. `0.04` | wenn der Sieger Puffer 0,03 hat |
| (a) Puffer ±0,01 | `e5_puffer004.yaml` und `e5_puffer006.yaml` | `horizons.kern.strategy_params.band: 0.04` bzw. `0.06` | wenn der Sieger Puffer 0,05 hat (e1_kb5) |
| (a) Risiko 9/15 % | `e5_risiko09.yaml`, `e5_risiko15.yaml` | `risk.risk_per_trade: 0.09` bzw. `0.15` | immer |
| (a) Stop 6/10 ATR | `e5_stop6.yaml`, `e5_stop10.yaml` | `risk.stop_loss_atr: 6.0` bzw. `10.0` | immer |
| (a) investiert 60/90 % | `e5_investiert60.yaml`, `e5_investiert90.yaml` | `risk.max_invested_pct: 0.60` bzw. `0.90` | immer |
| (a) Not-Aus 30/40 % | `e5_notaus30.yaml`, `e5_notaus40.yaml` | `risk.max_drawdown_pct: 0.30` bzw. `0.40` | wenn der Not-Aus nach E2 bleibt |
| (a) Kauf-Wochentag | `e5_wochentag0.yaml` bis `e5_wochentag5.yaml` (Stufe 2) | `horizons.kern.entry_weekday: 0` bis `5` (die anderen sechs Wochentage) | wenn der Wochentakt nach E3 bleibt |
| (a) Band 3/8 Prozentpunkte | `e5_nachfuehren003.yaml`, `e5_nachfuehren008.yaml` (Stufe 2) | `horizons.kern.resize_band: 0.03` bzw. `0.08` | wenn das Nachführen nach E4 bleibt |
| (b) Kostenstress | `e5_kostenstress.yaml` | `fee_factor: 1.5`, `slippage: 0.001` (Gebühren × 1,5, Slippage × 2) | immer |

Die Dateien für Wochentag und Band entstehen wie die von E3/E4 erst mit Stufe 2, mit genau dieser Überlagerung. In
`--varianten` stehen sie in der Reihenfolge der Tabelle, der Kostenstress zuletzt. Eine Überlagerung, die nur
`fee_factor` und `slippage` ändert, zählt als Kostenstress (b), alle anderen als Nachbarwerte (a).

## Experimente und Regeln

### E0 Messlatte

Wie stehen die heutigen Bots, der Chef, K1, P−1 und Bitcoin halten mit realistischen Kosten da, frisch mit 100?
Gerechnet werden Langfrist, KI, Risiko, Phasen, Chef (aus den drei Stil-Bots), K1, P−1 und Bitcoin halten nach
Kosten, 2012-2022, auf beiden Haupt-Caches; dazu derselbe Lauf mit `--gebuehren alt` als Kontrolle. Hier wird nichts
ausgewählt. Je Haupt-Cache wird **L_dev** eingefroren: der höchste Calmar 2012-2022 aus Langfrist, KI, Risiko,
Phasen, Chef, K1, P−1 und Bitcoin halten nach Kosten. Der Vergleich alte gegen normierte Kosten geht unverändert in
den Bericht.

### Regel G (E1 bis E4)

Ein Herausforderer ersetzt den Amtsinhaber nur, wenn in jedem Haupt-Cache alle vier Bedingungen gelten:

- **G1:** Calmar 2012-2022 mindestens Amtsinhaber + 0,05.
- **G2:** in keiner Hälfte (2012-2019, 2020-2022) ein tieferer Calmar als der Amtsinhaber.
- **G3:** gepaarter Block-Bootstrap 2012-2022: P(Calmar besser als der Amtsinhaber) ≥ 0,65.
- **G4:** Kosten ≤ 3 % pro Jahr und Umschlag ≤ 4 × Kapital pro Jahr (2012-2022).

Sonst bleibt der Amtsinhaber, auch wenn die Caches verschieden urteilen. Bei Gleichstand gewinnt die einfachere
Variante.

### E1 Kern

- **E1a:** Amtsinhaber `e1_kb3` (nur BTC/CHF, Puffer 0,03) gegen `e1_kb5` (Puffer 0,05).
- **E1b:** der Sieger aus E1a gegen dieselbe Config mit ETH/CHF (`e1_kbe`). Mit `slot_cap` hält BTC bis 75 %, bis ETH
  200 Tageskerzen Geschichte hat (etwa ab März 2018), danach je Coin 37,5 %.
- Entscheid je Stufe nach Regel G.
- **Tor nach E1:** Weiter geht es nur, wenn der E1-Sieger in jedem Haupt-Cache Calmar 2012-2022 ≥ 0,85 × L_dev
  (desselben Caches) und Kosten ≤ 3 % pro Jahr erreicht. Sonst wird die Leiter abgebrochen und so berichtet; E2 bis E5
  entfallen, und E6 prüft nur P−1 und K1 als Kandidaten, nach denselben Go-Regeln.

### E2 Sicherheitsnetz

Hilft der Not-Aus wirklich, oder bekommt er nur Gewinne gutgeschrieben, die die Linie auch geholt hätte? Amtsinhaber
ist der E1-Sieger mit Not-Aus 35 % / 30 Tage, Herausforderer sind `e2_ohne_notaus` (Nr. 1) und `e2_trail6` (Nr. 2,
Nachlauf-Stop 6 ATR, ohne Not-Aus). Für jeden Not-Aus des Amtsinhabers wird festgehalten, zu welchem Kurs und an
welchem Tag die Linie später verkauft hätte und wie gross die verpasste Erholung war (Rendite der 90 Tage danach).

- Es gilt Regel G; bei Gleichstand bleibt der Not-Aus.
- **E2-Flagge:** Hängt der Vorteil des Not-Aus an höchstens 2 Ereignissen, wird eine Flagge gesetzt. Dann muss in E6
  auch die Variante ohne Not-Aus (`e2_ohne_notaus` auf dem Kandidaten) die Go-Regeln 1-4 erfüllen.

### E3 Wochentakt (nur mit dem Code der Stufe 2)

Senkt Kaufen nur mit der Wochenkerze die Fehlsignale und Kosten so stark, dass der Calmar steigt? Amtsinhaber ist der
E2-Sieger (täglich kaufen und verkaufen), Herausforderer `e3_kauf_woche` (Nr. 1) und `e3_beides_woche` (Nr. 2).
Zusätzlich werden die Fehlsignale (Rundreisen unter 30 Tagen) je Coin und Jahr gezählt (kommt mit Stufe 2). Es gilt
Regel G; bei Gleichstand bleibt «täglich».

### E4 Grösse nachführen (nur mit dem Code der Stufe 2)

Machen harte Deckel (täglich verkleinern, nur an Kauftagen vergrössern) den Kern nach Kosten besser? Amtsinhaber ist
der E3-Sieger ohne Anpassung, Herausforderer `e4_nur_kleiner` (Nr. 1) und `e4_beides` (Nr. 2). Die Abgleich-Zeile
(Kapital = Start + Trades + offene Positionen) muss in jedem Simulationsschritt 0,00 ergeben; dazu Zahl und Kosten der
Anpassungs-Orders (kommt mit Stufe 2). Es gilt Regel G, mit besonderem Blick auf G4; bei Gleichstand bleibt «keine
Anpassung».

### E5 Robustheit (keine Auswahl)

Hält der Leiter-Sieger, wenn sich Kleinigkeiten ändern, noch ohne Blick auf 2023-2026? Nur bis 2022, frisch mit 100,
normierte Gebühren. **Bestanden, wenn in jedem Haupt-Cache alle Punkte gelten:**

- **(a)** Jeder Nachbarwert erreicht mindestens 75 % des Calmar 2012-2022 des Kandidaten.
- **(b)** Unter Kostenstress (Gebühren × 1,5, Slippage × 2) ist der Calmar 2012-2022 mindestens so hoch wie bei
  Bitcoin halten nach Kosten.
- **(c)** Auf der dritten Quelle (frisch 2016-2022) bleiben die Vorzeichen der Calmar-Unterschiede zu Bitcoin halten
  und zu P−1 dieselben wie im Haupt-Cache.
- **(d)** In mindestens 60 % der 28 3-Jahres-Fenster liegt der Calmar über Bitcoin halten, und in mindestens 75 %
  beträgt der Max. DD höchstens 0,6 × Bitcoin halten.
- **(e)** Bei den Crash-Starts 2014 und 2018 beträgt der Max. DD höchstens 0,6 × Bitcoin halten ab demselben Tag.

**Durchgefallen:** zurück zum E1-Sieger und nur diesen prüfen (E5 mit seinen Nachbarwerten), keine neuen Varianten.
Fällt auch er durch, gibt es kein E6 für den Kern, sondern ein No-Go mit Begründung.

### E6 Einmal-Prüfung

Schlägt die eingefrorene Fassung auf den weggesperrten Jahren ab 2023 die heutigen Bots, P−1 und Bitcoin halten?
Nach E5 wird der Kandidat eingefroren (Feld «E6-Kandidat» oben, mit Commit). Danach genau ein Lauf mit `--pruefung`
je Quelle (GitHub-Cache, PC-Cache, dritte Quelle), frisch mit 100 ab 01.01.2023 bis Datenende, normierte Gebühren,
mit den Fenstern oben. Mitgerechnet: Langfrist, KI, Risiko, Phasen, Chef, K1, P−1, Bitcoin halten nach Kosten und,
falls in E2 geflaggt, die Variante ohne Not-Aus; dazu der Crash-Start 01.01.2022 und die 12 gestaffelten Starts.

**Go nur, wenn in jedem Haupt-Cache alle Regeln gelten** (Fenster ab-2023Q1, wo nichts anderes steht):

1. Calmar ≥ bester Wert aus Langfrist, KI, Risiko, Phasen, Chef und K1, plus 0,10.
2. Calmar ≥ Bitcoin halten nach Kosten und ≥ P−1 − 0,05.
3. Max. DD ≤ 0,6 × Bitcoin halten, ebenso beim Crash-Start 2022.
4. CAGR ≥ ⅓ von Bitcoin halten (vorab von 0,5 gesenkt, weil 0,5 bei höchstens 75 % Investitionsgrad mit dem
   Calmar-Ziel kollidiert).
5. Kosten ≤ 3 % pro Jahr und Kostenanteil am Bruttogewinn ≤ 25 %.
6. In mindestens 8 der 12 gestaffelten Starts besser als der beste heutige Bot (nach Calmar; ist die Rendite bei
   beiden negativ, zählt die höhere Rendite).
7. Bei gesetzter E2-Flagge erfüllt auch die Variante ohne Not-Aus die Regeln 1-4.

**Sonderfall P−1:** Ist P−1 im Prüffenster um mehr als 0,05 besser (Calmar), ist es ein No-Go für den Kern. P−1 wird
dann vorgeschlagen, falls es die Regeln 1 und 3-5 erfüllt.

**Nur zur Information:** die dritte Quelle und der Bootstrap gegen Bitcoin halten. Zeigt die dritte Quelle bei
Regel 2 ein anderes Vorzeichen als ein Haupt-Cache, steht im Bericht eine Warnung.

Ist das Tor nach E1 nicht bestanden, sind P−1 und K1 die Kandidaten, je mit den Go-Regeln (für P−1 entfällt der
Sonderfall). Ist E6 bis 19.11. nicht fertig, wird der Entscheid verschoben.

### E7 Demo-Abgleich nach dem Start (nur bei Go)

Ab dem Start wird jede Woche der Demo-Zeitraum auf Kraken-CHF-Tageskerzen nachgerechnet und Order für Order
verglichen: Tag, Richtung, Grösse, Kosten und bezahlter halber Spread; dazu täglich die Abgleich-Zeile (Kapital =
Start + Trades + offene Positionen). Der Bot wird angehalten und der Fehler behoben, wenn mehr als 10 % der Orders
abweichen (Tag um mehr als 1 verschoben, andere Richtung oder Grösse über ±20 %) oder die Kosten über dem 1,5-fachen
der Simulation liegen. Liegt der halbe Spread im Mittel über 0,15 %, wird ein festes Ausführungsfenster am Tag als
Variante simuliert. Regeln werden frühestens nach 6 Monaten geändert und nur mit neuer Simulation nach diesem Plan.
Der Code dafür kommt mit Stufe 4.

Später und nicht Teil dieser Prüfung: E8 Altcoin-Satellit im Schatten (frühestens Februar 2027), E9 Limit-Orders,
E10 News im Schattenmodus, E11 Franken-Sicht.

## Auslegungen

Vor der ersten Rechnung festgehalten; so rechnet `tradingbot/auswertung.py`.

- **Fehlende Zahl:** Fehlt eine Zahl (Lauf fehlt, Kennzahl leer), gilt die Bedingung als nicht erfüllt.
- **Grenzwerte** gelten auf den gerundeten Kennzahlen (Calmar zwei Nachkommastellen, Prozente eine bzw. zwei), mit
  einer Toleranz von 10⁻⁹, damit zum Beispiel 0,30 + 0,05 ≤ 0,35 gilt. «Über» und «besser» heissen echt grösser.
- **Mehrere Herausforderer:** Bestehen mehrere Regel G, muss der spätere (komplexere) auch den früheren nach Regel G
  schlagen, sonst bleibt die einfachere Variante.
- **Weg durch die Leiter:** E1 beginnt bei e1_kb3, dem Amtsinhaber von E1a. Gewinnt e1_kb5, ist «e1_kb3+e1_kb5» in
  E1b Amtsinhaber, und seine Ergebnisdateien behalten beide Rollen (`rollen`). E2 geht vom Sieger von E1 aus, E3 vom
  Sieger von E2, E4 vom Sieger von E3 (fehlt eine Stufe, vom letzten Sieger davor). Gruppen mit einem anderen
  Amtsinhaber, zum Beispiel nach einer Rechnung mit einem früheren Sieger, zeigt der Bericht als überholt; sie zählen
  weder für den Sieger noch für die E2-Flagge.
- **Vorläufig:** Fehlen einem Haupt-Cache Läufe eines Schritts, die ein anderer Haupt-Cache hat, sind Sieger, Tor,
  Flagge und Entscheid dieses Schritts vorläufig (so im Bericht). Hat er gar keine Läufe des Schritts, ist ohne ihn
  entschieden; sonst gelten seine fehlenden Zahlen als nicht erfüllt.
- **Tor:** Fehlt E0 im selben Cache, gibt es dort kein L_dev, und das Tor gilt als nicht bestanden.
- **E2-Flagge:** Sie gilt, wenn der Not-Aus bleibt (der Amtsinhaber gewinnt E2) und er 2012-2022 in mindestens einem
  Haupt-Cache höchstens 2-mal auslöst.
- **Regel G4 und Go-Regel 5:** Umschlag und Kosten pro Jahr im Verhältnis zum Ø Kapital; Kosten = Gebühren +
  Slippage + Zinsen. Ohne Bruttogewinn gibt es keinen Kostenanteil, Regel 5 gilt dann als nicht erfüllt.
- **E5 (b)** vergleicht mit Bitcoin halten zu normalen Kosten; **E5 (c)** mit den Calmar-Unterschieden 2016-2022
  (Kandidat minus Bitcoin halten, Kandidat minus P−1), gleich heisst dasselbe Vorzeichen in jedem Haupt-Cache.
- **Rücksprung nach verfehltem E5:** Er geschieht nicht automatisch. Der Bericht sagt «zurück zum E1-Sieger», und E5
  wird von Hand neu gestartet, mit dem E1-Sieger als Kandidat und seinen Nachbarwerten. Verfehlt der E1-Sieger selbst
  E5 (auch wenn er schon der Leiter-Sieger war), sagt der Bericht «kein E6 für den Kern, No-Go». Ein Kern-Kandidat
  ohne bestandenes E5 bekommt auch in E6 ein No-Go; P−1 und K1 brauchen kein E5.
- **Kandidat in E6** ist der Amtsinhaber des E6-Laufs (`--config` und `--sieger`); Herausforderer in E6 sind nur die
  Varianten ohne Not-Aus für Regel 7.
- **Go-Regel 6** zählt den Chef zu den heutigen Bots: Langfrist, KI, Risiko, Phasen und Chef (wie Regel 1 ohne K1).
- **Sonderfall P−1:** Er greift, wenn P−1 in irgendeinem Haupt-Cache um mehr als 0,05 besser ist. Vorgeschlagen wird
  P−1 nur, wenn es die Regeln 1 und 3-5 in jedem Haupt-Cache erfüllt.
- **Dritte Quelle:** coinbase, sonst bitfinex (wenn coinbase beim ersten Laden nicht erreichbar ist). Sie hat nur BTC
  und ETH; für K1 gibt es darum keine dritte Quelle.
- **Chef:** Er rechnet aus den gerundeten Kapitalkurven der drei Stil-Bots im selben Fenster, auf GitHub aus ihren
  Ergebnisdateien und auf dem PC im selben Lauf; beides gibt dasselbe Ergebnis. Sein Ergebnis nennt Commit und
  Kurs-Fingerabdruck jedes Stil-Laufs und alle Kursdateien; war ein Stil-Lauf nicht sauber, ist es der Chef auch.
- **Ein Lauf** im Sinn von «genau einmal je Quelle» ist ein GitHub-Lauf (alle Einträge mit derselben GitHub-Lauf-Nummer)
  bzw. ein Aufruf von `scripts\profi_pc.bat`. Sind P−1 und K1 die Kandidaten, gehören zwei Aufrufe dazu (zuerst P−1,
  dann K1 mit `--nur-bot k1`). Bricht ein Job ab, darf genau dieser Job mit `--nur-bot` und `--nur-fenster`
  wiederholt werden; auch das steht im Prüfprotokoll. Weitere Läufe mit Kursen ab 2023 gibt es nicht.

## Prüfprotokoll

`lernen/PROFI_PRUEFPROTOKOLL.md` wird nur angehängt. Jeder Lauf mit `--pruefung` schreibt vor der Rechnung einen
Eintrag: Zeit (UTC), auf GitHub die Lauf-Nummer, Commit (mit Hinweis bei Änderungen ohne Commit), Quellen,
Cache-Fingerabdruck (eingefroren oder nicht), Befehl und Läufe (Bot: Fenster). Auf GitHub schreibt jeder Job einen
eigenen Eintrag, und der letzte Job hängt alle an, auch nach Fehlern oder Abbruch; auf dem PC lädt das Skript den
Eintrag und die fertigen Teilergebnisse auch nach einem Abbruch hoch. Jeder Eintrag ist genau eine Zeile: So bleiben
beim Zusammenführen die Einträge gleichzeitiger Läufe beide vollständig erhalten (`.gitattributes`: `merge=union`),
auch bei gleichem Befehl.

## Befehle

### Vorbereitung (einmal, vor E0)

1. Hiran bestätigt den Massstab (Feld oben).
2. Diese Datei und `bots/profi/` sind committet. Der Hash dieses Commits kommt oben bei «Eingefrorene Fassung» an die
   Stelle des Platzhalters, in Backticks (so liest ihn der Bericht); das ist ein eigener Commit, der nur diese Zeile
   ändert.
3. `.github/workflows/profi.yml` kommt zusätzlich auf main, nur diese Datei: GitHub zeigt «Run workflow» nur für
   Abläufe, die auf dem Hauptzweig liegen. Gerechnet wird trotzdem der Stand des Zweigs, der bei «Use workflow from»
   gewählt ist; auf main bricht der Ablauf sofort ab.
4. Der erste GitHub-Lauf (E0) läuft allein, bis sein erster Job «vorbereiten» fertig ist: Er lädt die Kurse und
   friert den Cache ein.

### GitHub

Actions → «Profi-Bot-Prüfung» → Run workflow → «Use workflow from»: `claude/project-thread-usz8e3`. Was hier nicht
steht, bleibt leer (`gebuehren` normiert, `pruefung` aus). Mehrere Dateien mit Leerzeichen getrennt.

Zuerst laufen alle Tests, dann je Bot und Fenster ein eigener Job auf dem eingefrorenen Cache (`--cache-fest`), der
Chef nach den drei Stil-Bots. Der letzte Job speichert `lernen/profi/`, `lernen/PROFI_ERGEBNISSE.md` und das
Prüfprotokoll auf denselben Zweig. Bot-Stände fasst der Ablauf nie an. Einen weiteren Lauf erst starten, wenn der Job
«vorbereiten» des vorigen fertig ist: GitHub hält nur einen wartenden Lauf, ein dritter bricht ihn still ab.

### Hirans PC

Das erste Mal: die Datei `scripts/profi_pc.bat` vom Zweig `claude/project-thread-usz8e3` herunterladen (auf GitHub die
Datei öffnen, «Download raw file»), doppelklicken (bei einer Windows-Warnung «Weitere Informationen» → «Trotzdem
ausführen»), als Schritt `E0` eingeben und die weiteren Angaben leer lassen. Das Skript holt das Projekt nach
`%USERPROFILE%\trading-bot-profi`, installiert, was fehlt, lädt beim ersten Mal die Kurse und friert sie als Zip ein,
rechnet und lädt die Ergebnisse hoch. Danach in der Eingabeaufforderung:

```bat
cd %USERPROFILE%\trading-bot-profi
scripts\profi_pc.bat <Schritt> <Angaben>
```

oder doppelklicken und Schritt und Angaben eintippen. Das Fenster offen und den PC eingeschaltet lassen: E0 dauert
mehrere Stunden, E6 läuft über Nacht.

### Die Befehle je Schritt

`S` steht für die Überlagerungen aller bisherigen Sieger in der Reihenfolge E1a, E1b, E2, E3, E4, zum Beispiel
`bots/profi/varianten/e1_kb5.yaml bots/profi/varianten/e2_trail6.yaml`; bleibt der Amtsinhaber, kommt nichts dazu.
Ist `S` leer, fallen `sieger` bzw. `--sieger` weg. Der Name des Amtsinhabers im Bericht zeigt `S`, zum Beispiel
«e1_kb3+e1_kb5+e2_trail6». `N` steht für die Nachbarwerte und den Kostenstress aus der E5-Tabelle, die für den
Kandidaten gelten.

| Schritt | GitHub (Eingaben) | PC (`scripts\profi_pc.bat …`) |
|---|---|---|
| E0 | `schritt` E0 | `E0` |
| E0 Kontrolle | `schritt` E0, `gebuehren` alt | `E0 --gebuehren alt` |
| E1a | `schritt` E1, `varianten` `bots/profi/varianten/e1_kb5.yaml` | `E1 --varianten bots/profi/varianten/e1_kb5.yaml` |
| E1b | `schritt` E1, `config` `bots/profi/e1_kb3.yaml`, `sieger` S, `varianten` `bots/profi/varianten/e1_kbe.yaml` | `E1 --config bots/profi/e1_kb3.yaml --sieger S --varianten bots/profi/varianten/e1_kbe.yaml` |
| E2 | `schritt` E2, `config` `bots/profi/e1_kb3.yaml`, `sieger` S, `varianten` `bots/profi/varianten/e2_ohne_notaus.yaml bots/profi/varianten/e2_trail6.yaml` | `E2 --config bots/profi/e1_kb3.yaml --sieger S --varianten bots/profi/varianten/e2_ohne_notaus.yaml bots/profi/varianten/e2_trail6.yaml` |
| E3 | `schritt` E3, `config` `bots/profi/e1_kb3.yaml`, `sieger` S, `varianten` `bots/profi/varianten/e3_kauf_woche.yaml bots/profi/varianten/e3_beides_woche.yaml` | `E3 --config bots/profi/e1_kb3.yaml --sieger S --varianten bots/profi/varianten/e3_kauf_woche.yaml bots/profi/varianten/e3_beides_woche.yaml` |
| E4 | `schritt` E4, `config` `bots/profi/e1_kb3.yaml`, `sieger` S, `varianten` `bots/profi/varianten/e4_nur_kleiner.yaml bots/profi/varianten/e4_beides.yaml` | `E4 --config bots/profi/e1_kb3.yaml --sieger S --varianten bots/profi/varianten/e4_nur_kleiner.yaml bots/profi/varianten/e4_beides.yaml` |
| E5 | `schritt` E5, `config` `bots/profi/e1_kb3.yaml`, `sieger` S, `varianten` N | `E5 --config bots/profi/e1_kb3.yaml --sieger S --varianten N` |
| E5 (c) dritte Quelle | `schritt` E5, `config` `bots/profi/e1_kb3.yaml`, `sieger` S, `quellen` coinbase (bzw. bitfinex), `nur_fenster` 2016-2022 | – |
| E6 | `schritt` E6, `config` `bots/profi/e1_kb3.yaml`, `sieger` S, bei E2-Flagge `varianten` `bots/profi/varianten/e2_ohne_notaus.yaml`, `pruefung` ja | `E6 --config bots/profi/e1_kb3.yaml --sieger S --pruefung`, bei E2-Flagge dazu `--varianten bots/profi/varianten/e2_ohne_notaus.yaml` |
| E6 dritte Quelle | wie E6, dazu `quellen` coinbase (bzw. bitfinex), `nur_bot` «Name des Kandidaten» `p_minus_1 bitcoin_halten`, `nur_fenster` ab-2023Q1; ohne `varianten` | – |
| E6, Tor nicht bestanden | zuerst `schritt` E6, `config` `bots/profi/p_minus_1.yaml`, `pruefung` ja; danach `schritt` E6, `config` `bots/profi/k1.yaml`, `nur_bot` k1, `pruefung` ja; dritte Quelle nur für P−1 (`nur_bot` `p_minus_1 bitcoin_halten`, `nur_fenster` ab-2023Q1) | zuerst `E6 --config bots/profi/p_minus_1.yaml --pruefung`, danach `E6 --config bots/profi/k1.yaml --nur-bot k1 --pruefung` |

Nach jedem Lauf steht der Bericht in `lernen/PROFI_ERGEBNISSE.md` (Kennzahlen, L_dev, Regel G mit Sieger, Tor,
Not-Aus-Tabelle mit E2-Flagge, E5-Kriterien, Go-Regeln mit Entscheid). Neu bauen ohne Rechnung:
`python -m tradingbot profi --zusammenfassen`. Welche Jobs ein Schritt rechnet, zeigt
`python -m tradingbot profi --schritt … --liste`.

## Zeitplan

Verschoben wegen des Nutzungslimits vom 31.10. bis 4.11.:

| Was | Wann |
|---|---|
| Messwerkzeug und diese Vorab-Registrierung (Stufe 1a) | bis 6.11. |
| Kern: E0, E1, E2 (GitHub und PC) | 6. bis 10.11. |
| Wochentakt und Grösse: E3, E4 (Stufe 2), nur falls Zeit | 9. bis 12.11. |
| Robustheit E5, danach den Kandidaten einfrieren | 12. bis 13.11. |
| Einmal-Prüfung E6 | 14. bis 16.11. |
| Bericht für Hiran | 17. bis 19.11. |
| Entscheid | 20.11. |
| Start als 5. Demo-Bot | frühestens 23.11. und nur nach Hirans Go |

## Bei Zeitnot

- E3 und E4 entfallen, wenn der Code der Stufe 2 bis 12.11. nicht fertig und getestet ist; dann wird der E2-Sieger
  eingefroren. Sonst wird verschoben statt abgekürzt.
- Fehlt der PC-Lauf, zählt der GitHub-Cache allein, und der Bericht am 20.11. zeigt das als Schwäche.
- Ist E6 bis 19.11. nicht sauber fertig, wird der Entscheid verschoben, nicht abgekürzt.

## Entscheid am 20.11.

Hiran bekommt eine Seite in einfacher Sprache, alle Zahlen nach Kosten, mit einem von drei Ausgängen:

- **Go:** Start als 5. Demo-Bot mit 100 CHF Spielgeld, frühestens am 23.11. und nur nach Hirans Zustimmung.
- **No-Go mit Vorschlag:** zum Beispiel P−1 als 5. Bot oder K1 als Config-Änderung des Langfrist-Bots; beides nur nach
  Hirans Ja.
- **Verschieben,** wenn E6 nicht sauber fertig ist.

Was nicht passiert: kein echtes Geld, kein Hebel, keine Shorts. Die vier Demo-Bots laufen unverändert weiter.
