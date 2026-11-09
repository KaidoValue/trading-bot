# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **09.11.2026 10:35** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 100.00 CHF Startkapital selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 100.00 CHF | 100.00 CHF | 100.00 CHF |
| **Kapital jetzt** | **97.13 CHF** | **100.00 CHF** | **91.59 CHF** |
| Gewinn / Verlust | 🔴 -2.87 CHF (-2.87 %) | ⚪ +0.00 CHF (+0.00 %) | 🔴 -8.41 CHF (-8.41 %) |
| Im Einsatz (investiert) | 27.94 CHF (29 %) | 0.00 CHF (0 %) | 106.09 CHF (116 %) |
| Cash (nicht investiert) | 69.19 CHF | 100.00 CHF | -14.50 CHF |
| Offene Positionen | 2 | 0 | 5 |
| Abgeschlossene Trades | 0 | 0 | 1 |
| Gebühren bisher | 0.24 CHF | 0.00 CHF | 1.21 CHF |
| Gebührenstufe | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 31 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 0 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 151 CHF) |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 20 % · mittel 30 % · lang 50 % | mittel 54 % · lang 46 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.24 CHF) |
| Hebel aktuell | – | – | 1.16× (erlaubt 3×) |
| Buchhaltung | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) |
| Letzter Durchlauf | 09.11.2026 10:32 (vor 2 Min.) | 09.11.2026 10:33 (vor 2 Min.) | 09.11.2026 10:34 (vor 1 Min.) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 100.00 CHF |
| **Kapital jetzt** | **96.73 CHF** |
| Gewinn / Verlust | 🔴 -3.27 CHF (-3.27 %) |
| **Aktuelle Verteilung** | Langfrist 24 % · KI 30 % · Risiko 9 % · Cash 37 % |
| Marktphase (BTC, Tageskerzen) | Abwärtstrend, wild |
| Letzte Begründung | Marktphase «Abwärtstrend, wild», Einschätzung: Langfrist -1.9 %, KI +0.0 %, Risiko -7.0 % |
| Umschicht-Gebühren bisher | 1.26 CHF |
| Erfahrung im Gedächtnis | 317 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** KI +0.000 %/Lauf, Langfrist -0.005 %/Lauf, Risiko -0.019 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 60'793.40 CHF | 🔴 -0.58 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'725.35 CHF | 🔴 -0.73 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 558.03 CHF | 🔴 -0.38 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 0.89 CHF | 🔴 -1.88 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 70.96 CHF | 🟢 +0.16 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.26 CHF | 🔴 -0.63 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 994.10 CHF | 🟢 +0.06 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 59.94 CHF | 🔴 -1.77 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 04.11.2026 21:01 | 65'280.50 | 60'793.40 | 0.000306 | 19.98 CHF | 18.61 CHF | 🔴 -1.37 CHF (-6.87 %) | 52'267.92 (-14 %) |
| **HYPE** long (lang) | 04.11.2026 21:01 | 68.01 | 59.94 | 0.155592 | 10.58 CHF | 9.33 CHF | 🔴 -1.26 CHF (-11.87 %) | 35.88 (-40 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| ETH | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: kein Signal · [lang] BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] XRP/CHF: Signal 'raus', bleibe in Cash · [lang] SOL/CHF: kein Signal · [lang] TRX/CHF: kein Signal · [lang] ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · [lang] HYPE/CHF: Position offen, Signal bestätigt · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Signal 'raus', bleibe in Cash · [mittel] BNB/CHF: Signal 'raus', bleibe in Cash · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Signal 'raus', bleibe in Cash · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: Position gehört zum Horizont «lang» · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Position gehört zum Horizont «lang»

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | lang | 09.11.2026 10:31 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 09.11.2026 10:31 | Kein Signal |
| BNB/CHF | lang | 09.11.2026 10:31 | BNB/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| XRP/CHF | lang | 09.11.2026 10:31 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | lang | 09.11.2026 10:31 | Kein Signal |
| TRX/CHF | lang | 09.11.2026 10:31 | Kein Signal |
| ZEC/CHF | lang | 09.11.2026 10:31 | ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| HYPE/CHF | lang | 09.11.2026 10:31 | HYPE/CHF: Position offen, Signal bestätigt |
| BTC/CHF | mittel | 09.11.2026 10:31 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 09.11.2026 10:31 | ETH/CHF: Signal 'raus', bleibe in Cash |
| BNB/CHF | mittel | 09.11.2026 10:31 | BNB/CHF: Signal 'raus', bleibe in Cash |
| XRP/CHF | mittel | 09.11.2026 10:31 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | mittel | 09.11.2026 10:31 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | mittel | 09.11.2026 10:31 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | mittel | 09.11.2026 10:31 | ZEC/CHF: Signal 'raus', bleibe in Cash |
| HYPE/CHF | mittel | 09.11.2026 10:31 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | kurz | 09.11.2026 10:31 | BTC/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 09.11.2026 10:31 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | kurz | 09.11.2026 10:31 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | kurz | 09.11.2026 10:31 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | kurz | 09.11.2026 10:31 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 09.11.2026 10:31 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | kurz | 09.11.2026 10:31 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | kurz | 09.11.2026 10:31 | HYPE/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |

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
| ZEC | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash | 🔴 raus / Cash | 🟢 investiert sein |

**🧠 KI-Gedächtnis:** 3'743 Kerzen Erfahrung (zeitlich gewichtete Kerzen; ältere Erfahrung zählt weniger)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ETH | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| BNB | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| XRP | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| SOL | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| TRX | Seitwärts, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ZEC | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| HYPE | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 0 (noch keine hat die Prüfung bestanden), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | kurz | 09.11.2026 10:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 09.11.2026 10:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | kurz | 09.11.2026 10:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | kurz | 09.11.2026 10:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | kurz | 09.11.2026 10:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 09.11.2026 10:03 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | kurz | 09.11.2026 10:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | kurz | 09.11.2026 10:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BTC/CHF | mittel | 09.11.2026 09:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | mittel | 09.11.2026 09:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | mittel | 09.11.2026 09:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | mittel | 09.11.2026 09:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | mittel | 09.11.2026 09:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | mittel | 09.11.2026 09:03 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | mittel | 09.11.2026 09:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | mittel | 09.11.2026 09:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BTC/CHF | lang | 09.11.2026 01:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: 8/9 Strategien positiv gewichtet |
| ETH/CHF | lang | 09.11.2026 01:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: 3/9 Strategien positiv gewichtet |
| BNB/CHF | lang | 09.11.2026 01:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: 5/9 Strategien positiv gewichtet |
| XRP/CHF | lang | 09.11.2026 01:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine positiv gewichtete Strategie nach Kosten |
| SOL/CHF | lang | 09.11.2026 01:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: 5/9 Strategien positiv gewichtet |
| TRX/CHF | lang | 09.11.2026 01:03 | TRX/CHF: kein Einstieg gegen den langfristigen Trend (200-Tage-Linie) · KI: 2/9 Strategien positiv gewichtet |
| ZEC/CHF | lang | 09.11.2026 01:03 | ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · KI: 3/9 Strategien positiv gewichtet |
| HYPE/CHF | lang | 09.11.2026 01:03 | HYPE/CHF: kein Einstieg (Order kleiner als Mindestgrösse) · KI: 1/9 Strategien positiv gewichtet |

**KI-Forschung: getrennte Vorwärtstests mit Kosten**

Die Werte betreffen isolierte Testpositionen, keine erzielte Portfoliorendite.

| Horizont | Status | Ausgewertet | Offen | Datenlücken / ungültig |
|---|---|---|---|---|
| kurz | Sammelt Lernfälle | 128 | 8 | 0 |
| mittel | Sammelt Lernfälle | 22 | 8 | 0 |
| lang | Sammelt Lernfälle | 0 | 8 | 0 |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 02.11.2026 21:04 | 62'905.40 | 60'793.40 | 0.000523 | 32.87 CHF | 31.77 CHF | 🔴 -1.10 CHF (-3.36 %) | 53'337.04 (-12 %) |
| **ETH** long (lang) | 02.11.2026 21:04 | 1'843.99 | 1'725.35 | 0.012649 | 23.33 CHF | 21.82 CHF | 🔴 -1.50 CHF (-6.43 %) | 1'449.18 (-16 %) |
| **BNB** long (lang) | 02.11.2026 21:04 | 570.38 | 558.03 | 0.041690 | 23.78 CHF | 23.26 CHF | 🔴 -0.51 CHF (-2.17 %) | 450.90 (-19 %) |
| **SOL** long (lang) | 02.11.2026 21:04 | 75.10 | 70.96 | 0.233083 | 17.50 CHF | 16.54 CHF | 🔴 -0.97 CHF (-5.52 %) | 53.80 (-24 %) |
| **HYPE** long (lang) | 02.11.2026 21:04 | 68.38 | 59.94 | 0.211733 | 14.48 CHF | 12.69 CHF | 🔴 -1.79 CHF (-12.34 %) | 44.97 (-25 %) |

**Signale jetzt**

| Coin | mittel (4h) | lang (1d) |
|---|---|---|
| BTC | 🔴 raus / Cash | 🟢 investiert sein |
| ETH | 🔴 raus / Cash | ⚪ neutral |
| BNB | 🔴 raus / Cash | 🟢 investiert sein |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | ⚪ neutral |
| TRX | 🔴 raus / Cash | ⚪ neutral |
| ZEC | 🔴 raus / Cash | 🟢 investiert sein |
| HYPE | 🔴 raus / Cash | 🟢 investiert sein |

**Letzte Entscheidung:** [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Position gehört zum Horizont «lang» · [mittel] BNB/CHF: Position gehört zum Horizont «lang» · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Position gehört zum Horizont «lang» · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: Position gehört zum Horizont «lang»

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | mittel | 09.11.2026 09:04 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 09.11.2026 09:04 | ETH/CHF: Position gehört zum Horizont «lang» |
| BNB/CHF | mittel | 09.11.2026 09:04 | BNB/CHF: Position gehört zum Horizont «lang» |
| XRP/CHF | mittel | 09.11.2026 09:04 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | mittel | 09.11.2026 09:04 | SOL/CHF: Position gehört zum Horizont «lang» |
| TRX/CHF | mittel | 09.11.2026 09:04 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | mittel | 09.11.2026 09:04 | ZEC/CHF: Signal 'raus', bleibe in Cash |
| HYPE/CHF | mittel | 09.11.2026 09:04 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | lang | 09.11.2026 01:04 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 09.11.2026 01:04 | Kein Signal |
| BNB/CHF | lang | 09.11.2026 01:04 | BNB/CHF: Position offen, Signal bestätigt |
| XRP/CHF | lang | 09.11.2026 01:04 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | lang | 09.11.2026 01:04 | Kein Signal |
| TRX/CHF | lang | 09.11.2026 01:04 | Kein Signal |
| ZEC/CHF | lang | 09.11.2026 01:04 | ZEC/CHF: kein Einstieg (Order kleiner als Mindestgrösse) |
| HYPE/CHF | lang | 09.11.2026 01:04 | HYPE/CHF: Position offen, Signal bestätigt |

**Letzte abgeschlossene Trades**

| Coin | Gekauft | Verkauft | Einstieg | Ausstieg | Ergebnis | Grund |
|---|---|---|---|---|---|---|
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

- **Stimmung (Fear & Greed):** 29 von 100, Angst
- **Bewertung News:** +0.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** keine
