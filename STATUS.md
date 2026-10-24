# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **24.10.2026 08:23** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **991.98 CHF** | **970.04 CHF** | **941.94 CHF** |
| Gewinn / Verlust | 🔴 -8.02 CHF (-0.80 %) | 🔴 -29.96 CHF (-3.00 %) | 🔴 -58.06 CHF (-5.81 %) |
| Im Einsatz (investiert) | 407.02 CHF (41 %) | 249.91 CHF (26 %) | 2'825.53 CHF (300 %) |
| Cash (nicht investiert) | 584.96 CHF | 720.13 CHF | 3'767.48 CHF |
| Offene Positionen | 5 | 1 | 5 |
| Abgeschlossene Trades | 0 | 3 | 13 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 1.69 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **984.68 CHF** |
| Gewinn / Verlust | 🔴 -15.32 CHF (-1.53 %) |
| **Aktuelle Verteilung** | Langfrist 46 % · KI 12 % · Risiko 1 % · Cash 41 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -0.9 %, KI -5.2 %, Risiko -7.0 %, 🚨 Notbremse Risiko (-3.4 % in 3 Std.) |
| Umschicht-Gebühren bisher | 1.30 CHF |
| Erfahrung im Gedächtnis | 25 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.020 %/Lauf, KI -0.104 %/Lauf, Risiko -0.137 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'609.50 CHF | 🔴 -0.55 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'960.90 CHF | 🔴 -0.41 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 608.94 CHF | 🔴 -0.16 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.06 CHF | 🔴 -0.53 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.32 CHF | 🔴 -0.57 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.03 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 965.00 CHF | 🔴 -1.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 63.54 CHF | 🔴 -0.10 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'609.50 | 0.001485 | 100.05 CHF | 98.89 CHF | 🔴 -1.16 CHF (-1.16 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'960.90 | 0.040710 | 80.86 CHF | 79.83 CHF | 🔴 -1.03 CHF (-1.27 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 608.94 | 0.162070 | 100.02 CHF | 98.69 CHF | 🔴 -1.33 CHF (-1.33 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.06 | 58.690975 | 63.53 CHF | 62.34 CHF | 🔴 -1.19 CHF (-1.87 %) | 0.66 (-38 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 84.32 | 0.797780 | 68.91 CHF | 67.27 CHF | 🔴 -1.64 CHF (-2.38 %) | 55.00 (-35 %) |

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
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 249.91 CHF | 🔴 -0.15 CHF (-0.06 %) | 0.27 (-0 %) |

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

**🧠 KI-Gedächtnis:** 20'006 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| BNB | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| XRP | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| ZEC | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |

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
| **BNB** short | 23.10.2026 21:16 | 612.08 | 608.94 | 0.690998 | 422.95 CHF | 420.78 CHF | 🟢 +2.17 CHF (+0.51 %) | 615.33 (+1 %) |
| **TRX** short | 24.10.2026 01:19 | 0.27 | 0.27 | 6397.535113 | 1'740.04 CHF | 1'740.97 CHF | 🔴 -0.93 CHF (-0.05 %) | 0.27 (+0 %) |
| **BTC** short | 24.10.2026 02:49 | 66'524.92 | 66'609.50 | 0.007261 | 483.03 CHF | 483.65 CHF | 🔴 -0.61 CHF (-0.13 %) | 66'938.10 (+0 %) |
| **ETH** short | 24.10.2026 05:22 | 1'967.27 | 1'960.90 | 0.086765 | 170.69 CHF | 170.14 CHF | 🟢 +0.55 CHF (+0.32 %) | 1'977.10 (+1 %) |
| **XRP** short | 24.10.2026 08:22 | 1.06 | 1.06 | 9.420074 | 10.00 CHF | 10.01 CHF | 🔴 -0.00 CHF (-0.05 %) | 1.07 (+1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash |

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: short eröffnet 9.420074 @ 1.06 · SOL/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ETH short | 24.10.2026 02:49 | 24.10.2026 05:22 | 1'955.06 | 1'969.23 | 🔴 -1.94 CHF | Stop-Loss (Gap) |
| SOL short | 23.10.2026 21:16 | 24.10.2026 02:49 | 85.65 | 84.41 | 🟢 +6.94 CHF | Take-Profit |
| XRP short | 23.10.2026 19:46 | 24.10.2026 02:49 | 1.08 | 1.06 | 🟢 +5.64 CHF | Take-Profit |
| ETH short | 24.10.2026 00:49 | 24.10.2026 01:49 | 1'955.05 | 1'968.60 | 🔴 -2.80 CHF | Stop-Loss (Gap) |
| BTC short | 24.10.2026 01:19 | 24.10.2026 01:49 | 66'436.76 | 66'919.24 | 🔴 -4.90 CHF | Stop-Loss (Gap) |
| TRX long | 23.10.2026 19:46 | 24.10.2026 01:19 | 0.27 | 0.27 | 🔴 -2.64 CHF | Signal |
| BTC short | 23.10.2026 19:46 | 24.10.2026 01:19 | 67'307.53 | 66'720.64 | 🟢 +3.13 CHF | Take-Profit |
| ETH short | 23.10.2026 21:46 | 24.10.2026 00:49 | 1'976.10 | 1'960.60 | 🟢 +7.20 CHF | Take-Profit |
| ETH long | 23.10.2026 21:16 | 23.10.2026 21:46 | 1'978.08 | 1'976.10 | 🔴 -1.77 CHF | Signal |
| SOL long | 23.10.2026 19:46 | 23.10.2026 21:16 | 86.26 | 85.65 | 🔴 -6.25 CHF | Signal |

## Charts

▲ grün = Kauf, ▼ rot = Verkauf, rote Linie = Stop-Loss, orange = 200-Tage-Linie. Die Bilder zeigen den Stand der letzten Aktualisierung; für den Live-Kurs auf «Live-Chart» klicken.

### BTC/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF)

![BTC/CHF](daten/charts/BTC-CHF.png)

### ETH/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF)

![ETH/CHF](daten/charts/ETH-CHF.png)

### BNB/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD)

![BNB/CHF](daten/charts/BNB-CHF.png)

### XRP/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD)

![XRP/CHF](daten/charts/XRP-CHF.png)

### SOL/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD)

![SOL/CHF](daten/charts/SOL-CHF.png)

### TRX/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD)

![TRX/CHF](daten/charts/TRX-CHF.png)

### ZEC/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD)

![ZEC/CHF](daten/charts/ZEC-CHF.png)

### HYPE/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD)

![HYPE/CHF](daten/charts/HYPE-CHF.png)

## Nachrichtenlage

- **Stimmung (Fear & Greed):** 51 von 100, neutral
- **Bewertung News:** +0.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** keine
