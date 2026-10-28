# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **28.10.2026 12:46** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **999.83 CHF** | **962.84 CHF** | **409.88 CHF** |
| Gewinn / Verlust | 🔴 -0.17 CHF (-0.02 %) | 🔴 -37.16 CHF (-3.72 %) | 🔴 -590.12 CHF (-59.01 %) |
| Im Einsatz (investiert) | 414.87 CHF (41 %) | 243.93 CHF (25 %) | 1'230.94 CHF (300 %) |
| Cash (nicht investiert) | 584.96 CHF | 718.91 CHF | -389.33 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 15 | 159 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 8.01 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **977.80 CHF** |
| Gewinn / Verlust | 🔴 -22.20 CHF (-2.22 %) |
| **Aktuelle Verteilung** | Langfrist 53 % · KI 21 % · Risiko 1 % · Cash 25 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.6 %, KI -1.5 %, Risiko -77.5 % |
| Umschicht-Gebühren bisher | 2.40 CHF |
| Erfahrung im Gedächtnis | 248 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.008 %/Lauf, KI +0.006 %/Lauf, Risiko -0.401 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'459.60 CHF | 🟢 +0.91 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'964.93 CHF | 🟢 +1.23 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 630.57 CHF | 🟢 +2.23 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.10 CHF | 🔴 -0.31 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 85.25 CHF | 🟢 +1.54 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.28 CHF | 🟢 +0.17 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'080.09 CHF | 🔴 -0.44 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 67.62 CHF | 🟢 +0.42 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 67'459.60 | 0.001485 | 100.05 CHF | 100.16 CHF | 🟢 +0.11 CHF (+0.11 %) | 53'251.84 (-21 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'964.93 | 0.040710 | 80.86 CHF | 79.99 CHF | 🔴 -0.87 CHF (-1.07 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 630.57 | 0.162070 | 100.02 CHF | 102.20 CHF | 🟢 +2.18 CHF (+2.18 %) | 483.48 (-23 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.10 | 58.690975 | 63.53 CHF | 64.52 CHF | 🟢 +0.99 CHF (+1.56 %) | 0.66 (-40 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 85.25 | 0.797780 | 68.91 CHF | 68.01 CHF | 🔴 -0.90 CHF (-1.30 %) | 55.00 (-35 %) |

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
| **BTC** long | 27.10.2026 16:00 | 66'509.84 | 67'459.60 | 0.003616 | 240.50 CHF | 243.93 CHF | 🟢 +3.43 CHF (+1.43 %) | 65'856.81 (-2 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | ⚪ neutral |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🟢 investiert sein |
| SOL | ⚪ neutral |
| TRX | 🟢 investiert sein |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 20'814 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| ETH | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| BNB | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| XRP | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| SOL | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| TRX | Aufwärtstrend, wild | trend (+0.073 %/Kerze), momentum (+0.066 %/Kerze), reversal (+0.057 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| HYPE | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: kein Signal · ETH/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · BNB/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · XRP/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · SOL/CHF: kein Signal · TRX/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0)

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
| **XRP** short | 28.10.2026 07:10 | 1.10 | 1.10 | 196.371129 | 215.89 CHF | 215.87 CHF | 🟢 +0.02 CHF (+0.01 %) | 1.11 (+1 %) |
| **TRX** long | 28.10.2026 08:42 | 0.27 | 0.28 | 780.939565 | 214.72 CHF | 214.88 CHF | 🟢 +0.16 CHF (+0.07 %) | 0.27 (-0 %) |
| **SOL** long | 28.10.2026 09:42 | 85.52 | 85.25 | 2.354513 | 201.35 CHF | 200.72 CHF | 🔴 -0.62 CHF (-0.31 %) | 84.97 (-0 %) |
| **ETH** long | 28.10.2026 12:13 | 1'965.91 | 1'964.93 | 0.107061 | 210.47 CHF | 210.37 CHF | 🔴 -0.11 CHF (-0.05 %) | 1'959.45 (-0 %) |
| **BNB** long | 28.10.2026 12:13 | 629.13 | 630.57 | 0.289090 | 181.88 CHF | 182.29 CHF | 🟢 +0.41 CHF (+0.23 %) | 625.76 (-1 %) |
| **BTC** long | 28.10.2026 12:45 | 67'493.33 | 67'459.60 | 0.003066 | 206.91 CHF | 206.81 CHF | 🔴 -0.10 CHF (-0.05 %) | 67'254.48 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🟢 investiert sein |
| TRX | 🟢 investiert sein |
| ZEC | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: gekauft 0.003066 @ 67493.33 · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BTC long | 28.10.2026 09:42 | 28.10.2026 12:15 | 67'734.15 | 67'366.30 | 🔴 -1.71 CHF | Stop-Loss (Gap) |
| BNB long | 28.10.2026 10:42 | 28.10.2026 12:13 | 623.82 | 627.87 | 🟢 +0.23 CHF | Take-Profit |
| ETH long | 28.10.2026 09:42 | 28.10.2026 12:13 | 1'972.99 | 1'963.95 | 🔴 -1.53 CHF | Stop-Loss (Gap) |
| BNB long | 28.10.2026 05:10 | 28.10.2026 10:42 | 618.50 | 623.18 | 🟢 +0.46 CHF | Take-Profit |
| SOL long | 27.10.2026 17:31 | 28.10.2026 09:42 | 83.71 | 84.93 | 🟢 +2.18 CHF | Take-Profit |
| ETH long | 28.10.2026 04:40 | 28.10.2026 09:42 | 1'958.99 | 1'970.69 | 🟢 +0.75 CHF | Take-Profit |
| BTC short | 28.10.2026 09:13 | 28.10.2026 09:42 | 67'273.65 | 67'734.15 | 🔴 -1.66 CHF | Stop-Loss (Gap) |
| BTC short | 28.10.2026 08:13 | 28.10.2026 09:13 | 67'066.45 | 67'340.95 | 🔴 -1.15 CHF | Stop-Loss (Gap) |
| HYPE long | 27.10.2026 20:34 | 28.10.2026 08:13 | 67.37 | 67.42 | 🔴 -1.01 CHF | Signal |
| ZEC long | 27.10.2026 20:04 | 28.10.2026 07:40 | 1'076.47 | 1'082.26 | 🟢 +0.03 CHF | Signal |

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
- 2026-10-28 11:23 UTC · **coindesk** · [Live updates: Bitcoin climbs above $81,000 as majors rally ahead of Fed decision](https://www.coindesk.com/business/2026/10/28/live-updates-bitcoin-climbs-above-usd81-000-as-majors-rally-ahead-of-fed-decision) _(Thema: rally)_
- 2026-10-28 09:15 UTC · **coindesk** · [Here's how much bitcoin and the S&P 500 could rally after midterms](https://www.coindesk.com/markets/2026/10/28/bitcoin-averages-over-50-in-the-12-months-after-midterms-s-and-p-500-gains-15) _(Thema: rally)_
- 2026-10-27 12:18 UTC · **cointelegraph** · [Bitcoin price analysis sees ‘strong rally’ as old coins become dormant](https://cointelegraph.com/markets/bitcoin-price-analysis-sees-strong-rally-as-old-coins-become-dormant?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: rally)_
