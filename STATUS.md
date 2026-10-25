# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **25.10.2026 22:05** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **990.36 CHF** | **958.80 CHF** | **717.79 CHF** |
| Gewinn / Verlust | 🔴 -9.64 CHF (-0.96 %) | 🔴 -41.20 CHF (-4.12 %) | 🔴 -282.21 CHF (-28.22 %) |
| Im Einsatz (investiert) | 405.40 CHF (41 %) | 249.88 CHF (26 %) | 1'605.74 CHF (224 %) |
| Cash (nicht investiert) | 584.96 CHF | 708.91 CHF | -768.89 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 8 | 59 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 5.05 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **978.71 CHF** |
| Gewinn / Verlust | 🔴 -21.29 CHF (-2.13 %) |
| **Aktuelle Verteilung** | Langfrist 48 % · KI 13 % · Risiko 1 % · Cash 38 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -0.4 %, KI -4.9 %, Risiko -29.1 % |
| Umschicht-Gebühren bisher | 1.80 CHF |
| Erfahrung im Gedächtnis | 110 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.006 %/Lauf, KI -0.034 %/Lauf, Risiko -0.275 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'258.20 CHF | 🔴 -0.62 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'931.88 CHF | 🔴 -0.77 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 609.65 CHF | 🟢 +0.08 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.07 CHF | 🟢 +0.05 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.69 CHF | 🔴 -0.68 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🟢 +0.39 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 998.41 CHF | 🟢 +0.43 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 63.49 CHF | 🟢 +0.56 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'258.20 | 0.001485 | 100.05 CHF | 98.37 CHF | 🔴 -1.68 CHF (-1.68 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'931.88 | 0.040710 | 80.86 CHF | 78.65 CHF | 🔴 -2.21 CHF (-2.73 %) | 1'371.11 (-29 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 609.65 | 0.162070 | 100.02 CHF | 98.81 CHF | 🔴 -1.21 CHF (-1.21 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.07 | 58.690975 | 63.53 CHF | 62.81 CHF | 🔴 -0.72 CHF (-1.13 %) | 0.66 (-39 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 83.69 | 0.797780 | 68.91 CHF | 66.77 CHF | 🔴 -2.14 CHF (-3.10 %) | 55.00 (-34 %) |

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
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 249.88 CHF | 🔴 -0.17 CHF (-0.07 %) | 0.27 (-0 %) |

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

**🧠 KI-Gedächtnis:** 20'318 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.009 %/Kerze), labor_4 (-0.011 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.009 %/Kerze), labor_4 (-0.011 %/Kerze) |
| BNB | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.003 %/Kerze), labor_4 (+0.003 %/Kerze) |
| XRP | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.003 %/Kerze), labor_4 (+0.003 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.007 %/Kerze), pullback (-0.009 %/Kerze), labor_4 (-0.011 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.003 %/Kerze), labor_4 (+0.003 %/Kerze) |
| ZEC | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.003 %/Kerze), labor_4 (+0.003 %/Kerze) |
| HYPE | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.003 %/Kerze), labor_4 (+0.003 %/Kerze) |

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
| **ZEC** long | 25.10.2026 14:29 | 988.96 | 998.41 | 0.380861 | 376.66 CHF | 380.26 CHF | 🟢 +3.60 CHF (+0.96 %) | 974.30 (-2 %) |
| **BNB** short | 25.10.2026 18:02 | 612.08 | 609.65 | 0.097646 | 59.77 CHF | 59.53 CHF | 🟢 +0.24 CHF (+0.40 %) | 615.41 (+1 %) |
| **XRP** long | 25.10.2026 18:02 | 1.08 | 1.07 | 45.829325 | 49.36 CHF | 49.04 CHF | 🔴 -0.32 CHF (-0.65 %) | 1.07 (-0 %) |
| **SOL** long | 25.10.2026 18:02 | 84.01 | 83.69 | 4.537892 | 381.24 CHF | 379.80 CHF | 🔴 -1.44 CHF (-0.38 %) | 83.38 (-0 %) |
| **ETH** long | 25.10.2026 22:04 | 1'932.67 | 1'931.88 | 0.190845 | 368.84 CHF | 368.69 CHF | 🔴 -0.15 CHF (-0.04 %) | 1'927.11 (-0 %) |
| **TRX** long | 25.10.2026 22:04 | 0.27 | 0.27 | 1353.949666 | 368.84 CHF | 368.42 CHF | 🔴 -0.42 CHF (-0.11 %) | 0.27 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🟢 investiert sein |
| BNB | 🔴 raus / Cash |
| XRP | 🟢 investiert sein |
| SOL | 🟢 investiert sein |
| TRX | 🟢 investiert sein |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: kein Einstieg (Tagesverlust-Limit) · ETH/CHF: gekauft 0.190845 @ 1932.67 · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: gekauft 1353.949666 @ 0.27 · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BTC long | 25.10.2026 21:04 | 25.10.2026 22:04 | 66'426.00 | 66'261.85 | 🔴 -1.88 CHF | Signal |
| ETH long | 25.10.2026 18:02 | 25.10.2026 22:04 | 1'942.75 | 1'930.73 | 🔴 -3.34 CHF | Stop-Loss (Gap) |
| TRX long | 25.10.2026 18:31 | 25.10.2026 20:34 | 0.27 | 0.27 | 🔴 -1.37 CHF | Take-Profit |
| BTC short | 25.10.2026 18:02 | 25.10.2026 18:31 | 66'457.25 | 66'661.71 | 🔴 -2.17 CHF | Signal |
| XRP short | 25.10.2026 07:26 | 25.10.2026 18:02 | 1.07 | 1.08 | 🔴 -9.08 CHF | Signal |
| TRX short | 25.10.2026 14:29 | 25.10.2026 18:02 | 0.27 | 0.27 | 🔴 -7.84 CHF | Stop-Loss (Gap) |
| TRX long | 25.10.2026 09:56 | 25.10.2026 14:29 | 0.27 | 0.27 | 🔴 -16.76 CHF | Signal |
| SOL short | 25.10.2026 07:26 | 25.10.2026 10:26 | 83.96 | 83.09 | 🟢 +9.24 CHF | Take-Profit |
| BNB short | 25.10.2026 07:26 | 25.10.2026 10:26 | 613.51 | 608.51 | 🟢 +1.66 CHF | Take-Profit |
| ETH short | 25.10.2026 07:26 | 25.10.2026 10:26 | 1'936.84 | 1'927.83 | 🟢 +0.85 CHF | Take-Profit |

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
