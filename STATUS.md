# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **28.10.2026 13:17** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **996.78 CHF** | **959.29 CHF** | **397.68 CHF** |
| Gewinn / Verlust | 🔴 -3.22 CHF (-0.32 %) | 🔴 -40.71 CHF (-4.07 %) | 🔴 -602.32 CHF (-60.23 %) |
| Im Einsatz (investiert) | 411.82 CHF (41 %) | 723.09 CHF (75 %) | 1'196.28 CHF (301 %) |
| Cash (nicht investiert) | 584.96 CHF | 236.20 CHF | 40.87 CHF |
| Offene Positionen | 5 | 3 | 6 |
| Abgeschlossene Trades | 0 | 15 | 163 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.01 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **975.16 CHF** |
| Gewinn / Verlust | 🔴 -24.84 CHF (-2.48 %) |
| **Aktuelle Verteilung** | Langfrist 53 % · KI 21 % · Risiko 1 % · Cash 25 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.6 %, KI -1.5 %, Risiko -77.5 % |
| Umschicht-Gebühren bisher | 2.40 CHF |
| Erfahrung im Gedächtnis | 249 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.006 %/Lauf, KI +0.003 %/Lauf, Risiko -0.421 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'000.00 CHF | 🟢 +0.22 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'945.81 CHF | 🟢 +0.24 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 627.64 CHF | 🟢 +1.79 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.09 CHF | 🔴 -1.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.49 CHF | 🟢 +0.67 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🟢 +0.00 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'074.19 CHF | 🔴 -0.95 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 67.08 CHF | 🔴 -0.34 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 67'000.00 | 0.001485 | 100.05 CHF | 99.47 CHF | 🔴 -0.58 CHF (-0.58 %) | 53'251.84 (-21 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'945.81 | 0.040710 | 80.86 CHF | 79.21 CHF | 🔴 -1.64 CHF (-2.03 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 627.64 | 0.162070 | 100.02 CHF | 101.72 CHF | 🟢 +1.70 CHF (+1.70 %) | 483.48 (-23 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.09 | 58.690975 | 63.53 CHF | 64.01 CHF | 🟢 +0.48 CHF (+0.76 %) | 0.66 (-40 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 84.49 | 0.797780 | 68.91 CHF | 67.40 CHF | 🔴 -1.50 CHF (-2.18 %) | 55.00 (-35 %) |

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
| **BTC** long | 27.10.2026 16:00 | 66'509.84 | 67'000.00 | 0.003616 | 240.50 CHF | 242.27 CHF | 🟢 +1.77 CHF (+0.74 %) | 65'856.81 (-2 %) |
| **ETH** long | 28.10.2026 13:15 | 1'946.78 | 1'945.81 | 0.123494 | 240.42 CHF | 240.30 CHF | 🔴 -0.12 CHF (-0.05 %) | 1'932.48 (-1 %) |
| **BNB** long | 28.10.2026 13:15 | 627.36 | 627.64 | 0.383218 | 240.42 CHF | 240.52 CHF | 🟢 +0.11 CHF (+0.05 %) | 621.00 (-1 %) |

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
| **XRP** short | 28.10.2026 07:10 | 1.10 | 1.09 | 196.371129 | 215.89 CHF | 214.17 CHF | 🟢 +1.72 CHF (+0.80 %) | 1.11 (+2 %) |
| **BNB** long | 28.10.2026 12:13 | 629.13 | 627.64 | 0.289090 | 181.88 CHF | 181.45 CHF | 🔴 -0.43 CHF (-0.24 %) | 625.76 (-0 %) |
| **BTC** long | 28.10.2026 13:15 | 67'033.50 | 67'000.00 | 0.003065 | 205.44 CHF | 205.34 CHF | 🔴 -0.10 CHF (-0.05 %) | 66'799.57 (-0 %) |
| **ETH** long | 28.10.2026 13:15 | 1'946.78 | 1'945.81 | 0.105529 | 205.44 CHF | 205.34 CHF | 🔴 -0.10 CHF (-0.05 %) | 1'941.08 (-0 %) |
| **SOL** long | 28.10.2026 13:15 | 84.57 | 84.49 | 2.182760 | 184.60 CHF | 184.42 CHF | 🔴 -0.18 CHF (-0.10 %) | 84.02 (-1 %) |
| **ZEC** short | 28.10.2026 13:15 | 1'072.45 | 1'074.19 | 0.191373 | 205.24 CHF | 205.57 CHF | 🔴 -0.33 CHF (-0.16 %) | 1'085.13 (+1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🟢 investiert sein |
| TRX | 🔴 raus / Cash |
| ZEC | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash |

**Letzte Entscheidung:** BTC/CHF: gekauft 0.003065 @ 67033.50 · ETH/CHF: gekauft 0.105529 @ 1946.78 · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: gekauft 2.182760 @ 84.57 · TRX/CHF: kein Einstieg (Tagesverlust-Limit) · ZEC/CHF: short eröffnet 0.191373 @ 1072.45 · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| TRX long | 28.10.2026 08:42 | 28.10.2026 13:15 | 0.27 | 0.27 | 🔴 -1.51 CHF | Signal |
| SOL long | 28.10.2026 09:42 | 28.10.2026 13:15 | 85.52 | 84.49 | 🔴 -3.45 CHF | Stop-Loss (Gap) |
| ETH long | 28.10.2026 12:13 | 28.10.2026 13:15 | 1'965.91 | 1'944.84 | 🔴 -2.80 CHF | Stop-Loss (Gap) |
| BTC long | 28.10.2026 12:45 | 28.10.2026 13:15 | 67'493.33 | 66'966.50 | 🔴 -2.15 CHF | Stop-Loss (Gap) |
| BTC long | 28.10.2026 09:42 | 28.10.2026 12:15 | 67'734.15 | 67'366.30 | 🔴 -1.71 CHF | Stop-Loss (Gap) |
| BNB long | 28.10.2026 10:42 | 28.10.2026 12:13 | 623.82 | 627.87 | 🟢 +0.23 CHF | Take-Profit |
| ETH long | 28.10.2026 09:42 | 28.10.2026 12:13 | 1'972.99 | 1'963.95 | 🔴 -1.53 CHF | Stop-Loss (Gap) |
| BNB long | 28.10.2026 05:10 | 28.10.2026 10:42 | 618.50 | 623.18 | 🟢 +0.46 CHF | Take-Profit |
| SOL long | 27.10.2026 17:31 | 28.10.2026 09:42 | 83.71 | 84.93 | 🟢 +2.18 CHF | Take-Profit |
| ETH long | 28.10.2026 04:40 | 28.10.2026 09:42 | 1'958.99 | 1'970.69 | 🟢 +0.75 CHF | Take-Profit |

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
- **Bewertung News:** +0.50 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** rally (gemeldet von coindesk, cointelegraph – blockiert Shorts)

**Schlagzeilen dazu:**

- 2026-10-28 11:32 UTC · **coindesk** · [Bitcoin rebounds above $81,000 as Asian chip rally spills into crypto, pepe jumps 9%](https://www.coindesk.com/markets/2026/10/28/bitcoin-rebounds-above-usd81-000-as-asian-chip-rally-spills-into-crypto-pepe-jumps-9) _(Thema: rally)_
- 2026-10-28 09:15 UTC · **coindesk** · [Here's how much bitcoin and the S&P 500 could rally after midterms](https://www.coindesk.com/markets/2026/10/28/bitcoin-averages-over-50-in-the-12-months-after-midterms-s-and-p-500-gains-15) _(Thema: rally)_
- 2026-10-27 12:18 UTC · **cointelegraph** · [Bitcoin price analysis sees ‘strong rally’ as old coins become dormant](https://cointelegraph.com/markets/bitcoin-price-analysis-sees-strong-rally-as-old-coins-become-dormant?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: rally)_
