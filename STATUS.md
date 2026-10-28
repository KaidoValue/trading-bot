# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **28.10.2026 05:41** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **996.49 CHF** | **960.85 CHF** | **429.88 CHF** |
| Gewinn / Verlust | 🔴 -3.51 CHF (-0.35 %) | 🔴 -39.15 CHF (-3.91 %) | 🔴 -570.12 CHF (-57.01 %) |
| Im Einsatz (investiert) | 411.53 CHF (41 %) | 486.18 CHF (51 %) | 1'290.35 CHF (300 %) |
| Cash (nicht investiert) | 584.96 CHF | 474.67 CHF | -860.46 CHF |
| Offene Positionen | 5 | 2 | 6 |
| Abgeschlossene Trades | 0 | 14 | 147 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 7.82 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **976.10 CHF** |
| Gewinn / Verlust | 🔴 -23.90 CHF (-2.39 %) |
| **Aktuelle Verteilung** | Langfrist 53 % · KI 21 % · Risiko 1 % · Cash 25 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist +0.6 %, KI -1.5 %, Risiko -77.5 % |
| Umschicht-Gebühren bisher | 2.40 CHF |
| Erfahrung im Gedächtnis | 232 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.007 %/Lauf, KI +0.005 %/Lauf, Risiko -0.416 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'110.40 CHF | 🟢 +0.38 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'952.33 CHF | 🟢 +0.58 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 618.39 CHF | 🟢 +0.26 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.10 CHF | 🔴 -0.02 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 84.60 CHF | 🟢 +0.78 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.13 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'094.09 CHF | 🟢 +0.86 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 67.49 CHF | 🟢 +0.23 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 67'110.40 | 0.001485 | 100.05 CHF | 99.64 CHF | 🔴 -0.41 CHF (-0.41 %) | 53'251.84 (-21 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'952.33 | 0.040710 | 80.86 CHF | 79.48 CHF | 🔴 -1.38 CHF (-1.70 %) | 1'371.11 (-30 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 618.39 | 0.162070 | 100.02 CHF | 100.22 CHF | 🟢 +0.20 CHF (+0.20 %) | 483.48 (-22 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.10 | 58.690975 | 63.53 CHF | 64.70 CHF | 🟢 +1.17 CHF (+1.84 %) | 0.66 (-40 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 84.60 | 0.797780 | 68.91 CHF | 67.50 CHF | 🔴 -1.41 CHF (-2.05 %) | 55.00 (-35 %) |

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
| **BTC** long | 27.10.2026 16:00 | 66'509.84 | 67'110.40 | 0.003616 | 240.50 CHF | 242.67 CHF | 🟢 +2.17 CHF (+0.90 %) | 65'856.81 (-2 %) |
| **ETH** long | 27.10.2026 16:00 | 1'928.15 | 1'952.33 | 0.124729 | 240.50 CHF | 243.51 CHF | 🟢 +3.02 CHF (+1.25 %) | 1'908.65 (-2 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | ⚪ neutral |
| BNB | 🟢 investiert sein |
| XRP | 🟢 investiert sein |
| SOL | 🟢 investiert sein |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 20'758 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| ETH | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| BNB | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| XRP | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| SOL | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.034 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |
| HYPE | Aufwärtstrend, ruhig | trend (+0.062 %/Kerze), reversal (+0.031 %/Kerze), momentum (+0.030 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: kein Signal · BNB/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · XRP/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · SOL/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · TRX/CHF: Signal 'raus', bleibe in Cash · ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0) · HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,rally, Wert -1.0)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long | 27.10.2026 18:00 | 28.10.2026 01:06 | 622.33 | 614.56 | 🔴 -4.25 CHF | Stop-Loss (Gap) |
| ZEC long | 26.10.2026 10:10 | 27.10.2026 17:30 | 1'006.92 | 1'072.51 | 🟢 +14.25 CHF | Take-Profit |
| BTC long | 26.10.2026 10:10 | 26.10.2026 15:16 | 66'289.23 | 66'013.88 | 🔴 -1.61 CHF | Signal |
| ETH long | 26.10.2026 13:13 | 26.10.2026 14:13 | 1'930.96 | 1'911.28 | 🔴 -3.05 CHF | Signal |
| TRX long | 23.10.2026 20:16 | 26.10.2026 11:13 | 0.27 | 0.27 | 🔴 -0.31 CHF | Signal |
| BTC long | 26.10.2026 00:04 | 26.10.2026 00:34 | 66'419.29 | 65'838.16 | 🔴 -2.72 CHF | Stop-Loss (Gap) |
| ZEC long | 25.10.2026 06:23 | 25.10.2026 07:26 | 1'003.77 | 993.72 | 🔴 -3.67 CHF | Signal |
| BNB long | 25.10.2026 06:23 | 25.10.2026 07:26 | 616.82 | 613.83 | 🔴 -2.42 CHF | Signal |
| BTC long | 25.10.2026 05:23 | 25.10.2026 06:23 | 66'685.23 | 66'692.94 | 🔴 -0.60 CHF | Signal |
| BNB long | 24.10.2026 22:17 | 25.10.2026 05:53 | 604.10 | 615.07 | 🟢 +3.12 CHF | Take-Profit |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **SOL** long | 27.10.2026 17:31 | 83.71 | 84.60 | 2.822954 | 236.32 CHF | 238.83 CHF | 🟢 +2.51 CHF (+1.06 %) | 83.02 (-2 %) |
| **ZEC** long | 27.10.2026 20:04 | 1'076.47 | 1'094.09 | 0.170086 | 183.09 CHF | 186.09 CHF | 🟢 +3.00 CHF (+1.64 %) | 1'058.55 (-3 %) |
| **HYPE** long | 27.10.2026 20:34 | 67.37 | 67.49 | 3.342198 | 225.18 CHF | 225.55 CHF | 🟢 +0.38 CHF (+0.17 %) | 66.63 (-1 %) |
| **ETH** long | 28.10.2026 04:40 | 1'958.99 | 1'952.33 | 0.114031 | 223.39 CHF | 222.63 CHF | 🔴 -0.76 CHF (-0.34 %) | 1'951.18 (-0 %) |
| **XRP** long | 28.10.2026 04:40 | 1.11 | 1.10 | 201.269157 | 223.39 CHF | 221.87 CHF | 🔴 -1.52 CHF (-0.68 %) | 1.10 (-0 %) |
| **BNB** long | 28.10.2026 05:10 | 618.50 | 618.39 | 0.315947 | 195.41 CHF | 195.38 CHF | 🔴 -0.04 CHF (-0.02 %) | 615.54 (-0 %) |

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

**Letzte Entscheidung:** BTC/CHF: kein Einstieg (max. offene Positionen) · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: kein Einstieg (max. offene Positionen) · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: Position offen, Signal bestätigt

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BTC short | 28.10.2026 03:07 | 28.10.2026 05:10 | 66'995.79 | 67'228.20 | 🔴 -1.33 CHF | Signal |
| BNB short | 28.10.2026 03:40 | 28.10.2026 04:40 | 616.41 | 619.41 | 🔴 -2.26 CHF | Signal |
| TRX long | 27.10.2026 22:34 | 28.10.2026 04:10 | 0.27 | 0.27 | 🔴 -1.65 CHF | Signal |
| ETH short | 27.10.2026 22:34 | 28.10.2026 03:40 | 1'953.83 | 1'958.99 | 🔴 -1.21 CHF | Signal |
| BTC short | 28.10.2026 02:37 | 28.10.2026 03:07 | 66'759.80 | 67'062.81 | 🔴 -1.62 CHF | Stop-Loss (Gap) |
| BNB short | 28.10.2026 01:37 | 28.10.2026 02:37 | 613.83 | 617.68 | 🔴 -2.62 CHF | Stop-Loss (Gap) |
| BTC long | 27.10.2026 17:01 | 28.10.2026 01:37 | 66'733.35 | 66'758.30 | 🔴 -0.53 CHF | Signal |
| XRP long | 27.10.2026 15:31 | 27.10.2026 22:34 | 1.09 | 1.10 | 🟢 +0.09 CHF | Signal |
| ETH short | 27.10.2026 21:34 | 27.10.2026 22:34 | 1'941.93 | 1'955.79 | 🔴 -2.19 CHF | Stop-Loss (Gap) |
| TRX long | 27.10.2026 20:04 | 27.10.2026 21:34 | 0.27 | 0.27 | 🔴 -0.38 CHF | Take-Profit |

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

- 2026-10-27 18:16 UTC · **decrypt** · [Bitcoin Wallet Maker Keystone Pulls Devices as Stolen Key Opens Door to Fakes](https://decrypt.co/381983/bitcoin-wallet-keystone-devices-destroyed-stolen-key) _(Thema: hack)_
- 2026-10-27 12:18 UTC · **cointelegraph** · [Bitcoin price analysis sees ‘strong rally’ as old coins become dormant](https://cointelegraph.com/markets/bitcoin-price-analysis-sees-strong-rally-as-old-coins-become-dormant?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: rally)_
- 2026-10-27 11:40 UTC · **coindesk** · [Live updates: Bitcoin edges higher as Nasdaq surges 1.2%](https://www.coindesk.com/tech/2026/10/27/live-updates-bitcoin-holds-below-usd80-000-as-ai-buildout-draws-more-capital) _(Thema: rally)_
- 2026-10-27 11:32 UTC · **coindesk** · [Bitcoin drops below $80,000 as crypto ignores Asian tech rally, Fed meeting begins](https://www.coindesk.com/markets/2026/10/27/bitcoin-drops-below-usd80-000-as-crypto-ignores-asian-tech-rally-fed-meeting-begins) _(Thema: rally)_
- 2026-10-27 11:13 UTC · **coindesk** · [Crypto wallet maker Keystone to destroy almost 19,000 devices after security breach](https://www.coindesk.com/business/2026/10/27/crypto-wallet-maker-keystone-to-destroy-almost-19-000-devices-after-security-breach) _(Thema: hack)_
