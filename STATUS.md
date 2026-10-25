# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **25.10.2026 04:24** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **993.99 CHF** | **968.89 CHF** | **826.28 CHF** |
| Gewinn / Verlust | 🔴 -6.01 CHF (-0.60 %) | 🔴 -31.11 CHF (-3.11 %) | 🔴 -173.72 CHF (-17.37 %) |
| Im Einsatz (investiert) | 409.03 CHF (41 %) | 495.85 CHF (51 %) | 2'507.55 CHF (303 %) |
| Cash (nicht investiert) | 584.96 CHF | 473.04 CHF | -995.76 CHF |
| Offene Positionen | 5 | 2 | 6 |
| Abgeschlossene Trades | 0 | 4 | 40 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 3.50 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **983.26 CHF** |
| Gewinn / Verlust | 🔴 -16.74 CHF (-1.67 %) |
| **Aktuelle Verteilung** | Langfrist 43 % · KI 13 % · Risiko 1 % · Cash 43 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -1.5 %, KI -4.7 %, Risiko -29.5 %, 🚨 Notbremse Risiko (-7.2 % in 3 Std.) |
| Umschicht-Gebühren bisher | 1.66 CHF |
| Erfahrung im Gedächtnis | 71 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.004 %/Lauf, KI -0.038 %/Lauf, Risiko -0.231 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'823.60 CHF | 🟢 +0.22 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'950.71 CHF | 🟢 +0.19 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 614.39 CHF | 🟢 +0.70 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.08 CHF | 🟢 +0.79 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.56 CHF | 🟢 +0.19 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'001.76 CHF | 🟢 +0.61 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 63.17 CHF | 🔴 -0.10 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'823.60 | 0.001485 | 100.05 CHF | 99.21 CHF | 🔴 -0.84 CHF (-0.84 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'950.71 | 0.040710 | 80.86 CHF | 79.41 CHF | 🔴 -1.44 CHF (-1.79 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 614.39 | 0.162070 | 100.02 CHF | 99.57 CHF | 🔴 -0.45 CHF (-0.45 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.08 | 58.690975 | 63.53 CHF | 63.37 CHF | 🔴 -0.15 CHF (-0.24 %) | 0.66 (-39 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 84.56 | 0.797780 | 68.91 CHF | 67.46 CHF | 🔴 -1.45 CHF (-2.11 %) | 55.00 (-35 %) |

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
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 249.13 CHF | 🔴 -0.93 CHF (-0.37 %) | 0.27 (-0 %) |
| **BNB** long | 24.10.2026 22:17 | 604.10 | 614.39 | 0.401571 | 242.59 CHF | 246.72 CHF | 🟢 +4.13 CHF (+1.70 %) | 598.01 (-3 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🔴 raus / Cash |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🟢 investiert sein |
| ZEC | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 20'174 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| ETH | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.014 %/Kerze), labor_3 (-0.019 %/Kerze) |
| BNB | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_2 (+0.006 %/Kerze), labor_1 (+0.006 %/Kerze) |
| XRP | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| ZEC | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: kein Einstieg (max. offene Positionen) · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: Signal 'raus', bleibe in Cash · HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ZEC long | 25.10.2026 03:23 | 25.10.2026 04:23 | 1'006.55 | 1'003.58 | 🔴 -1.98 CHF | Signal |
| XRP long | 23.10.2026 23:16 | 24.10.2026 01:19 | 1.08 | 1.06 | 🔴 -5.15 CHF | Stop-Loss (Gap) |
| ZEC long | 23.10.2026 18:10 | 24.10.2026 00:49 | 1'020.51 | 960.79 | 🔴 -15.86 CHF | Stop-Loss (Gap) |
| BNB long | 23.10.2026 18:10 | 23.10.2026 21:16 | 617.52 | 611.79 | 🔴 -3.61 CHF | Signal |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **TRX** short | 24.10.2026 18:47 | 0.27 | 0.27 | 1263.453311 | 343.19 CHF | 342.75 CHF | 🟢 +0.44 CHF (+0.13 %) | 0.27 (+0 %) |
| **XRP** long | 24.10.2026 21:17 | 1.06 | 1.08 | 1390.100880 | 1'477.16 CHF | 1'501.02 CHF | 🟢 +23.86 CHF (+1.61 %) | 1.05 (-3 %) |
| **ETH** long | 25.10.2026 01:50 | 1'949.16 | 1'950.71 | 0.019104 | 37.24 CHF | 37.27 CHF | 🟢 +0.03 CHF (+0.08 %) | 1'939.17 (-1 %) |
| **SOL** long | 25.10.2026 02:20 | 84.44 | 84.56 | 4.892555 | 413.14 CHF | 413.70 CHF | 🟢 +0.56 CHF (+0.14 %) | 83.80 (-1 %) |
| **BTC** long | 25.10.2026 02:50 | 66'786.18 | 66'823.60 | 0.002926 | 195.42 CHF | 195.53 CHF | 🟢 +0.11 CHF (+0.06 %) | 66'524.75 (-0 %) |
| **BNB** long | 25.10.2026 03:53 | 615.10 | 614.39 | 0.028121 | 17.30 CHF | 17.28 CHF | 🔴 -0.02 CHF (-0.11 %) | 612.00 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🟢 investiert sein |
| SOL | 🟢 investiert sein |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash |

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long | 24.10.2026 22:47 | 25.10.2026 02:50 | 605.22 | 610.55 | 🟢 +0.67 CHF | Take-Profit |
| BTC short | 25.10.2026 01:50 | 25.10.2026 02:20 | 66'658.95 | 66'721.64 | 🔴 -1.48 CHF | Signal |
| BTC short | 24.10.2026 19:17 | 25.10.2026 01:50 | 66'151.31 | 66'725.65 | 🔴 -4.98 CHF | Stop-Loss (Gap) |
| ETH short | 24.10.2026 21:17 | 24.10.2026 22:47 | 1'929.78 | 1'935.27 | 🔴 -2.32 CHF | Signal |
| BNB short | 24.10.2026 21:17 | 24.10.2026 22:17 | 602.33 | 604.14 | 🔴 -3.39 CHF | Signal |
| SOL short | 24.10.2026 19:17 | 24.10.2026 22:17 | 82.87 | 83.86 | 🔴 -7.58 CHF | Stop-Loss (Gap) |
| XRP short | 24.10.2026 19:17 | 24.10.2026 21:17 | 1.05 | 1.06 | 🔴 -6.91 CHF | Signal |
| BNB short | 24.10.2026 19:17 | 24.10.2026 21:17 | 597.23 | 602.93 | 🔴 -6.52 CHF | Stop-Loss (Gap) |
| ETH short | 24.10.2026 19:17 | 24.10.2026 21:17 | 1'914.38 | 1'931.72 | 🔴 -5.15 CHF | Stop-Loss (Gap) |
| SOL short | 24.10.2026 17:14 | 24.10.2026 19:17 | 82.05 | 82.95 | 🔴 -7.56 CHF | Stop-Loss (Gap) |

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

- **Stimmung (Fear & Greed):** 54 von 100, neutral
- **Bewertung News:** +0.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** keine
