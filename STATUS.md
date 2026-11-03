# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **03.11.2026 04:35** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 100.00 CHF Startkapital selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 100.00 CHF | 100.00 CHF | 100.00 CHF |
| **Kapital jetzt** | **100.00 CHF** | **100.00 CHF** | **98.97 CHF** |
| Gewinn / Verlust | ⚪ +0.00 CHF (+0.00 %) | ⚪ +0.00 CHF (+0.00 %) | 🔴 -1.03 CHF (-1.03 %) |
| Im Einsatz (investiert) | 0.00 CHF (0 %) | 0.00 CHF (0 %) | 111.84 CHF (113 %) |
| Cash (nicht investiert) | 100.00 CHF | 100.00 CHF | -12.87 CHF |
| Offene Positionen | 0 | 0 | 5 |
| Abgeschlossene Trades | 0 | 0 | 0 |
| Gebühren bisher | 0.00 CHF | 0.00 CHF | 0.90 CHF |
| Gebührenstufe | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 0 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 0 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 112 CHF) |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 20 % · mittel 30 % · lang 50 % | mittel 50 % · lang 50 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.01 CHF) |
| Hebel aktuell | – | – | 1.13× (erlaubt 3×) |
| Buchhaltung | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) |
| Letzter Durchlauf | 03.11.2026 04:33 (vor 2 Min.) | 03.11.2026 04:33 (vor 1 Min.) | 03.11.2026 04:34 (vor 1 Min.) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 100.00 CHF |
| **Kapital jetzt** | **99.79 CHF** |
| Gewinn / Verlust | 🔴 -0.21 CHF (-0.21 %) |
| **Aktuelle Verteilung** | Langfrist 30 % · KI 30 % · Risiko 20 % · Cash 20 % |
| Marktphase (BTC, Tageskerzen) | Seitwärts, wild |
| Letzte Begründung | Paper-Neustart mit 100.00 CHF am 2026-11-02T19:38:40.499488+00:00 |
| Umschicht-Gebühren bisher | 0.00 CHF |
| Erfahrung im Gedächtnis | 17 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Langfrist +0.000 %/Lauf, KI +0.000 %/Lauf, Risiko -0.019 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 63'007.80 CHF | 🟢 +0.47 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'841.58 CHF | 🟢 +0.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 569.24 CHF | 🔴 -0.55 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.02 CHF | 🔴 -0.11 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 75.14 CHF | 🔴 -0.20 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.26 CHF | 🟢 +0.60 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 928.37 CHF | 🔴 -0.08 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 67.88 CHF | 🔴 -1.38 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

Keine offene Position, alles in Cash.

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| ETH | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| XRP | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |

**Letzte Entscheidung:** [lang] BTC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,insolvenz, Wert -1.0) · [lang] ETH/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,insolvenz, Wert -1.0) · [lang] BNB/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,insolvenz, Wert -1.0) · [lang] XRP/CHF: kein Signal · [lang] SOL/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,insolvenz, Wert -1.0) · [lang] TRX/CHF: kein Signal · [lang] ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,insolvenz, Wert -1.0) · [lang] HYPE/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack,insolvenz, Wert -1.0) · [mittel] BTC/CHF: Signal 'raus', bleibe in Cash · [mittel] ETH/CHF: Signal 'raus', bleibe in Cash · [mittel] BNB/CHF: Signal 'raus', bleibe in Cash · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Signal 'raus', bleibe in Cash · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: Signal 'raus', bleibe in Cash · [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

## 2️⃣ KI-Bot (lernend, kurz bis lang)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe._

Keine offene Position, alles in Cash.

**Signale jetzt**

| Coin | kurz (1h) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| ZEC | 🔴 raus / Cash | 🔴 raus / Cash | ⚪ neutral |
| HYPE | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 2'698 Kerzen Erfahrung (zeitlich gewichtete Kerzen; ältere Erfahrung zählt weniger)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ETH | Seitwärts, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| BNB | Abwärtstrend, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| XRP | Seitwärts, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| SOL | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| TRX | Abwärtstrend, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ZEC | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 0 (noch keine hat die Prüfung bestanden), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 02.11.2026 21:04 | 62'905.40 | 63'007.80 | 0.000523 | 32.87 CHF | 32.93 CHF | 🟢 +0.05 CHF (+0.16 %) | 53'337.04 (-15 %) |
| **ETH** long (lang) | 02.11.2026 21:04 | 1'843.99 | 1'841.58 | 0.012649 | 23.33 CHF | 23.29 CHF | 🔴 -0.03 CHF (-0.13 %) | 1'449.18 (-21 %) |
| **BNB** long (lang) | 02.11.2026 21:04 | 570.38 | 569.24 | 0.041690 | 23.78 CHF | 23.73 CHF | 🔴 -0.05 CHF (-0.20 %) | 450.90 (-21 %) |
| **SOL** long (lang) | 02.11.2026 21:04 | 75.10 | 75.14 | 0.233083 | 17.50 CHF | 17.51 CHF | 🟢 +0.01 CHF (+0.05 %) | 53.80 (-28 %) |
| **HYPE** long (lang) | 02.11.2026 21:04 | 68.38 | 67.88 | 0.211733 | 14.48 CHF | 14.37 CHF | 🔴 -0.11 CHF (-0.73 %) | 44.97 (-34 %) |

**Signale jetzt**

| Coin | mittel (4h) | lang (1d) |
|---|---|---|
| BTC | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🔴 raus / Cash | 🟢 investiert sein |
| BNB | 🔴 raus / Cash | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | ⚪ neutral |
| SOL | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🔴 raus / Cash | ⚪ neutral |
| ZEC | 🔴 raus / Cash | 🟢 investiert sein |
| HYPE | 🟢 investiert sein | 🟢 investiert sein |

**Letzte Entscheidung:** [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: Position gehört zum Horizont «lang» · [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: Position offen, Signal bestätigt · [lang] BNB/CHF: Position offen, Signal bestätigt · [lang] XRP/CHF: kein Signal · [lang] SOL/CHF: Position offen, Signal bestätigt · [lang] TRX/CHF: kein Signal · [lang] ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] HYPE/CHF: Position offen, Signal bestätigt

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

- **Stimmung (Fear & Greed):** 26 von 100, Angst
- **Bewertung News:** -1.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** hack (gemeldet von bitcoinmagazine, coindesk, decrypt – blockiert Käufe); insolvenz (gemeldet von coindesk, decrypt – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-11-02 21:16 UTC · **decrypt** · [Mystery $106 Million Crypto Theft Hits EU Entity Days After Binance Hack](https://decrypt.co/382383/mystery-106-million-crypto-theft-eu-entity-binance-hack) _(Thema: hack)_
- 2026-11-02 18:46 UTC · **decrypt** · [North Korea Is Laundering Binance Hack Loot at One New Wallet Every 25 Seconds](https://decrypt.co/382355/north-korea-laundering-binance-hack-loot-new-wallet-every-25-seconds) _(Thema: hack)_
- 2026-11-02 16:46 UTC · **decrypt** · [Brazil's Largest Exchange Mercado Bitcoin Halts Withdrawals After $40 Million Hack](https://decrypt.co/382341/mercado-bitcoin-halts-withdrawals-40-million-hack) _(Thema: hack)_
- 2026-11-02 15:53 UTC · **coindesk** · [Brazil’s Mercado Bitcoin halts withdrawals after $40 million drained across 10 chains](https://www.coindesk.com/business/2026/11/02/brazil-s-mercado-bitcoin-halts-withdrawals-after-usd40-million-drained-across-10-chains) _(Thema: hack)_
- 2026-11-02 14:57 UTC · **bitcoinmagazine** · [Binance Reopens Withdrawals as Hack Recovery Enters Second Week](https://bitcoinmagazine.com/news/binance-reopens-withdrawals-hack) _(Thema: hack)_
- 2026-11-02 10:36 UTC · **decrypt** · [FBI Blames North Korea for $6B Binance Hack as Exchange Reopens Withdrawals](https://decrypt.co/382316/fbi-blames-north-korea-for-6b-binance-hack-as-exchange-reopens-withdrawals) _(Thema: hack)_
- 2026-11-02 09:04 UTC · **coindesk** · [Binance hack fallout, U.S. midterms and jobs report: Crypto Week Ahead](https://www.coindesk.com/markets/2026/11/02/binance-hack-fallout-u-s-midterms-and-jobs-report-crypto-week-ahead) _(Thema: hack)_
- 2026-11-02 08:49 UTC · **coindesk** · [Live updates: Bitcoin bounce fades as Binance exploit, AI unwind continue to weigh](https://www.coindesk.com/markets/2026/11/02/live-updates-binance-records-usd6-billion-outflows-after-starting-withdrawals-less-then-4-of-total-holdings) _(Thema: hack)_
