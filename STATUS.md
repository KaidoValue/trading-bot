# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **28.10.2026 20:21** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt aber auch mittelfristig (4h) und kurzfristig (1h), long und short. Max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, long und short.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: handelt kurz (30 Min.), mittel (4h) und lang (Tageskerzen), long und short, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **995.96 CHF** | **949.13 CHF** | **381.09 CHF** |
| Gewinn / Verlust | 🔴 -4.04 CHF (-0.40 %) | 🔴 -50.87 CHF (-5.09 %) | 🔴 -618.91 CHF (-61.89 %) |
| Im Einsatz (investiert) | 536.40 CHF (54 %) | 1'048.66 CHF (110 %) | 1'703.49 CHF (447 %) |
| Cash (nicht investiert) | 708.79 CHF | 1'041.29 CHF | 1'068.01 CHF |
| Offene Positionen | 7 | 6 | 8 |
| Abgeschlossene Trades | 0 | 18 | 171 |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: trend 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | kurz: breakout 30m · mittel: breakout 4h · lang: breakout 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 40 % · mittel 30 % · lang 30 % | kurz 40 % · mittel 30 % · lang 30 % |
| Short erlaubt | ja | ja | ja |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.47 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **971.24 CHF** |
| Gewinn / Verlust | 🔴 -28.76 CHF (-2.88 %) |
| **Aktuelle Verteilung** | Langfrist 32 % · KI 21 % · Risiko 3 % · Cash 44 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.5 %, KI -2.9 %, Risiko -76.0 %, 🚨 Notbremse Risiko (-3.7 % in 3 Std.) |
| Umschicht-Gebühren bisher | 3.27 CHF |
| Erfahrung im Gedächtnis | 264 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.005 %/Lauf, KI -0.004 %/Lauf, Risiko -0.406 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'128.50 CHF | 🟢 +0.41 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'952.03 CHF | 🟢 +0.56 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 622.09 CHF | 🟢 +1.02 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.10 CHF | 🔴 -0.29 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.48 CHF | 🟢 +0.79 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.45 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'067.30 CHF | 🔴 -1.46 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 66.93 CHF | 🔴 -0.44 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt aber auch mittelfristig (4h) und kurzfristig (1h), long und short. Max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 23.10.2026 18:09 | 67'388.78 | 67'128.50 | 0.001485 | 100.05 CHF | 99.66 CHF | 🔴 -0.39 CHF (-0.39 %) | 53'251.84 (-21 %) |
| **ETH** long (lang) | 23.10.2026 18:09 | 1'986.19 | 1'952.03 | 0.040710 | 80.86 CHF | 79.47 CHF | 🔴 -1.39 CHF (-1.72 %) | 1'371.11 (-30 %) |
| **BNB** long (lang) | 23.10.2026 19:15 | 617.14 | 622.09 | 0.162070 | 100.02 CHF | 100.82 CHF | 🟢 +0.80 CHF (+0.80 %) | 483.48 (-22 %) |
| **XRP** long (lang) | 23.10.2026 19:15 | 1.08 | 1.10 | 58.690975 | 63.53 CHF | 64.43 CHF | 🟢 +0.90 CHF (+1.42 %) | 0.66 (-40 %) |
| **SOL** long (lang) | 23.10.2026 19:15 | 86.38 | 84.48 | 0.797780 | 68.91 CHF | 67.40 CHF | 🔴 -1.51 CHF (-2.19 %) | 55.00 (-35 %) |
| **TRX** short (kurz) | 28.10.2026 20:17 | 0.27 | 0.27 | 365.077967 | 99.60 CHF | 99.67 CHF | 🔴 -0.07 CHF (-0.07 %) | 0.27 (+0 %) |
| **ZEC** short (kurz) | 28.10.2026 20:17 | 1'064.43 | 1'067.30 | 0.023373 | 24.88 CHF | 24.95 CHF | 🔴 -0.07 CHF (-0.27 %) | 1'092.74 (+2 %) |

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

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: Position offen, Signal bestätigt · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [lang] ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [lang] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Position gehört zum Horizont «lang» · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [mittel] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.0) · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: kein Signal · [kurz] BNB/CHF: Position gehört zum Horizont «lang» · [kurz] XRP/CHF: Position gehört zum Horizont «lang» · [kurz] SOL/CHF: Position gehört zum Horizont «lang» · [kurz] TRX/CHF: short eröffnet 365.077967 @ 0.27 · [kurz] ZEC/CHF: short eröffnet 0.023373 @ 1064.43 · [kurz] HYPE/CHF: kein Signal

## 2️⃣ KI-Bot (lernend, kurz bis lang)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, long und short._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **ETH** long (kurz) | 28.10.2026 16:15 | 1'934.17 | 1'952.03 | 0.123031 | 237.96 CHF | 240.16 CHF | 🟢 +2.20 CHF (+0.92 %) | 1'916.06 (-2 %) |
| **BNB** long (kurz) | 28.10.2026 16:15 | 621.75 | 622.09 | 0.382729 | 237.96 CHF | 238.09 CHF | 🟢 +0.13 CHF (+0.06 %) | 614.56 (-1 %) |
| **BTC** short (mittel) | 28.10.2026 20:19 | 67'094.94 | 67'128.50 | 0.003544 | 237.81 CHF | 237.93 CHF | 🔴 -0.12 CHF (-0.05 %) | 68'876.82 (+3 %) |
| **XRP** short (mittel) | 28.10.2026 20:19 | 1.10 | 1.10 | 43.275678 | 47.46 CHF | 47.51 CHF | 🔴 -0.05 CHF (-0.10 %) | 1.14 (+4 %) |
| **TRX** short (lang) | 28.10.2026 20:19 | 0.27 | 0.27 | 870.667829 | 237.55 CHF | 237.70 CHF | 🔴 -0.14 CHF (-0.06 %) | 0.29 (+5 %) |
| **HYPE** short (lang) | 28.10.2026 20:19 | 66.85 | 66.93 | 0.706372 | 47.22 CHF | 47.28 CHF | 🔴 -0.05 CHF (-0.11 %) | 80.08 (+20 %) |

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
| **BTC** short (kurz) | 28.10.2026 13:45 | 66'924.92 | 67'128.50 | 0.004792 | 320.73 CHF | 321.70 CHF | 🔴 -0.98 CHF (-0.30 %) | 67'193.98 (+0 %) |
| **SOL** short (kurz) | 28.10.2026 13:45 | 84.18 | 84.48 | 7.717403 | 649.68 CHF | 652.00 CHF | 🔴 -2.32 CHF (-0.36 %) | 84.78 (+0 %) |
| **BNB** short (kurz) | 28.10.2026 17:48 | 618.73 | 622.09 | 0.033407 | 20.67 CHF | 20.78 CHF | 🔴 -0.11 CHF (-0.54 %) | 622.30 (+0 %) |
| **ETH** long (kurz) | 28.10.2026 19:48 | 1'950.58 | 1'952.03 | 0.083780 | 163.42 CHF | 163.54 CHF | 🟢 +0.12 CHF (+0.07 %) | 1'941.70 (-1 %) |
| **XRP** long (mittel) | 28.10.2026 20:19 | 1.10 | 1.10 | 178.546264 | 196.03 CHF | 196.00 CHF | 🔴 -0.02 CHF (-0.01 %) | 1.07 (-3 %) |
| **TRX** long (mittel) | 28.10.2026 20:19 | 0.27 | 0.27 | 544.830158 | 148.80 CHF | 148.74 CHF | 🔴 -0.05 CHF (-0.04 %) | 0.27 (-1 %) |
| **ZEC** short (lang) | 28.10.2026 20:19 | 1'066.19 | 1'067.30 | 0.067046 | 71.48 CHF | 71.56 CHF | 🔴 -0.07 CHF (-0.10 %) | 1'351.76 (+27 %) |
| **HYPE** short (lang) | 28.10.2026 20:19 | 66.92 | 66.93 | 1.929710 | 129.14 CHF | 129.15 CHF | 🔴 -0.02 CHF (-0.01 %) | 76.85 (+15 %) |

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

**Letzte Entscheidung:** [kurz] BTC/CHF: Position offen, Signal bestätigt · [kurz] ETH/CHF: Position offen, Signal bestätigt · [kurz] BNB/CHF: Position offen, Signal bestätigt · [kurz] XRP/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] SOL/CHF: Position offen, Signal bestätigt · [kurz] TRX/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [kurz] HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [mittel] BTC/CHF: Position gehört zum Horizont «kurz» · [mittel] ETH/CHF: Position gehört zum Horizont «kurz» · [mittel] BNB/CHF: Position gehört zum Horizont «kurz» · [mittel] XRP/CHF: gekauft 178.546264 @ 1.10 · [mittel] SOL/CHF: Position gehört zum Horizont «kurz» · [mittel] TRX/CHF: gekauft 544.830158 @ 0.27 · [mittel] ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [mittel] HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] BTC/CHF: Position gehört zum Horizont «kurz» · [lang] ETH/CHF: Position gehört zum Horizont «kurz» · [lang] BNB/CHF: Position gehört zum Horizont «kurz» · [lang] XRP/CHF: Position gehört zum Horizont «mittel» · [lang] SOL/CHF: Position gehört zum Horizont «kurz» · [lang] TRX/CHF: Position gehört zum Horizont «mittel» · [lang] ZEC/CHF: short eröffnet 0.067046 @ 1066.19 · [lang] HYPE/CHF: short eröffnet 1.929710 @ 66.92

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ETH short | 28.10.2026 13:45 | 28.10.2026 19:48 | 1'938.49 | 1'950.58 | 🔴 -1.78 CHF | Stop-Loss (Gap) |
| ZEC short | 28.10.2026 13:15 | 28.10.2026 17:48 | 1'072.45 | 1'049.22 | 🟢 +3.40 CHF | Take-Profit |
| XRP short | 28.10.2026 07:10 | 28.10.2026 17:48 | 1.10 | 1.09 | 🟢 +1.62 CHF | Take-Profit |
| BNB long | 28.10.2026 13:45 | 28.10.2026 15:16 | 625.56 | 621.32 | 🔴 -0.69 CHF | Stop-Loss (Gap) |
| SOL long | 28.10.2026 13:15 | 28.10.2026 13:45 | 84.57 | 84.18 | 🔴 -1.81 CHF | Signal |
| BTC long | 28.10.2026 13:15 | 28.10.2026 13:45 | 67'033.50 | 66'924.92 | 🔴 -0.87 CHF | Signal |
| BNB long | 28.10.2026 12:13 | 28.10.2026 13:45 | 629.13 | 624.93 | 🔴 -2.15 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 13:45 | 1'946.78 | 1'938.49 | 🔴 -1.41 CHF | Stop-Loss (Gap) |
| TRX long | 28.10.2026 08:42 | 28.10.2026 13:15 | 0.27 | 0.27 | 🔴 -1.51 CHF | Signal |
| SOL long | 28.10.2026 09:42 | 28.10.2026 13:15 | 85.52 | 84.49 | 🔴 -3.45 CHF | Stop-Loss (Gap) |

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
