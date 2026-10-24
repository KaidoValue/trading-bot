# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **24.10.2026 02:50** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **991.48 CHF** | **970.18 CHF** | **944.79 CHF** |
| Gewinn / Verlust | 🔴 -8.52 CHF (-0.85 %) | 🔴 -29.82 CHF (-2.98 %) | 🔴 -55.21 CHF (-5.52 %) |
| Im Einsatz (investiert) | 406.52 CHF (41 %) | 250.04 CHF (26 %) | 2'841.90 CHF (301 %) |
| Cash (nicht investiert) | 584.96 CHF | 720.13 CHF | 3'786.69 CHF |
| Offene Positionen | 5 | 1 | 4 |
| Abgeschlossene Trades | 0 | 3 | 12 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.91 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **984.67 CHF** |
| Gewinn / Verlust | 🔴 -15.33 CHF (-1.53 %) |
| **Aktuelle Verteilung** | Langfrist 47 % · KI 12 % · Risiko 3 % · Cash 38 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -0.6 %, KI -5.3 %, Risiko -6.6 % |
| Umschicht-Gebühren bisher | 1.20 CHF |
| Erfahrung im Gedächtnis | 13 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.042 %/Lauf, KI -0.200 %/Lauf, Risiko -0.241 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'583.90 CHF | 🔴 -0.59 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'958.22 CHF | 🔴 -0.55 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 607.09 CHF | 🔴 -0.53 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.06 CHF | 🔴 -0.69 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.33 CHF | 🔴 -0.62 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.04 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 964.42 CHF | 🔴 -1.18 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 63.15 CHF | 🔴 -0.78 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'583.90 | 0.001485 | 100.05 CHF | 98.86 CHF | 🔴 -1.19 CHF (-1.19 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'958.22 | 0.040710 | 80.86 CHF | 79.72 CHF | 🔴 -1.14 CHF (-1.41 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 607.09 | 0.162070 | 100.02 CHF | 98.39 CHF | 🔴 -1.63 CHF (-1.63 %) | 483.48 (-20 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.06 | 58.690975 | 63.53 CHF | 62.28 CHF | 🔴 -1.25 CHF (-1.96 %) | 0.66 (-38 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 84.33 | 0.797780 | 68.91 CHF | 67.28 CHF | 🔴 -1.63 CHF (-2.37 %) | 55.00 (-35 %) |

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
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 250.04 CHF | 🔴 -0.01 CHF (-0.00 %) | 0.27 (-0 %) |

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

**🧠 KI-Gedächtnis:** 19'958 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| ETH | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| BNB | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| XRP | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| SOL | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| ZEC | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |
| HYPE | Abwärtstrend, wild | pullback (-0.011 %/Kerze), labor_4 (-0.015 %/Kerze), labor_3 (-0.020 %/Kerze) |

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
| **BNB** short | 23.10.2026 21:16 | 612.08 | 607.09 | 0.690998 | 422.95 CHF | 419.50 CHF | 🟢 +3.45 CHF (+0.82 %) | 615.33 (+1 %) |
| **TRX** short | 24.10.2026 01:19 | 0.27 | 0.27 | 6397.535113 | 1'740.04 CHF | 1'741.94 CHF | 🔴 -1.90 CHF (-0.11 %) | 0.27 (+0 %) |
| **BTC** short | 24.10.2026 02:49 | 66'524.92 | 66'583.90 | 0.007261 | 483.03 CHF | 483.46 CHF | 🔴 -0.43 CHF (-0.09 %) | 66'938.10 (+1 %) |
| **ETH** short | 24.10.2026 02:49 | 1'955.06 | 1'958.22 | 0.100603 | 196.68 CHF | 197.00 CHF | 🔴 -0.32 CHF (-0.16 %) | 1'967.36 (+0 %) |

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

**Letzte Entscheidung:** BTC/CHF: short eröffnet 0.007261 @ 66524.92 · ETH/CHF: short eröffnet 0.100603 @ 1955.06 · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · SOL/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| SOL short | 23.10.2026 21:16 | 24.10.2026 02:49 | 85.65 | 84.41 | 🟢 +6.94 CHF | Take-Profit |
| XRP short | 23.10.2026 19:46 | 24.10.2026 02:49 | 1.08 | 1.06 | 🟢 +5.64 CHF | Take-Profit |
| ETH short | 24.10.2026 00:49 | 24.10.2026 01:49 | 1'955.05 | 1'968.60 | 🔴 -2.80 CHF | Stop-Loss (Gap) |
| BTC short | 24.10.2026 01:19 | 24.10.2026 01:49 | 66'436.76 | 66'919.24 | 🔴 -4.90 CHF | Stop-Loss (Gap) |
| TRX long | 23.10.2026 19:46 | 24.10.2026 01:19 | 0.27 | 0.27 | 🔴 -2.64 CHF | Signal |
| BTC short | 23.10.2026 19:46 | 24.10.2026 01:19 | 67'307.53 | 66'720.64 | 🟢 +3.13 CHF | Take-Profit |
| ETH short | 23.10.2026 21:46 | 24.10.2026 00:49 | 1'976.10 | 1'960.60 | 🟢 +7.20 CHF | Take-Profit |
| ETH long | 23.10.2026 21:16 | 23.10.2026 21:46 | 1'978.08 | 1'976.10 | 🔴 -1.77 CHF | Signal |
| SOL long | 23.10.2026 19:46 | 23.10.2026 21:16 | 86.26 | 85.65 | 🔴 -6.25 CHF | Signal |
| ZEC long | 23.10.2026 20:17 | 23.10.2026 21:16 | 1'035.29 | 1'013.39 | 🔴 -12.19 CHF | Stop-Loss (Gap) |

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
