# 📈 Trading-Bot: Übersicht (Demo mit Spielgeld)

Stand: **13.11.2026 15:35** Schweizer Zeit · wird jede Stunde automatisch aktualisiert

> 🖥️ **[Zur Trading-Oberfläche](https://kaidovalue.github.io/trading-bot/)** (übersichtlich, mit Live-Chart)

## Auf einen Blick

- **1️⃣ Langfrist-Bot (Hauptbot):** Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr.
- **2️⃣ KI-Bot (lernend, kurz bis lang):** Lernende KI mit Gedächtnis: merkt sich für jede Marktphase, welche Strategie funktioniert, mit zeitlich abgewerteter Erfahrung. Nutzt zusätzlich selbst erfundene Strategien aus dem Strategie-Labor. Handelt auf drei Horizonten (1h Daytrading, 4h, Tageskerzen) mit je eigenem Gedächtnis, nur in Trendrichtung. Neue Lernlogik: noch keine validierte Renditeaussage. Laborstrategien erst nach separater Paper-Probe.
- **3️⃣ Risiko-Bot (aggressiv, Hebel 3×):** Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten.
- **4️⃣ Chef-Bot:** verteilt eigene 100.00 CHF Startkapital selbstständig auf die drei Stile oben, je nachdem, was in der aktuellen Marktphase am besten läuft.

| | **1️⃣ Langfrist-Bot (Hauptbot)** | **2️⃣ KI-Bot (lernend, kurz bis lang)** | **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** |
|---|---|---|---|
| Startkapital | 100.00 CHF | 100.00 CHF | 100.00 CHF |
| **Kapital jetzt** | **96.70 CHF** | **100.00 CHF** | **88.54 CHF** |
| Gewinn / Verlust | 🔴 -3.30 CHF (-3.30 %) | ⚪ +0.00 CHF (+0.00 %) | 🔴 -11.46 CHF (-11.46 %) |
| Im Einsatz (investiert) | 27.51 CHF (28 %) | 0.00 CHF (0 %) | 66.00 CHF (75 %) |
| Cash (nicht investiert) | 69.19 CHF | 100.00 CHF | 22.54 CHF |
| Offene Positionen | 2 | 0 | 3 |
| Abgeschlossene Trades | 0 | 0 | 3 |
| Gebühren bisher | 0.24 CHF | 0.00 CHF | 1.51 CHF |
| Gebührenstufe | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 31 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 0 CHF) | Stufe 1: 0.80 % je Market-Order (30-Tage-Umsatz 189 CHF) |
| Horizonte (Strategie, Kerzen) | lang: regime 1d · mittel: buch_triple_screen 4h · kurz: adaptive 1h | kurz: adaptive_memory 1h · mittel: adaptive_memory 4h · lang: adaptive_memory 1d | mittel: trend 4h · lang: regime 1d |
| Kapitalanteil je Horizont | lang 50 % · mittel 25 % · kurz 25 % | kurz 20 % · mittel 30 % · lang 50 % | mittel 72 % · lang 28 % |
| Short erlaubt | nein | nein | nein |
| Hebel | ohne | ohne | 3× (Zinsen bisher 0.33 CHF) |
| Hebel aktuell | – | – | 0.75× (erlaubt 3×) |
| Buchhaltung | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) | ✅ stimmt (Abweichung 0.00 CHF) |
| Letzter Durchlauf | 13.11.2026 15:32 (vor 2 Min.) | 13.11.2026 15:33 (vor 1 Min.) | 13.11.2026 15:34 (vor 1 Min.) |

## 4️⃣ Chef-Bot (verteilt auf die drei Stile)

Er handelt nicht selbst, sondern legt sein eigenes Kapital anteilig in die Stile der drei anderen Bots an und schichtet um, wenn ein Stil in der aktuellen Marktphase besser läuft. Feste Grenzen: höchstens 20 % im Risiko-Stil (Hebel), Notbremse bei mehr als 3 % Verlust eines Stils in 3 Stunden.

| | |
|---|---|
| Startkapital | 100.00 CHF |
| **Kapital jetzt** | **95.01 CHF** |
| Gewinn / Verlust | 🔴 -4.99 CHF (-4.99 %) |
| **Aktuelle Verteilung** | Langfrist 26 % · KI 30 % · Risiko 10 % · Cash 34 % |
| Marktphase (BTC, Tageskerzen) | Abwärtstrend, wild |
| Letzte Begründung | Marktphase «Abwärtstrend, wild», Einschätzung: Langfrist -1.4 %, KI +0.0 %, Risiko -6.5 % |
| Umschicht-Gebühren bisher | 1.90 CHF |
| Erfahrung im Gedächtnis | 512 Läufe |

**Was das Gedächtnis in dieser Phase weiss:** KI +0.000 %/Lauf, Langfrist -0.003 %/Lauf, Risiko -0.018 %/Lauf


## Kurse

| Coin | Kurs jetzt | 24 Std. | Live-Chart |
|---|---|---|---|
| **BTC** | 58'147.10 CHF | 🔴 -2.66 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BTCCHF) |
| **ETH** | 1'644.78 CHF | 🔴 -2.41 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ETHCHF) |
| **BNB** | 537.29 CHF | 🔴 -2.39 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:BNBUSD) |
| **XRP** | 0.87 CHF | 🔴 -0.76 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:XRPUSD) |
| **SOL** | 68.24 CHF | 🔴 -0.29 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:SOLUSD) |
| **TRX** | 0.26 CHF | 🔴 -0.65 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:TRXUSD) |
| **ZEC** | 808.80 CHF | 🟢 +0.91 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:ZECUSD) |
| **HYPE** | 62.39 CHF | 🟢 +2.39 % | [öffnen](https://www.tradingview.com/chart/?symbol=KRAKEN:HYPEUSD) |

## 1️⃣ Langfrist-Bot (Hauptbot)

_Schwerpunkt langfristig (200-Tage-Linie, Wochen bis Monate), handelt auch mittelfristig (4h) und kurzfristig (1h), nur in Trendrichtung. Bis 100 % investiert, je Coin bis 20 %. Simulation 2011-2022: +58 %/Jahr, 2023-2026: +40 %/Jahr._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 04.11.2026 21:01 | 65'280.50 | 58'147.10 | 0.000306 | 19.98 CHF | 17.80 CHF | 🔴 -2.18 CHF (-10.93 %) | 52'267.92 (-10 %) |
| **HYPE** long (lang) | 04.11.2026 21:01 | 68.01 | 62.39 | 0.155592 | 10.58 CHF | 9.71 CHF | 🔴 -0.87 CHF (-8.26 %) | 35.88 (-43 %) |

**Signale jetzt**

| Coin | lang (1d) | mittel (4h) | kurz (1h) |
|---|---|---|---|
| BTC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| ETH | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| BNB | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| XRP | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| SOL | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| TRX | ⚪ neutral | 🔴 raus / Cash | 🔴 raus / Cash |
| ZEC | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |
| HYPE | 🟢 investiert sein | 🔴 raus / Cash | 🔴 raus / Cash |

**Letzte Entscheidung:** [lang] BTC/CHF: Position offen, Signal bestätigt · [lang] ETH/CHF: kein Signal · [lang] BNB/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.00) · [lang] XRP/CHF: Signal 'raus', bleibe in Cash · [lang] SOL/CHF: Signal 'raus', bleibe in Cash · [lang] TRX/CHF: kein Signal · [lang] ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.00) · [lang] HYPE/CHF: Position offen, Signal bestätigt · [mittel] BTC/CHF: Position gehört zum Horizont «lang» · [mittel] ETH/CHF: Signal 'raus', bleibe in Cash · [mittel] BNB/CHF: Signal 'raus', bleibe in Cash · [mittel] XRP/CHF: Signal 'raus', bleibe in Cash · [mittel] SOL/CHF: Signal 'raus', bleibe in Cash · [mittel] TRX/CHF: Signal 'raus', bleibe in Cash · [mittel] ZEC/CHF: Signal 'raus', bleibe in Cash · [mittel] HYPE/CHF: Position gehört zum Horizont «lang» · [kurz] BTC/CHF: Position gehört zum Horizont «lang» · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Position gehört zum Horizont «lang»

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | lang | 13.11.2026 15:31 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 13.11.2026 15:31 | Kein Signal |
| BNB/CHF | lang | 13.11.2026 15:31 | BNB/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.00) |
| XRP/CHF | lang | 13.11.2026 15:31 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | lang | 13.11.2026 15:31 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | lang | 13.11.2026 15:31 | Kein Signal |
| ZEC/CHF | lang | 13.11.2026 15:31 | ZEC/CHF: Einstieg pausiert wegen Nachrichtenlage (bestätigte Themen: hack, Wert -1.00) |
| HYPE/CHF | lang | 13.11.2026 15:31 | HYPE/CHF: Position offen, Signal bestätigt |
| BTC/CHF | mittel | 13.11.2026 15:31 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 13.11.2026 15:31 | ETH/CHF: Signal 'raus', bleibe in Cash |
| BNB/CHF | mittel | 13.11.2026 15:31 | BNB/CHF: Signal 'raus', bleibe in Cash |
| XRP/CHF | mittel | 13.11.2026 15:31 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | mittel | 13.11.2026 15:31 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | mittel | 13.11.2026 15:31 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | mittel | 13.11.2026 15:31 | ZEC/CHF: Signal 'raus', bleibe in Cash |
| HYPE/CHF | mittel | 13.11.2026 15:31 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | kurz | 13.11.2026 15:31 | BTC/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 13.11.2026 15:31 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | kurz | 13.11.2026 15:31 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | kurz | 13.11.2026 15:31 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | kurz | 13.11.2026 15:31 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 13.11.2026 15:31 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | kurz | 13.11.2026 15:31 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | kurz | 13.11.2026 15:31 | HYPE/CHF: Position gehört zum Horizont «lang» · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |

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
| TRX | 🔴 raus / Cash | 🔴 raus / Cash | ⚪ neutral |
| ZEC | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |
| HYPE | 🔴 raus / Cash | 🔴 raus / Cash | 🔴 raus / Cash |

**🧠 KI-Gedächtnis:** 4'419 Kerzen Erfahrung (zeitlich gewichtete Kerzen; ältere Erfahrung zählt weniger)

| Coin | Marktphase jetzt | Hier vertraut die KI am meisten |
|---|---|---|
| BTC | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ETH | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| BNB | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| XRP | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| SOL | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| TRX | Seitwärts, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| ZEC | Abwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |
| HYPE | Aufwärtstrend, wild | trend (+0.000 %/Kerze), mean_reversion (+0.000 %/Kerze), breakout (+0.000 %/Kerze) |

**🧪 Selbst erfundene Strategien im Einsatz:** 0 (noch keine hat die Prüfung bestanden), Details in [lernen/LABOR.md](lernen/LABOR.md)

**Letzte Entscheidung:** [kurz] BTC/CHF: Signal 'raus', bleibe in Cash · [kurz] ETH/CHF: Signal 'raus', bleibe in Cash · [kurz] BNB/CHF: Signal 'raus', bleibe in Cash · [kurz] XRP/CHF: Signal 'raus', bleibe in Cash · [kurz] SOL/CHF: Signal 'raus', bleibe in Cash · [kurz] TRX/CHF: Signal 'raus', bleibe in Cash · [kurz] ZEC/CHF: Signal 'raus', bleibe in Cash · [kurz] HYPE/CHF: Signal 'raus', bleibe in Cash

**Gespeicherte Entscheidungen je Coin und Horizont**

| Coin | Horizont | Geprüft (CH) | Begründung |
|---|---|---|---|
| BTC/CHF | kurz | 13.11.2026 15:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | kurz | 13.11.2026 15:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | kurz | 13.11.2026 15:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | kurz | 13.11.2026 15:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | kurz | 13.11.2026 15:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | kurz | 13.11.2026 15:03 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | kurz | 13.11.2026 15:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | kurz | 13.11.2026 15:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BTC/CHF | mittel | 13.11.2026 13:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ETH/CHF | mittel | 13.11.2026 13:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BNB/CHF | mittel | 13.11.2026 13:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| XRP/CHF | mittel | 13.11.2026 13:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| SOL/CHF | mittel | 13.11.2026 13:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| TRX/CHF | mittel | 13.11.2026 13:03 | TRX/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| ZEC/CHF | mittel | 13.11.2026 13:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| HYPE/CHF | mittel | 13.11.2026 13:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine simulierten Ausführungen: Filter, Kapital und Mindestorder prüfen |
| BTC/CHF | lang | 13.11.2026 01:03 | BTC/CHF: Signal 'raus', bleibe in Cash · KI: 6/9 Strategien positiv gewichtet |
| ETH/CHF | lang | 13.11.2026 01:03 | ETH/CHF: Signal 'raus', bleibe in Cash · KI: 2/9 Strategien positiv gewichtet |
| BNB/CHF | lang | 13.11.2026 01:03 | BNB/CHF: Signal 'raus', bleibe in Cash · KI: 4/9 Strategien positiv gewichtet |
| XRP/CHF | lang | 13.11.2026 01:03 | XRP/CHF: Signal 'raus', bleibe in Cash · KI: Keine positiv gewichtete Strategie nach Kosten |
| SOL/CHF | lang | 13.11.2026 01:03 | SOL/CHF: Signal 'raus', bleibe in Cash · KI: 5/9 Strategien positiv gewichtet |
| TRX/CHF | lang | 13.11.2026 01:03 | TRX/CHF: kein Einstieg gegen den langfristigen Trend (200-Tage-Linie) · KI: 2/9 Strategien positiv gewichtet |
| ZEC/CHF | lang | 13.11.2026 01:03 | ZEC/CHF: Signal 'raus', bleibe in Cash · KI: 2/9 Strategien positiv gewichtet |
| HYPE/CHF | lang | 13.11.2026 01:03 | HYPE/CHF: Signal 'raus', bleibe in Cash · KI: Keine positiv gewichtete Strategie nach Kosten |

**KI-Forschung: getrennte Vorwärtstests mit Kosten**

Die Werte betreffen isolierte Testpositionen, keine erzielte Portfoliorendite.

| Horizont | Status | Ausgewertet | Offen | Datenlücken / ungültig |
|---|---|---|---|---|
| kurz | Sammelt Lernfälle | 252 | 8 | 0 |
| mittel | Sammelt Lernfälle | 47 | 8 | 0 |
| lang | Sammelt Lernfälle | 8 | 8 | 0 |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

_Risikofreudig mit Hebel 3×: 200-Tage-Linie (lang) und Trendfolge (4h), nur in Trendrichtung; Daytrading (30-Min.-Ausbrüche) seit 29.10. pausiert, weil es 64 % verlor. Simulation 2011-2022: +66 %/Jahr, 2023-2026: +59 %/Jahr, Rückgänge bis −62 %, 5 % Risiko pro Trade, Hebel 3× mit Zinsen und Zwangsschliessung wie an der Börse, ignoriert Nachrichten._

**Offene Positionen**

| Coin | Gekauft am | Einstiegskurs | Kurs jetzt | Menge | Einsatz | Wert jetzt | Gewinn / Verlust | Stop-Loss |
|---|---|---|---|---|---|---|---|---|
| **BTC** long (lang) | 02.11.2026 21:04 | 62'905.40 | 58'147.10 | 0.000523 | 32.87 CHF | 30.39 CHF | 🔴 -2.49 CHF (-7.56 %) | 53'337.04 (-8 %) |
| **BNB** long (lang) | 02.11.2026 21:04 | 570.38 | 537.29 | 0.041690 | 23.78 CHF | 22.40 CHF | 🔴 -1.38 CHF (-5.80 %) | 450.90 (-16 %) |
| **HYPE** long (lang) | 02.11.2026 21:04 | 68.38 | 62.39 | 0.211733 | 14.48 CHF | 13.21 CHF | 🔴 -1.27 CHF (-8.76 %) | 44.97 (-28 %) |

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
| BTC/CHF | mittel | 13.11.2026 13:04 | BTC/CHF: Position gehört zum Horizont «lang» |
| ETH/CHF | mittel | 13.11.2026 13:04 | ETH/CHF: Signal 'raus', bleibe in Cash |
| BNB/CHF | mittel | 13.11.2026 13:04 | BNB/CHF: Position gehört zum Horizont «lang» |
| XRP/CHF | mittel | 13.11.2026 13:04 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | mittel | 13.11.2026 13:04 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | mittel | 13.11.2026 13:04 | TRX/CHF: Signal 'raus', bleibe in Cash |
| ZEC/CHF | mittel | 13.11.2026 13:04 | ZEC/CHF: Signal 'raus', bleibe in Cash |
| HYPE/CHF | mittel | 13.11.2026 13:04 | HYPE/CHF: Position gehört zum Horizont «lang» |
| BTC/CHF | lang | 13.11.2026 01:04 | BTC/CHF: Position offen, Signal bestätigt |
| ETH/CHF | lang | 13.11.2026 01:04 | Kein Signal |
| BNB/CHF | lang | 13.11.2026 01:04 | BNB/CHF: Position offen, Signal bestätigt |
| XRP/CHF | lang | 13.11.2026 01:04 | XRP/CHF: Signal 'raus', bleibe in Cash |
| SOL/CHF | lang | 13.11.2026 01:04 | SOL/CHF: Signal 'raus', bleibe in Cash |
| TRX/CHF | lang | 13.11.2026 01:04 | Kein Signal |
| ZEC/CHF | lang | 13.11.2026 01:04 | ZEC/CHF: kein Einstieg (Obergrenze für investiertes Kapital erreicht) |
| HYPE/CHF | lang | 13.11.2026 01:04 | HYPE/CHF: Position offen, Signal bestätigt |

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

- **Stimmung (Fear & Greed):** 20 von 100, extreme Angst
- **Bewertung News:** -1.00 (−1 sehr negativ bis +1 sehr positiv)
- **Bestätigte Themen:** hack (gemeldet von bitcoinmagazine, coindesk – blockiert Käufe)

**Schlagzeilen dazu:**

- 2026-11-13 00:15 UTC · **bitcoinmagazine** · [DOJ Wins Court Authority to Seize $1.2 Billion of North Korea’s Stolen Binance Crypto as Freezes Top $2.7 Billion](https://bitcoinmagazine.com/news/doj-north-korea-binance-1-2-billion-seize) _(Thema: hack)_
- 2026-11-12 22:55 UTC · **coindesk** · [North Korea's Binance hack faces U.S. crackdown as DOJ targets $1.2 billion in stolen crypto](https://www.coindesk.com/policy/2026/11/12/north-korea-s-binance-hack-faces-u-s-crackdown-as-doj-targets-usd1-2-billion-in-stolen-crypto) _(Thema: hack)_
