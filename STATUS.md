# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **23.10.2026 23:20** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 1'000 CHF selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **996.47 CHF** | **990.39 CHF** | **940.76 CHF** |
| Gewinn / Verlust | 🔴 -3.53 CHF (-0.35 %) | 🔴 -9.61 CHF (-0.96 %) | 🔴 -59.24 CHF (-5.92 %) |
| Im Einsatz (investiert) | 411.52 CHF (41 %) | 747.37 CHF (75 %) | 4'005.95 CHF (426 %) |
| Cash (nicht investiert) | 584.96 CHF | 243.02 CHF | 4'045.95 CHF |
| Offene Positionen | 5 | 3 | 6 |
| Abgeschlossene Trades | 0 | 1 | 5 |
| Strategie | regime, 1d-Kerzen | adaptive_memory, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.40 CHF) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), mindestens 10 % Cash, nach mehr als 10 % Verlust Risiko-Anteil halbiert, Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 1'000.00 CHF |
| **Kapital jetzt** | **995.08 CHF** |
| Gewinn / Verlust | 🔴 -4.92 CHF (-0.49 %) |
| **Aktuelle Verteilung** | Langfrist 49 % · KI 23 % · Risiko 1 % · Cash 27 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist -0.1 %, KI -0.8 %, Risiko -6.6 %, 🚨 Notbremse Risiko (-3.1 % in 3 Std.) |
| Umschicht-Gebühren bisher | 0.37 CHF |
| Erfahrung im Gedächtnis | 6 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist -0.007 %/Lauf, KI -0.092 %/Lauf, Risiko -0.606 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'200.70 CHF | 🟢 +0.84 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'982.11 CHF | 🟢 +1.53 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 612.21 CHF | 🟢 +1.50 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.08 CHF | 🟢 +0.01 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 85.82 CHF | 🟢 +0.37 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🟢 +0.50 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'017.34 CHF | 🟢 +1.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 64.17 CHF | 🟢 +0.48 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 67'200.70 | 0.001485 | 100.05 CHF | 99.77 CHF | 🔴 -0.28 CHF (-0.28 %) | 53'251.84 (-21 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'982.11 | 0.040710 | 80.86 CHF | 80.69 CHF | 🔴 -0.17 CHF (-0.21 %) | 1'371.11 (-31 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 612.21 | 0.162070 | 100.02 CHF | 99.22 CHF | 🔴 -0.80 CHF (-0.80 %) | 483.48 (-21 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.08 | 58.690975 | 63.53 CHF | 63.37 CHF | 🔴 -0.16 CHF (-0.25 %) | 0.66 (-39 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 85.82 | 0.797780 | 68.91 CHF | 68.46 CHF | 🔴 -0.44 CHF (-0.64 %) | 55.00 (-36 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🟢 investiert sein |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🟢 investiert sein |
| SOL | 🟢 investiert sein |
| TRX | ⚪ neutral |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: kein Signal · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

## 2️⃣ KI-Bot (lernend, Daytrading)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, und vergisst nichts. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **ZEC** long | 23.10.2026 18:10 | 1'020.51 | 1'017.34 | 0.245099 | 250.12 CHF | 249.35 CHF | 🔴 -0.78 CHF (-0.31 %) | 982.27 (-3 %) |
| **TRX** long | 23.10.2026 20:16 | 0.27 | 0.27 | 918.327343 | 250.05 CHF | 250.17 CHF | 🟢 +0.12 CHF (+0.05 %) | 0.27 (-0 %) |
| **XRP** long | 23.10.2026 23:16 | 1.08 | 1.08 | 229.549349 | 248.00 CHF | 247.85 CHF | 🔴 -0.16 CHF (-0.06 %) | 1.06 (-1 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash |
| XRP | 🟢 investiert sein |
| SOL | 🔴 raus / Cash |
| TRX | 🟢 investiert sein |
| ZEC | ⚪ neutral |
| HYPE | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 19'934 Kerzen Erfahrung (wächst bei jedem Lauf)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| BNB | Seitwärts, wild | mean_reversion (+0.033 %/Kerze), labor_1 (+0.006 %/Kerze), labor_2 (+0.006 %/Kerze) |
| XRP | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |
| TRX | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| ZEC | Seitwärts, ruhig | mean_reversion (+0.014 %/Kerze), labor_4 (+0.003 %/Kerze), labor_3 (+0.002 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (-0.008 %/Kerze), pullback (-0.010 %/Kerze), labor_4 (-0.011 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 4 (labor_3, labor_4, labor_2, labor_1), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** BTC/CHF: Signal 'raus', bleibe in Cash · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: Signal 'raus', bleibe in Cash · XRP/CHF: gekauft 229.549349 @ 1.08 · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Signal · HYPE/CHF: Signal 'raus', bleibe in Cash

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| BNB long | 23.10.2026 18:10 | 23.10.2026 21:16 | 617.52 | 611.79 | 🔴 -3.61 CHF | Signal |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** short | 23.10.2026 19:46 | 67'307.53 | 67'200.70 | 0.007573 | 509.75 CHF | 508.94 CHF | 🟢 +0.81 CHF (+0.16 %) | 67'668.15 (+1 %) |
| **XRP** short | 23.10.2026 19:46 | 1.08 | 1.08 | 471.664724 | 509.75 CHF | 509.26 CHF | 🟢 +0.48 CHF (+0.09 %) | 1.09 (+1 %) |
| **TRX** long | 23.10.2026 19:46 | 0.27 | 0.27 | 1653.266901 | 449.97 CHF | 450.38 CHF | 🟢 +0.41 CHF (+0.09 %) | 0.27 (-0 %) |
| **BNB** short | 23.10.2026 21:16 | 612.08 | 612.21 | 0.690998 | 422.95 CHF | 423.04 CHF | 🔴 -0.09 CHF (-0.02 %) | 615.33 (+1 %) |
| **SOL** short | 23.10.2026 21:16 | 85.65 | 85.82 | 8.655636 | 741.33 CHF | 742.82 CHF | 🔴 -1.49 CHF (-0.20 %) | 86.35 (+1 %) |
| **ETH** short | 23.10.2026 21:46 | 1'976.10 | 1'982.11 | 0.691944 | 1'367.35 CHF | 1'371.51 CHF | 🔴 -4.16 CHF (-0.30 %) | 1'985.82 (+0 %) |

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

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Position offen, Signal bestätigt · SOL/CHF: Position offen, Signal bestätigt · TRX/CHF: Position offen, Signal bestätigt · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| ETH long | 23.10.2026 21:16 | 23.10.2026 21:46 | 1'978.08 | 1'976.10 | 🔴 -1.77 CHF | Signal |
| SOL long | 23.10.2026 19:46 | 23.10.2026 21:16 | 86.26 | 85.65 | 🔴 -6.25 CHF | Signal |
| ZEC long | 23.10.2026 20:17 | 23.10.2026 21:16 | 1'035.29 | 1'013.39 | 🔴 -12.19 CHF | Stop-Loss (Gap) |
| ETH long | 23.10.2026 19:46 | 23.10.2026 21:16 | 1'989.75 | 1'976.10 | 🔴 -4.82 CHF | Stop-Loss (Gap) |
| BNB long | 23.10.2026 19:46 | 23.10.2026 20:17 | 615.23 | 614.18 | 🔴 -3.52 CHF | Signal |

## Charts

▲ grün = Kauf, ▼ rot = Verkauf, rote Linie = Stop-Loss, orange = 200-Tage-Linie. Die Bilder zeigen den Stand der letzten Aktualisierung; für den Live-Kurs auf «Live-Chart» klicken.

### BTC/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF)

![BTC/CHF](daten/charts/BTC-CHF.png)

### ETH/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF)

![ETH/CHF](daten/charts/ETH-CHF.png)

### BNB/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD)

![BNB/CHF](daten/charts/BNB-CHF.png)

### XRP/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD)

![XRP/CHF](daten/charts/XRP-CHF.png)

### SOL/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD)

![SOL/CHF](daten/charts/SOL-CHF.png)

### TRX/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD)

![TRX/CHF](daten/charts/TRX-CHF.png)

### ZEC/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD)

![ZEC/CHF](daten/charts/ZEC-CHF.png)

### HYPE/CHF · [Live-Chart](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD)

![HYPE/CHF](daten/charts/HYPE-CHF.png)

## Nachrichtenlage

- **Stimmung (Fear & Greed):** 50 von 100, neutral
- **Bewertung News:** -0.30 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** klage (gemeldet von bitcoinmagazine, cointelegraph – nur Hinweis, blockiert nicht)

**Schlagzeilen dazu:**

- 2026-10-22 21:39 UTC · **cointelegraph** · [Circle shareholder sues Trump, World Liberty and Steve Witkoff over crypto deals](https://cointelegraph.com/news/circle-shareholder-lawsuit-donald-trump-world-liberty-financial-steve-witkoff-crypto-corruption?utm_source=rss_feed&utm_medium=rss&utm_campaign=rss_partner_inbound) _(Thema: klage)_
- 2026-10-22 21:23 UTC · **bitcoinmagazine** · [Circle Shareholder Sues Trump, Alleging Unconstitutional Profits From $2B UAE Crypto Deals](https://bitcoinmagazine.com/news/trump-sued-for-alleged-crypto-corruption) _(Thema: klage)_
