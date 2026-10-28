# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **28.10.2026 20:51** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt aber auch mittelfristig (4h) und kurzfristig (1h), long und short. Max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, long und short.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: handelt kurz (30 Min.), mittel (4h) und lang (Tageskerzen), long und short, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **997.45 CHF** | **949.19 CHF** | **370.75 CHF** |
| Gewinn / Verlust | 🔴 -2.55 CHF (-0.26 %) | 🔴 -50.81 CHF (-5.08 %) | 🔴 -629.25 CHF (-62.93 %) |
| Im Einsatz (investiert) | 537.82 CHF (54 %) | 1'051.17 CHF (111 %) | 900.72 CHF (243 %) |
| Cash (nicht investiert) | 708.79 CHF | 1'041.27 CHF | 252.51 CHF |
| Offene Positionen | 7 | 6 | 6 |
| Abgeschlossene Trades | 0 | 18 | 174 |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: trend 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | kurz: breakout 30m · mittel: breakout 4h · lang: breakout 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 40 % · mittel 30 % · lang 30 % | kurz 32 % · mittel 34 % · lang 34 % |
| Short erlaubt | ja | ja | ja |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.48 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **970.92 CHF** |
| Gewinn / Verlust | 🔴 -29.08 CHF (-2.91 %) |
| **Aktuelle Verteilung** | Langfrist 32 % · KI 21 % · Risiko 3 % · Cash 44 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.5 %, KI -2.9 %, Risiko -76.0 %, 🚨 Notbremse Risiko (-3.7 % in 3 Std.) |
| Umschicht-Gebühren bisher | 3.27 CHF |
| Erfahrung im Gedächtnis | 265 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.006 %/Lauf, KI -0.004 %/Lauf, Risiko -0.422 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'396.00 CHF | 🟢 +0.81 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'957.79 CHF | 🟢 +0.86 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 623.61 CHF | 🟢 +1.24 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.10 CHF | 🟢 +0.14 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.85 CHF | 🟢 +1.21 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.58 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'070.37 CHF | 🔴 -1.20 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 67.39 CHF | 🟢 +0.22 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt aber auch mittelfristig (4h) und kurzfristig (1h), long und short. Max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 23.10.2026 18:09 | 67'388.78 | 67'396.00 | 0.001485 | 100.05 CHF | 100.06 CHF | 🟢 +0.01 CHF (+0.01 %) | 53'251.84 (-21 %) |
| **ETH** long (lang) | 23.10.2026 18:09 | 1'986.19 | 1'957.79 | 0.040710 | 80.86 CHF | 79.70 CHF | 🔴 -1.16 CHF (-1.43 %) | 1'371.11 (-30 %) |
| **BNB** long (lang) | 23.10.2026 19:15 | 617.14 | 623.61 | 0.162070 | 100.02 CHF | 101.07 CHF | 🟢 +1.05 CHF (+1.05 %) | 483.48 (-22 %) |
| **XRP** long (lang) | 23.10.2026 19:15 | 1.08 | 1.10 | 58.690975 | 63.53 CHF | 64.72 CHF | 🟢 +1.19 CHF (+1.87 %) | 0.66 (-41 %) |
| **SOL** long (lang) | 23.10.2026 19:15 | 86.38 | 84.85 | 0.797780 | 68.91 CHF | 67.69 CHF | 🔴 -1.22 CHF (-1.77 %) | 55.00 (-35 %) |
| **TRX** short (kurz) | 28.10.2026 20:17 | 0.27 | 0.27 | 365.077967 | 99.60 CHF | 99.56 CHF | 🟢 +0.04 CHF (+0.04 %) | 0.27 (+1 %) |
| **ZEC** short (kurz) | 28.10.2026 20:17 | 1'064.43 | 1'070.37 | 0.023373 | 24.88 CHF | 25.02 CHF | 🔴 -0.14 CHF (-0.56 %) | 1'092.74 (+2 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | ⚪ neutral |
| BNB | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| XRP | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein | 🟢 investiert sein | ⚪ neutral |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: Position offen, Signal bestätigt · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: Position gehört zum Horizont «kurz» · [lang] ZEC/CHF: Position gehört zum Horizont «kurz» · [lang] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Position gehört zum Horizont «lang» · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Position gehört zum Horizont «kurz» · [mittel] ZEC/CHF: Position gehört zum Horizont «kurz» · [mittel] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: kein Signal · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: Position gehört zum Horizont «lang» · [kurz] SOL/CHF: Position gehört zum Horizont «lang» · [kurz] TRX/CHF: Position offen, Signal bestätigt · [kurz] ZEC/CHF: Position offen, Signal bestätigt · [kurz] HYPE/CHF: kein Signal

## 2️⃣ KI-Bot (lernend, kurz bis lang)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, long und short._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **ETH** long (kurz) | 28.10.2026 16:15 | 1'934.17 | 1'957.79 | 0.123031 | 237.96 CHF | 240.87 CHF | 🟢 +2.91 CHF (+1.22 %) | 1'916.06 (-2 %) |
| **BNB** long (kurz) | 28.10.2026 16:15 | 621.75 | 623.61 | 0.382729 | 237.96 CHF | 238.67 CHF | 🟢 +0.71 CHF (+0.30 %) | 614.56 (-1 %) |
| **BTC** short (mittel) | 28.10.2026 20:19 | 67'094.94 | 67'396.00 | 0.003544 | 237.81 CHF | 238.87 CHF | 🔴 -1.07 CHF (-0.45 %) | 68'876.82 (+2 %) |
| **XRP** short (mittel) | 28.10.2026 20:19 | 1.10 | 1.10 | 43.275678 | 47.46 CHF | 47.72 CHF | 🔴 -0.26 CHF (-0.55 %) | 1.14 (+4 %) |
| **TRX** short (lang) | 28.10.2026 20:19 | 0.27 | 0.27 | 870.667829 | 237.55 CHF | 237.43 CHF | 🟢 +0.12 CHF (+0.05 %) | 0.29 (+5 %) |
| **HYPE** short (lang) | 28.10.2026 20:19 | 66.85 | 67.39 | 0.706372 | 47.22 CHF | 47.60 CHF | 🔴 -0.38 CHF (-0.80 %) | 80.08 (+19 %) |

**Signale jetzt**

| Coin | kurz (1h) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🔴 raus / Cash | 🔴 raus / Cash | ⚪ neutral |
| ETH | ⚪ neutral | 🟢 investiert sein | 🔴 raus / Cash |
| BNB | ⚪ neutral | 🟢 investiert sein | ⚪ neutral |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | ⚪ neutral |
| SOL | ⚪ neutral | ⚪ neutral | ⚪ neutral |
| TRX | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash | 🔴 raus / Cash | ⚪ neutral |
| HYPE | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 20'878 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ETH | Aufwärtstrend, ruhig | trend (+0.060 %/Kerze), reversal (+0.029 %/Kerze), momentum (+0.027 %/Kerze) |
| BNB | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.065 %/Kerze), reversal (+0.056 %/Kerze) |
| XRP | Aufwärtstrend, ruhig | trend (+0.060 %/Kerze), reversal (+0.029 %/Kerze), momentum (+0.027 %/Kerze) |
| SOL | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.065 %/Kerze), reversal (+0.056 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.060 %/Kerze), reversal (+0.029 %/Kerze), momentum (+0.027 %/Kerze) |
| HYPE | Aufwärtstrend, ruhig | trend (+0.060 %/Kerze), reversal (+0.029 %/Kerze), momentum (+0.027 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] ETH/CHF: kein Signal · [kurz] BNB/CHF: kein Signal · [kurz] XRP/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] SOL/CHF: kein Signal · [kurz] TRX/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] HYPE/CHF: kein Signal · [mittel] BTC/CHF: short eröffnet 0.003544 @ 67094.94 · [mittel] ETH/CHF: Position gehört zum Horizont «kurz» · [mittel] BNB/CHF: Position gehört zum Horizont «kurz» · [mittel] XRP/CHF: short eröffnet 43.275678 @ 1.10 · [mittel] SOL/CHF: kein Signal · [mittel] TRX/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [mittel] HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] BTC/CHF: kein Signal · [lang] ETH/CHF: Position gehört zum Horizont «kurz» · [lang] BNB/CHF: kein Signal · [lang] XRP/CHF: Position gehört zum Horizont «mittel» · [lang] SOL/CHF: kein Signal · [lang] TRX/CHF: short eröffnet 870.667829 @ 0.27 · [lang] ZEC/CHF: kein Signal · [lang] HYPE/CHF: short eröffnet 0.706372 @ 66.85

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long | 28.10.2026 13:15 | 28.10.2026 15:45 | 627.36 | 619.66 | 🔴 -4.18 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 15:45 | 1'946.78 | 1'929.91 | 🔴 -2.70 CHF | Stop-Loss (Gap) |
| BTC long | 27.10.2026 16:00 | 28.10.2026 14:15 | 66'509.84 | 66'883.94 | 🟢 +0.72 CHF | Signal |
| ETH long | 27.10.2026 16:00 | 28.10.2026 09:42 | 1'928.15 | 1'963.28 | 🟢 +3.74 CHF | Take-Profit |
| BNB long | 27.10.2026 18:00 | 28.10.2026 01:06 | 622.33 | 614.56 | 🔴 -4.25 CHF | Stop-Loss (Gap) |
| ZEC long | 26.10.2026 10:10 | 27.10.2026 17:30 | 1'006.92 | 1'072.51 | 🟢 +14.25 CHF | Take-Profit |
| BTC long | 26.10.2026 10:10 | 26.10.2026 15:16 | 66'289.23 | 66'013.88 | 🔴 -1.61 CHF | Signal |
| ETH long | 26.10.2026 13:13 | 26.10.2026 14:13 | 1'930.96 | 1'911.28 | 🔴 -3.05 CHF | Signal |
| TRX long | 23.10.2026 20:16 | 26.10.2026 11:13 | 0.27 | 0.27 | 🔴 -0.31 CHF | Signal |
| BTC long | 26.10.2026 00:04 | 26.10.2026 00:34 | 66'419.29 | 65'838.16 | 🔴 -2.72 CHF | Stop-Loss (Gap) |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: handelt kurz (30 Min.), mittel (4h) und lang (Tageskerzen), long und short, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **ETH** long (kurz) | 28.10.2026 19:48 | 1'950.58 | 1'957.79 | 0.083780 | 163.42 CHF | 164.02 CHF | 🟢 +0.60 CHF (+0.37 %) | 1'941.70 (-1 %) |
| **XRP** long (mittel) | 28.10.2026 20:19 | 1.10 | 1.10 | 178.546264 | 196.03 CHF | 196.88 CHF | 🟢 +0.85 CHF (+0.44 %) | 1.07 (-3 %) |
| **TRX** long (mittel) | 28.10.2026 20:19 | 0.27 | 0.27 | 544.830158 | 148.80 CHF | 148.58 CHF | 🔴 -0.22 CHF (-0.15 %) | 0.27 (-1 %) |
| **ZEC** short (lang) | 28.10.2026 20:19 | 1'066.19 | 1'070.37 | 0.067046 | 71.48 CHF | 71.76 CHF | 🔴 -0.28 CHF (-0.39 %) | 1'351.76 (+26 %) |
| **HYPE** short (lang) | 28.10.2026 20:19 | 66.92 | 67.39 | 1.929710 | 129.14 CHF | 130.04 CHF | 🔴 -0.90 CHF (-0.70 %) | 76.85 (+14 %) |
| **BTC** short (kurz) | 28.10.2026 20:49 | 67'362.30 | 67'396.00 | 0.002811 | 189.34 CHF | 189.43 CHF | 🔴 -0.09 CHF (-0.05 %) | 67'662.18 (+0 %) |

**Signale jetzt**

| Coin | kurz (30m) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| ETH | 🟢 investiert sein | 🟢 investiert sein | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash | 🟢 investiert sein | 🔴 raus / Cash |

**Letzte Entscheidung:** [kurz] BTC/CHF: short eröffnet 0.002811 @ 67362.30 · [kurz] ETH/CHF: Position offen, Signal bestätigt · [kurz] BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] XRP/CHF: Position gehört zum Horizont «mittel» · [kurz] SOL/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] TRX/CHF: Position gehört zum Horizont «mittel» · [kurz] ZEC/CHF: Position gehört zum Horizont «lang» · [kurz] HYPE/CHF: Position gehört zum Horizont «lang»

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| SOL short (kurz) | 28.10.2026 13:45 | 28.10.2026 20:49 | 84.18 | 85.00 | 🔴 -9.72 CHF | Stop-Loss (Gap) |
| BNB short (kurz) | 28.10.2026 17:48 | 28.10.2026 20:49 | 618.73 | 623.99 | 🔴 -0.28 CHF | Stop-Loss (Gap) |
| BTC short (kurz) | 28.10.2026 13:45 | 28.10.2026 20:49 | 66'924.92 | 67'429.70 | 🔴 -3.26 CHF | Stop-Loss (Gap) |
| ETH short | 28.10.2026 13:45 | 28.10.2026 19:48 | 1'938.49 | 1'950.58 | 🔴 -1.78 CHF | Stop-Loss (Gap) |
| ZEC short | 28.10.2026 13:15 | 28.10.2026 17:48 | 1'072.45 | 1'049.22 | 🟢 +3.40 CHF | Take-Profit |
| XRP short | 28.10.2026 07:10 | 28.10.2026 17:48 | 1.10 | 1.09 | 🟢 +1.62 CHF | Take-Profit |
| BNB long | 28.10.2026 13:45 | 28.10.2026 15:16 | 625.56 | 621.32 | 🔴 -0.69 CHF | Stop-Loss (Gap) |
| SOL long | 28.10.2026 13:15 | 28.10.2026 13:45 | 84.57 | 84.18 | 🔴 -1.81 CHF | Signal |
| BTC long | 28.10.2026 13:15 | 28.10.2026 13:45 | 67'033.50 | 66'924.92 | 🔴 -0.87 CHF | Signal |
| BNB long | 28.10.2026 12:13 | 28.10.2026 13:45 | 629.13 | 624.93 | 🔴 -2.15 CHF | Stop-Loss (Gap) |

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
