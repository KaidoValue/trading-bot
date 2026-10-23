# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **23.10.2026 19:17** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert.
- **2️⃣ KI-Bot (lernend, Daytrading):** Lernende KI: gewichtet 9 Strategien nach ihrem Erfolg der letzten Wochen. Handelt auf 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, Daytrading)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 1'000.00 CHF | 1'000.00 CHF | 1'000.00 CHF |
| **Kapital jetzt** | **998.37 CHF** | **1'000.12 CHF** | **956.83 CHF** |
| Gewinn / Verlust | 🔴 -1.63 CHF (-0.16 %) | 🟢 +0.12 CHF (+0.01 %) | 🔴 -43.17 CHF (-4.32 %) |
| Im Einsatz (investiert) | 413.42 CHF (41 %) | 502.97 CHF (50 %) | 8'950.97 CHF (935 %) |
| Cash (nicht investiert) | 584.96 CHF | 497.15 CHF | -1'993.62 CHF |
| Offene Positionen | 5 | 2 | 6 |
| Abgeschlossene Trades | 0 | 0 | 0 |
| Strategie | regime, 1d-Kerzen | adaptive, 1h-Kerzen | breakout, 30m-Kerzen |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.00 CHF) |

## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 67'434.10 CHF | 🟢 +1.19 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'988.76 CHF | 🟢 +1.87 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 616.52 CHF | 🟢 +2.20 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.08 CHF | 🟢 +0.21 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 86.37 CHF | 🟢 +0.99 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.27 CHF | 🟢 +0.33 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'033.25 CHF | 🟢 +2.61 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 64.88 CHF | 🟢 +1.56 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Hält Coins über Wochen bis Monate, solange der Kurs über der 200-Tage-Linie liegt. Wenige Trades, max. 50 % investiert._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long | 23.10.2026 18:09 | 67'388.78 | 67'434.10 | 0.001485 | 100.05 CHF | 100.12 CHF | 🟢 +0.07 CHF (+0.07 %) | 53'251.84 (-21 %) |
| **ETH** long | 23.10.2026 18:09 | 1'986.19 | 1'988.76 | 0.040710 | 80.86 CHF | 80.96 CHF | 🟢 +0.10 CHF (+0.13 %) | 1'371.11 (-31 %) |
| **BNB** long | 23.10.2026 19:15 | 617.14 | 616.52 | 0.162070 | 100.02 CHF | 99.92 CHF | 🔴 -0.10 CHF (-0.10 %) | 483.48 (-22 %) |
| **XRP** long | 23.10.2026 19:15 | 1.08 | 1.08 | 58.690975 | 63.53 CHF | 63.51 CHF | 🔴 -0.02 CHF (-0.03 %) | 0.66 (-39 %) |
| **SOL** long | 23.10.2026 19:15 | 86.38 | 86.37 | 0.797780 | 68.91 CHF | 68.91 CHF | 🔴 -0.00 CHF (-0.00 %) | 55.00 (-36 %) |

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

**Letzte Entscheidung:** BTC/CHF: Position offen, Signal bestätigt · ETH/CHF: Position offen, Signal bestätigt · BNB/CHF: gekauft 0.162070 @ 617.14 · XRP/CHF: gekauft 58.690975 @ 1.08 · SOL/CHF: gekauft 0.797780 @ 86.38 · TRX/CHF: kein Signal · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

## 2️⃣ KI-Bot (lernend, Daytrading)

_Lernende KI: gewichtet 9 Strategien nach ihrem Erfolg der letzten Wochen. Handelt auf 1-Stunden-Kerzen, Positionen meist Stunden bis 1–2 Tage._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BNB** long | 23.10.2026 18:10 | 617.52 | 616.52 | 0.405049 | 250.12 CHF | 249.72 CHF | 🔴 -0.40 CHF (-0.16 %) | 611.14 (-1 %) |
| **ZEC** long | 23.10.2026 18:10 | 1'020.51 | 1'033.25 | 0.245099 | 250.12 CHF | 253.25 CHF | 🟢 +3.12 CHF (+1.25 %) | 982.27 (-5 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash |

**Letzte Entscheidung:** BTC/CHF: Signal 'raus', bleibe in Cash · ETH/CHF: Signal 'raus', bleibe in Cash · BNB/CHF: Position offen, Signal bestätigt · XRP/CHF: Signal 'raus', bleibe in Cash · SOL/CHF: Signal 'raus', bleibe in Cash · TRX/CHF: Signal 'raus', bleibe in Cash · ZEC/CHF: Position offen, Signal bestätigt · HYPE/CHF: Signal 'raus', bleibe in Cash

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Sehr risikofreudig: viele Trades alle 30 Minuten, setzt auch auf fallende Kurse (Short), 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** short | 23.10.2026 19:16 | 67'400.38 | 67'434.10 | 0.022244 | 1'499.25 CHF | 1'500.00 CHF | 🔴 -0.75 CHF (-0.05 %) | 67'771.70 (+1 %) |
| **ETH** long | 23.10.2026 19:16 | 1'989.75 | 1'988.76 | 0.754239 | 1'500.75 CHF | 1'500.00 CHF | 🔴 -0.75 CHF (-0.05 %) | 1'978.49 (-1 %) |
| **BNB** long | 23.10.2026 19:16 | 616.80 | 616.52 | 2.433107 | 1'500.75 CHF | 1'500.05 CHF | 🔴 -0.70 CHF (-0.05 %) | 613.21 (-1 %) |
| **XRP** short | 23.10.2026 19:16 | 1.08 | 1.08 | 1386.400937 | 1'499.25 CHF | 1'500.26 CHF | 🔴 -1.01 CHF (-0.07 %) | 1.09 (+1 %) |
| **SOL** long | 23.10.2026 19:16 | 86.41 | 86.37 | 17.368464 | 1'500.75 CHF | 1'500.20 CHF | 🔴 -0.55 CHF (-0.04 %) | 85.60 (-1 %) |
| **TRX** long | 23.10.2026 19:16 | 0.27 | 0.27 | 5332.381943 | 1'451.12 CHF | 1'450.46 CHF | 🔴 -0.66 CHF (-0.05 %) | 0.27 (-0 %) |

**Signale jetzt**

| Coin | Signal |
|---|---|
| BTC | 🔴 raus / Cash |
| ETH | 🟢 investiert sein |
| BNB | 🟢 investiert sein |
| XRP | 🔴 raus / Cash |
| SOL | 🟢 investiert sein |
| TRX | 🟢 investiert sein |
| ZEC | 🟢 investiert sein |
| HYPE | 🟢 investiert sein |

**Letzte Entscheidung:** BTC/CHF: short eröffnet 0.022244 @ 67400.38 · ETH/CHF: gekauft 0.754239 @ 1989.75 · BNB/CHF: gekauft 2.433107 @ 616.80 · XRP/CHF: short eröffnet 1386.400937 @ 1.08 · SOL/CHF: gekauft 17.368464 @ 86.41 · TRX/CHF: gekauft 5332.381943 @ 0.27 · ZEC/CHF: kein Einstieg (max. offene Positionen) · HYPE/CHF: kein Einstieg (max. offene Positionen)

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
