# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **24.10.2026 17:15** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **983.65 CHF** | **969.38 CHF** | **904.36 CHF** |
| Gewinn / Verlust | 🔴 -16.35 CHF (-1.63 %) | 🔴 -30.62 CHF (-3.06 %) | 🔴 -95.64 CHF (-9.56 %) |
| Im Einsatz (investiert) | 398.70 CHF (41 %) | 249.25 CHF (26 %) | 2'745.55 CHF (304 %) |
| Cash (nicht investiert) | 584.96 CHF | 720.13 CHF | 3'649.91 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 3 | 23 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 2.61 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **980.21 CHF** |
| Gewinn / Verlust | 🔴 -19.79 CHF (-1.98 %) |
| **Aktuelle Verteilung** | Langfrist 38 % · KI 13 % · Risiko 1 % · Cash 49 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -2.5 %, KI -4.9 %, Risiko -13.7 % |
| Umschicht-Gebühren bisher | 1.52 CHF |
| Erfahrung im Gedächtnis | 44 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.030 %/Lauf, KI -0.061 %/Lauf, Risiko -0.170 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 65'791.30 CHF | 🔴 -1.77 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'908.00 CHF | 🔴 -3.10 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 595.57 CHF | 🔴 -2.36 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.04 CHF | 🔴 -2.24 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 82.16 CHF | 🔴 -3.12 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.30 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 933.61 CHF | 🔴 -4.28 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 61.77 CHF | 🔴 -2.89 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 65'791.30 | 0.001485 | 100.05 CHF | 97.68 CHF | 🔴 -2.37 CHF (-2.37 %) | 53'251.84 (-19 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'908.00 | 0.040710 | 80.86 CHF | 77.68 CHF | 🔴 -3.18 CHF (-3.94 %) | 1'371.11 (-28 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 595.57 | 0.162070 | 100.02 CHF | 96.52 CHF | 🔴 -3.50 CHF (-3.50 %) | 483.48 (-19 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.04 | 58.690975 | 63.53 CHF | 61.28 CHF | 🔴 -2.25 CHF (-3.55 %) | 0.66 (-37 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 82.16 | 0.797780 | 68.91 CHF | 65.55 CHF | 🔴 -3.36 CHF (-4.88 %) | 55.00 (-33 %) |

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
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 249.25 CHF | 🔴 -0.80 CHF (-0.32 %) | 0.27 (-0 %) |

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

**🧠 KI-Gedächtnis:** 20'078 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.013 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.013 %/Kerze) |
| BNB | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.013 %/Kerze) |
| XRP | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.013 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.013 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| ZEC | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.013 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.013 %/Kerze) |

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
| **BNB** short | 24.10.2026 16:44 | 599.83 | 595.57 | 0.778677 | 467.07 CHF | 463.75 CHF | 🟢 +3.32 CHF (+0.71 %) | 602.66 (+1 %) |
| **BTC** short | 24.10.2026 17:14 | 65'758.40 | 65'791.30 | 0.007099 | 466.79 CHF | 467.02 CHF | 🔴 -0.23 CHF (-0.05 %) | 66'048.50 (+0 %) |
| **ETH** short | 24.10.2026 17:14 | 1'907.05 | 1'908.00 | 0.244769 | 466.79 CHF | 467.02 CHF | 🔴 -0.23 CHF (-0.05 %) | 1'915.92 (+0 %) |
| **XRP** short | 24.10.2026 17:14 | 1.04 | 1.04 | 447.612519 | 466.79 CHF | 467.32 CHF | 🔴 -0.54 CHF (-0.11 %) | 1.05 (+1 %) |
| **SOL** short | 24.10.2026 17:14 | 82.05 | 82.16 | 5.688816 | 466.79 CHF | 467.40 CHF | 🔴 -0.61 CHF (-0.13 %) | 82.70 (+1 %) |
| **TRX** short | 24.10.2026 17:14 | 0.27 | 0.27 | 1521.785732 | 412.75 CHF | 413.04 CHF | 🔴 -0.29 CHF (-0.07 %) | 0.27 (+0 %) |

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

**Letzte Entscheidung:** BTC/CHF: short eröffnet 0.007099 @ 65758.40 · ETH/CHF: short eröffnet 0.244769 @ 1907.05 · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: short eröffnet 447.612519 @ 1.04 · SOL/CHF: short eröffnet 5.688816 @ 82.05 · TRX/CHF: short eröffnet 1521.785732 @ 0.27 · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| TRX short | 24.10.2026 16:14 | 24.10.2026 17:14 | 0.27 | 0.27 | 🔴 -1.71 CHF | Take-Profit |
| SOL short | 24.10.2026 09:55 | 24.10.2026 17:14 | 83.99 | 83.03 | 🟢 +0.07 CHF | Take-Profit |
| XRP short | 24.10.2026 08:22 | 24.10.2026 17:14 | 1.06 | 1.05 | 🟢 +0.07 CHF | Take-Profit |
| ETH short | 24.10.2026 11:25 | 24.10.2026 17:14 | 1'948.90 | 1'939.05 | 🟢 +0.42 CHF | Take-Profit |
| BTC short | 24.10.2026 02:49 | 24.10.2026 17:14 | 66'524.92 | 65'831.29 | 🟢 +3.79 CHF | Take-Profit |
| BNB short | 24.10.2026 10:25 | 24.10.2026 16:44 | 605.36 | 600.64 | 🟢 +1.11 CHF | Take-Profit |
| TRX long | 24.10.2026 13:44 | 24.10.2026 16:14 | 0.27 | 0.27 | 🔴 -7.79 CHF | Stop-Loss (Gap) |
| TRX short | 24.10.2026 01:19 | 24.10.2026 13:44 | 0.27 | 0.27 | 🔴 -12.93 CHF | Signal |
| ETH short | 24.10.2026 05:22 | 24.10.2026 11:25 | 1'967.27 | 1'951.52 | 🟢 +0.93 CHF | Take-Profit |
| BNB short | 23.10.2026 21:16 | 24.10.2026 10:25 | 612.08 | 606.81 | 🟢 +1.46 CHF | Take-Profit |

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
