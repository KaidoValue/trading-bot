# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **24.10.2026 16:15** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **988.58 CHF** | **969.98 CHF** | **914.85 CHF** |
| Gewinn / Verlust | 🔴 -11.42 CHF (-1.14 %) | 🔴 -30.02 CHF (-3.00 %) | 🔴 -85.15 CHF (-8.51 %) |
| Im Einsatz (investiert) | 403.63 CHF (41 %) | 249.85 CHF (26 %) | 1'555.59 CHF (170 %) |
| Cash (nicht investiert) | 584.96 CHF | 720.13 CHF | 2'470.45 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 3 | 17 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 2.57 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **982.85 CHF** |
| Gewinn / Verlust | 🔴 -17.15 CHF (-1.72 %) |
| **Aktuelle Verteilung** | Langfrist 46 % · KI 12 % · Risiko 1 % · Cash 41 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -0.9 %, KI -5.2 %, Risiko -7.0 %, 🚨 Notbremse Risiko (-3.4 % in 3 Std.) |
| Umschicht-Gebühren bisher | 1.30 CHF |
| Erfahrung im Gedächtnis | 42 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.020 %/Lauf, KI -0.062 %/Lauf, Risiko -0.151 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'398.60 CHF | 🔴 -0.87 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'952.00 CHF | 🔴 -0.86 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 600.82 CHF | 🔴 -1.46 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.05 CHF | 🔴 -1.31 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.20 CHF | 🔴 -1.86 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.02 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 945.12 CHF | 🔴 -3.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 62.30 CHF | 🔴 -2.02 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'398.60 | 0.001485 | 100.05 CHF | 98.58 CHF | 🔴 -1.47 CHF (-1.47 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'952.00 | 0.040710 | 80.86 CHF | 79.47 CHF | 🔴 -1.39 CHF (-1.72 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 600.82 | 0.162070 | 100.02 CHF | 97.37 CHF | 🔴 -2.65 CHF (-2.65 %) | 483.48 (-20 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.05 | 58.690975 | 63.53 CHF | 61.83 CHF | 🔴 -1.70 CHF (-2.67 %) | 0.66 (-38 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 83.20 | 0.797780 | 68.91 CHF | 66.38 CHF | 🔴 -2.53 CHF (-3.68 %) | 55.00 (-34 %) |

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
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 249.85 CHF | 🔴 -0.20 CHF (-0.08 %) | 0.27 (-0 %) |

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

**🧠 KI-Gedächtnis:** 20'070 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| BNB | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| XRP | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.012 %/Kerze) |
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
| **BTC** short | 24.10.2026 02:49 | 66'524.92 | 66'398.60 | 0.007261 | 483.03 CHF | 482.12 CHF | 🟢 +0.92 CHF (+0.19 %) | 66'938.10 (+1 %) |
| **XRP** short | 24.10.2026 08:22 | 1.06 | 1.05 | 9.420074 | 10.00 CHF | 9.92 CHF | 🟢 +0.08 CHF (+0.78 %) | 1.07 (+1 %) |
| **SOL** short | 24.10.2026 09:55 | 83.99 | 83.20 | 0.136771 | 11.49 CHF | 11.38 CHF | 🟢 +0.11 CHF (+0.94 %) | 84.56 (+2 %) |
| **BNB** short | 24.10.2026 10:25 | 605.36 | 600.82 | 0.692002 | 418.91 CHF | 415.77 CHF | 🟢 +3.15 CHF (+0.75 %) | 608.33 (+1 %) |
| **ETH** short | 24.10.2026 11:25 | 1'948.90 | 1'952.00 | 0.086569 | 168.71 CHF | 168.98 CHF | 🔴 -0.27 CHF (-0.16 %) | 1'955.77 (+0 %) |
| **TRX** short | 24.10.2026 16:14 | 0.27 | 0.27 | 1718.019456 | 467.20 CHF | 467.42 CHF | 🔴 -0.22 CHF (-0.05 %) | 0.27 (+0 %) |

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

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: short eröffnet 1718.019456 @ 0.27 · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| TRX long | 24.10.2026 13:44 | 24.10.2026 16:14 | 0.27 | 0.27 | 🔴 -7.79 CHF | Stop-Loss (Gap) |
| TRX short | 24.10.2026 01:19 | 24.10.2026 13:44 | 0.27 | 0.27 | 🔴 -12.93 CHF | Signal |
| ETH short | 24.10.2026 05:22 | 24.10.2026 11:25 | 1'967.27 | 1'951.52 | 🟢 +0.93 CHF | Take-Profit |
| BNB short | 23.10.2026 21:16 | 24.10.2026 10:25 | 612.08 | 606.81 | 🟢 +1.46 CHF | Take-Profit |
| ETH short | 24.10.2026 02:49 | 24.10.2026 05:22 | 1'955.06 | 1'969.23 | 🔴 -1.94 CHF | Stop-Loss (Gap) |
| SOL short | 23.10.2026 21:16 | 24.10.2026 02:49 | 85.65 | 84.41 | 🟢 +6.94 CHF | Take-Profit |
| XRP short | 23.10.2026 19:46 | 24.10.2026 02:49 | 1.08 | 1.06 | 🟢 +5.64 CHF | Take-Profit |
| ETH short | 24.10.2026 00:49 | 24.10.2026 01:49 | 1'955.05 | 1'968.60 | 🔴 -2.80 CHF | Stop-Loss (Gap) |
| BTC short | 24.10.2026 01:19 | 24.10.2026 01:49 | 66'436.76 | 66'919.24 | 🔴 -4.90 CHF | Stop-Loss (Gap) |
| TRX long | 23.10.2026 19:46 | 24.10.2026 01:19 | 0.27 | 0.27 | 🔴 -2.64 CHF | Signal |

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
