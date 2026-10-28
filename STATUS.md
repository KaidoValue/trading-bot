# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **28.10.2026 16:49** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **994.20 CHF** | **949.53 CHF** | **395.11 CHF** |
| Gewinn / Verlust | 🔴 -5.80 CHF (-0.58 %) | 🔴 -50.47 CHF (-5.05 %) | 🔴 -604.89 CHF (-60.49 %) |
| Im Einsatz (investiert) | 409.24 CHF (41 %) | 475.94 CHF (50 %) | 1'582.84 CHF (401 %) |
| Cash (nicht investiert) | 584.96 CHF | 473.59 CHF | 1'977.95 CHF |
| Offene Positionen | 5 | 2 | 5 |
| Abgeschlossene Trades | 0 | 18 | 168 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.27 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **971.46 CHF** |
| Gewinn / Verlust | 🔴 -28.54 CHF (-2.85 %) |
| **Aktuelle Verteilung** | Langfrist 51 % · KI 16 % · Risiko 1 % · Cash 32 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.2 %, KI -3.7 %, Risiko -84.1 % |
| Umschicht-Gebühren bisher | 2.59 CHF |
| Erfahrung im Gedächtnis | 257 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.004 %/Lauf, KI -0.004 %/Lauf, Risiko -0.401 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'820.00 CHF | 🔴 -0.05 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'935.12 CHF | 🔴 -0.31 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 621.48 CHF | 🟢 +0.68 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.09 CHF | 🔴 -1.51 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.66 CHF | 🔴 -0.43 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.13 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'057.53 CHF | 🔴 -2.60 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 66.15 CHF | 🔴 -1.84 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'820.00 | 0.001485 | 100.05 CHF | 99.21 CHF | 🔴 -0.84 CHF (-0.84 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'935.12 | 0.040710 | 80.86 CHF | 78.78 CHF | 🔴 -2.08 CHF (-2.57 %) | 1'371.11 (-29 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 621.48 | 0.162070 | 100.02 CHF | 100.72 CHF | 🟢 +0.70 CHF (+0.70 %) | 483.48 (-22 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.09 | 58.690975 | 63.53 CHF | 63.80 CHF | 🟢 +0.27 CHF (+0.42 %) | 0.66 (-40 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 83.66 | 0.797780 | 68.91 CHF | 66.74 CHF | 🔴 -2.17 CHF (-3.15 %) | 55.00 (-34 %) |

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
| **ETH** long | 28.10.2026 16:15 | 1'934.17 | 1'935.12 | 0.123031 | 237.96 CHF | 238.08 CHF | 🟢 +0.12 CHF (+0.05 %) | 1'916.06 (-1 %) |
| **BNB** long | 28.10.2026 16:15 | 621.75 | 621.48 | 0.382729 | 237.96 CHF | 237.86 CHF | 🔴 -0.10 CHF (-0.04 %) | 614.56 (-1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 20'846 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, ruhig | mean_reversion (+0.013 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |
| ETH | Seitwärts, ruhig | mean_reversion (+0.013 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |
| BNB | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.065 %/Kerze), reversal (+0.056 %/Kerze) |
| XRP | Aufwärtstrend, ruhig | trend (+0.059 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.028 %/Kerze) |
| SOL | Seitwärts, ruhig | mean_reversion (+0.013 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.059 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.028 %/Kerze) |
| HYPE | Aufwärtstrend, ruhig | trend (+0.059 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.028 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: Signal 'raus', bleibe in Cash · ETH/CHF: gekauft 0.123031 @ 1934.17 · BNB/CHF: gekauft 0.382729 @ 621.75 · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Signal 'raus', bleibe in Cash · ZEC/CHF: Signal 'raus', bleibe in Cash · HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long | 28.10.2026 13:15 | 28.10.2026 15:45 | 627.36 | 619.66 | 🔴 -4.18 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 15:45 | 1'946.78 | 1'929.91 | 🔴 -2.70 CHF | Stop-Loss (Gap) |
| BTC long | 27.10.2026 16:00 | 28.10.2026 14:15 | 66'509.84 | 66'883.94 | 🟢 +0.72 CHF | Signal |
| ETH long | 27.10.2026 16:00 | 28.10.2026 09:42 | 1'928.15 | 1'963.28 | 🟢 +3.74 CHF | Take-Profit |
| BNB long | 27.10.2026 18:00 | 28.10.2026 01:06 | 622.33 | 614.56 | 🔴 -4.25 CHF | Stop-Loss (Gap) |
| ZEC long | 26.10.2026 10:10 | 27.10.2026 17:30 | 1'006.92 | 1'072.51 | 🟢 +14.25 CHF | Take-Profit |
| BTC long | 26.10.2026 10:10 | 26.10.2026 15:16 | 66'289.23 | 66'013.88 | 🔴 -1.61 CHF | Signal |
| ETH long | 26.10.2026 13:13 | 26.10.2026 14:13 | 1'930.96 | 1'911.28 | 🔴 -3.05 CHF | Signal |
| TRX long | 23.10.2026 20:16 | 26.10.2026 11:13 | 0.27 | 0.27 | 🔴 -0.31 CHF | Signal |
| BTC long | 26.10.2026 00:04 | 26.10.2026 00:34 | 66'419.29 | 65'838.16 | 🔴 -2.72 CHF | Stop-Loss (Gap) |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **XRP** short | 28.10.2026 07:10 | 1.10 | 1.09 | 196.371129 | 215.89 CHF | 213.45 CHF | 🟢 +2.44 CHF (+1.13 %) | 1.11 (+2 %) |
| **ZEC** short | 28.10.2026 13:15 | 1'072.45 | 1'057.53 | 0.191373 | 205.24 CHF | 202.38 CHF | 🟢 +2.86 CHF (+1.39 %) | 1'085.13 (+3 %) |
| **BTC** short | 28.10.2026 13:45 | 66'924.92 | 66'820.00 | 0.004792 | 320.73 CHF | 320.23 CHF | 🟢 +0.50 CHF (+0.16 %) | 67'193.98 (+1 %) |
| **ETH** short | 28.10.2026 13:45 | 1'938.49 | 1'935.12 | 0.103957 | 201.52 CHF | 201.17 CHF | 🟢 +0.35 CHF (+0.17 %) | 1'945.98 (+1 %) |
| **SOL** short | 28.10.2026 13:45 | 84.18 | 83.66 | 7.717403 | 649.68 CHF | 645.61 CHF | 🟢 +4.07 CHF (+0.63 %) | 84.78 (+1 %) |

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

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long | 28.10.2026 13:45 | 28.10.2026 15:16 | 625.56 | 621.32 | 🔴 -0.69 CHF | Stop-Loss (Gap) |
| SOL long | 28.10.2026 13:15 | 28.10.2026 13:45 | 84.57 | 84.18 | 🔴 -1.81 CHF | Signal |
| BTC long | 28.10.2026 13:15 | 28.10.2026 13:45 | 67'033.50 | 66'924.92 | 🔴 -0.87 CHF | Signal |
| BNB long | 28.10.2026 12:13 | 28.10.2026 13:45 | 629.13 | 624.93 | 🔴 -2.15 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 13:45 | 1'946.78 | 1'938.49 | 🔴 -1.41 CHF | Stop-Loss (Gap) |
| TRX long | 28.10.2026 08:42 | 28.10.2026 13:15 | 0.27 | 0.27 | 🔴 -1.51 CHF | Signal |
| SOL long | 28.10.2026 09:42 | 28.10.2026 13:15 | 85.52 | 84.49 | 🔴 -3.45 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 12:13 | 28.10.2026 13:15 | 1'965.91 | 1'944.84 | 🔴 -2.80 CHF | Stop-Loss (Gap) |
| BTC long | 28.10.2026 12:45 | 28.10.2026 13:15 | 67'493.33 | 66'966.50 | 🔴 -2.15 CHF | Stop-Loss (Gap) |
| BTC long | 28.10.2026 09:42 | 28.10.2026 12:15 | 67'734.15 | 67'366.30 | 🔴 -1.71 CHF | Stop-Loss (Gap) |

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
