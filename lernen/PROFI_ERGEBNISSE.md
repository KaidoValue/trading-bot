# Profi-Bot: Ergebnisse der Auswertung

Aus 16 Ergebnisdateien in `lernen/profi/` (`python -m tradingbot profi --zusammenfassen`). Jedes Fenster ist ein frischer Start mit dem Startkapital. Calmar = CAGR / |Max. DD|. Entschieden wird nach den vorab registrierten Regeln, nur mit normierten Gebühren und in jedem Haupt-Cache; andere Quellen zählen nur zur Information. ✓ erfüllt, ✗ nicht erfüllt oder Zahl fehlt (–).

Vorab-Registrierung: [PROFI_PLAN.md](PROFI_PLAN.md), eingefrorene Fassung Commit `dce942282a04b2eeda025a315ed361e805dce2b8`.

## Caches

| | Quellen | Börsen der Kursdateien | eingefroren | Läufe | zählt für | Commits |
|---|---|---|---|---|---|---|
| **Cache ee111aa363f9** | bitstamp (USD), binance (USDT), binanceus (USD), kucoin (USDT) | binanceus, bitstamp, kucoin | ja | 16 | Entscheide | 4fe71ac40526, cda7f449de55 |

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

