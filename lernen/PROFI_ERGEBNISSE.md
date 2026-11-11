# Profi-Bot: Ergebnisse der Auswertung

Aus 23 Ergebnisdateien in `lernen/profi/` (`python -m tradingbot profi --zusammenfassen`). Jedes Fenster ist ein frischer Start mit dem Startkapital. Calmar = CAGR / |Max. DD|. Entschieden wird nach den vorab registrierten Regeln, nur mit normierten Gebühren und in jedem Haupt-Cache; andere Quellen zählen nur zur Information. ✓ erfüllt, ✗ nicht erfüllt oder Zahl fehlt (–).

Vorab-Registrierung: [PROFI_PLAN.md](PROFI_PLAN.md), eingefrorene Fassung Commit `dce942282a04b2eeda025a315ed361e805dce2b8`.

## Caches

| | Quellen | Börsen der Kursdateien | eingefroren | Läufe | zählt für | Commits |
|---|---|---|---|---|---|---|
| **Cache ee111aa363f9** | bitstamp (USD), binance (USDT), binanceus (USD), kucoin (USDT) | binanceus, bitstamp, kucoin | ja | 23 | Entscheide | 39961fe3b194, c011d2d4df76, cda7f449de55 |

Nur ein Haupt-Cache: Die Entscheide stützen sich auf eine einzige Datenquelle (Schwäche).

## E0 Messlatte

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

