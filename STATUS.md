# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **05.11.2026 07:35** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 100.00 CHF Startkapital selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 100.00 CHF | 100.00 CHF | 100.00 CHF |
| **Kapital jetzt** | **99.77 CHF** | **100.00 CHF** | **103.07 CHF** |
| Gewinn / Verlust | 🔴 -0.23 CHF (-0.23 %) | ⚪ +0.00 CHF (+0.00 %) | 🟢 +3.07 CHF (+3.07 %) |
| Im Einsatz (investiert) | 30.58 CHF (31 %) | 0.00 CHF (0 %) | 136.39 CHF (132 %) |
| Cash (nicht investiert) | 69.19 CHF | 100.00 CHF | -33.32 CHF |
| Offene Positionen | 2 | 0 | 6 |
| Abgeschlossene Trades | 0 | 0 | 0 |
| Gebühren bisher | 0.24 CHF | 0.00 CHF | 1.06 CHF |
| Gebührenstufe | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 31 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 0 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 132 CHF) |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 20 % · mittel 30 % · lang 50 % | mittel 50 % · lang 50 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.11 CHF) |
| Hebel aktuell | – | – | 1.32× (erlaubt 3×) |
| Buchhaltung | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) |
| Letzter Durchlauf | 05.11.2026 07:32 (vor 2 Min.) | 05.11.2026 07:33 (vor 1 Min.) | 05.11.2026 07:34 (vor 1 Min.) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 100.00 CHF |
| **Kapital jetzt** | **99.95 CHF** |
| Gewinn / Verlust | 🔴 -0.05 CHF (-0.05 %) |
| **Aktuelle Verteilung** | Langfrist 30 % · KI 30 % · Risiko 20 % · Cash 20 % |
| Marktphase (BTC, Tageskerzen) | Aufwärtstrend, wild |
| Letzte Begründung | Marktphase «Aufwärtstrend, wild», Einschätzung: Langfrist +0.0 %, KI +0.0 %, Risiko -3.0 % |
| Umschicht-Gebühren bisher | 0.46 CHF |
| Erfahrung im Gedächtnis | 119 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** Risiko +0.036 %/Lauf, KI +0.000 %/Lauf, Langfrist -0.004 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 65'500.00 CHF | 🔴 -0.28 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'973.26 CHF | 🟢 +0.14 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 579.59 CHF | 🔴 -1.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 1.06 CHF | 🟢 +0.21 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 77.98 CHF | 🟢 +0.31 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.26 CHF | 🔴 -0.30 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 1'074.70 CHF | 🟢 +1.91 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 67.71 CHF | 🔴 -0.67 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 04.11.2026 21:01 | 65'280.50 | 65'500.00 | 0.000306 | 19.98 CHF | 20.05 CHF | 🟢 +0.07 CHF (+0.34 %) | 52'267.92 (-20 %) |
| **HYPE** long (lang) | 04.11.2026 21:01 | 68.01 | 67.71 | 0.155592 | 10.58 CHF | 10.53 CHF | 🔴 -0.05 CHF (-0.46 %) | 35.88 (-47 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | ⚪ neutral | 🔴 raus / Cash |
| ETH | 🟢 investiert sein | ⚪ neutral | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| XRP | 🟢 investiert sein | ⚪ neutral | 🔴 raus / Cash |
| SOL | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | ⚪ neutral | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] XRP/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] SOL/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] TRX/CHF: Signal 'raus', bleibe in Cash · [lang] ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] HYPE/CHF: Position offen, Signal bestätigt · [mittel] BTC/CHF: kein Signal · [mittel] ETH/CHF: kein Signal · [mittel] BNB/CHF: Signal 'raus', bleibe in Cash · [mittel] XRP/CHF: kein Signal · [mittel] SOL/CHF: Signal 'raus', bleibe in Cash · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: kein Signal · [mittel] HYPE/CHF: Position gehört zum Horizont «lang» · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Position gehört zum Horizont «lang»

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | lang | 05.11.2026 07:31 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 05.11.2026 07:31 | ETH/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| BNB/CHF | lang | 05.11.2026 07:31 | BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| XRP/CHF | lang | 05.11.2026 07:31 | XRP/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| SOL/CHF | lang | 05.11.2026 07:31 | SOL/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| TRX/CHF | lang | 05.11.2026 07:31 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | lang | 05.11.2026 07:31 | ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| HYPE/CHF | lang | 05.11.2026 07:31 | HYPE/CHF: Position offen, Signal bestätigt |
| BTC/CHF | mittel | 05.11.2026 07:31 | Kein Signal |
| ETH/CHF | mittel | 05.11.2026 07:31 | Kein Signal |
| BNB/CHF | mittel | 05.11.2026 07:31 | BNB/CHF: Signal 'raus', bleibe in Cash |
| XRP/CHF | mittel | 05.11.2026 07:31 | Kein Signal |
| SOL/CHF | mittel | 05.11.2026 07:31 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | mittel | 05.11.2026 07:31 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | mittel | 05.11.2026 07:31 | Kein Signal |
| HYPE/CHF | mittel | 05.11.2026 07:31 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | kurz | 05.11.2026 07:31 | BTC/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 05.11.2026 07:31 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | kurz | 05.11.2026 07:31 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | kurz | 05.11.2026 07:31 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | kurz | 05.11.2026 07:31 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 05.11.2026 07:31 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | kurz | 05.11.2026 07:31 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | kurz | 05.11.2026 07:31 | HYPE/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |

## 2️⃣ KI-Bot (lernend, kurz bis lang)

_Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe._

Keine offene Position, alles in Cash.

**Signale jetzt**

| Coin | kurz (1h) | mittel (4h) | lang (1d) |
|---|---|---|---|
| BTC | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| ETH | 🔴 raus / Cash | 🔴 raus / Cash | ⚪ neutral |
| BNB | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| ZEC | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 3'059 Kerzen Erfahrung (zeitlich gewichtete Kerzen; ältere Erfahrung zählt weniger)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Aufwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ETH | Aufwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| BNB | Seitwärts, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| XRP | Aufwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| SOL | Aufwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| TRX | Seitwärts, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ZEC | Aufwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| HYPE | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 0 (noch keine hat die Prüfung bestanden), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | kurz | 05.11.2026 07:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 05.11.2026 07:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | kurz | 05.11.2026 07:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | kurz | 05.11.2026 07:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | kurz | 05.11.2026 07:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 05.11.2026 07:03 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | kurz | 05.11.2026 07:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | kurz | 05.11.2026 07:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BTC/CHF | mittel | 05.11.2026 05:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | mittel | 05.11.2026 05:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | mittel | 05.11.2026 05:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | mittel | 05.11.2026 05:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | mittel | 05.11.2026 05:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | mittel | 05.11.2026 05:03 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | mittel | 05.11.2026 05:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | mittel | 05.11.2026 05:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BTC/CHF | lang | 05.11.2026 01:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: 6/9 Strategien positiv gewichtet |
| ETH/CHF | lang | 05.11.2026 01:03 | Kein Signal · KI: 4/9 Strategien positiv gewichtet |
| BNB/CHF | lang | 05.11.2026 01:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: 5/9 Strategien positiv gewichtet |
| XRP/CHF | lang | 05.11.2026 01:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: 2/9 Strategien positiv gewichtet |
| SOL/CHF | lang | 05.11.2026 01:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: 7/9 Strategien positiv gewichtet |
| TRX/CHF | lang | 05.11.2026 01:03 | TRX/CHF: kein Einstieg gegen den langfristigen Trend (200-Tage-Linie) · KI: 2/9 Strategien positiv gewichtet |
| ZEC/CHF | lang | 05.11.2026 01:03 | ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · KI: 4/9 Strategien positiv gewichtet |
| HYPE/CHF | lang | 05.11.2026 01:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: 2/9 Strategien positiv gewichtet |

**KI-Forschung: getrennte Vorwärtstests mit Kosten**

Die Werte betreffen isolierte Testpositionen, keine erzielte Portfoliorendite.

| Horizont | Status | Ausgewertet | Offen | Datenlücken / ungültig |
|---|---|---|---|---|
| kurz | Sammelt Lernfälle | 3 | 8 | 0 |
| mittel | Sammelt Lernfälle | 0 | 8 | 0 |
| lang | Sammelt Lernfälle | 0 | 8 | 0 |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 02.11.2026 21:04 | 62'905.40 | 65'500.00 | 0.000523 | 32.87 CHF | 34.23 CHF | 🟢 +1.36 CHF (+4.12 %) | 53'337.04 (-19 %) |
| **ETH** long (lang) | 02.11.2026 21:04 | 1'843.99 | 1'973.26 | 0.012649 | 23.33 CHF | 24.96 CHF | 🟢 +1.64 CHF (+7.01 %) | 1'449.18 (-27 %) |
| **BNB** long (lang) | 02.11.2026 21:04 | 570.38 | 579.59 | 0.041690 | 23.78 CHF | 24.16 CHF | 🟢 +0.38 CHF (+1.61 %) | 450.90 (-22 %) |
| **SOL** long (lang) | 02.11.2026 21:04 | 75.10 | 77.98 | 0.233083 | 17.50 CHF | 18.18 CHF | 🟢 +0.67 CHF (+3.84 %) | 53.80 (-31 %) |
| **HYPE** long (lang) | 02.11.2026 21:04 | 68.38 | 67.71 | 0.211733 | 14.48 CHF | 14.34 CHF | 🔴 -0.14 CHF (-0.99 %) | 44.97 (-34 %) |
| **XRP** long (lang) | 04.11.2026 01:04 | 1.05 | 1.06 | 19.302774 | 20.19 CHF | 20.53 CHF | 🟢 +0.34 CHF (+1.69 %) | 0.79 (-26 %) |

**Signale jetzt**

| Coin | mittel (4h) | lang (1d) |
|---|---|---|
| BTC | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🟢 investiert sein | 🟢 investiert sein |
| BNB | 🔴 raus / Cash | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | 🟢 investiert sein |
| SOL | 🔴 raus / Cash | 🟢 investiert sein |
| TRX | 🔴 raus / Cash | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash | 🟢 investiert sein |

**Letzte Entscheidung:** [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Position gehört zum Horizont «lang» · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: kein Einstieg (Kursziel 2.87%, erforderlich 8.50% inkl. Gebührenpuffer) · [mittel] HYPE/CHF: Position gehört zum Horizont «lang»

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | mittel | 05.11.2026 05:04 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 05.11.2026 05:04 | ETH/CHF: Position gehört zum Horizont «lang» |
| BNB/CHF | mittel | 05.11.2026 05:04 | BNB/CHF: Position gehört zum Horizont «lang» |
| XRP/CHF | mittel | 05.11.2026 05:04 | XRP/CHF: Position gehört zum Horizont «lang» |
| SOL/CHF | mittel | 05.11.2026 05:04 | SOL/CHF: Position gehört zum Horizont «lang» |
| TRX/CHF | mittel | 05.11.2026 05:04 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | mittel | 05.11.2026 05:04 | ZEC/CHF: kein Einstieg (Kursziel 2.87%, erforderlich 8.50% inkl. Gebührenpuffer) |
| HYPE/CHF | mittel | 05.11.2026 05:04 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | lang | 05.11.2026 01:04 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 05.11.2026 01:04 | ETH/CHF: Position offen, Signal bestätigt |
| BNB/CHF | lang | 05.11.2026 01:04 | BNB/CHF: Position offen, Signal bestätigt |
| XRP/CHF | lang | 05.11.2026 01:04 | XRP/CHF: Position offen, Signal bestätigt |
| SOL/CHF | lang | 05.11.2026 01:04 | SOL/CHF: Position offen, Signal bestätigt |
| TRX/CHF | lang | 05.11.2026 01:04 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | lang | 05.11.2026 01:04 | ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| HYPE/CHF | lang | 05.11.2026 01:04 | HYPE/CHF: Position offen, Signal bestätigt |

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

**Zusätzliche Sprachanalyse:** Sprachanalyse ausgeschaltet

- **Stimmung (Fear & Greed):** 50 von 100, neutral
- **Bewertung News:** +0.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** keine
