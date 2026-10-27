# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **27.10.2026 07:26** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **987.39 CHF** | **947.48 CHF** | **498.19 CHF** |
| Gewinn / Verlust | 🔴 -12.61 CHF (-1.26 %) | 🔴 -52.52 CHF (-5.25 %) | 🔴 -501.81 CHF (-50.18 %) |
| Im Einsatz (investiert) | 402.44 CHF (41 %) | 238.44 CHF (25 %) | 1'466.65 CHF (294 %) |
| Cash (nicht investiert) | 584.96 CHF | 709.04 CHF | 1'964.83 CHF |
| Offene Positionen | 5 | 1 | 6 |
| Abgeschlossene Trades | 0 | 12 | 114 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 7.07 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **971.45 CHF** |
| Gewinn / Verlust | 🔴 -28.55 CHF (-2.85 %) |
| **Aktuelle Verteilung** | Langfrist 48 % · KI 16 % · Risiko 1 % · Cash 35 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, ruhig |
| Letzte Begründung | Marktphase «Aufwärtstrend, ruhig», Einschätzung: Langfrist -0.4 %, KI -3.5 %, Risiko -52.8 %, 🚨 Notbremse Risiko (-9.6 % in 3 Std.) |
| Umschicht-Gebühren bisher | 2.15 CHF |
| Erfahrung im Gedächtnis | 183 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.002 %/Lauf, KI -0.012 %/Lauf, Risiko -0.500 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 65'847.80 CHF | 🔴 -0.60 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'901.72 CHF | 🔴 -0.72 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 607.92 CHF | 🔴 -0.93 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.07 CHF | 🔴 -0.85 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 82.50 CHF | 🔴 -1.05 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🔴 -0.19 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'004.04 CHF | 🔴 -1.43 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 64.07 CHF | 🔴 -1.01 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 65'847.80 | 0.001485 | 100.05 CHF | 97.76 CHF | 🔴 -2.29 CHF (-2.29 %) | 53'251.84 (-19 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'901.72 | 0.040710 | 80.86 CHF | 77.42 CHF | 🔴 -3.44 CHF (-4.25 %) | 1'371.11 (-28 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 607.92 | 0.162070 | 100.02 CHF | 98.53 CHF | 🔴 -1.49 CHF (-1.49 %) | 483.48 (-20 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.07 | 58.690975 | 63.53 CHF | 62.91 CHF | 🔴 -0.62 CHF (-0.97 %) | 0.66 (-39 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 82.50 | 0.797780 | 68.91 CHF | 65.82 CHF | 🔴 -3.09 CHF (-4.49 %) | 55.00 (-33 %) |

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
| **ZEC** long | 26.10.2026 10:10 | 1'006.92 | 1'004.04 | 0.237480 | 239.12 CHF | 238.44 CHF | 🔴 -0.68 CHF (-0.29 %) | 973.10 (-3 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 20'582 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.009 %/Kerze), labor_4 (-0.011 %/Kerze) |
| BNB | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_3 (+0.004 %/Kerze), labor_4 (+0.003 %/Kerze) |
| XRP | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.009 %/Kerze), labor_4 (-0.011 %/Kerze) |
| TRX | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.005 %/Kerze) |
| ZEC | Aufwärtstrend, ruhig | trend (+0.059 %/Kerze), momentum (+0.028 %/Kerze), reversal (+0.028 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.071 %/Kerze), momentum (+0.065 %/Kerze), reversal (+0.055 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: verbot, Wert -0.8) · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: Signal 'raus', bleibe in Cash · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Signal 'raus', bleibe in Cash · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: verbot, Wert -0.8)

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
| **ETH** short | 26.10.2026 16:17 | 1'924.05 | 1'901.72 | 0.141196 | 271.67 CHF | 268.51 CHF | 🟢 +3.15 CHF (+1.16 %) | 1'937.43 (+2 %) |
| **SOL** short | 26.10.2026 21:19 | 82.87 | 82.50 | 0.875427 | 72.54 CHF | 72.22 CHF | 🟢 +0.32 CHF (+0.44 %) | 83.66 (+1 %) |
| **TRX** short | 27.10.2026 01:52 | 0.27 | 0.27 | 942.078499 | 256.24 CHF | 255.83 CHF | 🟢 +0.41 CHF (+0.16 %) | 0.27 (+0 %) |
| **HYPE** short | 27.10.2026 01:52 | 65.05 | 64.07 | 3.939016 | 256.24 CHF | 252.38 CHF | 🟢 +3.85 CHF (+1.50 %) | 65.86 (+3 %) |
| **ZEC** short | 27.10.2026 03:52 | 1'011.80 | 1'004.04 | 0.550923 | 557.42 CHF | 553.15 CHF | 🟢 +4.27 CHF (+0.77 %) | 1'028.00 (+2 %) |
| **BTC** short | 27.10.2026 06:55 | 66'070.45 | 65'847.80 | 0.000980 | 64.77 CHF | 64.55 CHF | 🟢 +0.22 CHF (+0.34 %) | 66'336.38 (+1 %) |

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

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: kein Einstieg (max. offene Positionen) · XRP/CHF: kein Einstieg (max. offene Positionen) · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: Position offen, Signal bestätigt

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BTC short | 27.10.2026 04:22 | 27.10.2026 06:55 | 65'754.41 | 66'136.55 | 🔴 -0.56 CHF | Stop-Loss (Gap) |
| XRP long | 27.10.2026 01:22 | 27.10.2026 04:22 | 1.08 | 1.07 | 🔴 -4.06 CHF | Stop-Loss (Gap) |
| ZEC long | 26.10.2026 13:14 | 27.10.2026 03:52 | 1'015.64 | 1'011.80 | 🔴 -2.66 CHF | Signal |
| BNB short | 26.10.2026 22:19 | 27.10.2026 01:52 | 611.75 | 615.46 | 🔴 -0.18 CHF | Signal |
| BTC short | 27.10.2026 00:52 | 27.10.2026 01:52 | 66'143.71 | 66'345.66 | 🔴 -1.46 CHF | Signal |
| TRX short | 26.10.2026 20:19 | 27.10.2026 01:22 | 0.27 | 0.27 | 🔴 -0.61 CHF | Take-Profit |
| XRP short | 26.10.2026 22:19 | 27.10.2026 00:52 | 1.06 | 1.08 | 🔴 -6.82 CHF | Stop-Loss (Gap) |
| XRP long | 26.10.2026 16:17 | 26.10.2026 22:19 | 1.07 | 1.06 | 🔴 -5.52 CHF | Signal |
| BNB long | 26.10.2026 16:46 | 26.10.2026 22:19 | 616.17 | 611.75 | 🔴 -3.18 CHF | Signal |
| BTC long | 26.10.2026 17:17 | 26.10.2026 21:19 | 66'377.77 | 65'976.80 | 🔴 -0.88 CHF | Signal |

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
- **Bewertung News:** -0.80 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** verbot (gemeldet von coindesk, decrypt – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-10-26 22:16 UTC · **decrypt** · [Canada’s Draft Stablecoin Rules Cap Redemption Fees at 1% and Ban Yield](https://decrypt.co/381889/canada-draft-stablecoin-rules-redemption-fees-ban-yield) _(Thema: verbot)_
- 2026-10-26 14:23 UTC · **coindesk** · [Canada opens consultation on draft stablecoin rules, maintains ban on yields](https://www.coindesk.com/policy/2026/10/26/canada-opens-consultation-on-draft-stablecoin-rules-maintains-ban-on-yields) _(Thema: verbot)_
