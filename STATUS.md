# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **02.11.2026 15:05** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Simulation 2011-2022: +18 %/Jahr, 2023-2026: +14 %/Jahr.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **961.13 CHF** | **922.04 CHF** | **331.25 CHF** |
| Gewinn / Verlust | 🔴 -38.87 CHF (-3.89 %) | 🔴 -77.96 CHF (-7.80 %) | 🔴 -668.75 CHF (-66.87 %) |
| Im Einsatz (investiert) | 435.09 CHF (45 %) | 0.00 CHF (0 %) | 401.55 CHF (121 %) |
| Cash (nicht investiert) | 526.04 CHF | 922.04 CHF | -70.30 CHF |
| Offene Positionen | 6 | 0 | 6 |
| Abgeschlossene Trades | 3 | 24 | 183 |
| Gebühren bisher | 4.40 CHF | 44.26 CHF | 561.19 CHF |
| Gebührenstufe | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 870 CHF) | Stufe 3: 0.38 % je Market-Order (30-Tage-Umsatz 10'817 CHF) | Stufe 6: 0.25 % je Market-Order (30-Tage-Umsatz 129'360 CHF) |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 48 % · mittel 26 % · kurz 26 % | kurz 24 % · mittel 35 % · lang 41 % | mittel 67 % · lang 33 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 9.50 CHF) |
| Hebel aktuell | – | – | 1.21× (erlaubt 3×) |
| Buchhaltung | ✅ stimmt (Abweichung 0.00 CHF) · Altlasten vor 28.10.: 0.01 CHF | ✅ stimmt (Abweichung 0.00 CHF) · Altlasten vor 28.10.: 0.04 CHF | ✅ stimmt (Abweichung 0.00 CHF) · Altlasten vor 28.10.: 8.50 CHF |
| Letzter Durchlauf | 02.11.2026 15:02 (vor 2 Min.) | 02.11.2026 15:03 (vor 1 Min.) | 02.11.2026 15:04 (gerade eben) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **948.08 CHF** |
| Gewinn / Verlust | 🔴 -51.92 CHF (-5.19 %) |
| **Aktuelle Verteilung** | Langfrist 25 % · KI 17 % · Risiko 3 % · Cash 55 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist -1.6 %, KI -4.2 %, Risiko -67.4 % |
| Umschicht-Gebühren bisher | 5.11 CHF |
| Erfahrung im Gedächtnis | 503 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.005 %/Lauf, KI -0.013 %/Lauf, Risiko -0.289 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 63'815.00 CHF | 🔴 -1.20 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'875.11 CHF | 🔴 -0.16 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 576.51 CHF | 🔴 -1.20 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.03 CHF | 🟢 +0.19 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 77.15 CHF | 🔴 -0.30 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.26 CHF | 🟢 +1.48 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'033.26 CHF | 🟢 +2.22 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 70.35 CHF | 🔴 -2.19 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 23.10.2026 18:09 | 67'388.78 | 63'815.00 | 0.001485 | 100.05 CHF | 94.74 CHF | 🔴 -5.31 CHF (-5.30 %) | 53'251.84 (-17 %) |
| **ETH** long (lang) | 23.10.2026 18:09 | 1'986.19 | 1'875.11 | 0.040710 | 80.86 CHF | 76.34 CHF | 🔴 -4.52 CHF (-5.59 %) | 1'371.11 (-27 %) |
| **BNB** long (lang) | 23.10.2026 19:15 | 617.14 | 576.51 | 0.162070 | 100.02 CHF | 93.43 CHF | 🔴 -6.59 CHF (-6.58 %) | 483.48 (-16 %) |
| **XRP** long (lang) | 23.10.2026 19:15 | 1.08 | 1.03 | 58.690975 | 63.53 CHF | 60.20 CHF | 🔴 -3.33 CHF (-5.24 %) | 0.66 (-36 %) |
| **SOL** long (lang) | 23.10.2026 19:15 | 86.38 | 77.15 | 0.797780 | 68.91 CHF | 61.55 CHF | 🔴 -7.36 CHF (-10.69 %) | 55.00 (-29 %) |
| **ZEC** long (lang) | 01.11.2026 16:31 | 1'021.01 | 1'033.26 | 0.047253 | 48.25 CHF | 48.82 CHF | 🟢 +0.58 CHF (+1.20 %) | 278.44 (-73 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| XRP | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🔴 raus / Cash | 🟢 investiert sein |
| HYPE | 🟢 investiert sein | ⚪ neutral | 🔴 raus / Cash |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: kein Signal · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: Signal 'raus', bleibe in Cash · [lang] ZEC/CHF: Position offen, Signal bestätigt · [lang] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Position gehört zum Horizont «lang» · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: Position gehört zum Horizont «lang» · [mittel] HYPE/CHF: kein Signal · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Position gehört zum Horizont «lang» · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: Position gehört zum Horizont «lang» · [kurz] SOL/CHF: Position gehört zum Horizont «lang» · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Position gehört zum Horizont «lang» · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| TRX long (lang) | 29.10.2026 18:11 | 31.10.2026 23:28 | 0.27 | 0.25 | 🔴 -8.69 CHF | Stop-Loss |
| ZEC short (kurz) | 28.10.2026 20:17 | 28.10.2026 22:22 | 1'064.43 | 1'082.08 | 🔴 -0.67 CHF | Vorrang lang |
| TRX short (kurz) | 28.10.2026 20:17 | 28.10.2026 22:22 | 0.27 | 0.27 | 🔴 -0.90 CHF | Vorrang lang |

## 2️⃣ KI-Bot (lernend, kurz bis lang)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Simulation 2011-2022: +18 %/Jahr, 2023-2026: +14 %/Jahr._

Keine offene Position, alles in Cash.

**Signale jetzt**

| Coin | kurz (1h) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🟢 investiert sein | ⚪ neutral | ⚪ neutral |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash | ⚪ neutral | ⚪ neutral |
| XRP | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | 🟢 investiert sein | ⚪ neutral |
| TRX | 🔴 raus / Cash | ⚪ neutral | ⚪ neutral |
| ZEC | ⚪ neutral | 🟢 investiert sein | ⚪ neutral |
| HYPE | 🔴 raus / Cash | ⚪ neutral | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 21'798 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, ruhig | labor_5 (+0.022 %/Kerze), mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze) |
| ETH | Seitwärts, ruhig | labor_5 (+0.022 %/Kerze), mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze) |
| BNB | Abwärtstrend, ruhig | trend (-0.009 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.010 %/Kerze) |
| XRP | Seitwärts, ruhig | labor_5 (+0.022 %/Kerze), mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.009 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.010 %/Kerze) |
| TRX | Abwärtstrend, ruhig | trend (-0.009 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.010 %/Kerze) |
| ZEC | Seitwärts, ruhig | labor_5 (+0.022 %/Kerze), mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (-0.009 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.010 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 5 (labor_3, labor_4, labor_2, labor_1, labor_5), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [kurz] ETH/CHF: kein Einstieg (erwartete Bewegung zu klein für die Gebühren) · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: kein Signal · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: kein Signal · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long (lang) | 28.10.2026 16:15 | 30.10.2026 01:20 | 621.75 | 582.59 | 🔴 -17.38 CHF | Signal |
| HYPE short (lang) | 28.10.2026 20:19 | 29.10.2026 18:50 | 66.85 | 77.50 | 🔴 -7.96 CHF | Von Hand geschlossen |
| TRX short (lang) | 28.10.2026 20:19 | 29.10.2026 18:50 | 0.27 | 0.27 | 🔴 -2.62 CHF | Von Hand geschlossen |
| ETH long (mittel) | 28.10.2026 16:15 | 29.10.2026 01:23 | 1'934.17 | 1'953.68 | 🟢 +1.16 CHF | Vorrang lang |
| BTC short (mittel) | 28.10.2026 20:19 | 29.10.2026 01:23 | 67'094.94 | 67'266.32 | 🔴 -1.89 CHF | Vorrang lang |
| XRP short (mittel) | 28.10.2026 20:19 | 28.10.2026 21:18 | 1.10 | 1.10 | 🔴 -0.59 CHF | Signal |
| BNB long | 28.10.2026 13:15 | 28.10.2026 15:45 | 627.36 | 619.66 | 🔴 -5.43 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 15:45 | 1'946.78 | 1'929.91 | 🔴 -3.33 CHF | Stop-Loss (Gap) |
| BTC long | 27.10.2026 16:00 | 28.10.2026 14:15 | 66'509.84 | 66'883.94 | 🟢 +0.10 CHF | Signal |
| ETH long | 27.10.2026 16:00 | 28.10.2026 09:42 | 1'928.15 | 1'963.28 | 🟢 +3.12 CHF | Take-Profit |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 29.10.2026 01:24 | 67'266.32 | 63'815.00 | 0.001914 | 128.78 CHF | 122.17 CHF | 🔴 -6.61 CHF (-5.13 %) | 57'602.04 (-10 %) |
| **ETH** long (lang) | 29.10.2026 01:24 | 1'955.64 | 1'875.11 | 0.029964 | 58.60 CHF | 56.18 CHF | 🔴 -2.41 CHF (-4.12 %) | 1'542.64 (-18 %) |
| **BNB** long (lang) | 30.10.2026 01:21 | 568.49 | 576.51 | 0.142673 | 81.11 CHF | 82.25 CHF | 🟢 +1.14 CHF (+1.41 %) | 445.65 (-23 %) |
| **SOL** long (lang) | 30.10.2026 01:21 | 77.50 | 77.15 | 0.783734 | 60.74 CHF | 60.46 CHF | 🔴 -0.28 CHF (-0.46 %) | 55.18 (-28 %) |
| **ZEC** long (lang) | 30.10.2026 01:21 | 992.34 | 1'033.26 | 0.029945 | 29.72 CHF | 30.94 CHF | 🟢 +1.23 CHF (+4.12 %) | 410.56 (-60 %) |
| **HYPE** long (lang) | 30.10.2026 01:21 | 73.47 | 70.35 | 0.704156 | 51.73 CHF | 49.54 CHF | 🔴 -2.19 CHF (-4.24 %) | 48.72 (-31 %) |

**Signale jetzt**

| Coin | mittel (4h) | lang (1d) |
|---|---|---|
| BTC | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🔴 raus / Cash | 🟢 investiert sein |
| BNB | 🔴 raus / Cash | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | ⚪ neutral |
| SOL | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🔴 raus / Cash | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🟢 investiert sein |
| HYPE | 🟢 investiert sein | 🟢 investiert sein |

**Letzte Entscheidung:** [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: Position gehört zum Horizont «lang» · [mittel] HYPE/CHF: Position gehört zum Horizont «lang»

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| TRX long (lang) | 30.10.2026 01:21 | 31.10.2026 16:40 | 0.30 | 0.26 | 🔴 -18.66 CHF | Stop-Loss |
| TRX long (mittel) | 28.10.2026 20:19 | 29.10.2026 22:17 | 0.27 | 0.28 | 🟢 +0.56 CHF | Take-Profit |
| BNB long (mittel) | 28.10.2026 21:19 | 29.10.2026 12:08 | 623.82 | 624.61 | 🔴 -1.74 CHF | Stop-Loss (Gap) |
| XRP long (mittel) | 28.10.2026 20:19 | 29.10.2026 04:28 | 1.10 | 1.07 | 🔴 -7.63 CHF | Stop-Loss (Gap) |
| HYPE short (lang) | 28.10.2026 20:19 | 29.10.2026 01:24 | 66.92 | 66.77 | 🔴 -1.07 CHF | Signal |
| ZEC short (lang) | 28.10.2026 20:19 | 29.10.2026 01:24 | 1'066.19 | 1'083.41 | 🔴 -1.92 CHF | Signal |
| BTC long (mittel) | 28.10.2026 21:19 | 29.10.2026 01:24 | 67'178.57 | 67'199.08 | 🔴 -0.16 CHF | Signal |
| ETH long (kurz) | 28.10.2026 19:48 | 29.10.2026 01:24 | 1'950.58 | 1'953.68 | 🔴 -0.60 CHF | Signal |
| BTC short (kurz) | 28.10.2026 20:49 | 28.10.2026 21:19 | 67'362.30 | 67'178.57 | 🔴 -0.47 CHF | Signal |
| SOL short (kurz) | 28.10.2026 13:45 | 28.10.2026 20:49 | 84.18 | 85.00 | 🔴 -13.10 CHF | Stop-Loss (Gap) |

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

- **Stimmung (Fear & Greed):** 37 von 100, Angst
- **Bewertung News:** -1.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** hack (gemeldet von coindesk, cointelegraph, decrypt – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-11-02 12:40 UTC · **cointelegraph** · [Binance hackers begin swapping stolen Solana tokens for Bitcoin: Chainalysis](https://cointelegraph.com/news/binance-hackers-solana-new-phase-laundering-chainalysis?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: hack)_
- 2026-11-02 11:19 UTC · **cointelegraph** · [From Uptober to Hacktober: Are Bitcoin’s seasonal patterns becoming obsolete?](https://cointelegraph.com/markets/uptober-hacktober-bitcoin-seasonal-pattern?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: hack)_
- 2026-11-02 10:36 UTC · **decrypt** · [FBI Blames North Korea for $6B Binance Hack as Exchange Reopens Withdrawals](https://decrypt.co/382316/fbi-blames-north-korea-for-6b-binance-hack-as-exchange-reopens-withdrawals) _(Thema: hack)_
- 2026-11-02 09:04 UTC · **coindesk** · [Binance hack fallout, U.S. midterms and jobs report: Crypto Week Ahead](https://www.coindesk.com/markets/2026/11/02/binance-hack-fallout-u-s-midterms-and-jobs-report-crypto-week-ahead) _(Thema: hack)_
- 2026-11-02 07:50 UTC · **cointelegraph** · [Bitcoin ETFs sink into October outflows with $643M exit after Binance hack](https://cointelegraph.com/markets/bitcoin-etfs-october-red-binance-hack-outflows?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: hack)_
- 2026-11-02 05:18 UTC · **coindesk** · [Strangers are begging the Binance hacker for bitcoin, one ‘help me bro’ at a time](https://www.coindesk.com/tech/2026/11/02/strangers-are-begging-the-binance-hacker-for-bitcoin-one-help-me-bro-at-a-time) _(Thema: hack)_
- 2026-11-02 04:42 UTC · **coindesk** · [Bitcoin claws back toward $79,000 as markets shake off crypto's biggest hack](https://www.coindesk.com/markets/2026/11/02/bitcoin-claws-back-toward-usd79-000-as-markets-shake-off-crypto-s-biggest-hack) _(Thema: hack)_
- 2026-11-02 04:41 UTC · **coindesk** · [BTCPay, a bitcoin payment tool, tells users to switch off their servers after reports of drained wallets](https://www.coindesk.com/tech/2026/11/02/btcpay-a-bitcoin-payment-tool-tells-users-to-switch-off-their-servers-after-reports-of-drained-wallets) _(Thema: hack)_
