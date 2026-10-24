# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **24.10.2026 21:48** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **988.85 CHF** | **969.71 CHF** | **821.49 CHF** |
| Gewinn / Verlust | 🔴 -11.15 CHF (-1.11 %) | 🔴 -30.29 CHF (-3.03 %) | 🔴 -178.51 CHF (-17.85 %) |
| Im Einsatz (investiert) | 403.90 CHF (41 %) | 249.57 CHF (26 %) | 3'545.46 CHF (432 %) |
| Cash (nicht investiert) | 584.96 CHF | 720.13 CHF | 1'410.06 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 3 | 34 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 3.08 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **981.13 CHF** |
| Gewinn / Verlust | 🔴 -18.87 CHF (-1.89 %) |
| **Aktuelle Verteilung** | Langfrist 43 % · KI 13 % · Risiko 1 % · Cash 43 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -1.5 %, KI -4.7 %, Risiko -29.5 %, 🚨 Notbremse Risiko (-7.2 % in 3 Std.) |
| Umschicht-Gebühren bisher | 1.66 CHF |
| Erfahrung im Gedächtnis | 54 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.015 %/Lauf, KI -0.049 %/Lauf, Risiko -0.314 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'430.60 CHF | 🔴 -0.82 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'931.25 CHF | 🔴 -1.92 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 602.76 CHF | 🔴 -1.29 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.06 CHF | 🔴 -0.52 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.40 CHF | 🔴 -1.77 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.28 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 976.94 CHF | 🟢 +0.04 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 62.78 CHF | 🔴 -1.41 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'430.60 | 0.001485 | 100.05 CHF | 98.63 CHF | 🔴 -1.42 CHF (-1.42 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'931.25 | 0.040710 | 80.86 CHF | 78.62 CHF | 🔴 -2.24 CHF (-2.77 %) | 1'371.11 (-29 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 602.76 | 0.162070 | 100.02 CHF | 97.69 CHF | 🔴 -2.33 CHF (-2.33 %) | 483.48 (-20 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.06 | 58.690975 | 63.53 CHF | 62.42 CHF | 🔴 -1.11 CHF (-1.74 %) | 0.66 (-38 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 83.40 | 0.797780 | 68.91 CHF | 66.54 CHF | 🔴 -2.37 CHF (-3.44 %) | 55.00 (-34 %) |

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
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 249.57 CHF | 🔴 -0.48 CHF (-0.19 %) | 0.27 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🟢 investiert sein |
| ZEC | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 20'110 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.019 %/Kerze) |
| ETH | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.019 %/Kerze) |
| BNB | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.019 %/Kerze) |
| XRP | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.019 %/Kerze) |
| SOL | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.019 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| ZEC | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: Signal 'raus', bleibe in Cash · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: Signal 'raus', bleibe in Cash · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: Signal 'raus', bleibe in Cash · HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| XRP long | 23.10.2026 23:16 | 24.10.2026 01:19 | 1.08 | 1.06 | 🔴 -5.15 CHF | Stop-Loss (Gap) |
| ZEC long | 23.10.2026 18:10 | 24.10.2026 00:49 | 1'020.51 | 960.79 | 🔴 -15.86 CHF | Stop-Loss (Gap) |
| BNB long | 23.10.2026 18:10 | 23.10.2026 21:16 | 617.52 | 611.79 | 🔴 -3.61 CHF | Signal |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **TRX** short | 24.10.2026 18:47 | 0.27 | 0.27 | 1263.453311 | 343.19 CHF | 343.37 CHF | 🔴 -0.18 CHF (-0.05 %) | 0.27 (+0 %) |
| **BTC** short | 24.10.2026 19:17 | 66'151.31 | 66'430.60 | 0.006661 | 440.63 CHF | 442.50 CHF | 🔴 -1.86 CHF (-0.42 %) | 66'553.33 (+0 %) |
| **SOL** short | 24.10.2026 19:17 | 82.87 | 83.40 | 5.317297 | 440.63 CHF | 443.48 CHF | 🔴 -2.85 CHF (-0.65 %) | 83.76 (+0 %) |
| **ETH** short | 24.10.2026 21:17 | 1'929.78 | 1'931.25 | 0.220328 | 425.19 CHF | 425.51 CHF | 🔴 -0.32 CHF (-0.08 %) | 1'942.68 (+1 %) |
| **BNB** short | 24.10.2026 21:17 | 602.33 | 602.76 | 0.683769 | 411.85 CHF | 412.15 CHF | 🔴 -0.30 CHF (-0.07 %) | 605.91 (+1 %) |
| **XRP** long | 24.10.2026 21:17 | 1.06 | 1.06 | 1390.100880 | 1'477.16 CHF | 1'478.45 CHF | 🟢 +1.28 CHF (+0.09 %) | 1.05 (-1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash |
| XRP | 🟢 investiert sein |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| XRP short | 24.10.2026 19:17 | 24.10.2026 21:17 | 1.05 | 1.06 | 🔴 -6.91 CHF | Signal |
| BNB short | 24.10.2026 19:17 | 24.10.2026 21:17 | 597.23 | 602.93 | 🔴 -6.52 CHF | Stop-Loss (Gap) |
| ETH short | 24.10.2026 19:17 | 24.10.2026 21:17 | 1'914.38 | 1'931.72 | 🔴 -5.15 CHF | Stop-Loss (Gap) |
| SOL short | 24.10.2026 17:14 | 24.10.2026 19:17 | 82.05 | 82.95 | 🔴 -7.56 CHF | Stop-Loss (Gap) |
| XRP short | 24.10.2026 17:14 | 24.10.2026 19:17 | 1.04 | 1.05 | 🔴 -6.87 CHF | Stop-Loss (Gap) |
| BNB short | 24.10.2026 17:44 | 24.10.2026 19:17 | 592.95 | 597.83 | 🔴 -6.11 CHF | Stop-Loss (Gap) |
| ETH short | 24.10.2026 17:44 | 24.10.2026 19:17 | 1'890.95 | 1'916.30 | 🔴 -7.44 CHF | Stop-Loss (Gap) |
| BTC short | 24.10.2026 17:14 | 24.10.2026 19:17 | 65'758.40 | 66'217.49 | 🔴 -4.48 CHF | Stop-Loss (Gap) |
| TRX short | 24.10.2026 17:14 | 24.10.2026 18:17 | 0.27 | 0.27 | 🔴 -3.54 CHF | Stop-Loss (Gap) |
| BNB short | 24.10.2026 16:44 | 24.10.2026 17:44 | 599.83 | 595.37 | 🟢 +1.06 CHF | Take-Profit |

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
- **Bewertung News:** +0.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** keine
