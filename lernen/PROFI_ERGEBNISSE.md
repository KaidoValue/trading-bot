# Profi-Bot: Ergebnisse der Auswertung

Aus 36 Ergebnisdateien in `lernen/profi/` (`python -m tradingbot profi --zusammenfassen`). Jedes Fenster ist ein frischer Start mit dem Startkapital. Calmar = CAGR / |Max. DD|. Entschieden wird nach den vorab registrierten Regeln, nur mit normierten Gebühren und in jedem Haupt-Cache; andere Quellen zählen nur zur Information. ✓ erfüllt, ✗ nicht erfüllt oder Zahl fehlt (–).

Vorab-Registrierung: [PROFI_PLAN.md](PROFI_PLAN.md), eingefrorene Fassung Commit `dce942282a04b2eeda025a315ed361e805dce2b8`.

## Caches

| | Quellen | Börsen der Kursdateien | eingefroren | Läufe | zählt für | Commits |
|---|---|---|---|---|---|---|
| **Cache ee111aa363f9** | bitstamp (USD), binance (USDT), binanceus (USD), kucoin (USDT) | binanceus, bitstamp, kucoin | ja | 36 | Entscheide | 39961fe3b194, c011d2d4df76, cda7f449de55, e13f4f514529 |

Nur ein Haupt-Cache: Die Entscheide stützen sich auf eine einzige Datenquelle (Schwäche).

## E0 Messlatte

### Kennzahlen: Cache ee111aa363f9, Gebühren alt

| | Fenster | CAGR % | Max. DD % | Calmar | Trades | Gebühren | Kosten %/Jahr | Umschlag/Jahr | Ø investiert % | Kostenanteil % | Not-Aus | Δ Calmar halten | Δ Calmar P−1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **KI** | 2012-2022 | 18.40 | -22.90 | 0.80 | 162 | 28.83 | 1.09 | 3.51 | 8.50 | 6 | 1 | -0.48 | -0.84 |
| **Langfrist** | 2012-2022 | 53.10 | -44.10 | 1.20 | 108 | 384.82 | 1.13 | 3.65 | 25.80 | 4.10 | 7 | -0.08 | -0.44 |
| **Phasen** | 2012-2022 | 49.50 | -41.60 | 1.19 | 103 | 232.22 | 0.96 | 3.09 | 21.50 | 3.30 | 4 | -0.09 | -0.45 |
| **Risiko** | 2012-2022 | 47.40 | -65.70 | 0.72 | 94 | 508.99 | 3.62 | 5.75 | 35.60 | 14.90 | 0 | -0.56 | -0.92 |
| **K1** | 2012-2022 | 48.20 | -54.50 | 0.88 | 98 | 218.23 | 1.12 | 3.62 | 23 | 3.40 | 5 | -0.40 | -0.76 |
| **P−1** | 2012-2022 | 119.20 | -72.60 | 1.64 | 17 | 16'380.36 | 0.99 | 3.18 | 61.10 | 3.40 | 0 | 0.36 | – |
| **Chef** | 2012-2022 | 17.90 | -47.30 | 0.38 | 0 | – | – | – | – | – | – | -0.90 | -1.26 |
| **Bitcoin halten nach Kosten** | 2012-2022 | 108.90 | -84.90 | 1.28 | 0 | 0.26 | 0 | 0 | 100 | 0 | 0 | – | -0.36 |

### Kennzahlen: Cache ee111aa363f9, Gebühren normiert

| | Fenster | CAGR % | Max. DD % | Calmar | Trades | Gebühren | Kosten %/Jahr | Umschlag/Jahr | Ø investiert % | Kostenanteil % | Not-Aus | Δ Calmar halten | Δ Calmar P−1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **KI** | 2012-2022 | 12.30 | -21.50 | 0.57 | 135 | 52.24 | 2.30 | 2.71 | 7.20 | 17.70 | 2 | -0.71 | -0.99 |
| **Langfrist** | 2012-2022 | 58.70 | -42.90 | 1.37 | 98 | 1'404.49 | 2.96 | 3.48 | 26.40 | 8.60 | 6 | 0.09 | -0.19 |
| **Phasen** | 2012-2022 | 45.80 | -44.20 | 1.04 | 102 | 564.38 | 2.42 | 2.85 | 20.80 | 8.80 | 4 | -0.24 | -0.52 |
| **Risiko** | 2012-2022 | 42.40 | -65.70 | 0.65 | 96 | 820.35 | 3.05 | 3.59 | 34.30 | 15.40 | 0 | -0.63 | -0.91 |
| **K1** | 2012-2022 | 53.20 | -54.70 | 0.97 | 98 | 982.27 | 3.08 | 3.62 | 27.50 | 8.80 | 5 | -0.31 | -0.59 |
| **P−1** | 2012-2022 | 115.90 | -74.20 | 1.56 | 17 | 44'455.29 | 2.72 | 3.20 | 61.30 | 9.10 | 0 | 0.28 | – |
| **Chef** | 2012-2022 | 17.80 | -44.50 | 0.40 | 0 | – | – | – | – | – | – | -0.88 | -1.16 |
| **Bitcoin halten nach Kosten** | 2012-2022 | 108.80 | -84.90 | 1.28 | 0 | 0.79 | 0 | 0 | 100 | 0 | 0 | – | -0.28 |

### L_dev (höchster Calmar 2012-2022 der Vergleichs-Bots)

| | L_dev | Bot |
|---|---|---|
| **Cache ee111aa363f9** | 1.56 | P−1 |

### Alte (fest 0,26 %) gegen normierte Kosten: Cache ee111aa363f9, 2012-2022

| | CAGR % alt | CAGR % normiert | Calmar alt | Calmar normiert | Kosten %/Jahr alt | Kosten %/Jahr normiert |
|---|---|---|---|---|---|---|
| **KI** | 18.40 | 12.30 | 0.80 | 0.57 | 1.09 | 2.30 |
| **Langfrist** | 53.10 | 58.70 | 1.20 | 1.37 | 1.13 | 2.96 |
| **Phasen** | 49.50 | 45.80 | 1.19 | 1.04 | 0.96 | 2.42 |
| **Risiko** | 47.40 | 42.40 | 0.72 | 0.65 | 3.62 | 3.05 |
| **K1** | 48.20 | 53.20 | 0.88 | 0.97 | 1.12 | 3.08 |
| **P−1** | 119.20 | 115.90 | 1.64 | 1.56 | 0.99 | 2.72 |
| **Chef** | 17.90 | 17.80 | 0.38 | 0.40 | – | – |
| **Bitcoin halten nach Kosten** | 108.90 | 108.80 | 1.28 | 1.28 | 0 | 0 |

## E1 Kern

### Kennzahlen: Cache ee111aa363f9, Gebühren normiert

| | Fenster | CAGR % | Max. DD % | Calmar | Trades | Gebühren | Kosten %/Jahr | Umschlag/Jahr | Ø investiert % | Kostenanteil % | Not-Aus | Δ Calmar halten | Δ Calmar P−1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **e1_kb3** | 2012-2022 | 64.40 | -61.40 | 1.05 | 20 | 1'026.97 | 1.06 | 1.24 | 33.50 | 4.40 | 4 | -0.23 | -0.51 |
| **e1_kb3+e1_kb5** | 2012-2022 | 63.40 | -61.40 | 1.03 | 18 | 888.19 | 0.99 | 1.17 | 33.10 | 4.10 | 5 | -0.25 | -0.53 |
| **e1_kb3+e1_kbe** | 2012-2022 | 75.50 | -61.40 | 1.23 | 28 | 1'912.97 | 1.38 | 1.63 | 38.30 | 4 | 5 | -0.05 | -0.33 |
| **P−1** | 2012-2022 | 115.90 | -74.20 | 1.56 | 17 | 44'455.29 | 2.72 | 3.20 | 61.30 | 9.10 | 0 | 0.28 | – |
| **Bitcoin halten nach Kosten** | 2012-2022 | 108.80 | -84.90 | 1.28 | 0 | 0.79 | 0 | 0 | 100 | 0 | 0 | – | -0.28 |
| **e1_kb3** | 2012-2019 | 86.30 | -61.40 | 1.40 | 14 | 392.12 | 1.15 | 1.35 | 38 | 2.80 | 3 | -0.34 | -0.68 |
| **e1_kb3+e1_kb5** | 2012-2019 | 84.70 | -61.40 | 1.38 | 12 | 359.54 | 1.11 | 1.31 | 37.80 | 2.80 | 3 | -0.36 | -0.70 |
| **e1_kb3+e1_kbe** | 2012-2019 | 84.20 | -61.40 | 1.37 | 19 | 615.38 | 1.87 | 2.19 | 39 | 4.70 | 4 | -0.37 | -0.71 |
| **P−1** | 2012-2019 | 154.60 | -74.20 | 2.08 | 12 | 10'310.95 | 2.69 | 3.16 | 65.20 | 5.90 | 0 | 0.34 | – |
| **Bitcoin halten nach Kosten** | 2012-2019 | 147.90 | -84.90 | 1.74 | 0 | 0.79 | 0 | 0 | 100 | 0 | 0 | – | -0.34 |
| **e1_kb3** | 2020-2022 | 17.80 | -40.20 | 0.44 | 6 | 4.39 | 1.01 | 1.19 | 21.60 | 6.80 | 1 | 0.03 | -0.27 |
| **e1_kb3+e1_kb5** | 2020-2022 | 17.20 | -41.10 | 0.42 | 6 | 4.37 | 1.01 | 1.19 | 21.70 | 7.10 | 1 | 0.01 | -0.29 |
| **e1_kb3+e1_kbe** | 2020-2022 | 54.40 | -39.20 | 1.39 | 9 | 9.82 | 1.23 | 1.45 | 36.30 | 3.80 | 1 | 0.98 | 0.68 |
| **P−1** | 2020-2022 | 39.20 | -55.20 | 0.71 | 5 | 19.41 | 2.74 | 3.22 | 50.90 | 10.80 | 0 | 0.30 | – |
| **Bitcoin halten nach Kosten** | 2020-2022 | 31.70 | -76.70 | 0.41 | 0 | 0.79 | 0.07 | 0.08 | 100 | 0.70 | 0 | – | -0.30 |

### Regel G gegen den Amtsinhaber e1_kb3

| | G1 Calmar +0,05 | G2 keine Hälfte schlechter | G3 Bootstrap ≥ 0,65 | G4 Kosten ≤ 3 %, Umschlag ≤ 4× | besteht |
|---|---|---|---|---|---|
| **e1_kb3+e1_kb5 · Cache ee111aa363f9** | ✗ 1.03 gegen 1.05 | ✗ 1.38 gegen 1.40 · 0.42 gegen 0.44 | ✗ P = 0.43 | ✓ 0.99 %, 1.17× | ✗ |
| **e1_kb3+e1_kbe · Cache ee111aa363f9** | ✓ 1.23 gegen 1.05 | ✗ 1.37 gegen 1.40 · 1.39 gegen 0.44 | ✓ P = 0.79 | ✓ 1.38 %, 1.63× | ✗ |

**Sieger: e1_kb3** (der Amtsinhaber bleibt)

**Sieger von E1: e1_kb3**

### Tor nach E1

| | Calmar ≥ 0,85 × L_dev | Kosten ≤ 3 % | besteht |
|---|---|---|---|
| **Cache ee111aa363f9** | ✗ 1.05 gegen 1.33 | ✓ 1.06 % | ✗ |

**Tor nicht bestanden:** Die Leiter wird abgebrochen; E6 prüft nur P−1 und K1 als Kandidaten.

## E6 Einmal-Prüfung

### Kennzahlen: Cache ee111aa363f9, Gebühren normiert

| | Fenster | CAGR % | Max. DD % | Calmar | Trades | Gebühren | Kosten %/Jahr | Umschlag/Jahr | Ø investiert % | Kostenanteil % | Not-Aus | Δ Calmar halten | Δ Calmar P−1 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **K1** | ab-2023Q1 (bis 2026-11-11) | 30.20 | -31 | 0.98 | 65 | 25.39 | 3.48 | 4.09 | 74.50 | 13.20 | 0 | – | – |
| **K1** | Crash-2022 (bis 2026-11-11) | 16.60 | -31.70 | 0.52 | 73 | 21.37 | 3.24 | 3.81 | 58.70 | 17 | 0 | – | – |
| **K1** | ab-2023Q2 (bis 2026-11-11) | 26.20 | -32.60 | 0.80 | 58 | 19.99 | 3.30 | 3.88 | 71.40 | 13.90 | 0 | – | – |
| **K1** | ab-2023Q3 (bis 2026-11-11) | 34.30 | -30.60 | 1.12 | 53 | 21.84 | 3.32 | 3.91 | 73 | 12 | 0 | – | – |
| **K1** | ab-2023Q4 (bis 2026-11-11) | 26.30 | -40.80 | 0.65 | 60 | 21.93 | 4.09 | 4.81 | 70.20 | 17.90 | 1 | – | – |
| **K1** | ab-2024Q1 (bis 2026-11-11) | 21.10 | -40.90 | 0.52 | 56 | 17.49 | 4.16 | 4.89 | 67.80 | 20.30 | 1 | – | – |
| **K1** | ab-2024Q2 (bis 2026-11-11) | 11 | -42.50 | 0.26 | 45 | 11.85 | 3.94 | 4.63 | 60.10 | 28.70 | 1 | – | – |
| **K1** | ab-2024Q3 (bis 2026-11-11) | 19.30 | -34.70 | 0.56 | 42 | 12.08 | 3.83 | 4.51 | 64.20 | 19.90 | 0 | – | – |
| **K1** | ab-2024Q4 (bis 2026-11-11) | 20.20 | -43 | 0.47 | 34 | 10.87 | 3.65 | 4.30 | 63.20 | 19.60 | 1 | – | – |
| **K1** | ab-2025Q1 (bis 2026-11-11) | 3.50 | -31.20 | 0.11 | 22 | 5.19 | 2.96 | 3.48 | 49.90 | 45.70 | 0 | – | – |
| **K1** | ab-2025Q2 (bis 2026-11-11) | 10.30 | -31.80 | 0.32 | 17 | 4.79 | 2.82 | 3.32 | 55.20 | 22.90 | 0 | – | – |
| **K1** | ab-2025Q3 (bis 2026-11-11) | 13.40 | -31.70 | 0.42 | 13 | 3.97 | 2.72 | 3.20 | 54.70 | 18.40 | 0 | – | – |
| **K1** | ab-2025Q4 (bis 2026-11-11) | -4.40 | -28.50 | -0.15 | 11 | 3.06 | 3.32 | 3.91 | 42.20 | – | 0 | – | – |

### Go-Regeln für K1

| | Cache ee111aa363f9 |
|---|---|
| **1. Calmar ≥ bester Vergleichs-Bot + 0,10** | ✗ 0.98 gegen – |
| **2. Calmar ≥ halten und ≥ P−1 − 0,05** | ✗ 0.98 gegen halten –, P−1 − 0,05 – |
| **3. Max. DD ≤ 0,6 × halten, auch Crash 2022** | ✗ -31.0 % gegen – %; Crash 2022 -31.7 % gegen – % |
| **4. CAGR ≥ ⅓ von halten** | ✗ 30.2 % gegen ⅓ × – % |
| **5. Kosten ≤ 3 %, Kostenanteil ≤ 25 %** | ✗ 3.48 %/Jahr, Kostenanteil 13.2 % |
| **6. in ≥ 8 von 12 Fenstern besser als der beste heutige Bot** | ✗ 0 von 12 |
| **7. bei E2-Flagge: ohne Not-Aus erfüllt 1-4** | ✓ keine E2-Flagge |
| **Go** | ✗ |
| **P−1 besser um mehr als 0,05** | ✗ – gegen 0.98 |
| **P−1 erfüllt die Regeln 1 und 3-5** | ✗ 1✗ 3✗ 4✗ 5✗ |

**Entscheid: No-Go**

Nur zur Information (dritte Quelle und Bootstrap):

| | Bootstrap P(besser als halten) |
|---|---|
| **Cache ee111aa363f9** | – |

