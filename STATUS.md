# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **29.10.2026 11:39** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Simulation 2011-2022: +18 %/Jahr, 2023-2026: +14 %/Jahr.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang), Trendfolge (4h) und Ausbrüche (30 Min.), nur in Trendrichtung. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **988.60 CHF** | **942.56 CHF** | **357.81 CHF** |
| Gewinn / Verlust | 🔴 -11.40 CHF (-1.14 %) | 🔴 -57.44 CHF (-5.74 %) | 🔴 -642.19 CHF (-64.22 %) |
| Im Einsatz (investiert) | 405.23 CHF (41 %) | 465.14 CHF (49 %) | 376.63 CHF (105 %) |
| Cash (nicht investiert) | 583.37 CHF | 1'052.09 CHF | -18.81 CHF |
| Offene Positionen | 5 | 3 | 4 |
| Abgeschlossene Trades | 2 | 21 | 180 |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | kurz: breakout 30m · mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 20 % · mittel 30 % · lang 50 % | kurz 32 % · mittel 31 % · lang 36 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.60 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 50 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **965.73 CHF** |
| Gewinn / Verlust | 🔴 -34.27 CHF (-3.43 %) |
| **Aktuelle Verteilung** | Langfrist 32 % · KI 21 % · Risiko 3 % · Cash 44 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.5 %, KI -2.9 %, Risiko -76.0 %, 🚨 Notbremse Risiko (-3.7 % in 3 Std.) |
| Umschicht-Gebühren bisher | 3.27 CHF |
| Erfahrung im Gedächtnis | 297 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.000 %/Lauf, KI -0.007 %/Lauf, Risiko -0.367 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'324.70 CHF | 🔴 -1.41 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'920.39 CHF | 🔴 -1.73 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 613.89 CHF | 🔴 -2.50 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.07 CHF | 🔴 -2.59 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.16 CHF | 🔴 -1.92 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🟢 +0.49 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'048.68 CHF | 🔴 -3.42 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 68.61 CHF | 🟢 +2.60 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 23.10.2026 18:09 | 67'388.78 | 66'324.70 | 0.001485 | 100.05 CHF | 98.47 CHF | 🔴 -1.58 CHF (-1.58 %) | 53'251.84 (-20 %) |
| **ETH** long (lang) | 23.10.2026 18:09 | 1'986.19 | 1'920.39 | 0.040710 | 80.86 CHF | 78.18 CHF | 🔴 -2.68 CHF (-3.31 %) | 1'371.11 (-29 %) |
| **BNB** long (lang) | 23.10.2026 19:15 | 617.14 | 613.89 | 0.162070 | 100.02 CHF | 99.49 CHF | 🔴 -0.53 CHF (-0.53 %) | 483.48 (-21 %) |
| **XRP** long (lang) | 23.10.2026 19:15 | 1.08 | 1.07 | 58.690975 | 63.53 CHF | 62.74 CHF | 🔴 -0.79 CHF (-1.24 %) | 0.66 (-39 %) |
| **SOL** long (lang) | 23.10.2026 19:15 | 86.38 | 83.16 | 0.797780 | 68.91 CHF | 66.35 CHF | 🔴 -2.56 CHF (-3.72 %) | 55.00 (-34 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| BNB | 🟢 investiert sein | ⚪ neutral | 🔴 raus / Cash |
| XRP | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | ⚪ neutral | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: Position offen, Signal bestätigt · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [lang] ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [lang] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: kein Signal · [mittel] XRP/CHF: Position gehört zum Horizont «lang» · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [mittel] ZEC/CHF: kein Signal · [mittel] HYPE/CHF: Signal 'raus', bleibe in Cash · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Position gehört zum Horizont «lang» · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: Position gehört zum Horizont «lang» · [kurz] SOL/CHF: Position gehört zum Horizont «lang» · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

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
| **BNB** long (lang) | 28.10.2026 16:15 | 621.75 | 613.89 | 0.289635 | 180.08 CHF | 177.81 CHF | 🔴 -2.27 CHF (-1.26 %) | 562.99 (-8 %) |
| **TRX** short (lang) | 28.10.2026 20:19 | 0.27 | 0.27 | 870.667829 | 237.55 CHF | 238.88 CHF | 🔴 -1.32 CHF (-0.56 %) | 0.29 (+4 %) |
| **HYPE** short (lang) | 28.10.2026 20:19 | 66.85 | 68.61 | 0.706372 | 47.22 CHF | 48.46 CHF | 🔴 -1.24 CHF (-2.62 %) | 80.08 (+17 %) |

**Signale jetzt**

| Coin | kurz (1h) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash | ⚪ neutral | 🟢 investiert sein |
| XRP | 🟢 investiert sein | 🔴 raus / Cash | ⚪ neutral |
| SOL | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 20'998 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ETH | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| BNB | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| XRP | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| SOL | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ZEC | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| HYPE | Seitwärts, ruhig | mean_reversion (+0.013 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Position gehört zum Horizont «lang» · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Position gehört zum Horizont «lang»

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ETH long (mittel) | 28.10.2026 16:15 | 29.10.2026 01:23 | 1'934.17 | 1'953.68 | 🟢 +1.78 CHF | Vorrang lang |
| BTC short (mittel) | 28.10.2026 20:19 | 29.10.2026 01:23 | 67'094.94 | 67'266.32 | 🔴 -1.27 CHF | Vorrang lang |
| XRP short (mittel) | 28.10.2026 20:19 | 28.10.2026 21:18 | 1.10 | 1.10 | 🔴 -0.35 CHF | Signal |
| BNB long | 28.10.2026 13:15 | 28.10.2026 15:45 | 627.36 | 619.66 | 🔴 -4.18 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 15:45 | 1'946.78 | 1'929.91 | 🔴 -2.70 CHF | Stop-Loss (Gap) |
| BTC long | 27.10.2026 16:00 | 28.10.2026 14:15 | 66'509.84 | 66'883.94 | 🟢 +0.72 CHF | Signal |
| ETH long | 27.10.2026 16:00 | 28.10.2026 09:42 | 1'928.15 | 1'963.28 | 🟢 +3.74 CHF | Take-Profit |
| BNB long | 27.10.2026 18:00 | 28.10.2026 01:06 | 622.33 | 614.56 | 🔴 -4.25 CHF | Stop-Loss (Gap) |
| ZEC long | 26.10.2026 10:10 | 27.10.2026 17:30 | 1'006.92 | 1'072.51 | 🟢 +14.25 CHF | Take-Profit |
| BTC long | 26.10.2026 10:10 | 26.10.2026 15:16 | 66'289.23 | 66'013.88 | 🔴 -1.61 CHF | Signal |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang), Trendfolge (4h) und Ausbrüche (30 Min.), nur in Trendrichtung. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **TRX** long (mittel) | 28.10.2026 20:19 | 0.27 | 0.27 | 544.830158 | 148.80 CHF | 149.48 CHF | 🟢 +0.68 CHF (+0.46 %) | 0.27 (-1 %) |
| **BNB** long (mittel) | 28.10.2026 21:19 | 623.82 | 613.89 | 0.069438 | 43.32 CHF | 42.63 CHF | 🔴 -0.69 CHF (-1.59 %) | 614.50 (+0 %) |
| **BTC** long (lang) | 29.10.2026 01:24 | 67'266.32 | 66'324.70 | 0.001914 | 128.78 CHF | 126.98 CHF | 🔴 -1.80 CHF (-1.40 %) | 57'602.04 (-13 %) |
| **ETH** long (lang) | 29.10.2026 01:24 | 1'955.64 | 1'920.39 | 0.029964 | 58.60 CHF | 57.54 CHF | 🔴 -1.06 CHF (-1.80 %) | 1'542.64 (-20 %) |

**Signale jetzt**

| Coin | kurz (30m) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| BNB | 🔴 raus / Cash | 🟢 investiert sein | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| SOL | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🟢 investiert sein | 🟢 investiert sein | 🟢 investiert sein |
| ZEC | 🔴 raus / Cash | 🟢 investiert sein | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash | 🟢 investiert sein | 🟢 investiert sein |

**Letzte Entscheidung:** [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Position gehört zum Horizont «lang» · [kurz] BNB/CHF: Position gehört zum Horizont «mittel» · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Position gehört zum Horizont «mittel» · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| XRP long (mittel) | 28.10.2026 20:19 | 29.10.2026 04:28 | 1.10 | 1.07 | 🔴 -6.61 CHF | Stop-Loss (Gap) |
| HYPE short (lang) | 28.10.2026 20:19 | 29.10.2026 01:24 | 66.92 | 66.77 | 🔴 -0.40 CHF | Signal |
| ZEC short (lang) | 28.10.2026 20:19 | 29.10.2026 01:24 | 1'066.19 | 1'083.41 | 🔴 -1.54 CHF | Signal |
| BTC long (mittel) | 28.10.2026 21:19 | 29.10.2026 01:24 | 67'178.57 | 67'199.08 | 🔴 -0.08 CHF | Signal |
| ETH long (kurz) | 28.10.2026 19:48 | 29.10.2026 01:24 | 1'950.58 | 1'953.68 | 🔴 -0.17 CHF | Signal |
| BTC short (kurz) | 28.10.2026 20:49 | 28.10.2026 21:19 | 67'362.30 | 67'178.57 | 🟢 +0.03 CHF | Signal |
| SOL short (kurz) | 28.10.2026 13:45 | 28.10.2026 20:49 | 84.18 | 85.00 | 🔴 -9.72 CHF | Stop-Loss (Gap) |
| BNB short (kurz) | 28.10.2026 17:48 | 28.10.2026 20:49 | 618.73 | 623.99 | 🔴 -0.28 CHF | Stop-Loss (Gap) |
| BTC short (kurz) | 28.10.2026 13:45 | 28.10.2026 20:49 | 66'924.92 | 67'429.70 | 🔴 -3.26 CHF | Stop-Loss (Gap) |
| ETH short | 28.10.2026 13:45 | 28.10.2026 19:48 | 1'938.49 | 1'950.58 | 🔴 -1.78 CHF | Stop-Loss (Gap) |

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
