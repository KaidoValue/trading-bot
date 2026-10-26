# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **26.10.2026 07:41** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **987.80 CHF** | **955.25 CHF** | **668.46 CHF** |
| Gewinn / Verlust | 🔴 -12.20 CHF (-1.22 %) | 🔴 -44.75 CHF (-4.47 %) | 🔴 -331.54 CHF (-33.15 %) |
| Im Einsatz (investiert) | 402.85 CHF (41 %) | 249.68 CHF (26 %) | 2'934.77 CHF (439 %) |
| Cash (nicht investiert) | 584.96 CHF | 705.57 CHF | 929.25 CHF |
| Offene Positionen | 5 | 1 | 3 |
| Abgeschlossene Trades | 0 | 9 | 76 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 5.98 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **976.07 CHF** |
| Gewinn / Verlust | 🔴 -23.93 CHF (-2.39 %) |
| **Aktuelle Verteilung** | Langfrist 43 % · KI 15 % · Risiko 1 % · Cash 41 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist -1.4 %, KI -4.1 %, Risiko -28.2 % |
| Umschicht-Gebühren bisher | 1.98 CHF |
| Erfahrung im Gedächtnis | 131 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** KI -0.002 %/Lauf, Langfrist -0.006 %/Lauf, Risiko -0.314 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 65'886.20 CHF | 🔴 -0.07 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'916.43 CHF | 🟢 +0.13 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 608.39 CHF | 🟢 +0.04 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.06 CHF | 🔴 -0.77 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.07 CHF | 🔴 -0.48 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.07 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 992.55 CHF | 🔴 -0.67 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 63.02 CHF | 🟢 +0.28 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 65'886.20 | 0.001485 | 100.05 CHF | 97.82 CHF | 🔴 -2.23 CHF (-2.23 %) | 53'251.84 (-19 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'916.43 | 0.040710 | 80.86 CHF | 78.02 CHF | 🔴 -2.84 CHF (-3.51 %) | 1'371.11 (-28 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 608.39 | 0.162070 | 100.02 CHF | 98.60 CHF | 🔴 -1.42 CHF (-1.42 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.06 | 58.690975 | 63.53 CHF | 62.14 CHF | 🔴 -1.39 CHF (-2.19 %) | 0.66 (-38 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 83.07 | 0.797780 | 68.91 CHF | 66.27 CHF | 🔴 -2.64 CHF (-3.83 %) | 55.00 (-34 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🟢 investiert sein |
| SOL | 🟢 investiert sein |
| TRX | 🟢 investiert sein |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: kein Einstieg (max. offene Positionen) · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

## 2️⃣ KI-Bot (lernend, Daytrading)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 249.68 CHF | 🔴 -0.37 CHF (-0.15 %) | 0.27 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🟢 investiert sein |
| ZEC | ⚪ neutral |
| HYPE | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 20'390 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.014 %/Kerze), labor_3 (-0.019 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.009 %/Kerze), labor_4 (-0.011 %/Kerze) |
| BNB | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| XRP | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| SOL | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.014 %/Kerze), labor_3 (-0.019 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |
| ZEC | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |
| HYPE | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: Signal 'raus', bleibe in Cash · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: Signal 'raus', bleibe in Cash · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Signal · HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BTC long | 26.10.2026 00:04 | 26.10.2026 00:34 | 66'419.29 | 65'838.16 | 🔴 -2.72 CHF | Stop-Loss (Gap) |
| ZEC long | 25.10.2026 06:23 | 25.10.2026 07:26 | 1'003.77 | 993.72 | 🔴 -3.67 CHF | Signal |
| BNB long | 25.10.2026 06:23 | 25.10.2026 07:26 | 616.82 | 613.83 | 🔴 -2.42 CHF | Signal |
| BTC long | 25.10.2026 05:23 | 25.10.2026 06:23 | 66'685.23 | 66'692.94 | 🔴 -0.60 CHF | Signal |
| BNB long | 24.10.2026 22:17 | 25.10.2026 05:53 | 604.10 | 615.07 | 🟢 +3.12 CHF | Take-Profit |
| ZEC long | 25.10.2026 03:23 | 25.10.2026 04:23 | 1'006.55 | 1'003.58 | 🔴 -1.98 CHF | Signal |
| XRP long | 23.10.2026 23:16 | 24.10.2026 01:19 | 1.08 | 1.06 | 🔴 -5.15 CHF | Stop-Loss (Gap) |
| ZEC long | 23.10.2026 18:10 | 24.10.2026 00:49 | 1'020.51 | 960.79 | 🔴 -15.86 CHF | Stop-Loss (Gap) |
| BNB long | 23.10.2026 18:10 | 23.10.2026 21:16 | 617.52 | 611.79 | 🔴 -3.61 CHF | Signal |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **TRX** short | 26.10.2026 01:04 | 0.27 | 0.27 | 4588.862524 | 1'248.12 CHF | 1'247.66 CHF | 🟢 +0.45 CHF (+0.04 %) | 0.27 (+0 %) |
| **BTC** short | 26.10.2026 05:37 | 65'901.53 | 65'886.20 | 0.005314 | 350.20 CHF | 350.12 CHF | 🟢 +0.08 CHF (+0.02 %) | 66'240.07 (+1 %) |
| **BNB** long | 26.10.2026 06:40 | 611.29 | 608.39 | 2.197581 | 1'343.37 CHF | 1'336.99 CHF | 🔴 -6.38 CHF (-0.47 %) | 607.17 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · SOL/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ETH short | 26.10.2026 05:37 | 26.10.2026 07:40 | 1'906.97 | 1'917.39 | 🔴 -2.83 CHF | Signal |
| BNB short | 26.10.2026 05:37 | 26.10.2026 06:40 | 610.51 | 611.29 | 🔴 -0.73 CHF | Signal |
| BNB short | 26.10.2026 03:37 | 26.10.2026 05:37 | 605.39 | 611.12 | 🔴 -4.25 CHF | Stop-Loss (Gap) |
| ETH short | 26.10.2026 04:07 | 26.10.2026 05:37 | 1'893.39 | 1'908.87 | 🔴 -2.10 CHF | Stop-Loss (Gap) |
| BTC short | 26.10.2026 03:37 | 26.10.2026 05:37 | 65'401.68 | 65'967.47 | 🔴 -4.04 CHF | Stop-Loss (Gap) |
| ETH short | 26.10.2026 00:34 | 26.10.2026 04:07 | 1'910.62 | 1'896.25 | 🟢 +1.05 CHF | Take-Profit |
| HYPE short | 25.10.2026 22:34 | 26.10.2026 03:37 | 63.22 | 62.45 | 🟢 +2.60 CHF | Take-Profit |
| XRP short | 25.10.2026 23:04 | 26.10.2026 03:37 | 1.07 | 1.06 | 🟢 +4.12 CHF | Take-Profit |
| BNB short | 25.10.2026 18:02 | 26.10.2026 03:37 | 612.08 | 606.64 | 🟢 +0.22 CHF | Take-Profit |
| BTC short | 26.10.2026 00:34 | 26.10.2026 03:37 | 65'976.70 | 65'580.33 | 🟢 +1.23 CHF | Take-Profit |

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

- **Stimmung (Fear & Greed):** 50 von 100, neutral
- **Bewertung News:** +0.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** keine
