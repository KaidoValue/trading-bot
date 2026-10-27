# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **27.10.2026 16:32** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **994.07 CHF** | **962.41 CHF** | **463.23 CHF** |
| Gewinn / Verlust | 🔴 -5.93 CHF (-0.59 %) | 🔴 -37.59 CHF (-3.76 %) | 🔴 -536.77 CHF (-53.68 %) |
| Im Einsatz (investiert) | 409.11 CHF (41 %) | 735.62 CHF (76 %) | 918.48 CHF (198 %) |
| Cash (nicht investiert) | 584.96 CHF | 226.79 CHF | -455.25 CHF |
| Offene Positionen | 5 | 3 | 6 |
| Abgeschlossene Trades | 0 | 12 | 130 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 7.40 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **976.38 CHF** |
| Gewinn / Verlust | 🔴 -23.62 CHF (-2.36 %) |
| **Aktuelle Verteilung** | Langfrist 48 % · KI 16 % · Risiko 1 % · Cash 35 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist -0.4 %, KI -3.5 %, Risiko -52.8 %, 🚨 Notbremse Risiko (-9.6 % in 3 Std.) |
| Umschicht-Gebühren bisher | 2.15 CHF |
| Erfahrung im Gedächtnis | 203 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** KI +0.008 %/Lauf, Langfrist +0.006 %/Lauf, Risiko -0.468 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'566.20 CHF | 🟢 +0.49 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'938.00 CHF | 🟢 +1.17 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 620.58 CHF | 🟢 +0.99 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.09 CHF | 🟢 +1.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.48 CHF | 🔴 -0.01 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.31 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'066.18 CHF | 🟢 +4.53 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 65.67 CHF | 🟢 +1.32 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'566.20 | 0.001485 | 100.05 CHF | 98.83 CHF | 🔴 -1.22 CHF (-1.22 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'938.00 | 0.040710 | 80.86 CHF | 78.90 CHF | 🔴 -1.96 CHF (-2.43 %) | 1'371.11 (-29 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 620.58 | 0.162070 | 100.02 CHF | 100.58 CHF | 🟢 +0.56 CHF (+0.56 %) | 483.48 (-22 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.09 | 58.690975 | 63.53 CHF | 64.21 CHF | 🟢 +0.68 CHF (+1.07 %) | 0.66 (-40 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 83.48 | 0.797780 | 68.91 CHF | 66.60 CHF | 🔴 -2.31 CHF (-3.35 %) | 55.00 (-34 %) |

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
| **ZEC** long | 26.10.2026 10:10 | 1'006.92 | 1'066.18 | 0.237480 | 239.12 CHF | 253.20 CHF | 🟢 +14.07 CHF (+5.89 %) | 973.10 (-9 %) |
| **BTC** long | 27.10.2026 16:00 | 66'509.84 | 66'566.20 | 0.003616 | 240.50 CHF | 240.70 CHF | 🟢 +0.20 CHF (+0.08 %) | 65'856.81 (-1 %) |
| **ETH** long | 27.10.2026 16:00 | 1'928.15 | 1'938.00 | 0.124729 | 240.50 CHF | 241.73 CHF | 🟢 +1.23 CHF (+0.51 %) | 1'908.65 (-2 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🟢 investiert sein |
| BNB | 🔴 raus / Cash |
| XRP | 🟢 investiert sein |
| SOL | 🟢 investiert sein |
| TRX | 🟢 investiert sein |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 20'654 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| ETH | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| BNB | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |
| XRP | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.065 %/Kerze), reversal (+0.056 %/Kerze) |
| SOL | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.060 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.028 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.072 %/Kerze), momentum (+0.065 %/Kerze), reversal (+0.056 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: gekauft 0.003616 @ 66509.84 · ETH/CHF: gekauft 0.124729 @ 1928.15 · BNB/CHF: Signal 'raus', bleibe in Cash · XRP/CHF: kein Einstieg (max. offene Positionen) · SOL/CHF: kein Einstieg (max. offene Positionen) · TRX/CHF: kein Einstieg (max. offene Positionen) · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: kein Einstieg (max. offene Positionen)

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
| **BTC** long | 27.10.2026 12:58 | 66'132.05 | 66'566.20 | 0.001271 | 84.08 CHF | 84.63 CHF | 🟢 +0.55 CHF (+0.66 %) | 65'805.39 (-1 %) |
| **HYPE** long | 27.10.2026 13:31 | 64.90 | 65.67 | 0.980435 | 63.63 CHF | 64.39 CHF | 🟢 +0.75 CHF (+1.18 %) | 64.28 (-2 %) |
| **TRX** long | 27.10.2026 14:01 | 0.27 | 0.27 | 211.993071 | 57.64 CHF | 57.58 CHF | 🔴 -0.06 CHF (-0.11 %) | 0.27 (-0 %) |
| **XRP** long | 27.10.2026 15:31 | 1.09 | 1.09 | 217.140956 | 236.85 CHF | 237.56 CHF | 🟢 +0.71 CHF (+0.30 %) | 1.08 (-1 %) |
| **ETH** long | 27.10.2026 16:31 | 1'938.97 | 1'938.00 | 0.122367 | 237.27 CHF | 237.15 CHF | 🔴 -0.12 CHF (-0.05 %) | 1'927.73 (-1 %) |
| **BNB** long | 27.10.2026 16:31 | 620.82 | 620.58 | 0.382182 | 237.27 CHF | 237.17 CHF | 🔴 -0.09 CHF (-0.04 %) | 616.78 (-1 %) |

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

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: gekauft 0.122367 @ 1938.97 · BNB/CHF: gekauft 0.382182 @ 620.82 · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: kein Einstieg (max. offene Positionen) · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: Position offen, Signal bestätigt

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long | 27.10.2026 14:01 | 27.10.2026 16:31 | 614.64 | 619.56 | 🟢 +0.66 CHF | Take-Profit |
| ETH long | 27.10.2026 15:31 | 27.10.2026 16:31 | 1'920.05 | 1'935.48 | 🟢 +1.28 CHF | Take-Profit |
| ZEC long | 27.10.2026 09:28 | 27.10.2026 15:31 | 1'026.40 | 1'051.89 | 🟢 +13.78 CHF | Take-Profit |
| ETH long | 27.10.2026 14:01 | 27.10.2026 15:31 | 1'931.97 | 1'918.13 | 🔴 -2.34 CHF | Stop-Loss (Gap) |
| SOL short | 26.10.2026 21:19 | 27.10.2026 14:01 | 82.87 | 83.47 | 🔴 -0.91 CHF | Signal |
| TRX short | 27.10.2026 12:28 | 27.10.2026 14:01 | 0.27 | 0.27 | 🔴 -1.93 CHF | Stop-Loss (Gap) |
| ETH long | 27.10.2026 13:28 | 27.10.2026 14:01 | 1'913.39 | 1'926.80 | 🟢 +1.05 CHF | Take-Profit |
| XRP short | 27.10.2026 09:58 | 27.10.2026 13:31 | 1.07 | 1.08 | 🔴 -0.70 CHF | Signal |
| HYPE short | 27.10.2026 12:28 | 27.10.2026 13:28 | 64.27 | 64.99 | 🔴 -3.95 CHF | Stop-Loss (Gap) |
| BNB short | 27.10.2026 11:58 | 27.10.2026 12:28 | 611.25 | 611.51 | 🔴 -1.36 CHF | Signal |

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

- **Stimmung (Fear & Greed):** 48 von 100, neutral
- **Bewertung News:** +0.50 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** rally (gemeldet von coindesk, cointelegraph – blockiert Shorts)

**Schlagzeilen dazu:**

- 2026-10-27 12:18 UTC · **cointelegraph** · [Bitcoin price analysis sees ‘strong rally’ as old coins become dormant](https://cointelegraph.com/markets/bitcoin-price-analysis-sees-strong-rally-as-old-coins-become-dormant?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: rally)_
- 2026-10-27 11:32 UTC · **coindesk** · [Bitcoin drops below $80,000 as crypto ignores Asian tech rally, Fed meeting begins](https://www.coindesk.com/markets/2026/10/27/bitcoin-drops-below-usd80-000-as-crypto-ignores-asian-tech-rally-fed-meeting-begins) _(Thema: rally)_
