# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **25.10.2026 12:30** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **989.52 CHF** | **958.11 CHF** | **781.01 CHF** |
| Gewinn / Verlust | 🔴 -10.48 CHF (-1.05 %) | 🔴 -41.89 CHF (-4.19 %) | 🔴 -218.99 CHF (-21.90 %) |
| Im Einsatz (investiert) | 404.56 CHF (41 %) | 249.20 CHF (26 %) | 3'542.70 CHF (454 %) |
| Cash (nicht investiert) | 584.96 CHF | 708.91 CHF | -689.76 CHF |
| Offene Positionen | 5 | 1 | 2 |
| Abgeschlossene Trades | 0 | 8 | 52 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 4.41 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **979.04 CHF** |
| Gewinn / Verlust | 🔴 -20.96 CHF (-2.10 %) |
| **Aktuelle Verteilung** | Langfrist 48 % · KI 13 % · Risiko 1 % · Cash 38 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -0.4 %, KI -4.9 %, Risiko -29.1 % |
| Umschicht-Gebühren bisher | 1.80 CHF |
| Erfahrung im Gedächtnis | 89 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.008 %/Lauf, KI -0.043 %/Lauf, Risiko -0.246 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'319.50 CHF | 🔴 -0.53 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'919.09 CHF | 🔴 -1.43 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 611.42 CHF | 🟢 +0.22 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.07 CHF | 🔴 -0.47 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.11 CHF | 🔴 -1.52 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.02 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 984.93 CHF | 🔴 -1.07 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 62.62 CHF | 🔴 -0.97 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'319.50 | 0.001485 | 100.05 CHF | 98.46 CHF | 🔴 -1.59 CHF (-1.59 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'919.09 | 0.040710 | 80.86 CHF | 78.13 CHF | 🔴 -2.73 CHF (-3.38 %) | 1'371.11 (-29 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 611.42 | 0.162070 | 100.02 CHF | 99.09 CHF | 🔴 -0.93 CHF (-0.93 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.07 | 58.690975 | 63.53 CHF | 62.58 CHF | 🔴 -0.95 CHF (-1.50 %) | 0.66 (-38 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 83.11 | 0.797780 | 68.91 CHF | 66.31 CHF | 🔴 -2.60 CHF (-3.78 %) | 55.00 (-34 %) |

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
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 249.20 CHF | 🔴 -0.85 CHF (-0.34 %) | 0.27 (-0 %) |

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

**🧠 KI-Gedächtnis:** 20'238 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| BNB | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| XRP | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.003 %/Kerze) |
| ZEC | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: Signal 'raus', bleibe in Cash · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: Signal 'raus', bleibe in Cash · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: Signal 'raus', bleibe in Cash · HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
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
| **XRP** short | 25.10.2026 07:26 | 1.07 | 1.07 | 971.632217 | 1'042.91 CHF | 1'035.96 CHF | 🟢 +6.95 CHF (+0.67 %) | 1.08 (+1 %) |
| **TRX** long | 25.10.2026 09:56 | 0.27 | 0.27 | 9237.541771 | 2'509.10 CHF | 2'506.74 CHF | 🔴 -2.36 CHF (-0.09 %) | 0.27 (-0 %) |

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

**Letzte Entscheidung:** BTC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · ETH/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| SOL short | 25.10.2026 07:26 | 25.10.2026 10:26 | 83.96 | 83.09 | 🟢 +9.24 CHF | Take-Profit |
| BNB short | 25.10.2026 07:26 | 25.10.2026 10:26 | 613.51 | 608.51 | 🟢 +1.66 CHF | Take-Profit |
| ETH short | 25.10.2026 07:26 | 25.10.2026 10:26 | 1'936.84 | 1'927.83 | 🟢 +0.85 CHF | Take-Profit |
| BTC short | 25.10.2026 05:53 | 25.10.2026 10:26 | 66'618.57 | 66'366.98 | 🟢 +0.42 CHF | Take-Profit |
| TRX short | 24.10.2026 18:47 | 25.10.2026 09:56 | 0.27 | 0.27 | 🔴 -1.77 CHF | Signal |
| SOL long | 25.10.2026 02:20 | 25.10.2026 07:26 | 84.44 | 83.96 | 🔴 -4.51 CHF | Signal |
| XRP long | 25.10.2026 06:53 | 25.10.2026 07:26 | 1.07 | 1.07 | 🔴 -2.03 CHF | Signal |
| BNB long | 25.10.2026 03:53 | 25.10.2026 07:26 | 615.10 | 613.51 | 🔴 -0.13 CHF | Signal |
| ETH long | 25.10.2026 01:50 | 25.10.2026 07:26 | 1'949.16 | 1'936.84 | 🔴 -0.33 CHF | Stop-Loss (Gap) |
| XRP long | 25.10.2026 05:53 | 25.10.2026 06:53 | 1.08 | 1.07 | 🔴 -6.65 CHF | Stop-Loss (Gap) |

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
