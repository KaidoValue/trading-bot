# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **28.10.2026 11:43** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **999.80 CHF** | **963.21 CHF** | **414.74 CHF** |
| Gewinn / Verlust | 🔴 -0.20 CHF (-0.02 %) | 🔴 -36.79 CHF (-3.68 %) | 🔴 -585.26 CHF (-58.53 %) |
| Im Einsatz (investiert) | 414.84 CHF (41 %) | 244.30 CHF (25 %) | 1'242.02 CHF (299 %) |
| Cash (nicht investiert) | 584.96 CHF | 718.91 CHF | -394.58 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 15 | 156 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 7.99 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **977.97 CHF** |
| Gewinn / Verlust | 🔴 -22.03 CHF (-2.20 %) |
| **Aktuelle Verteilung** | Langfrist 53 % · KI 21 % · Risiko 1 % · Cash 25 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.6 %, KI -1.5 %, Risiko -77.5 % |
| Umschicht-Gebühren bisher | 2.40 CHF |
| Erfahrung im Gedächtnis | 245 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.009 %/Lauf, KI +0.006 %/Lauf, Risiko -0.402 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'561.10 CHF | 🟢 +1.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'966.00 CHF | 🟢 +1.28 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 627.35 CHF | 🟢 +1.60 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.10 CHF | 🔴 -0.19 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 85.44 CHF | 🟢 +1.66 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.28 CHF | 🟢 +0.21 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'087.17 CHF | 🟢 +0.11 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 68.14 CHF | 🟢 +1.10 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 67'561.10 | 0.001485 | 100.05 CHF | 100.31 CHF | 🟢 +0.26 CHF (+0.26 %) | 53'251.84 (-21 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'966.00 | 0.040710 | 80.86 CHF | 80.04 CHF | 🔴 -0.82 CHF (-1.02 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 627.35 | 0.162070 | 100.02 CHF | 101.67 CHF | 🟢 +1.65 CHF (+1.65 %) | 483.48 (-23 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.10 | 58.690975 | 63.53 CHF | 64.66 CHF | 🟢 +1.13 CHF (+1.79 %) | 0.66 (-40 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 85.44 | 0.797780 | 68.91 CHF | 68.16 CHF | 🔴 -0.75 CHF (-1.08 %) | 55.00 (-36 %) |

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
| **BTC** long | 27.10.2026 16:00 | 66'509.84 | 67'561.10 | 0.003616 | 240.50 CHF | 244.30 CHF | 🟢 +3.80 CHF (+1.58 %) | 65'856.81 (-3 %) |

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

**🧠 KI-Gedächtnis:** 20'806 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.031 %/Kerze) |
| ETH | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.031 %/Kerze) |
| BNB | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.031 %/Kerze) |
| XRP | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.031 %/Kerze) |
| SOL | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.031 %/Kerze) |
| TRX | Aufwärtstrend, wild | trend (+0.073 %/Kerze), momentum (+0.066 %/Kerze), reversal (+0.057 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.031 %/Kerze) |
| HYPE | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.031 %/Kerze) |

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
| **XRP** short | 28.10.2026 07:10 | 1.10 | 1.10 | 196.371129 | 215.89 CHF | 216.35 CHF | 🔴 -0.47 CHF (-0.22 %) | 1.11 (+1 %) |
| **TRX** long | 28.10.2026 08:42 | 0.27 | 0.28 | 780.939565 | 214.72 CHF | 215.19 CHF | 🟢 +0.47 CHF (+0.22 %) | 0.27 (-0 %) |
| **BTC** long | 28.10.2026 09:42 | 67'734.15 | 67'561.10 | 0.003148 | 213.25 CHF | 212.70 CHF | 🔴 -0.54 CHF (-0.26 %) | 67'484.43 (-0 %) |
| **ETH** long | 28.10.2026 09:42 | 1'972.99 | 1'966.00 | 0.108083 | 213.25 CHF | 212.49 CHF | 🔴 -0.76 CHF (-0.35 %) | 1'965.79 (-0 %) |
| **SOL** long | 28.10.2026 09:42 | 85.52 | 85.44 | 2.354513 | 201.35 CHF | 201.17 CHF | 🔴 -0.18 CHF (-0.09 %) | 84.97 (-1 %) |
| **BNB** long | 28.10.2026 10:42 | 623.82 | 627.35 | 0.293477 | 183.08 CHF | 184.11 CHF | 🟢 +1.03 CHF (+0.56 %) | 621.18 (-1 %) |

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

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long | 28.10.2026 05:10 | 28.10.2026 10:42 | 618.50 | 623.18 | 🟢 +0.46 CHF | Take-Profit |
| SOL long | 27.10.2026 17:31 | 28.10.2026 09:42 | 83.71 | 84.93 | 🟢 +2.18 CHF | Take-Profit |
| ETH long | 28.10.2026 04:40 | 28.10.2026 09:42 | 1'958.99 | 1'970.69 | 🟢 +0.75 CHF | Take-Profit |
| BTC short | 28.10.2026 09:13 | 28.10.2026 09:42 | 67'273.65 | 67'734.15 | 🔴 -1.66 CHF | Stop-Loss (Gap) |
| BTC short | 28.10.2026 08:13 | 28.10.2026 09:13 | 67'066.45 | 67'340.95 | 🔴 -1.15 CHF | Stop-Loss (Gap) |
| HYPE long | 27.10.2026 20:34 | 28.10.2026 08:13 | 67.37 | 67.42 | 🔴 -1.01 CHF | Signal |
| ZEC long | 27.10.2026 20:04 | 28.10.2026 07:40 | 1'076.47 | 1'082.26 | 🟢 +0.03 CHF | Signal |
| BTC long | 28.10.2026 06:10 | 28.10.2026 07:10 | 67'068.12 | 67'053.56 | 🔴 -0.60 CHF | Signal |
| XRP long | 28.10.2026 04:40 | 28.10.2026 06:10 | 1.11 | 1.10 | 🔴 -3.15 CHF | Stop-Loss (Gap) |
| BTC short | 28.10.2026 03:07 | 28.10.2026 05:10 | 66'995.79 | 67'228.20 | 🔴 -1.33 CHF | Signal |

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
- **Bewertung News:** -1.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** rally (gemeldet von coindesk, cointelegraph – blockiert Shorts); hack (gemeldet von coindesk, decrypt – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-10-28 09:15 UTC · **coindesk** · [Here's how much bitcoin and the S&P 500 could rally after midterms](https://www.coindesk.com/markets/2026/10/28/bitcoin-averages-over-50-in-the-12-months-after-midterms-s-and-p-500-gains-15) _(Thema: rally)_
- 2026-10-27 18:16 UTC · **decrypt** · [Bitcoin Wallet Maker Keystone Pulls Devices as Stolen Key Opens Door to Fakes](https://decrypt.co/381983/bitcoin-wallet-keystone-devices-destroyed-stolen-key) _(Thema: hack)_
- 2026-10-27 12:18 UTC · **cointelegraph** · [Bitcoin price analysis sees ‘strong rally’ as old coins become dormant](https://cointelegraph.com/markets/bitcoin-price-analysis-sees-strong-rally-as-old-coins-become-dormant?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: rally)_
- 2026-10-27 11:40 UTC · **coindesk** · [Live updates: Bitcoin edges higher as Nasdaq surges 1.2%](https://www.coindesk.com/tech/2026/10/27/live-updates-bitcoin-holds-below-usd80-000-as-ai-buildout-draws-more-capital) _(Thema: rally)_
- 2026-10-27 11:32 UTC · **coindesk** · [Bitcoin drops below $80,000 as crypto ignores Asian tech rally, Fed meeting begins](https://www.coindesk.com/markets/2026/10/27/bitcoin-drops-below-usd80-000-as-crypto-ignores-asian-tech-rally-fed-meeting-begins) _(Thema: rally)_
- 2026-10-27 11:13 UTC · **coindesk** · [Crypto wallet maker Keystone to destroy almost 19,000 devices after security breach](https://www.coindesk.com/business/2026/10/27/crypto-wallet-maker-keystone-to-destroy-almost-19-000-devices-after-security-breach) _(Thema: hack)_
