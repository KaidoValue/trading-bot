# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **09.11.2026 22:39** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> ⚠️ **1️⃣ Langfrist-Bot (Hauptbot):** letzter Fehler 09.11.2026 22:05: RequestTimeout: Kerzen HYPE/CHF 1h: kraken GET https://api.kraken.com/0/public/OHLC?pair=HYPEUSD&interval=60

> ⚠️ **2️⃣ KI-Bot (lernend, kurz bis lang):** letzter Fehler 09.11.2026 22:09: RequestTimeout: Kerzen HYPE/CHF 1d: kraken GET https://api.kraken.com/0/public/OHLC?pair=HYPEUSD&interval=1440

> ⚠️ **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** letzter Fehler 09.11.2026 22:11: RequestTimeout: Kerzen HYPE/CHF 1d: kraken GET https://api.kraken.com/0/public/OHLC?pair=HYPEUSD&interval=1440

> ⚠️ **Bot-Lauf 09.11.2026 22:11:** 30-Tage-Lernexperiment: Durchlauf fehlgeschlagen

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 100.00 CHF | 100.00 CHF | 100.00 CHF |
| **Kapital jetzt** | **97.59 CHF** | **100.00 CHF** | **92.75 CHF** |
| Gewinn / Verlust | 🔴 -2.41 CHF (-2.41 %) | ⚪ +0.00 CHF (+0.00 %) | 🔴 -7.25 CHF (-7.25 %) |
| Im Einsatz (investiert) | 28.39 CHF (29 %) | 0.00 CHF (0 %) | 107.26 CHF (116 %) |
| Cash (nicht investiert) | 69.19 CHF | 100.00 CHF | -14.51 CHF |
| Offene Positionen | 2 | 0 | 5 |
| Abgeschlossene Trades | 0 | 0 | 1 |
| Gebühren bisher | 0.24 CHF | 0.00 CHF | 1.21 CHF |
| Gebührenstufe | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 31 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 0 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 151 CHF) |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 20 % · mittel 30 % · lang 50 % | mittel 54 % · lang 46 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.25 CHF) |
| Hebel aktuell | – | – | 1.16× (erlaubt 3×) |
| Buchhaltung | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) |
| Letzter Durchlauf | 09.11.2026 22:05 (vor 33 Min.) | 09.11.2026 22:09 (vor 30 Min.) | 09.11.2026 22:11 (vor 28 Min.) |


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 61'349.90 CHF (Kurs vom 09.11.2026 19:04) | – | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'730.91 CHF | 🔴 -0.41 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 566.23 CHF | 🟢 +0.73 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 0.90 CHF | 🔴 -1.45 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 71.28 CHF (Kurs vom 09.11.2026 22:01) | – | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.26 CHF | 🔴 -0.82 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 961.31 CHF | 🔴 -3.58 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 61.80 CHF | 🟢 +0.91 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 04.11.2026 21:01 | 65'280.50 | 61'349.90 | 0.000306 | 19.98 CHF | 18.78 CHF | 🔴 -1.20 CHF (-6.02 %) | 52'267.92 (-15 %) |
| **HYPE** long (lang) | 04.11.2026 21:01 | 68.01 | 61.80 | 0.155592 | 10.58 CHF | 9.62 CHF | 🔴 -0.97 CHF (-9.14 %) | 35.88 (-42 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BNB | 🟢 investiert sein | – | – |
| XRP | 🔴 raus / Cash | – | – |
| SOL | ⚪ neutral | – | – |
| TRX | ⚪ neutral | – | – |
| ZEC | 🟢 investiert sein | – | – |
| HYPE | 🟢 investiert sein | – | – |

**Letzte Entscheidung:** BTC/CHF: kein aktueller Kurs, Position zum letzten Kurs vom 09.11. 18:01 UTC bewertet, Stops und Signale ausgesetzt · [lang] ETH/CHF: keine Kerzen, Signal ausgesetzt · [lang] BNB/CHF: keine Kerzen, Signal ausgesetzt · [lang] XRP/CHF: keine Kerzen, Signal ausgesetzt · [lang] SOL/CHF: keine Kerzen, Signal ausgesetzt · [lang] TRX/CHF: keine Kerzen, Signal ausgesetzt · [lang] ZEC/CHF: keine Kerzen, Signal ausgesetzt · [lang] HYPE/CHF: keine Kerzen, Signal ausgesetzt · [mittel] ETH/CHF: keine Kerzen, Signal ausgesetzt · [mittel] BNB/CHF: keine Kerzen, Signal ausgesetzt · [mittel] XRP/CHF: keine Kerzen, Signal ausgesetzt · [mittel] SOL/CHF: keine Kerzen, Signal ausgesetzt · [mittel] TRX/CHF: keine Kerzen, Signal ausgesetzt · [mittel] ZEC/CHF: keine Kerzen, Signal ausgesetzt · [mittel] HYPE/CHF: keine Kerzen, Signal ausgesetzt · [kurz] ETH/CHF: keine Kerzen, Signal ausgesetzt · [kurz] BNB/CHF: keine Kerzen, Signal ausgesetzt · [kurz] XRP/CHF: keine Kerzen, Signal ausgesetzt · [kurz] SOL/CHF: keine Kerzen, Signal ausgesetzt · [kurz] TRX/CHF: keine Kerzen, Signal ausgesetzt · [kurz] ZEC/CHF: keine Kerzen, Signal ausgesetzt · [kurz] HYPE/CHF: keine Kerzen, Signal ausgesetzt

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | lang | 09.11.2026 19:01 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| BNB/CHF | lang | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| XRP/CHF | lang | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| SOL/CHF | lang | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| TRX/CHF | lang | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| ZEC/CHF | lang | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| HYPE/CHF | lang | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| BTC/CHF | mittel | 09.11.2026 19:01 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| BNB/CHF | mittel | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| XRP/CHF | mittel | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| SOL/CHF | mittel | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| TRX/CHF | mittel | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| ZEC/CHF | mittel | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| HYPE/CHF | mittel | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| BTC/CHF | kurz | 09.11.2026 19:01 | BTC/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| BNB/CHF | kurz | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| XRP/CHF | kurz | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| SOL/CHF | kurz | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| TRX/CHF | kurz | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| ZEC/CHF | kurz | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |
| HYPE/CHF | kurz | 09.11.2026 22:01 | Keine Kerzen, Signal ausgesetzt |

## 2️⃣ KI-Bot (lernend, kurz bis lang)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe._

Keine offene Position, alles in Cash.

**Signale jetzt**

| Coin | kurz (1h) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BNB | – | – | 🔴 raus / Cash |
| XRP | – | – | 🔴 raus / Cash |
| SOL | – | – | 🔴 raus / Cash |
| TRX | – | – | 🟢 investiert sein |
| ZEC | – | – | 🟢 investiert sein |
| HYPE | – | – | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 3'804 Kerzen Erfahrung (zeitlich gewichtete Kerzen; ältere Erfahrung zählt weniger)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|

**🧪 Selbst erfundene Strategien im Einsatz:** 0 (noch keine hat die Prüfung bestanden), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: kein aktueller Kurs, Signale ausgesetzt · SOL/CHF: kein aktueller Kurs, Signale ausgesetzt · [kurz] ETH/CHF: keine Kerzen, Signal ausgesetzt · [kurz] BNB/CHF: keine Kerzen, Signal ausgesetzt · [kurz] XRP/CHF: keine Kerzen, Signal ausgesetzt · [kurz] TRX/CHF: keine Kerzen, Signal ausgesetzt · [kurz] ZEC/CHF: keine Kerzen, Signal ausgesetzt · [kurz] HYPE/CHF: keine Kerzen, Signal ausgesetzt · [mittel] ETH/CHF: keine Kerzen, Signal ausgesetzt · [mittel] BNB/CHF: keine Kerzen, Signal ausgesetzt · [mittel] XRP/CHF: keine Kerzen, Signal ausgesetzt · [mittel] TRX/CHF: keine Kerzen, Signal ausgesetzt · [mittel] ZEC/CHF: keine Kerzen, Signal ausgesetzt · [mittel] HYPE/CHF: keine Kerzen, Signal ausgesetzt · [lang] ETH/CHF: keine Kerzen, Signal ausgesetzt · [lang] BNB/CHF: keine Kerzen, Signal ausgesetzt · [lang] XRP/CHF: keine Kerzen, Signal ausgesetzt · [lang] TRX/CHF: keine Kerzen, Signal ausgesetzt · [lang] ZEC/CHF: keine Kerzen, Signal ausgesetzt · [lang] HYPE/CHF: keine Kerzen, Signal ausgesetzt

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | kurz | 09.11.2026 19:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| BNB/CHF | kurz | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| XRP/CHF | kurz | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| SOL/CHF | kurz | 09.11.2026 19:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| ZEC/CHF | kurz | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| HYPE/CHF | kurz | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| BTC/CHF | mittel | 09.11.2026 17:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | mittel | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| BNB/CHF | mittel | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| XRP/CHF | mittel | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| SOL/CHF | mittel | 09.11.2026 17:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | mittel | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| ZEC/CHF | mittel | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| HYPE/CHF | mittel | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| BTC/CHF | lang | 09.11.2026 01:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: 8/9 Strategien positiv gewichtet |
| ETH/CHF | lang | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| BNB/CHF | lang | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| XRP/CHF | lang | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| SOL/CHF | lang | 09.11.2026 01:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: 5/9 Strategien positiv gewichtet |
| TRX/CHF | lang | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| ZEC/CHF | lang | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |
| HYPE/CHF | lang | 09.11.2026 22:06 | Keine Kerzen, Signal ausgesetzt |

**KI-Forschung: getrennte Vorwärtstests mit Kosten**

Die Werte betreffen isolierte Testpositionen, keine erzielte Portfoliorendite.

| Horizont | Status | Ausgewertet | Offen | Datenlücken / ungültig |
|---|---|---|---|---|
| kurz | Sammelt Lernfälle | 145 | 8 | 0 |
| mittel | Sammelt Lernfälle | 22 | 8 | 0 |
| lang | Sammelt Lernfälle | 0 | 8 | 0 |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 02.11.2026 21:04 | 62'905.40 | 61'349.90 | 0.000523 | 32.87 CHF | 32.06 CHF | 🔴 -0.81 CHF (-2.47 %) | 53'337.04 (-13 %) |
| **ETH** long (lang) | 02.11.2026 21:04 | 1'843.99 | 1'730.91 | 0.012649 | 23.33 CHF | 21.89 CHF | 🔴 -1.43 CHF (-6.13 %) | 1'449.18 (-16 %) |
| **BNB** long (lang) | 02.11.2026 21:04 | 570.38 | 566.23 | 0.041690 | 23.78 CHF | 23.61 CHF | 🔴 -0.17 CHF (-0.73 %) | 450.90 (-20 %) |
| **SOL** long (lang) | 02.11.2026 21:04 | 75.10 | 71.28 | 0.233083 | 17.50 CHF | 16.61 CHF | 🔴 -0.89 CHF (-5.08 %) | 53.80 (-25 %) |
| **HYPE** long (lang) | 02.11.2026 21:04 | 68.38 | 61.80 | 0.211733 | 14.48 CHF | 13.09 CHF | 🔴 -1.39 CHF (-9.63 %) | 44.97 (-27 %) |

**Signale jetzt**

| Coin | mittel (4h) | lang (1d) |
|---|---|---|
| BNB | – | 🟢 investiert sein |
| XRP | – | 🔴 raus / Cash |
| SOL | – | ⚪ neutral |
| TRX | – | ⚪ neutral |
| ZEC | – | 🟢 investiert sein |
| HYPE | – | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: kein aktueller Kurs, Position zum letzten Kurs vom 09.11. 18:04 UTC bewertet, Stops und Signale ausgesetzt · BNB/CHF: kein aktueller Kurs, Position zum letzten Kurs vom 09.11. 18:04 UTC bewertet, Stops und Signale ausgesetzt · XRP/CHF: kein aktueller Kurs, Signale ausgesetzt · SOL/CHF: kein aktueller Kurs, Position zum letzten Kurs vom 09.11. 18:04 UTC bewertet, Stops und Signale ausgesetzt · TRX/CHF: kein aktueller Kurs, Signale ausgesetzt · ZEC/CHF: kein aktueller Kurs, Signale ausgesetzt · HYPE/CHF: kein aktueller Kurs, Position zum letzten Kurs vom 09.11. 18:04 UTC bewertet, Stops und Signale ausgesetzt · [mittel] ETH/CHF: keine Kerzen, Signal ausgesetzt · [lang] ETH/CHF: keine Kerzen, Signal ausgesetzt

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | mittel | 09.11.2026 17:04 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 09.11.2026 22:09 | Keine Kerzen, Signal ausgesetzt |
| BNB/CHF | mittel | 09.11.2026 17:04 | BNB/CHF: Position gehört zum Horizont «lang» |
| XRP/CHF | mittel | 09.11.2026 17:04 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | mittel | 09.11.2026 17:04 | SOL/CHF: Position gehört zum Horizont «lang» |
| TRX/CHF | mittel | 09.11.2026 17:04 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | mittel | 09.11.2026 17:04 | ZEC/CHF: Signal 'raus', bleibe in Cash |
| HYPE/CHF | mittel | 09.11.2026 17:04 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | lang | 09.11.2026 01:04 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 09.11.2026 22:09 | Keine Kerzen, Signal ausgesetzt |
| BNB/CHF | lang | 09.11.2026 01:04 | BNB/CHF: Position offen, Signal bestätigt |
| XRP/CHF | lang | 09.11.2026 01:04 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | lang | 09.11.2026 01:04 | Kein Signal |
| TRX/CHF | lang | 09.11.2026 01:04 | Kein Signal |
| ZEC/CHF | lang | 09.11.2026 01:04 | ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| HYPE/CHF | lang | 09.11.2026 01:04 | HYPE/CHF: Position offen, Signal bestätigt |

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| XRP long (lang) | 04.11.2026 01:04 | 06.11.2026 01:04 | 1.05 | 0.99 | 🔴 -1.49 CHF | Signal |

## Charts

▲ grün = Kauf, ▼ rot = Verkauf, rote Linie = Stop-Loss, orange = 200-Tage-Linie. Die Bilder zeigen den Stand der letzten Aktualisierung; für den Live-Kurs auf «Live-Chart» klicken.

## Nachrichtenlage

**Zusätzliche Sprachanalyse:** Sprachanalyse ausgeschaltet

- **Stimmung (Fear & Greed):** 29 von 100, Angst
- **Bewertung News:** +0.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** keine
- **Ereignis:** powell (fed): Federal Reserve Board announces approval of two applications by Mutual Federal Bancorp, MHC, and MFB Bancorp, Inc. (federalreserve, 21:00 UTC)
