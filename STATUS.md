# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **29.10.2026 00:55** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Simulation 2011-2022: +18 %/Jahr, 2023-2026: +14 %/Jahr.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang), Trendfolge (4h) und Ausbrüche (30 Min.), nur in Trendrichtung. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **995.57 CHF** | **950.39 CHF** | **368.57 CHF** |
| Gewinn / Verlust | 🔴 -4.43 CHF (-0.44 %) | 🔴 -49.61 CHF (-4.96 %) | 🔴 -631.43 CHF (-63.14 %) |
| Im Einsatz (investiert) | 412.20 CHF (41 %) | 1'001.71 CHF (105 %) | 930.53 CHF (252 %) |
| Cash (nicht investiert) | 583.37 CHF | 993.36 CHF | -159.33 CHF |
| Offene Positionen | 5 | 5 | 7 |
| Abgeschlossene Trades | 2 | 19 | 175 |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | kurz: breakout 30m · mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 20 % · mittel 30 % · lang 50 % | kurz 32 % · mittel 34 % · lang 34 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.55 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 50 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **970.44 CHF** |
| Gewinn / Verlust | 🔴 -29.56 CHF (-2.96 %) |
| **Aktuelle Verteilung** | Langfrist 32 % · KI 21 % · Risiko 3 % · Cash 44 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.5 %, KI -2.9 %, Risiko -76.0 %, 🚨 Notbremse Risiko (-3.7 % in 3 Std.) |
| Umschicht-Gebühren bisher | 3.27 CHF |
| Erfahrung im Gedächtnis | 274 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.004 %/Lauf, KI -0.003 %/Lauf, Risiko -0.402 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'147.50 CHF | 🟢 +0.44 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'945.76 CHF | 🟢 +0.24 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 627.03 CHF | 🟢 +2.01 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.09 CHF | 🔴 -0.41 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.53 CHF | 🟢 +1.03 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.47 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'082.49 CHF | 🟢 +0.13 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 66.71 CHF | 🔴 -0.58 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 23.10.2026 18:09 | 67'388.78 | 67'147.50 | 0.001485 | 100.05 CHF | 99.69 CHF | 🔴 -0.36 CHF (-0.36 %) | 53'251.84 (-21 %) |
| **ETH** long (lang) | 23.10.2026 18:09 | 1'986.19 | 1'945.76 | 0.040710 | 80.86 CHF | 79.21 CHF | 🔴 -1.65 CHF (-2.04 %) | 1'371.11 (-30 %) |
| **BNB** long (lang) | 23.10.2026 19:15 | 617.14 | 627.03 | 0.162070 | 100.02 CHF | 101.62 CHF | 🟢 +1.60 CHF (+1.60 %) | 483.48 (-23 %) |
| **XRP** long (lang) | 23.10.2026 19:15 | 1.08 | 1.09 | 58.690975 | 63.53 CHF | 64.24 CHF | 🟢 +0.71 CHF (+1.11 %) | 0.66 (-40 %) |
| **SOL** long (lang) | 23.10.2026 19:15 | 86.38 | 84.53 | 0.797780 | 68.91 CHF | 67.43 CHF | 🔴 -1.48 CHF (-2.14 %) | 55.00 (-35 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| BNB | 🟢 investiert sein | ⚪ neutral | 🟢 investiert sein |
| XRP | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | ⚪ neutral | ⚪ neutral |
| HYPE | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: Position offen, Signal bestätigt · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [lang] ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [lang] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: kein Signal · [mittel] XRP/CHF: Position gehört zum Horizont «lang» · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: kein Signal · [mittel] HYPE/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Position gehört zum Horizont «lang» · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: Position gehört zum Horizont «lang» · [kurz] SOL/CHF: Position gehört zum Horizont «lang» · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: kein Signal · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ZEC short (kurz) | 28.10.2026 20:17 | 28.10.2026 22:22 | 1'064.43 | 1'082.08 | 🔴 -0.54 CHF | Vorrang lang |
| TRX short (kurz) | 28.10.2026 20:17 | 28.10.2026 22:22 | 0.27 | 0.27 | 🔴 -0.38 CHF | Vorrang lang |

## 2️⃣ KI-Bot (lernend, kurz bis lang)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Simulation 2011-2022: +18 %/Jahr, 2023-2026: +14 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **ETH** long (kurz) | 28.10.2026 16:15 | 1'934.17 | 1'945.76 | 0.123031 | 237.96 CHF | 239.39 CHF | 🟢 +1.43 CHF (+0.60 %) | 1'916.06 (-2 %) |
| **BNB** long (kurz) | 28.10.2026 16:15 | 621.75 | 627.03 | 0.382729 | 237.96 CHF | 239.98 CHF | 🟢 +2.02 CHF (+0.85 %) | 614.56 (-2 %) |
| **BTC** short (mittel) | 28.10.2026 20:19 | 67'094.94 | 67'147.50 | 0.003544 | 237.81 CHF | 237.99 CHF | 🔴 -0.19 CHF (-0.08 %) | 68'876.82 (+3 %) |
| **TRX** short (lang) | 28.10.2026 20:19 | 0.27 | 0.27 | 870.667829 | 237.55 CHF | 237.22 CHF | 🟢 +0.33 CHF (+0.14 %) | 0.29 (+5 %) |
| **HYPE** short (lang) | 28.10.2026 20:19 | 66.85 | 66.71 | 0.706372 | 47.22 CHF | 47.12 CHF | 🟢 +0.10 CHF (+0.21 %) | 80.08 (+20 %) |

**Signale jetzt**

| Coin | kurz (1h) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | ⚪ neutral | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | ⚪ neutral | 🟢 investiert sein | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | ⚪ neutral | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | 🟢 investiert sein | ⚪ neutral |
| SOL | ⚪ neutral | 🟢 investiert sein | ⚪ neutral |
| TRX | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 20'910 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.064 %/Kerze), reversal (+0.056 %/Kerze) |
| ETH | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.064 %/Kerze), reversal (+0.056 %/Kerze) |
| BNB | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.064 %/Kerze), reversal (+0.056 %/Kerze) |
| XRP | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.064 %/Kerze), reversal (+0.056 %/Kerze) |
| SOL | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.064 %/Kerze), reversal (+0.056 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.028 %/Kerze), momentum (+0.026 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.064 %/Kerze), reversal (+0.056 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: kein Signal · [kurz] ETH/CHF: kein Signal · [kurz] BNB/CHF: Position offen, Signal bestätigt · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: kein Signal · [kurz] TRX/CHF: Position gehört zum Horizont «lang» · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Position gehört zum Horizont «lang»

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| XRP short (mittel) | 28.10.2026 20:19 | 28.10.2026 21:18 | 1.10 | 1.10 | 🔴 -0.35 CHF | Signal |
| BNB long | 28.10.2026 13:15 | 28.10.2026 15:45 | 627.36 | 619.66 | 🔴 -4.18 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 15:45 | 1'946.78 | 1'929.91 | 🔴 -2.70 CHF | Stop-Loss (Gap) |
| BTC long | 27.10.2026 16:00 | 28.10.2026 14:15 | 66'509.84 | 66'883.94 | 🟢 +0.72 CHF | Signal |
| ETH long | 27.10.2026 16:00 | 28.10.2026 09:42 | 1'928.15 | 1'963.28 | 🟢 +3.74 CHF | Take-Profit |
| BNB long | 27.10.2026 18:00 | 28.10.2026 01:06 | 622.33 | 614.56 | 🔴 -4.25 CHF | Stop-Loss (Gap) |
| ZEC long | 26.10.2026 10:10 | 27.10.2026 17:30 | 1'006.92 | 1'072.51 | 🟢 +14.25 CHF | Take-Profit |
| BTC long | 26.10.2026 10:10 | 26.10.2026 15:16 | 66'289.23 | 66'013.88 | 🔴 -1.61 CHF | Signal |
| ETH long | 26.10.2026 13:13 | 26.10.2026 14:13 | 1'930.96 | 1'911.28 | 🔴 -3.05 CHF | Signal |
| TRX long | 23.10.2026 20:16 | 26.10.2026 11:13 | 0.27 | 0.27 | 🔴 -0.31 CHF | Signal |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang), Trendfolge (4h) und Ausbrüche (30 Min.), nur in Trendrichtung. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **ETH** long (kurz) | 28.10.2026 19:48 | 1'950.58 | 1'945.76 | 0.083780 | 163.42 CHF | 163.02 CHF | 🔴 -0.40 CHF (-0.25 %) | 1'941.70 (-0 %) |
| **XRP** long (mittel) | 28.10.2026 20:19 | 1.10 | 1.09 | 178.546264 | 196.03 CHF | 195.41 CHF | 🔴 -0.61 CHF (-0.31 %) | 1.07 (-2 %) |
| **TRX** long (mittel) | 28.10.2026 20:19 | 0.27 | 0.27 | 544.830158 | 148.80 CHF | 148.45 CHF | 🔴 -0.35 CHF (-0.24 %) | 0.27 (-1 %) |
| **ZEC** short (lang) | 28.10.2026 20:19 | 1'066.19 | 1'082.49 | 0.067046 | 71.48 CHF | 72.58 CHF | 🔴 -1.09 CHF (-1.53 %) | 1'351.76 (+25 %) |
| **HYPE** short (lang) | 28.10.2026 20:19 | 66.92 | 66.71 | 1.929710 | 129.14 CHF | 128.74 CHF | 🟢 +0.40 CHF (+0.31 %) | 76.85 (+15 %) |
| **BNB** long (kurz) | 28.10.2026 21:19 | 623.82 | 627.03 | 0.302920 | 188.97 CHF | 189.94 CHF | 🟢 +0.97 CHF (+0.51 %) | 619.78 (-1 %) |
| **BTC** long (mittel) | 28.10.2026 21:19 | 67'178.57 | 67'147.50 | 0.000483 | 32.42 CHF | 32.40 CHF | 🔴 -0.01 CHF (-0.05 %) | 65'937.69 (-2 %) |

**Signale jetzt**

| Coin | kurz (30m) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| BNB | 🟢 investiert sein | 🟢 investiert sein | 🟢 investiert sein |
| XRP | 🟢 investiert sein | 🟢 investiert sein | 🟢 investiert sein |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🔴 raus / Cash | 🟢 investiert sein | 🟢 investiert sein |
| ZEC | 🟢 investiert sein | 🟢 investiert sein | 🟢 investiert sein |
| HYPE | 🟢 investiert sein | 🟢 investiert sein | 🟢 investiert sein |

**Letzte Entscheidung:** [kurz] BTC/CHF: Position gehört zum Horizont «mittel» · [kurz] ETH/CHF: Position offen, Signal bestätigt · [kurz] BNB/CHF: Position offen, Signal bestätigt · [kurz] XRP/CHF: Position gehört zum Horizont «mittel» · [kurz] SOL/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [kurz] TRX/CHF: Position gehört zum Horizont «mittel» · [kurz] ZEC/CHF: Position gehört zum Horizont «lang» · [kurz] HYPE/CHF: Position gehört zum Horizont «lang»

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BTC short (kurz) | 28.10.2026 20:49 | 28.10.2026 21:19 | 67'362.30 | 67'178.57 | 🟢 +0.03 CHF | Signal |
| SOL short (kurz) | 28.10.2026 13:45 | 28.10.2026 20:49 | 84.18 | 85.00 | 🔴 -9.72 CHF | Stop-Loss (Gap) |
| BNB short (kurz) | 28.10.2026 17:48 | 28.10.2026 20:49 | 618.73 | 623.99 | 🔴 -0.28 CHF | Stop-Loss (Gap) |
| BTC short (kurz) | 28.10.2026 13:45 | 28.10.2026 20:49 | 66'924.92 | 67'429.70 | 🔴 -3.26 CHF | Stop-Loss (Gap) |
| ETH short | 28.10.2026 13:45 | 28.10.2026 19:48 | 1'938.49 | 1'950.58 | 🔴 -1.78 CHF | Stop-Loss (Gap) |
| ZEC short | 28.10.2026 13:15 | 28.10.2026 17:48 | 1'072.45 | 1'049.22 | 🟢 +3.40 CHF | Take-Profit |
| XRP short | 28.10.2026 07:10 | 28.10.2026 17:48 | 1.10 | 1.09 | 🟢 +1.62 CHF | Take-Profit |
| BNB long | 28.10.2026 13:45 | 28.10.2026 15:16 | 625.56 | 621.32 | 🔴 -0.69 CHF | Stop-Loss (Gap) |
| SOL long | 28.10.2026 13:15 | 28.10.2026 13:45 | 84.57 | 84.18 | 🔴 -1.81 CHF | Signal |
| BTC long | 28.10.2026 13:15 | 28.10.2026 13:45 | 67'033.50 | 66'924.92 | 🔴 -0.87 CHF | Signal |

## Charts

▲ grün = Kauf, ▼ rot = Verkauf, rote Linie = Stop-Loss, orange = 200-Tage-Linie. Die Bilder zeigen den Stand der letzten Aktualisierung; für den Live-Kurs auf «Live-Chart» klicken.

### BTC/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF)

![BTC/CHF](https://raw.githubusercontent.com/KaidoValue/trading-bot/charts/BTC-CHF.png)

### ETH/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF)

![ETH/CHF](https://raw.githubusercontent.com/KaidoValue/trading-bot/charts/ETH-CHF.png)

### BNB/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD)

![BNB/CHF](https://raw.githubusercontent.com/KaidoValue/trading-bot/charts/BNB-CHF.png)

### XRP/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD)

![XRP/CHF](https://raw.githubusercontent.com/KaidoValue/trading-bot/charts/XRP-CHF.png)

### SOL/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD)

![SOL/CHF](https://raw.githubusercontent.com/KaidoValue/trading-bot/charts/SOL-CHF.png)

### TRX/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD)

![TRX/CHF](https://raw.githubusercontent.com/KaidoValue/trading-bot/charts/TRX-CHF.png)

### ZEC/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD)

![ZEC/CHF](https://raw.githubusercontent.com/KaidoValue/trading-bot/charts/ZEC-CHF.png)

### HYPE/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD)

![HYPE/CHF](https://raw.githubusercontent.com/KaidoValue/trading-bot/charts/HYPE-CHF.png)

## Nachrichtenlage

- **Stimmung (Fear & Greed):** 51 von 100, neutral
- **Bewertung News:** -1.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** hack (gemeldet von bitcoinmagazine, cointelegraph – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-10-28 17:43 UTC · **bitcoinmagazine** · [Centralized Exchange and DeFi Losses Dominate 2026 Crypto Hacks Despite Hardware Wallet Failures](https://bitcoinmagazine.com/technical/centralized-exchange-and-defi-losses-dominate-2026-crypto-hacks-despite-hardware-wallet-failures) _(Thema: hack)_
- 2026-10-28 17:05 UTC · **cointelegraph** · [Crypto PAC spending before midterms possibly obscured after reported FEC hack](https://cointelegraph.com/news/crypto-pac-spending-midterms-fec-hack?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: hack)_
