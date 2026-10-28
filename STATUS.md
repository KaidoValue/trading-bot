# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **28.10.2026 13:46** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **995.79 CHF** | **957.50 CHF** | **388.43 CHF** |
| Gewinn / Verlust | 🔴 -4.21 CHF (-0.42 %) | 🔴 -42.50 CHF (-4.25 %) | 🔴 -611.57 CHF (-61.16 %) |
| Im Einsatz (investiert) | 410.84 CHF (41 %) | 721.30 CHF (75 %) | 1'648.49 CHF (424 %) |
| Cash (nicht investiert) | 584.96 CHF | 236.20 CHF | 1'920.82 CHF |
| Offene Positionen | 5 | 3 | 6 |
| Abgeschlossene Trades | 0 | 15 | 167 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.02 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **974.04 CHF** |
| Gewinn / Verlust | 🔴 -25.96 CHF (-2.60 %) |
| **Aktuelle Verteilung** | Langfrist 53 % · KI 21 % · Risiko 1 % · Cash 25 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.6 %, KI -1.5 %, Risiko -77.5 % |
| Umschicht-Gebühren bisher | 2.40 CHF |
| Erfahrung im Gedächtnis | 250 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.005 %/Lauf, KI +0.002 %/Lauf, Risiko -0.435 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'958.40 CHF | 🟢 +0.16 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'939.46 CHF | 🔴 -0.09 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 625.41 CHF | 🟢 +1.36 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.09 CHF | 🔴 -1.25 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.21 CHF | 🟢 +0.27 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🟢 +0.03 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'066.77 CHF | 🔴 -1.70 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 66.81 CHF | 🔴 -0.81 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'958.40 | 0.001485 | 100.05 CHF | 99.41 CHF | 🔴 -0.64 CHF (-0.64 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'939.46 | 0.040710 | 80.86 CHF | 78.96 CHF | 🔴 -1.90 CHF (-2.35 %) | 1'371.11 (-29 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 625.41 | 0.162070 | 100.02 CHF | 101.36 CHF | 🟢 +1.34 CHF (+1.34 %) | 483.48 (-23 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.09 | 58.690975 | 63.53 CHF | 63.93 CHF | 🟢 +0.40 CHF (+0.63 %) | 0.66 (-40 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 84.21 | 0.797780 | 68.91 CHF | 67.18 CHF | 🔴 -1.73 CHF (-2.51 %) | 55.00 (-35 %) |

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
| **BTC** long | 27.10.2026 16:00 | 66'509.84 | 66'958.40 | 0.003616 | 240.50 CHF | 242.12 CHF | 🟢 +1.62 CHF (+0.67 %) | 65'856.81 (-2 %) |
| **ETH** long | 28.10.2026 13:15 | 1'946.78 | 1'939.46 | 0.123494 | 240.42 CHF | 239.51 CHF | 🔴 -0.90 CHF (-0.38 %) | 1'932.48 (-0 %) |
| **BNB** long | 28.10.2026 13:15 | 627.36 | 625.41 | 0.383218 | 240.42 CHF | 239.67 CHF | 🔴 -0.75 CHF (-0.31 %) | 621.00 (-1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | ⚪ neutral |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | ⚪ neutral |
| SOL | ⚪ neutral |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 20'822 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.029 %/Kerze) |
| ETH | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.029 %/Kerze) |
| BNB | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.029 %/Kerze) |
| XRP | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.029 %/Kerze) |
| SOL | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.029 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.029 %/Kerze) |
| HYPE | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.029 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: kein Signal · ETH/CHF: gekauft 0.123494 @ 1946.78 · BNB/CHF: gekauft 0.383218 @ 627.36 · XRP/CHF: kein Signal · SOL/CHF: kein Signal · TRX/CHF: Signal 'raus', bleibe in Cash · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ETH long | 27.10.2026 16:00 | 28.10.2026 09:42 | 1'928.15 | 1'963.28 | 🟢 +3.74 CHF | Take-Profit |
| BNB long | 27.10.2026 18:00 | 28.10.2026 01:06 | 622.33 | 614.56 | 🔴 -4.25 CHF | Stop-Loss (Gap) |
| ZEC long | 26.10.2026 10:10 | 27.10.2026 17:30 | 1'006.92 | 1'072.51 | 🟢 +14.25 CHF | Take-Profit |
| BTC long | 26.10.2026 10:10 | 26.10.2026 15:16 | 66'289.23 | 66'013.88 | 🔴 -1.61 CHF | Signal |
| ETH long | 26.10.2026 13:13 | 26.10.2026 14:13 | 1'930.96 | 1'911.28 | 🔴 -3.05 CHF | Signal |
| TRX long | 23.10.2026 20:16 | 26.10.2026 11:13 | 0.27 | 0.27 | 🔴 -0.31 CHF | Signal |
| BTC long | 26.10.2026 00:04 | 26.10.2026 00:34 | 66'419.29 | 65'838.16 | 🔴 -2.72 CHF | Stop-Loss (Gap) |
| ZEC long | 25.10.2026 06:23 | 25.10.2026 07:26 | 1'003.77 | 993.72 | 🔴 -3.67 CHF | Signal |
| BNB long | 25.10.2026 06:23 | 25.10.2026 07:26 | 616.82 | 613.83 | 🔴 -2.42 CHF | Signal |
| BTC long | 25.10.2026 05:23 | 25.10.2026 06:23 | 66'685.23 | 66'692.94 | 🔴 -0.60 CHF | Signal |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **XRP** short | 28.10.2026 07:10 | 1.10 | 1.09 | 196.371129 | 215.89 CHF | 213.90 CHF | 🟢 +1.98 CHF (+0.92 %) | 1.11 (+2 %) |
| **ZEC** short | 28.10.2026 13:15 | 1'072.45 | 1'066.77 | 0.191373 | 205.24 CHF | 204.15 CHF | 🟢 +1.09 CHF (+0.53 %) | 1'085.13 (+2 %) |
| **BTC** short | 28.10.2026 13:45 | 66'924.92 | 66'958.40 | 0.004792 | 320.73 CHF | 320.89 CHF | 🔴 -0.16 CHF (-0.05 %) | 67'193.98 (+0 %) |
| **ETH** short | 28.10.2026 13:45 | 1'938.49 | 1'939.46 | 0.103957 | 201.52 CHF | 201.62 CHF | 🔴 -0.10 CHF (-0.05 %) | 1'945.98 (+0 %) |
| **BNB** long | 28.10.2026 13:45 | 625.56 | 625.41 | 0.092816 | 58.06 CHF | 58.05 CHF | 🔴 -0.01 CHF (-0.02 %) | 621.84 (-1 %) |
| **SOL** short | 28.10.2026 13:45 | 84.18 | 84.21 | 7.717403 | 649.68 CHF | 649.88 CHF | 🔴 -0.20 CHF (-0.03 %) | 84.78 (+1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash |

**Letzte Entscheidung:** BTC/CHF: short eröffnet 0.004792 @ 66924.92 · ETH/CHF: short eröffnet 0.103957 @ 1938.49 · BNB/CHF: gekauft 0.092816 @ 625.56 · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: short eröffnet 7.717403 @ 84.18 · TRX/CHF: kein Einstieg (max. offene Positionen) · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| SOL long | 28.10.2026 13:15 | 28.10.2026 13:45 | 84.57 | 84.18 | 🔴 -1.81 CHF | Signal |
| BTC long | 28.10.2026 13:15 | 28.10.2026 13:45 | 67'033.50 | 66'924.92 | 🔴 -0.87 CHF | Signal |
| BNB long | 28.10.2026 12:13 | 28.10.2026 13:45 | 629.13 | 624.93 | 🔴 -2.15 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 13:15 | 28.10.2026 13:45 | 1'946.78 | 1'938.49 | 🔴 -1.41 CHF | Stop-Loss (Gap) |
| TRX long | 28.10.2026 08:42 | 28.10.2026 13:15 | 0.27 | 0.27 | 🔴 -1.51 CHF | Signal |
| SOL long | 28.10.2026 09:42 | 28.10.2026 13:15 | 85.52 | 84.49 | 🔴 -3.45 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 12:13 | 28.10.2026 13:15 | 1'965.91 | 1'944.84 | 🔴 -2.80 CHF | Stop-Loss (Gap) |
| BTC long | 28.10.2026 12:45 | 28.10.2026 13:15 | 67'493.33 | 66'966.50 | 🔴 -2.15 CHF | Stop-Loss (Gap) |
| BTC long | 28.10.2026 09:42 | 28.10.2026 12:15 | 67'734.15 | 67'366.30 | 🔴 -1.71 CHF | Stop-Loss (Gap) |
| BNB long | 28.10.2026 10:42 | 28.10.2026 12:13 | 623.82 | 627.87 | 🟢 +0.23 CHF | Take-Profit |

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
