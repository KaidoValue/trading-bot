# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **27.10.2026 23:38** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **994.29 CHF** | **960.85 CHF** | **445.33 CHF** |
| Gewinn / Verlust | 🔴 -5.71 CHF (-0.57 %) | 🔴 -39.15 CHF (-3.92 %) | 🔴 -554.67 CHF (-55.47 %) |
| Im Einsatz (investiert) | 409.33 CHF (41 %) | 722.81 CHF (75 %) | 1'342.06 CHF (301 %) |
| Cash (nicht investiert) | 584.96 CHF | 238.04 CHF | -437.69 CHF |
| Offene Positionen | 5 | 3 | 6 |
| Abgeschlossene Trades | 0 | 13 | 140 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 7.65 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **975.30 CHF** |
| Gewinn / Verlust | 🔴 -24.70 CHF (-2.47 %) |
| **Aktuelle Verteilung** | Langfrist 53 % · KI 21 % · Risiko 1 % · Cash 25 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.6 %, KI -1.5 %, Risiko -77.5 % |
| Umschicht-Gebühren bisher | 2.40 CHF |
| Erfahrung im Gedächtnis | 219 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** KI +0.005 %/Lauf, Langfrist +0.005 %/Lauf, Risiko -0.434 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 66'889.20 CHF | 🟢 +0.98 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'945.00 CHF | 🟢 +1.54 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 615.78 CHF | 🟢 +0.23 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.09 CHF | 🟢 +1.13 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 83.73 CHF | 🟢 +0.31 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🟢 +0.66 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'079.23 CHF | 🟢 +5.83 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 67.22 CHF | 🟢 +3.73 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 66'889.20 | 0.001485 | 100.05 CHF | 99.31 CHF | 🔴 -0.74 CHF (-0.74 %) | 53'251.84 (-20 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'945.00 | 0.040710 | 80.86 CHF | 79.18 CHF | 🔴 -1.68 CHF (-2.07 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 615.78 | 0.162070 | 100.02 CHF | 99.80 CHF | 🔴 -0.22 CHF (-0.22 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.09 | 58.690975 | 63.53 CHF | 64.24 CHF | 🟢 +0.72 CHF (+1.13 %) | 0.66 (-40 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 83.73 | 0.797780 | 68.91 CHF | 66.80 CHF | 🔴 -2.11 CHF (-3.06 %) | 55.00 (-34 %) |

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
| **BTC** long | 27.10.2026 16:00 | 66'509.84 | 66'889.20 | 0.003616 | 240.50 CHF | 241.87 CHF | 🟢 +1.37 CHF (+0.57 %) | 65'856.81 (-2 %) |
| **ETH** long | 27.10.2026 16:00 | 1'928.15 | 1'945.00 | 0.124729 | 240.50 CHF | 242.60 CHF | 🟢 +2.10 CHF (+0.87 %) | 1'908.65 (-2 %) |
| **BNB** long | 27.10.2026 18:00 | 622.33 | 615.78 | 0.387047 | 240.87 CHF | 238.34 CHF | 🔴 -2.53 CHF (-1.05 %) | 615.54 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🟢 investiert sein |
| SOL | 🟢 investiert sein |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 20'710 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, wild | mean_reversion (+0.035 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ETH | Seitwärts, wild | mean_reversion (+0.035 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| BNB | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.028 %/Kerze) |
| XRP | Aufwärtstrend, wild | trend (+0.073 %/Kerze), momentum (+0.066 %/Kerze), reversal (+0.057 %/Kerze) |
| SOL | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.035 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.061 %/Kerze), reversal (+0.030 %/Kerze), momentum (+0.028 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.073 %/Kerze), momentum (+0.066 %/Kerze), reversal (+0.057 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: kein Einstieg (max. offene Positionen) · SOL/CHF: kein Einstieg (max. offene Positionen) · TRX/CHF: Signal 'raus', bleibe in Cash · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ZEC long | 26.10.2026 10:10 | 27.10.2026 17:30 | 1'006.92 | 1'072.51 | 🟢 +14.25 CHF | Take-Profit |
| BTC long | 26.10.2026 10:10 | 26.10.2026 15:16 | 66'289.23 | 66'013.88 | 🔴 -1.61 CHF | Signal |
| ETH long | 26.10.2026 13:13 | 26.10.2026 14:13 | 1'930.96 | 1'911.28 | 🔴 -3.05 CHF | Signal |
| TRX long | 23.10.2026 20:16 | 26.10.2026 11:13 | 0.27 | 0.27 | 🔴 -0.31 CHF | Signal |
| BTC long | 26.10.2026 00:04 | 26.10.2026 00:34 | 66'419.29 | 65'838.16 | 🔴 -2.72 CHF | Stop-Loss (Gap) |
| ZEC long | 25.10.2026 06:23 | 25.10.2026 07:26 | 1'003.77 | 993.72 | 🔴 -3.67 CHF | Signal |
| BNB long | 25.10.2026 06:23 | 25.10.2026 07:26 | 616.82 | 613.83 | 🔴 -2.42 CHF | Signal |
| BTC long | 25.10.2026 05:23 | 25.10.2026 06:23 | 66'685.23 | 66'692.94 | 🔴 -0.60 CHF | Signal |
| BNB long | 24.10.2026 22:17 | 25.10.2026 05:53 | 604.10 | 615.07 | 🟢 +3.12 CHF | Take-Profit |
| ZEC long | 25.10.2026 03:23 | 25.10.2026 04:23 | 1'006.55 | 1'003.58 | 🔴 -1.98 CHF | Signal |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 27.10.2026 17:01 | 66'733.35 | 66'889.20 | 0.003549 | 236.84 CHF | 237.40 CHF | 🟢 +0.55 CHF (+0.23 %) | 66'388.66 (-1 %) |
| **SOL** long | 27.10.2026 17:31 | 83.71 | 83.73 | 2.822954 | 236.32 CHF | 236.38 CHF | 🟢 +0.05 CHF (+0.02 %) | 83.02 (-1 %) |
| **ZEC** long | 27.10.2026 20:04 | 1'076.47 | 1'079.23 | 0.170086 | 183.09 CHF | 183.56 CHF | 🟢 +0.47 CHF (+0.26 %) | 1'058.55 (-2 %) |
| **HYPE** long | 27.10.2026 20:34 | 67.37 | 67.22 | 3.342198 | 225.18 CHF | 224.68 CHF | 🔴 -0.50 CHF (-0.22 %) | 66.63 (-1 %) |
| **ETH** short | 27.10.2026 22:34 | 1'953.83 | 1'945.00 | 0.118004 | 230.56 CHF | 229.52 CHF | 🟢 +1.04 CHF (+0.45 %) | 1'962.86 (+1 %) |
| **TRX** long | 27.10.2026 22:34 | 0.27 | 0.27 | 840.777060 | 230.79 CHF | 230.53 CHF | 🔴 -0.26 CHF (-0.11 %) | 0.27 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash |
| SOL | 🟢 investiert sein |
| TRX | 🟢 investiert sein |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: kein Einstieg (max. offene Positionen) · XRP/CHF: kein Einstieg (max. offene Positionen) · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: Position offen, Signal bestätigt

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| XRP long | 27.10.2026 15:31 | 27.10.2026 22:34 | 1.09 | 1.10 | 🟢 +0.09 CHF | Signal |
| ETH short | 27.10.2026 21:34 | 27.10.2026 22:34 | 1'941.93 | 1'955.79 | 🔴 -2.19 CHF | Stop-Loss (Gap) |
| TRX long | 27.10.2026 20:04 | 27.10.2026 21:34 | 0.27 | 0.27 | 🔴 -0.38 CHF | Take-Profit |
| BNB long | 27.10.2026 16:31 | 27.10.2026 20:34 | 620.82 | 618.80 | 🔴 -2.00 CHF | Signal |
| ETH long | 27.10.2026 16:31 | 27.10.2026 20:04 | 1'938.97 | 1'941.61 | 🔴 -0.29 CHF | Signal |
| TRX short | 27.10.2026 19:04 | 27.10.2026 20:04 | 0.27 | 0.27 | 🔴 -1.76 CHF | Stop-Loss (Gap) |
| TRX short | 27.10.2026 18:01 | 27.10.2026 19:04 | 0.27 | 0.27 | 🔴 -1.88 CHF | Stop-Loss (Gap) |
| TRX long | 27.10.2026 14:01 | 27.10.2026 18:01 | 0.27 | 0.27 | 🔴 -0.49 CHF | Stop-Loss (Gap) |
| HYPE long | 27.10.2026 13:31 | 27.10.2026 17:31 | 64.90 | 66.01 | 🟢 +0.75 CHF | Take-Profit |
| BTC long | 27.10.2026 12:58 | 27.10.2026 17:01 | 66'132.05 | 66'652.88 | 🟢 +0.44 CHF | Take-Profit |

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
- **Bewertung News:** -1.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** rally (gemeldet von coindesk, cointelegraph – blockiert Shorts); hack (gemeldet von coindesk, decrypt – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-10-27 18:16 UTC · **decrypt** · [Bitcoin Wallet Maker Keystone Pulls Devices as Stolen Key Opens Door to Fakes](https://decrypt.co/381983/bitcoin-wallet-keystone-devices-destroyed-stolen-key) _(Thema: hack)_
- 2026-10-27 12:18 UTC · **cointelegraph** · [Bitcoin price analysis sees ‘strong rally’ as old coins become dormant](https://cointelegraph.com/markets/bitcoin-price-analysis-sees-strong-rally-as-old-coins-become-dormant?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: rally)_
- 2026-10-27 11:40 UTC · **coindesk** · [Live updates: Bitcoin edges higher as Nasdaq surges 1.2%](https://www.coindesk.com/tech/2026/10/27/live-updates-bitcoin-holds-below-usd80-000-as-ai-buildout-draws-more-capital) _(Thema: rally)_
- 2026-10-27 11:32 UTC · **coindesk** · [Bitcoin drops below $80,000 as crypto ignores Asian tech rally, Fed meeting begins](https://www.coindesk.com/markets/2026/10/27/bitcoin-drops-below-usd80-000-as-crypto-ignores-asian-tech-rally-fed-meeting-begins) _(Thema: rally)_
- 2026-10-27 11:13 UTC · **coindesk** · [Crypto wallet maker Keystone to destroy almost 19,000 devices after security breach](https://www.coindesk.com/business/2026/10/27/crypto-wallet-maker-keystone-to-destroy-almost-19-000-devices-after-security-breach) _(Thema: hack)_
