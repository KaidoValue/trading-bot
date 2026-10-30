# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **30.10.2026 01:51** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Simulation 2011-2022: +18 %/Jahr, 2023-2026: +14 %/Jahr.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **971.34 CHF** | **922.04 CHF** | **349.06 CHF** |
| Gewinn / Verlust | 🔴 -28.66 CHF (-2.87 %) | 🔴 -77.96 CHF (-7.80 %) | 🔴 -650.94 CHF (-65.09 %) |
| Im Einsatz (investiert) | 471.95 CHF (49 %) | 0.00 CHF (0 %) | 535.34 CHF (153 %) |
| Cash (nicht investiert) | 499.39 CHF | 922.04 CHF | -186.28 CHF |
| Offene Positionen | 6 | 0 | 7 |
| Abgeschlossene Trades | 2 | 24 | 182 |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 23 % · mittel 35 % · lang 42 % | mittel 47 % · lang 53 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.60 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **952.69 CHF** |
| Gewinn / Verlust | 🔴 -47.31 CHF (-4.73 %) |
| **Aktuelle Verteilung** | Langfrist 20 % · KI 6 % · Risiko 3 % · Cash 70 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -3.2 %, KI -7.9 %, Risiko -59.8 % |
| Umschicht-Gebühren bisher | 4.35 CHF |
| Erfahrung im Gedächtnis | 328 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.013 %/Lauf, KI -0.038 %/Lauf, Risiko -0.283 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 63'084.30 CHF | 🔴 -1.66 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'812.53 CHF | 🔴 -1.97 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 568.22 CHF | 🔴 -0.75 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.01 CHF | 🔴 -1.01 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 77.48 CHF | 🔴 -1.24 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.30 CHF | 🟢 +1.22 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'011.07 CHF | 🟢 +0.84 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 74.93 CHF | 🟢 +2.60 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 23.10.2026 18:09 | 67'388.78 | 63'084.30 | 0.001485 | 100.05 CHF | 93.66 CHF | 🔴 -6.39 CHF (-6.39 %) | 53'251.84 (-16 %) |
| **ETH** long (lang) | 23.10.2026 18:09 | 1'986.19 | 1'812.53 | 0.040710 | 80.86 CHF | 73.79 CHF | 🔴 -7.07 CHF (-8.74 %) | 1'371.11 (-24 %) |
| **BNB** long (lang) | 23.10.2026 19:15 | 617.14 | 568.22 | 0.162070 | 100.02 CHF | 92.09 CHF | 🔴 -7.93 CHF (-7.93 %) | 483.48 (-15 %) |
| **XRP** long (lang) | 23.10.2026 19:15 | 1.08 | 1.01 | 58.690975 | 63.53 CHF | 58.99 CHF | 🔴 -4.53 CHF (-7.14 %) | 0.66 (-35 %) |
| **SOL** long (lang) | 23.10.2026 19:15 | 86.38 | 77.48 | 0.797780 | 68.91 CHF | 61.81 CHF | 🔴 -7.10 CHF (-10.30 %) | 55.00 (-29 %) |
| **TRX** long (lang) | 29.10.2026 18:11 | 0.27 | 0.30 | 305.677317 | 83.55 CHF | 91.61 CHF | 🟢 +8.06 CHF (+9.65 %) | 0.25 (-17 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| XRP | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🟢 investiert sein | 🟢 investiert sein | 🟢 investiert sein |
| ZEC | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| HYPE | 🟢 investiert sein | ⚪ neutral | 🟢 investiert sein |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: kein Signal · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: Position offen, Signal bestätigt · [lang] ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [lang] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Position gehört zum Horizont «lang» · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Position gehört zum Horizont «lang» · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: kein Signal · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Position gehört zum Horizont «lang» · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: Position gehört zum Horizont «lang» · [kurz] SOL/CHF: Position gehört zum Horizont «lang» · [kurz] TRX/CHF: Position gehört zum Horizont «lang» · [kurz] ZEC/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [kurz] HYPE/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren)

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
| BNB | 🔴 raus / Cash | ⚪ neutral | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | 🟢 investiert sein | ⚪ neutral |
| TRX | ⚪ neutral | 🟢 investiert sein | 🟢 investiert sein |
| ZEC | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| HYPE | ⚪ neutral | 🟢 investiert sein | ⚪ neutral |

**🧠 KI-Gedächtnis:** 21'110 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| ETH | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| BNB | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| XRP | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| SOL | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| TRX | Aufwärtstrend, wild | trend (+0.075 %/Kerze), momentum (+0.064 %/Kerze), reversal (+0.055 %/Kerze) |
| ZEC | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.075 %/Kerze), momentum (+0.064 %/Kerze), reversal (+0.055 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: kein Signal · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: kein Signal · [mittel] BTC/CHF: Signal 'raus', bleibe in Cash · [mittel] ETH/CHF: kein Signal · [mittel] BNB/CHF: kein Signal · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [mittel] TRX/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [lang] BTC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [lang] ETH/CHF: Signal 'raus', bleibe in Cash · [lang] BNB/CHF: Signal 'raus', bleibe in Cash · [lang] XRP/CHF: Signal 'raus', bleibe in Cash · [lang] SOL/CHF: kein Signal · [lang] TRX/CHF: kein Einstieg (Pause nach Verlustserie) · [lang] ZEC/CHF: Signal 'raus', bleibe in Cash · [lang] HYPE/CHF: kein Signal

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
| **BTC** long (lang) | 29.10.2026 01:24 | 67'266.32 | 63'084.30 | 0.001914 | 128.78 CHF | 120.77 CHF | 🔴 -8.01 CHF (-6.22 %) | 57'602.04 (-9 %) |
| **ETH** long (lang) | 29.10.2026 01:24 | 1'955.64 | 1'812.53 | 0.029964 | 58.60 CHF | 54.31 CHF | 🔴 -4.29 CHF (-7.32 %) | 1'542.64 (-15 %) |
| **BNB** long (lang) | 30.10.2026 01:21 | 568.49 | 568.22 | 0.142673 | 81.11 CHF | 81.07 CHF | 🔴 -0.04 CHF (-0.05 %) | 445.65 (-22 %) |
| **SOL** long (lang) | 30.10.2026 01:21 | 77.50 | 77.48 | 0.783734 | 60.74 CHF | 60.72 CHF | 🔴 -0.02 CHF (-0.04 %) | 55.18 (-29 %) |
| **TRX** long (lang) | 30.10.2026 01:21 | 0.30 | 0.30 | 451.864670 | 134.74 CHF | 135.42 CHF | 🟢 +0.68 CHF (+0.51 %) | 0.26 (-13 %) |
| **ZEC** long (lang) | 30.10.2026 01:21 | 992.34 | 1'011.07 | 0.029945 | 29.72 CHF | 30.28 CHF | 🟢 +0.56 CHF (+1.89 %) | 410.56 (-59 %) |
| **HYPE** long (lang) | 30.10.2026 01:21 | 73.47 | 74.93 | 0.704156 | 51.73 CHF | 52.77 CHF | 🟢 +1.03 CHF (+2.00 %) | 48.72 (-35 %) |

**Signale jetzt**

| Coin | mittel (4h) | lang (1d) |
|---|---|---|
| BTC | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🔴 raus / Cash | 🟢 investiert sein |
| BNB | 🟢 investiert sein | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | ⚪ neutral |
| SOL | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🟢 investiert sein | 🟢 investiert sein |
| ZEC | 🟢 investiert sein | 🟢 investiert sein |
| HYPE | 🟢 investiert sein | 🟢 investiert sein |

**Letzte Entscheidung:** [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Signal 'raus', bleibe in Cash · [mittel] TRX/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [mittel] ZEC/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [mittel] HYPE/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: gekauft 0.142673 @ 568.49 · [lang] XRP/CHF: kein Signal · [lang] SOL/CHF: gekauft 0.783734 @ 77.50 · [lang] TRX/CHF: gekauft 451.864670 @ 0.30 · [lang] ZEC/CHF: gekauft 0.029945 @ 992.34 · [lang] HYPE/CHF: gekauft 0.704156 @ 73.47

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
- **Bestätigte Themen:** hack (gemeldet von bitcoinmagazine, coindesk, cointelegraph, decrypt – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-10-29 23:24 UTC · **cointelegraph** · [Binance hack rattles crypto markets as BNB falls 7%, Bitcoin slides](https://cointelegraph.com/markets/binance-hack-rattles-crypto-markets-bnb-bitcoin-slide?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: hack)_
- 2026-10-29 23:06 UTC · **bitcoinmagazine** · [Bitcoin Price Slides Below $79,000 as Binance Loses $5.8 Billion in Massive Hack](https://bitcoinmagazine.com/news/bitcoin-price-slides-binance) _(Thema: hack)_
- 2026-10-29 22:57 UTC · **decrypt** · [Binance Hacker Hunts for Exit Ramps as DeFi Exchanges Pause Markets](https://decrypt.co/382194/binance-hack-exit-ramps-defi-exchange-ethereum) _(Thema: hack)_
- 2026-10-29 21:12 UTC · **coindesk** · [Binance loses $5.7 billion in 'biggest crypto hack in history'](https://www.coindesk.com/business/2026/10/29/potential-multi-billion-binance-hack-hitting-crypto-markets) _(Thema: hack)_
- 2026-10-29 19:23 UTC · **cointelegraph** · [Polymarket suspended trading amid reports of user funds being drained](https://cointelegraph.com/news/polymarket-suspends-trading-user-funds-compromised?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: hack)_
- 2026-10-29 18:55 UTC · **coindesk** · [Polymarket suspends trading after third-party breach leads to user losses](https://www.coindesk.com/markets/2026/10/29/polymarket-suspends-trading-after-third-party-breach-leads-to-user-losses) _(Thema: hack)_
- 2026-10-29 18:46 UTC · **decrypt** · [Hackers Publish Work Details of 41,000 Homeland Security Employees](https://decrypt.co/382181/hackers-publish-work-details-homeland-security-employees) _(Thema: hack)_
- 2026-10-29 10:41 UTC · **coindesk** · [Live updates: Binance confirms security breach, says 'will cover all hacking losses'](https://www.coindesk.com/business/2026/10/29/live-updates-bitcoin-clings-to-usd80-000-as-strategy-s-cushion-thins-before-earnings) _(Thema: hack)_
