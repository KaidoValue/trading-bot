# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **31.10.2026 03:41** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Simulation 2011-2022: +18 %/Jahr, 2023-2026: +14 %/Jahr.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **972.33 CHF** | **922.04 CHF** | **344.60 CHF** |
| Gewinn / Verlust | 🔴 -27.67 CHF (-2.77 %) | 🔴 -77.96 CHF (-7.80 %) | 🔴 -655.40 CHF (-65.54 %) |
| Im Einsatz (investiert) | 472.94 CHF (49 %) | 0.00 CHF (0 %) | 531.12 CHF (154 %) |
| Cash (nicht investiert) | 499.39 CHF | 922.04 CHF | -186.52 CHF |
| Offene Positionen | 6 | 0 | 7 |
| Abgeschlossene Trades | 2 | 24 | 182 |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 23 % · mittel 35 % · lang 42 % | mittel 47 % · lang 53 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.84 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **952.36 CHF** |
| Gewinn / Verlust | 🔴 -47.64 CHF (-4.76 %) |
| **Aktuelle Verteilung** | Langfrist 23 % · KI 12 % · Risiko 3 % · Cash 62 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -2.3 %, KI -6.0 %, Risiko -53.4 % |
| Umschicht-Gebühren bisher | 4.55 CHF |
| Erfahrung im Gedächtnis | 383 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.008 %/Lauf, KI -0.026 %/Lauf, Risiko -0.199 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 63'839.80 CHF | 🟢 +0.17 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'854.62 CHF | 🟢 +0.19 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 581.11 CHF | 🟢 +0.11 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.04 CHF | 🔴 -0.01 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 79.85 CHF | 🟢 +0.56 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.73 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'052.07 CHF | 🟢 +0.41 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 74.08 CHF | 🔴 -0.11 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 23.10.2026 18:09 | 67'388.78 | 63'839.80 | 0.001485 | 100.05 CHF | 94.78 CHF | 🔴 -5.27 CHF (-5.27 %) | 53'251.84 (-17 %) |
| **ETH** long (lang) | 23.10.2026 18:09 | 1'986.19 | 1'854.62 | 0.040710 | 80.86 CHF | 75.50 CHF | 🔴 -5.36 CHF (-6.62 %) | 1'371.11 (-26 %) |
| **BNB** long (lang) | 23.10.2026 19:15 | 617.14 | 581.11 | 0.162070 | 100.02 CHF | 94.18 CHF | 🔴 -5.84 CHF (-5.84 %) | 483.48 (-17 %) |
| **XRP** long (lang) | 23.10.2026 19:15 | 1.08 | 1.04 | 58.690975 | 63.53 CHF | 60.78 CHF | 🔴 -2.75 CHF (-4.33 %) | 0.66 (-37 %) |
| **SOL** long (lang) | 23.10.2026 19:15 | 86.38 | 79.85 | 0.797780 | 68.91 CHF | 63.70 CHF | 🔴 -5.21 CHF (-7.56 %) | 55.00 (-31 %) |
| **TRX** long (lang) | 29.10.2026 18:11 | 0.27 | 0.27 | 305.677317 | 83.55 CHF | 84.00 CHF | 🟢 +0.45 CHF (+0.54 %) | 0.25 (-10 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| XRP | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🟢 investiert sein | ⚪ neutral | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🟢 investiert sein | 🟢 investiert sein |
| HYPE | 🟢 investiert sein | ⚪ neutral | 🟢 investiert sein |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: kein Signal · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: Position offen, Signal bestätigt · [lang] ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: crash,hack, Wert -1.0) · [lang] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: crash,hack, Wert -1.0) · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Position gehört zum Horizont «lang» · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: kein Signal · [mittel] ZEC/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [mittel] HYPE/CHF: kein Signal · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Position gehört zum Horizont «lang» · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: Position gehört zum Horizont «lang» · [kurz] SOL/CHF: Position gehört zum Horizont «lang» · [kurz] TRX/CHF: Position gehört zum Horizont «lang» · [kurz] ZEC/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [kurz] HYPE/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ZEC short (kurz) | 28.10.2026 20:17 | 28.10.2026 22:22 | 1'064.43 | 1'082.08 | 🔴 -0.54 CHF | Vorrang lang |
| TRX short (kurz) | 28.10.2026 20:17 | 28.10.2026 22:22 | 0.27 | 0.27 | 🔴 -0.38 CHF | Vorrang lang |

## 2️⃣ KI-Bot (lernend, kurz bis lang)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Simulation 2011-2022: +18 %/Jahr, 2023-2026: +14 %/Jahr._

Keine offene Position, alles in Cash.

**Signale jetzt**

| Coin | kurz (1h) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🔴 raus / Cash | ⚪ neutral | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash | ⚪ neutral | ⚪ neutral |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| SOL | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash | 🟢 investiert sein | ⚪ neutral |
| ZEC | ⚪ neutral | 🔴 raus / Cash | ⚪ neutral |
| HYPE | ⚪ neutral | 🟢 investiert sein | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 21'318 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, wild | pullback (-0.010 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| ETH | Abwärtstrend, wild | pullback (-0.010 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| BNB | Abwärtstrend, wild | pullback (-0.010 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| XRP | Abwärtstrend, wild | pullback (-0.010 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| SOL | Abwärtstrend, wild | pullback (-0.010 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ZEC | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.062 %/Kerze), reversal (+0.053 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: kein Signal · [kurz] HYPE/CHF: kein Signal

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long (lang) | 28.10.2026 16:15 | 30.10.2026 01:20 | 621.75 | 582.59 | 🔴 -16.15 CHF | Signal |
| HYPE short (lang) | 28.10.2026 20:19 | 29.10.2026 18:50 | 66.85 | 77.50 | 🔴 -7.71 CHF | Von Hand geschlossen |
| TRX short (lang) | 28.10.2026 20:19 | 29.10.2026 18:50 | 0.27 | 0.27 | 🔴 -1.38 CHF | Von Hand geschlossen |
| ETH long (mittel) | 28.10.2026 16:15 | 29.10.2026 01:23 | 1'934.17 | 1'953.68 | 🟢 +1.78 CHF | Vorrang lang |
| BTC short (mittel) | 28.10.2026 20:19 | 29.10.2026 01:23 | 67'094.94 | 67'266.32 | 🔴 -1.27 CHF | Vorrang lang |
| XRP short (mittel) | 28.10.2026 20:19 | 28.10.2026 21:18 | 1.10 | 1.10 | 🔴 -0.35 CHF | Signal |
| BNB long | 28.10.2026 13:15 | 28.10.2026 15:45 | 627.36 | 619.66 | 🔴 -4.18 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 15:45 | 1'946.78 | 1'929.91 | 🔴 -2.70 CHF | Stop-Loss (Gap) |
| BTC long | 27.10.2026 16:00 | 28.10.2026 14:15 | 66'509.84 | 66'883.94 | 🟢 +0.72 CHF | Signal |
| ETH long | 27.10.2026 16:00 | 28.10.2026 09:42 | 1'928.15 | 1'963.28 | 🟢 +3.74 CHF | Take-Profit |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 29.10.2026 01:24 | 67'266.32 | 63'839.80 | 0.001914 | 128.78 CHF | 122.22 CHF | 🔴 -6.56 CHF (-5.09 %) | 57'602.04 (-10 %) |
| **ETH** long (lang) | 29.10.2026 01:24 | 1'955.64 | 1'854.62 | 0.029964 | 58.60 CHF | 55.57 CHF | 🔴 -3.03 CHF (-5.17 %) | 1'542.64 (-17 %) |
| **BNB** long (lang) | 30.10.2026 01:21 | 568.49 | 581.11 | 0.142673 | 81.11 CHF | 82.91 CHF | 🟢 +1.80 CHF (+2.22 %) | 445.65 (-23 %) |
| **SOL** long (lang) | 30.10.2026 01:21 | 77.50 | 79.85 | 0.783734 | 60.74 CHF | 62.58 CHF | 🟢 +1.84 CHF (+3.02 %) | 55.18 (-31 %) |
| **TRX** long (lang) | 30.10.2026 01:21 | 0.30 | 0.27 | 451.864670 | 134.74 CHF | 124.17 CHF | 🔴 -10.57 CHF (-7.84 %) | 0.26 (-6 %) |
| **ZEC** long (lang) | 30.10.2026 01:21 | 992.34 | 1'052.07 | 0.029945 | 29.72 CHF | 31.50 CHF | 🟢 +1.79 CHF (+6.02 %) | 410.56 (-61 %) |
| **HYPE** long (lang) | 30.10.2026 01:21 | 73.47 | 74.08 | 0.704156 | 51.73 CHF | 52.17 CHF | 🟢 +0.43 CHF (+0.84 %) | 48.72 (-34 %) |

**Signale jetzt**

| Coin | mittel (4h) | lang (1d) |
|---|---|---|
| BTC | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🔴 raus / Cash | 🟢 investiert sein |
| BNB | 🔴 raus / Cash | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | ⚪ neutral |
| SOL | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🟢 investiert sein | 🟢 investiert sein |
| ZEC | 🟢 investiert sein | 🟢 investiert sein |
| HYPE | 🟢 investiert sein | 🟢 investiert sein |

**Letzte Entscheidung:** [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Position gehört zum Horizont «lang» · [mittel] ZEC/CHF: Position gehört zum Horizont «lang» · [mittel] HYPE/CHF: Position gehört zum Horizont «lang» · [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: kein Signal · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: Position offen, Signal bestätigt · [lang] ZEC/CHF: Position offen, Signal bestätigt · [lang] HYPE/CHF: Position offen, Signal bestätigt

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| TRX long (mittel) | 28.10.2026 20:19 | 29.10.2026 22:17 | 0.27 | 0.28 | 🟢 +1.33 CHF | Take-Profit |
| BNB long (mittel) | 28.10.2026 21:19 | 29.10.2026 12:08 | 623.82 | 624.61 | 🔴 -0.75 CHF | Stop-Loss (Gap) |
| XRP long (mittel) | 28.10.2026 20:19 | 29.10.2026 04:28 | 1.10 | 1.07 | 🔴 -6.61 CHF | Stop-Loss (Gap) |
| HYPE short (lang) | 28.10.2026 20:19 | 29.10.2026 01:24 | 66.92 | 66.77 | 🔴 -0.40 CHF | Signal |
| ZEC short (lang) | 28.10.2026 20:19 | 29.10.2026 01:24 | 1'066.19 | 1'083.41 | 🔴 -1.54 CHF | Signal |
| BTC long (mittel) | 28.10.2026 21:19 | 29.10.2026 01:24 | 67'178.57 | 67'199.08 | 🔴 -0.08 CHF | Signal |
| ETH long (kurz) | 28.10.2026 19:48 | 29.10.2026 01:24 | 1'950.58 | 1'953.68 | 🔴 -0.17 CHF | Signal |
| BTC short (kurz) | 28.10.2026 20:49 | 28.10.2026 21:19 | 67'362.30 | 67'178.57 | 🟢 +0.03 CHF | Signal |
| SOL short (kurz) | 28.10.2026 13:45 | 28.10.2026 20:49 | 84.18 | 85.00 | 🔴 -9.72 CHF | Stop-Loss (Gap) |
| BNB short (kurz) | 28.10.2026 17:48 | 28.10.2026 20:49 | 618.73 | 623.99 | 🔴 -0.28 CHF | Stop-Loss (Gap) |

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

- **Stimmung (Fear & Greed):** 30 von 100, Angst
- **Bewertung News:** -1.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** hack (gemeldet von coindesk, cointelegraph, decrypt – blockiert Käufe); crash (gemeldet von coindesk, cointelegraph, decrypt – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-10-30 21:16 UTC · **decrypt** · [Binance Hack Shows Why Offshore Exchanges Need US Oversight, CFTC Chair Says](https://decrypt.co/382285/binance-hack-why-offshore-exchanges-need-us-oversight-cftc-chair) _(Thema: hack)_
- 2026-10-30 20:06 UTC · **decrypt** · [Worried About Crypto Hacks? Buy Bitcoin Proxies in Stock Market Instead, Say Wall Street Firms](https://decrypt.co/382282/crypto-hacks-buy-bitcoin-proxies-stock-market-wall-street) _(Thema: hack)_
- 2026-10-30 18:45 UTC · **decrypt** · [Binance Hack: Why Bitcoin Didn't Crash Like It Did in 2018](https://decrypt.co/382257/binance-hack-why-bitcoin-didnt-crash) _(Thema: hack)_
- 2026-10-30 17:50 UTC · **decrypt** · [Secret Service, FBI Join Binance Hack Probe as Circle Freezes $823 Million](https://decrypt.co/382268/secret-service-fbi-binance-hack-probe) _(Thema: hack)_
- 2026-10-30 17:48 UTC · **cointelegraph** · [Coinbase leads crypto stock selloff following $6.3B Binance hack](https://cointelegraph.com/markets/coinbase-leads-crypto-stock-selloff-shares-tumble?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: hack)_
- 2026-10-30 16:49 UTC · **cointelegraph** · [As it happened: Binance’s record $6.3B crypto hack](https://cointelegraph.com/news/live-updates-binance-63b-hack-linked-to-north-koreas-tradertraitor?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: hack)_
- 2026-10-30 16:06 UTC · **cointelegraph** · [Bitcoin risks worst October in 12 years as tech sell-off spreads to gold](https://cointelegraph.com/markets/bitcoin-risks-worst-october-in-12-years-as-tech-sell-off-spreads-to-gold?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: crash)_
- 2026-10-30 14:13 UTC · **coindesk** · [Wall Street analysts urge investors to buy crypto stocks after $6.3 billion Binance hack](https://www.coindesk.com/markets/2026/10/30/wall-street-analysts-urge-investors-to-buy-crypto-stocks-on-weakness-after-usd6-3-billion-binance-hack) _(Thema: hack)_
