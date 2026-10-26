# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **26.10.2026 21:50** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **988.67 CHF** | **948.34 CHF** | **516.26 CHF** |
| Gewinn / Verlust | 🔴 -11.33 CHF (-1.13 %) | 🔴 -51.66 CHF (-5.17 %) | 🔴 -483.74 CHF (-48.37 %) |
| Im Einsatz (investiert) | 403.72 CHF (41 %) | 239.31 CHF (25 %) | 1'550.18 CHF (300 %) |
| Cash (nicht investiert) | 584.96 CHF | 709.04 CHF | 184.56 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 12 | 105 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 6.55 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **972.54 CHF** |
| Gewinn / Verlust | 🔴 -27.46 CHF (-2.75 %) |
| **Aktuelle Verteilung** | Langfrist 48 % · KI 16 % · Risiko 1 % · Cash 35 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist -0.4 %, KI -3.5 %, Risiko -52.8 %, 🚨 Notbremse Risiko (-9.6 % in 3 Std.) |
| Umschicht-Gebühren bisher | 2.15 CHF |
| Erfahrung im Gedächtnis | 162 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.000 %/Lauf, KI -0.016 %/Lauf, Risiko -0.649 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 65'973.10 CHF | 🟢 +0.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'914.02 CHF | 🟢 +0.00 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 612.19 CHF | 🟢 +0.29 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.07 CHF | 🔴 -0.50 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 82.84 CHF | 🔴 -1.13 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.07 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'007.69 CHF | 🟢 +0.47 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 64.24 CHF | 🟢 +1.82 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 65'973.10 | 0.001485 | 100.05 CHF | 97.95 CHF | 🔴 -2.10 CHF (-2.10 %) | 53'251.84 (-19 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'914.02 | 0.040710 | 80.86 CHF | 77.92 CHF | 🔴 -2.94 CHF (-3.63 %) | 1'371.11 (-28 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 612.19 | 0.162070 | 100.02 CHF | 99.22 CHF | 🔴 -0.80 CHF (-0.80 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.07 | 58.690975 | 63.53 CHF | 62.54 CHF | 🔴 -0.98 CHF (-1.55 %) | 0.66 (-38 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 82.84 | 0.797780 | 68.91 CHF | 66.09 CHF | 🔴 -2.82 CHF (-4.10 %) | 55.00 (-34 %) |

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
| **ZEC** long | 26.10.2026 10:10 | 1'006.92 | 1'007.69 | 0.237480 | 239.12 CHF | 239.31 CHF | 🟢 +0.18 CHF (+0.08 %) | 973.10 (-3 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 20'502 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| ETH | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| BNB | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| XRP | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| SOL | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| ZEC | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.065 %/Kerze), reversal (+0.055 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.065 %/Kerze), reversal (+0.055 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: kein Einstieg (Pause nach Verlustserie) · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: Signal 'raus', bleibe in Cash · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Signal 'raus', bleibe in Cash · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: kein Einstieg (Pause nach Verlustserie)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BTC long | 26.10.2026 10:10 | 26.10.2026 15:16 | 66'289.23 | 66'013.88 | 🔴 -1.61 CHF | Signal |
| ETH long | 26.10.2026 13:13 | 26.10.2026 14:13 | 1'930.96 | 1'911.28 | 🔴 -3.05 CHF | Signal |
| TRX long | 23.10.2026 20:16 | 26.10.2026 11:13 | 0.27 | 0.27 | 🔴 -0.31 CHF | Signal |
| BTC long | 26.10.2026 00:04 | 26.10.2026 00:34 | 66'419.29 | 65'838.16 | 🔴 -2.72 CHF | Stop-Loss (Gap) |
| ZEC long | 25.10.2026 06:23 | 25.10.2026 07:26 | 1'003.77 | 993.72 | 🔴 -3.67 CHF | Signal |
| BNB long | 25.10.2026 06:23 | 25.10.2026 07:26 | 616.82 | 613.83 | 🔴 -2.42 CHF | Signal |
| BTC long | 25.10.2026 05:23 | 25.10.2026 06:23 | 66'685.23 | 66'692.94 | 🔴 -0.60 CHF | Signal |
| BNB long | 24.10.2026 22:17 | 25.10.2026 05:53 | 604.10 | 615.07 | 🟢 +3.12 CHF | Take-Profit |
| ZEC long | 25.10.2026 03:23 | 25.10.2026 04:23 | 1'006.55 | 1'003.58 | 🔴 -1.98 CHF | Signal |
| XRP long | 23.10.2026 23:16 | 24.10.2026 01:19 | 1.08 | 1.06 | 🔴 -5.15 CHF | Stop-Loss (Gap) |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **ZEC** long | 26.10.2026 13:14 | 1'015.64 | 1'007.69 | 0.292014 | 296.58 CHF | 294.26 CHF | 🔴 -2.32 CHF (-0.78 %) | 998.92 (-1 %) |
| **ETH** short | 26.10.2026 16:17 | 1'924.05 | 1'914.02 | 0.141196 | 271.67 CHF | 270.25 CHF | 🟢 +1.42 CHF (+0.52 %) | 1'937.43 (+1 %) |
| **XRP** long | 26.10.2026 16:17 | 1.07 | 1.07 | 366.561314 | 393.67 CHF | 390.62 CHF | 🔴 -3.05 CHF (-0.77 %) | 1.06 (-0 %) |
| **BNB** long | 26.10.2026 16:46 | 616.17 | 612.19 | 0.418263 | 257.72 CHF | 256.05 CHF | 🔴 -1.67 CHF (-0.65 %) | 611.69 (-0 %) |
| **TRX** short | 26.10.2026 20:19 | 0.27 | 0.27 | 976.393340 | 266.57 CHF | 266.47 CHF | 🟢 +0.10 CHF (+0.04 %) | 0.27 (+0 %) |
| **SOL** short | 26.10.2026 21:19 | 82.87 | 82.84 | 0.875427 | 72.54 CHF | 72.52 CHF | 🟢 +0.02 CHF (+0.03 %) | 83.66 (+1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash |
| BNB | 🟢 investiert sein |
| XRP | 🟢 investiert sein |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash |

**Letzte Entscheidung:** BTC/CHF: kein Einstieg (max. offene Positionen) · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BTC long | 26.10.2026 17:17 | 26.10.2026 21:19 | 66'377.77 | 65'976.80 | 🔴 -0.88 CHF | Signal |
| SOL long | 26.10.2026 19:49 | 26.10.2026 20:19 | 83.15 | 83.25 | 🔴 -1.00 CHF | Signal |
| SOL long | 26.10.2026 18:17 | 26.10.2026 19:49 | 83.99 | 83.06 | 🔴 -4.47 CHF | Stop-Loss (Gap) |
| HYPE long | 26.10.2026 13:43 | 26.10.2026 18:17 | 64.01 | 65.20 | 🟢 +3.63 CHF | Take-Profit |
| TRX short | 26.10.2026 16:17 | 26.10.2026 16:46 | 0.27 | 0.27 | 🔴 -1.03 CHF | Signal |
| BTC short | 26.10.2026 16:17 | 26.10.2026 16:46 | 66'395.79 | 66'782.57 | 🔴 -2.37 CHF | Signal |
| SOL short | 26.10.2026 15:17 | 26.10.2026 16:17 | 83.73 | 84.38 | 🔴 -3.24 CHF | Signal |
| XRP short | 26.10.2026 15:17 | 26.10.2026 16:17 | 1.07 | 1.07 | 🔴 -3.17 CHF | Signal |
| ETH short | 26.10.2026 14:43 | 26.10.2026 16:17 | 1'904.86 | 1'925.97 | 🔴 -3.90 CHF | Stop-Loss (Gap) |
| BTC short | 26.10.2026 14:43 | 26.10.2026 16:17 | 65'767.10 | 66'462.21 | 🔴 -3.75 CHF | Stop-Loss (Gap) |

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
