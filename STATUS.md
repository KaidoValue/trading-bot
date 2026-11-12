# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **12.11.2026 08:35** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 100.00 CHF Startkapital selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 100.00 CHF | 100.00 CHF | 100.00 CHF |
| **Kapital jetzt** | **97.17 CHF** | **100.00 CHF** | **90.50 CHF** |
| Gewinn / Verlust | 🔴 -2.83 CHF (-2.83 %) | ⚪ +0.00 CHF (+0.00 %) | 🔴 -9.50 CHF (-9.50 %) |
| Im Einsatz (investiert) | 27.98 CHF (29 %) | 0.00 CHF (0 %) | 67.93 CHF (75 %) |
| Cash (nicht investiert) | 69.19 CHF | 100.00 CHF | 22.57 CHF |
| Offene Positionen | 2 | 0 | 3 |
| Abgeschlossene Trades | 0 | 0 | 3 |
| Gebühren bisher | 0.24 CHF | 0.00 CHF | 1.51 CHF |
| Gebührenstufe | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 31 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 0 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 189 CHF) |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 20 % · mittel 30 % · lang 50 % | mittel 72 % · lang 28 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.30 CHF) |
| Hebel aktuell | – | – | 0.75× (erlaubt 3×) |
| Buchhaltung | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) |
| Letzter Durchlauf | 12.11.2026 08:32 (vor 2 Min.) | 12.11.2026 08:33 (vor 1 Min.) | 12.11.2026 08:34 (vor 1 Min.) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 100.00 CHF |
| **Kapital jetzt** | **95.68 CHF** |
| Gewinn / Verlust | 🔴 -4.32 CHF (-4.32 %) |
| **Aktuelle Verteilung** | Langfrist 28 % · KI 30 % · Risiko 16 % · Cash 26 % |
| Marktphase (BTC, Tageskerzen) | Abwärtstrend, wild |
| Letzte Begründung | Marktphase «Abwärtstrend, wild», Einschätzung: Langfrist -0.7 %, KI +0.0 %, Risiko -4.6 % |
| Umschicht-Gebühren bisher | 1.71 CHF |
| Erfahrung im Gedächtnis | 450 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** KI +0.000 %/Lauf, Langfrist -0.002 %/Lauf, Risiko -0.014 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 61'197.60 CHF | 🔴 -0.54 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'705.09 CHF | 🔴 -0.55 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 560.30 CHF | 🔴 -0.95 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 0.87 CHF | 🔴 -0.70 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 68.99 CHF | 🔴 -0.42 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.26 CHF | 🔴 -0.01 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 822.27 CHF | 🟢 +2.63 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 59.45 CHF | 🔴 -0.86 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 04.11.2026 21:01 | 65'280.50 | 61'197.60 | 0.000306 | 19.98 CHF | 18.73 CHF | 🔴 -1.25 CHF (-6.25 %) | 52'267.92 (-15 %) |
| **HYPE** long (lang) | 04.11.2026 21:01 | 68.01 | 59.45 | 0.155592 | 10.58 CHF | 9.25 CHF | 🔴 -1.33 CHF (-12.59 %) | 35.88 (-40 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| ETH | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | ⚪ neutral | ⚪ neutral | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: kein Signal · [lang] BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] XRP/CHF: Signal 'raus', bleibe in Cash · [lang] SOL/CHF: Signal 'raus', bleibe in Cash · [lang] TRX/CHF: kein Signal · [lang] ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] HYPE/CHF: Position offen, Signal bestätigt · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Signal 'raus', bleibe in Cash · [mittel] BNB/CHF: Signal 'raus', bleibe in Cash · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Signal 'raus', bleibe in Cash · [mittel] TRX/CHF: kein Signal · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: Position gehört zum Horizont «lang» · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Position gehört zum Horizont «lang»

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | lang | 12.11.2026 08:31 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 12.11.2026 08:31 | Kein Signal |
| BNB/CHF | lang | 12.11.2026 08:31 | BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| XRP/CHF | lang | 12.11.2026 08:31 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | lang | 12.11.2026 08:31 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | lang | 12.11.2026 08:31 | Kein Signal |
| ZEC/CHF | lang | 12.11.2026 08:31 | ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| HYPE/CHF | lang | 12.11.2026 08:31 | HYPE/CHF: Position offen, Signal bestätigt |
| BTC/CHF | mittel | 12.11.2026 08:31 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 12.11.2026 08:31 | ETH/CHF: Signal 'raus', bleibe in Cash |
| BNB/CHF | mittel | 12.11.2026 08:31 | BNB/CHF: Signal 'raus', bleibe in Cash |
| XRP/CHF | mittel | 12.11.2026 08:31 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | mittel | 12.11.2026 08:31 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | mittel | 12.11.2026 08:31 | Kein Signal |
| ZEC/CHF | mittel | 12.11.2026 08:31 | ZEC/CHF: Signal 'raus', bleibe in Cash |
| HYPE/CHF | mittel | 12.11.2026 08:31 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | kurz | 12.11.2026 08:31 | BTC/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 12.11.2026 08:31 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | kurz | 12.11.2026 08:31 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | kurz | 12.11.2026 08:31 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | kurz | 12.11.2026 08:31 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 12.11.2026 08:31 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | kurz | 12.11.2026 08:31 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | kurz | 12.11.2026 08:31 | HYPE/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |

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
| ZEC | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 4'214 Kerzen Erfahrung (zeitlich gewichtete Kerzen; ältere Erfahrung zählt weniger)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Seitwärts, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ETH | Abwärtstrend, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| BNB | Abwärtstrend, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| XRP | Abwärtstrend, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| SOL | Abwärtstrend, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| TRX | Seitwärts, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ZEC | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| HYPE | Abwärtstrend, ruhig | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 0 (noch keine hat die Prüfung bestanden), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | kurz | 12.11.2026 08:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 12.11.2026 08:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | kurz | 12.11.2026 08:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | kurz | 12.11.2026 08:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | kurz | 12.11.2026 08:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 12.11.2026 08:03 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | kurz | 12.11.2026 08:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | kurz | 12.11.2026 08:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BTC/CHF | mittel | 12.11.2026 05:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | mittel | 12.11.2026 05:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | mittel | 12.11.2026 05:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | mittel | 12.11.2026 05:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | mittel | 12.11.2026 05:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | mittel | 12.11.2026 05:03 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | mittel | 12.11.2026 05:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | mittel | 12.11.2026 05:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BTC/CHF | lang | 12.11.2026 01:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: 6/9 Strategien positiv gewichtet |
| ETH/CHF | lang | 12.11.2026 01:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: 2/9 Strategien positiv gewichtet |
| BNB/CHF | lang | 12.11.2026 01:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: 5/9 Strategien positiv gewichtet |
| XRP/CHF | lang | 12.11.2026 01:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine positiv gewichtete Strategie nach Kosten |
| SOL/CHF | lang | 12.11.2026 01:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: 5/9 Strategien positiv gewichtet |
| TRX/CHF | lang | 12.11.2026 01:03 | TRX/CHF: kein Einstieg gegen den langfristigen Trend (200-Tage-Linie) · KI: 2/9 Strategien positiv gewichtet |
| ZEC/CHF | lang | 12.11.2026 01:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: 3/9 Strategien positiv gewichtet |
| HYPE/CHF | lang | 12.11.2026 01:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: 1/9 Strategien positiv gewichtet |

**KI-Forschung: getrennte Vorwärtstests mit Kosten**

Die Werte betreffen isolierte Testpositionen, keine erzielte Portfoliorendite.

| Horizont | Status | Ausgewertet | Offen | Datenlücken / ungültig |
|---|---|---|---|---|
| kurz | Sammelt Lernfälle | 207 | 8 | 0 |
| mittel | Sammelt Lernfälle | 39 | 8 | 0 |
| lang | Sammelt Lernfälle | 8 | 8 | 0 |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 02.11.2026 21:04 | 62'905.40 | 61'197.60 | 0.000523 | 32.87 CHF | 31.98 CHF | 🔴 -0.89 CHF (-2.71 %) | 53'337.04 (-13 %) |
| **BNB** long (lang) | 02.11.2026 21:04 | 570.38 | 560.30 | 0.041690 | 23.78 CHF | 23.36 CHF | 🔴 -0.42 CHF (-1.77 %) | 450.90 (-20 %) |
| **HYPE** long (lang) | 02.11.2026 21:04 | 68.38 | 59.45 | 0.211733 | 14.48 CHF | 12.59 CHF | 🔴 -1.89 CHF (-13.06 %) | 44.97 (-24 %) |

**Signale jetzt**

| Coin | mittel (4h) | lang (1d) |
|---|---|---|
| BTC | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🔴 raus / Cash | ⚪ neutral |
| BNB | 🔴 raus / Cash | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | 🔴 raus / Cash | ⚪ neutral |
| ZEC | 🔴 raus / Cash | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash | 🟢 investiert sein |

**Letzte Entscheidung:** [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Signal 'raus', bleibe in Cash · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Signal 'raus', bleibe in Cash · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: Position gehört zum Horizont «lang»

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | mittel | 12.11.2026 05:04 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 12.11.2026 05:04 | ETH/CHF: Signal 'raus', bleibe in Cash |
| BNB/CHF | mittel | 12.11.2026 05:04 | BNB/CHF: Position gehört zum Horizont «lang» |
| XRP/CHF | mittel | 12.11.2026 05:04 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | mittel | 12.11.2026 05:04 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | mittel | 12.11.2026 05:04 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | mittel | 12.11.2026 05:04 | ZEC/CHF: Signal 'raus', bleibe in Cash |
| HYPE/CHF | mittel | 12.11.2026 05:04 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | lang | 12.11.2026 01:04 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 12.11.2026 01:04 | Kein Signal |
| BNB/CHF | lang | 12.11.2026 01:04 | BNB/CHF: Position offen, Signal bestätigt |
| XRP/CHF | lang | 12.11.2026 01:04 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | lang | 12.11.2026 01:04 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | lang | 12.11.2026 01:04 | Kein Signal |
| ZEC/CHF | lang | 12.11.2026 01:04 | ZEC/CHF: kein Einstieg (Obergrenze für investiertes Kapital erreicht) |
| HYPE/CHF | lang | 12.11.2026 01:04 | HYPE/CHF: Position offen, Signal bestätigt |

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
| SOL long (lang) | 02.11.2026 21:04 | 11.11.2026 01:04 | 75.10 | 68.79 | 🔴 -1.74 CHF | Signal |
| ETH long (lang) | 02.11.2026 21:04 | 11.11.2026 01:04 | 1'843.99 | 1'692.30 | 🔴 -2.28 CHF | Signal |
| XRP long (lang) | 04.11.2026 01:04 | 06.11.2026 01:04 | 1.05 | 0.99 | 🔴 -1.49 CHF | Signal |

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

- **Stimmung (Fear & Greed):** 28 von 100, Angst
- **Bewertung News:** +0.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** keine
