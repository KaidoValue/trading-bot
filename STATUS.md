# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **26.10.2026 19:50** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **989.92 CHF** | **950.35 CHF** | **523.98 CHF** |
| Gewinn / Verlust | 🔴 -10.08 CHF (-1.01 %) | 🔴 -49.65 CHF (-4.96 %) | 🔴 -476.02 CHF (-47.60 %) |
| Im Einsatz (investiert) | 404.97 CHF (41 %) | 241.31 CHF (25 %) | 1'574.10 CHF (300 %) |
| Cash (nicht investiert) | 584.96 CHF | 709.04 CHF | -508.66 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 12 | 103 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 6.49 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **973.61 CHF** |
| Gewinn / Verlust | 🔴 -26.39 CHF (-2.64 %) |
| **Aktuelle Verteilung** | Langfrist 48 % · KI 16 % · Risiko 1 % · Cash 35 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist -0.4 %, KI -3.5 %, Risiko -52.8 %, 🚨 Notbremse Risiko (-9.6 % in 3 Std.) |
| Umschicht-Gebühren bisher | 2.15 CHF |
| Erfahrung im Gedächtnis | 158 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.003 %/Lauf, KI -0.013 %/Lauf, Risiko -0.675 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'168.70 CHF | 🟢 +0.36 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'917.44 CHF | 🟢 +0.18 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 614.31 CHF | 🟢 +0.64 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.07 CHF | 🔴 -0.04 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.07 CHF | 🔴 -0.85 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.01 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'016.15 CHF | 🟢 +1.31 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 65.23 CHF | 🟢 +3.40 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'168.70 | 0.001485 | 100.05 CHF | 98.24 CHF | 🔴 -1.81 CHF (-1.81 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'917.44 | 0.040710 | 80.86 CHF | 78.06 CHF | 🔴 -2.80 CHF (-3.46 %) | 1'371.11 (-28 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 614.31 | 0.162070 | 100.02 CHF | 99.56 CHF | 🔴 -0.46 CHF (-0.46 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.07 | 58.690975 | 63.53 CHF | 62.84 CHF | 🔴 -0.69 CHF (-1.09 %) | 0.66 (-39 %) |
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
| **ZEC** long | 26.10.2026 10:10 | 1'006.92 | 1'016.15 | 0.237480 | 239.12 CHF | 241.31 CHF | 🟢 +2.19 CHF (+0.92 %) | 973.10 (-4 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🔴 raus / Cash |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🟢 investiert sein |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 20'486 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| ETH | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.014 %/Kerze), labor_3 (-0.020 %/Kerze) |
| BNB | Aufwärtstrend, wild | trend (+0.073 %/Kerze), momentum (+0.066 %/Kerze), reversal (+0.056 %/Kerze) |
| XRP | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| SOL | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| ZEC | Aufwärtstrend, wild | trend (+0.073 %/Kerze), momentum (+0.066 %/Kerze), reversal (+0.056 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.073 %/Kerze), momentum (+0.066 %/Kerze), reversal (+0.056 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: kein Einstieg (Pause nach Verlustserie) · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: kein Einstieg (Pause nach Verlustserie) · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: kein Einstieg (Pause nach Verlustserie) · TRX/CHF: Signal 'raus', bleibe in Cash · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: kein Einstieg (Pause nach Verlustserie)

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
| **ZEC** long | 26.10.2026 13:14 | 1'015.64 | 1'016.15 | 0.292014 | 296.58 CHF | 296.73 CHF | 🟢 +0.15 CHF (+0.05 %) | 998.92 (-2 %) |
| **ETH** short | 26.10.2026 16:17 | 1'924.05 | 1'917.44 | 0.141196 | 271.67 CHF | 270.73 CHF | 🟢 +0.93 CHF (+0.34 %) | 1'937.43 (+1 %) |
| **XRP** long | 26.10.2026 16:17 | 1.07 | 1.07 | 366.561314 | 393.67 CHF | 392.44 CHF | 🔴 -1.23 CHF (-0.31 %) | 1.06 (-1 %) |
| **BNB** long | 26.10.2026 16:46 | 616.17 | 614.31 | 0.418263 | 257.72 CHF | 256.94 CHF | 🔴 -0.78 CHF (-0.30 %) | 611.69 (-0 %) |
| **BTC** long | 26.10.2026 17:17 | 66'377.77 | 66'168.70 | 0.001530 | 101.58 CHF | 101.26 CHF | 🔴 -0.32 CHF (-0.31 %) | 65'931.82 (-0 %) |
| **SOL** long | 26.10.2026 19:49 | 83.15 | 83.07 | 3.081615 | 256.22 CHF | 255.99 CHF | 🔴 -0.23 CHF (-0.09 %) | 82.33 (-1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🔴 raus / Cash |
| BNB | 🟢 investiert sein |
| XRP | 🟢 investiert sein |
| SOL | 🟢 investiert sein |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: gekauft 3.081615 @ 83.15 · TRX/CHF: kein Einstieg (max. offene Positionen) · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| SOL long | 26.10.2026 18:17 | 26.10.2026 19:49 | 83.99 | 83.06 | 🔴 -4.47 CHF | Stop-Loss (Gap) |
| HYPE long | 26.10.2026 13:43 | 26.10.2026 18:17 | 64.01 | 65.20 | 🟢 +3.63 CHF | Take-Profit |
| TRX short | 26.10.2026 16:17 | 26.10.2026 16:46 | 0.27 | 0.27 | 🔴 -1.03 CHF | Signal |
| BTC short | 26.10.2026 16:17 | 26.10.2026 16:46 | 66'395.79 | 66'782.57 | 🔴 -2.37 CHF | Signal |
| SOL short | 26.10.2026 15:17 | 26.10.2026 16:17 | 83.73 | 84.38 | 🔴 -3.24 CHF | Signal |
| XRP short | 26.10.2026 15:17 | 26.10.2026 16:17 | 1.07 | 1.07 | 🔴 -3.17 CHF | Signal |
| ETH short | 26.10.2026 14:43 | 26.10.2026 16:17 | 1'904.86 | 1'925.97 | 🔴 -3.90 CHF | Stop-Loss (Gap) |
| BTC short | 26.10.2026 14:43 | 26.10.2026 16:17 | 65'767.10 | 66'462.21 | 🔴 -3.75 CHF | Stop-Loss (Gap) |
| XRP long | 26.10.2026 14:43 | 26.10.2026 15:17 | 1.06 | 1.07 | 🟢 +0.09 CHF | Signal |
| BNB long | 26.10.2026 14:43 | 26.10.2026 15:17 | 609.69 | 611.37 | 🔴 -0.70 CHF | Signal |

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
