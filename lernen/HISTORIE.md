# 🕰️ Geschichts-Simulation: alle Bots über die ganze Krypto-Geschichte

Zeitraum: **18.08.2011 bis 28.10.2026**, Startkapital je Bot 1'000 (USD). Jeder Bot handelt mit allen Zeithorizonten, allen Coins (sobald es sie gibt), seinen Risikoregeln, Hebel und Zinsen. Ohne historische News. Vergangene Ergebnisse sind keine Garantie.

Gebühren: Kraken-Gebührenstaffel wie für ein Konto mit 1'000 (ab 0,80 % je Order; ein über die Jahre gewachsenes Simulationskonto bekommt keinen Mengenrabatt). Dazu Slippage je Order, Margin-Kosten und Liquidationsgebühr.

## Gesamtergebnis

| | 1️⃣ Langfrist-Bot (Hauptbot) | 2️⃣ KI-Bot (lernend, kurz bis lang) | 3️⃣ Risiko-Bot (aggressiv, Hebel 3×) | 5️⃣ Phasen-Bot (wählt kurz, mittel oder lang selbst) | 4️⃣ Chef-Bot |
|---|---|---|---|---|---|
| **Endkapital** | 330'756 | 7'163.08 | 69'062.98 | 26'287.47 | 5'239.18 |
| **Rendite %** | 32'975.60 | 616.31 | 6'806.30 | 2'528.75 | 424.34 |
| **Buy & Hold %** | 745'313.94 | 745'313.94 | 745'313.94 | 745'313.94 | – |
| **B&H Drawdown %** | -84.86 | -84.86 | -84.86 | -84.86 | – |
| **Max. Drawdown %** | -43.91 | -20.83 | -65.73 | -48.05 | -49.84 |
| **Sharpe** | 1.22 | 1.02 | 0.83 | 0.90 | – |
| **Trades** | 169 | 304 | 156 | 296 | – |
| **Trefferquote %** | 23.70 | 44.40 | 22.40 | 24.30 | – |
| **CRV** | 8.27 | 2.24 | 5.42 | 8.20 | – |
| **Expectancy** | 1'572.07 | 20.59 | 339.99 | 79.84 | – |
| **Profit Factor** | 2.57 | 1.79 | 1.57 | 2.64 | – |
| **Max. Verlustserie** | 20 | 13 | 22 | 24 | – |
| **Not-Aus** | 8 | 6 | 0 | 5 | – |
| **Liquidationen** | 0 | 0 | 0 | 0 | – |

## Entwicklung und Prüfung

Die Einstellungen der Bots wurden nur mit den Jahren **bis 2022** gewählt. Die Jahre **ab 2023** waren dabei weggesperrt und zeigen, wie die Bots auf unbekannten Kursen abschneiden.

| | bis 2022: pro Jahr % | bis 2022: Max. DD % | bis 2022: Treffer % | bis 2022: Kosten %/Jahr | ab 2023: pro Jahr % | ab 2023: Max. DD % | ab 2023: Treffer % | ab 2023: Kosten %/Jahr |
|---|---|---|---|---|---|---|---|---|
| **1️⃣ Langfrist-Bot (Hauptbot)** | 56.30 | -42.90 | 23.50 | 2.80 | 20.80 | -35 | 23.90 | 2.60 |
| **2️⃣ KI-Bot (lernend, kurz bis lang)** | 15.70 | -19.40 | 45.70 | 2.50 | 8.40 | -17.90 | 42.40 | 4.40 |
| **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** | 40.20 | -65.70 | 22.90 | 2.90 | 10.90 | -40.50 | 21.70 | 5.30 |
| **5️⃣ Phasen-Bot (wählt kurz, mittel oder lang selbst)** | 26.40 | -44.20 | 23 | 2.20 | 17.10 | -35.70 | 25 | 4.30 |
| **Bitcoin halten** | 90.40 | -84.90 | – | – | 51.50 | -53.10 | – | – |

## 1️⃣ Langfrist-Bot (Hauptbot)

**Jahr für Jahr**

| | Rendite % | Kapital Ende | Trades | Trefferquote % |
|---|---|---|---|---|
| **2011** | 0 | 1'000 | 0 | – |
| **2012** | 17.30 | 1'173 | 0 | – |
| **2013** | 429.80 | 6'213 | 3 | 66.70 |
| **2014** | -18.80 | 5'046 | 4 | 25 |
| **2015** | 10.90 | 5'597 | 1 | 0 |
| **2016** | 37.50 | 7'695 | 0 | – |
| **2017** | 442.80 | 41'771 | 4 | 25 |
| **2018** | -26.90 | 30'519 | 12 | 16.70 |
| **2019** | 7.40 | 32'762 | 8 | 25 |
| **2020** | 54.60 | 50'638 | 18 | 22.20 |
| **2021** | 321.20 | 213'302 | 28 | 28.60 |
| **2022** | -24.80 | 160'310 | 20 | 15 |
| **2023** | 16.80 | 187'248 | 12 | 16.70 |
| **2024** | 32.60 | 248'285 | 26 | 15.40 |
| **2025** | 43 | 355'068 | 27 | 37 |
| **2026** | -6.80 | 330'756 | 6 | 16.70 |

**Nach Zeithorizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **lang** | 169 | 23.70 | 265'679 | 2.57 |

**Nach Coin**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **BNB/USD** | 25 | 20 | 98'829 | 3.42 |
| **BTC/USD** | 25 | 44 | 71'212 | 7.73 |
| **ETH/USD** | 14 | 50 | 31'482 | 6.64 |
| **HYPE/USD** | 3 | 0 | -3'343 | 0 |
| **SOL/USD** | 4 | 50 | 35'738 | 7.73 |
| **TRX/USD** | 17 | 23.50 | 31'387 | 2.78 |
| **XRP/USD** | 46 | 13 | -33'312 | 0.26 |
| **ZEC/USD** | 35 | 14.30 | 33'685 | 1.81 |

**Nach Richtung**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **long** | 169 | 23.70 | 265'679 | 2.57 |

**Nach Ausstiegsgrund**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **Not-Aus** | 19 | 47.40 | 133'185 | 15 |
| **Signal** | 146 | 19.90 | 6'266 | 1.04 |
| **Stop-Loss** | 2 | 0 | -11'763 | 0 |
| **Take-Profit** | 2 | 100 | 137'990 | – |

## 2️⃣ KI-Bot (lernend, kurz bis lang)

**Jahr für Jahr**

| | Rendite % | Kapital Ende | Trades | Trefferquote % |
|---|---|---|---|---|
| **2011** | 0 | 1'000 | 0 | – |
| **2012** | 11.60 | 1'116 | 7 | 42.90 |
| **2013** | 53.20 | 1'709 | 16 | 75 |
| **2014** | -5.40 | 1'617 | 5 | 0 |
| **2015** | 8.30 | 1'751 | 7 | 57.10 |
| **2016** | 15.90 | 2'030 | 8 | 50 |
| **2017** | 31.90 | 2'677 | 20 | 50 |
| **2018** | -9.10 | 2'434 | 13 | 38.50 |
| **2019** | 0.10 | 2'437 | 14 | 35.70 |
| **2020** | 22.30 | 2'979 | 37 | 43.20 |
| **2021** | 85.30 | 5'521 | 52 | 50 |
| **2022** | -4.80 | 5'253 | 7 | 0 |
| **2023** | 1.60 | 5'338 | 11 | 45.50 |
| **2024** | 20 | 6'406 | 45 | 37.80 |
| **2025** | 1.30 | 6'491 | 40 | 47.50 |
| **2026** | 10.40 | 7'163 | 22 | 40.90 |

**Nach Zeithorizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **lang** | 299 | 43.50 | 6'196 | 1.78 |
| **mittel** | 5 | 100 | 62 | – |

**Nach Coin**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **BNB/USD** | 32 | 50 | 558 | 1.60 |
| **BTC/USD** | 90 | 51.10 | 2'456 | 2.71 |
| **ETH/USD** | 35 | 45.70 | 160 | 1.16 |
| **HYPE/USD** | 3 | 66.70 | 291 | 20.32 |
| **SOL/USD** | 15 | 60 | 1'050 | 3.73 |
| **TRX/USD** | 38 | 42.10 | 46 | 1.03 |
| **XRP/USD** | 53 | 32.10 | 471 | 1.34 |
| **ZEC/USD** | 38 | 34.20 | 1'226 | 1.90 |

**Nach Richtung**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **long** | 304 | 44.40 | 6'258 | 1.79 |

**Nach Ausstiegsgrund**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **Not-Aus** | 12 | 25 | -280 | 0.10 |
| **Signal** | 141 | 26.20 | -2'439 | 0.30 |
| **Stop auf Einstand** | 1 | 100 | 5 | – |
| **Stop-Loss** | 56 | 0 | -4'121 | 0 |
| **Take-Profit** | 92 | 100 | 13'067 | – |
| **Vorrang lang** | 2 | 100 | 25 | – |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

**Jahr für Jahr**

| | Rendite % | Kapital Ende | Trades | Trefferquote % |
|---|---|---|---|---|
| **2011** | 0 | 1'000 | 0 | – |
| **2012** | 23 | 1'230 | 0 | – |
| **2013** | 285.90 | 4'747 | 2 | 100 |
| **2014** | -22.30 | 3'687 | 4 | 25 |
| **2015** | 23.30 | 4'544 | 1 | 0 |
| **2016** | 68.10 | 7'637 | 0 | – |
| **2017** | 690.50 | 60'375 | 4 | 25 |
| **2018** | -43.40 | 34'169 | 11 | 18.20 |
| **2019** | 11.10 | 37'945 | 8 | 37.50 |
| **2020** | 4.20 | 39'554 | 16 | 18.80 |
| **2021** | 76.60 | 69'838 | 27 | 25.90 |
| **2022** | -33.40 | 46'509 | 23 | 13 |
| **2023** | 13.30 | 52'710 | 11 | 18.20 |
| **2024** | 39.60 | 73'582 | 21 | 19 |
| **2025** | -7.40 | 68'133 | 20 | 35 |
| **2026** | 1.40 | 69'063 | 8 | 0 |

**Nach Zeithorizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **lang** | 155 | 21.90 | 52'487 | 1.56 |
| **mittel** | 1 | 100 | 551 | – |

**Nach Coin**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **BNB/USD** | 24 | 16.70 | -15'576 | 0.21 |
| **BTC/USD** | 23 | 43.50 | 39'160 | 6.42 |
| **ETH/USD** | 14 | 35.70 | 27'646 | 4.65 |
| **HYPE/USD** | 1 | 0 | -1'026 | 0 |
| **SOL/USD** | 3 | 66.70 | 10'677 | 3.82 |
| **TRX/USD** | 17 | 23.50 | 22'459 | 3.11 |
| **XRP/USD** | 39 | 12.80 | -14'464 | 0.40 |
| **ZEC/USD** | 35 | 14.30 | -15'838 | 0.18 |

**Nach Richtung**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **long** | 156 | 22.40 | 53'038 | 1.57 |

**Nach Ausstiegsgrund**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **Signal** | 149 | 21.50 | 34'655 | 1.44 |
| **Stop auf Einstand** | 1 | 100 | 551 | – |
| **Stop-Loss** | 4 | 0 | -13'994 | 0 |
| **Take-Profit** | 2 | 100 | 31'826 | – |

## 5️⃣ Phasen-Bot (wählt kurz, mittel oder lang selbst)

**Jahr für Jahr**

| | Rendite % | Kapital Ende | Trades | Trefferquote % |
|---|---|---|---|---|
| **2011** | 0 | 1'000 | 0 | – |
| **2012** | 4.30 | 1'043 | 0 | – |
| **2013** | 62.30 | 1'693 | 3 | 66.70 |
| **2014** | -6.20 | 1'588 | 4 | 25 |
| **2015** | 4.50 | 1'660 | 1 | 0 |
| **2016** | 15.90 | 1'923 | 0 | – |
| **2017** | 141.90 | 4'653 | 4 | 25 |
| **2018** | -13.30 | 4'036 | 11 | 18.20 |
| **2019** | 10.10 | 4'443 | 8 | 25 |
| **2020** | 43.30 | 6'369 | 19 | 21.10 |
| **2021** | 193.60 | 18'698 | 28 | 28.60 |
| **2022** | -23.10 | 14'371 | 22 | 13.60 |
| **2023** | -2.50 | 14'008 | 114 | 22.80 |
| **2024** | 27.40 | 17'842 | 47 | 25.50 |
| **2025** | 41.30 | 25'207 | 27 | 40.70 |
| **2026** | 4.30 | 26'287 | 8 | 0 |

**Nach Zeithorizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **kurz** | 1 | 100 | 55 | – |
| **lang** | 163 | 24.50 | 24'905 | 3.25 |
| **mittel** | 132 | 23.50 | -1'326 | 0.60 |

**Nach Coin**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **BNB/USD** | 51 | 21.60 | 6'123 | 2.72 |
| **BTC/USD** | 30 | 46.70 | 5'489 | 6.27 |
| **ETH/USD** | 23 | 39.10 | 3'964 | 5.86 |
| **HYPE/USD** | 3 | 0 | -274 | 0 |
| **SOL/USD** | 14 | 21.40 | 1'856 | 14.10 |
| **TRX/USD** | 50 | 16 | 2'385 | 2.17 |
| **XRP/USD** | 80 | 26.20 | -1'472 | 0.56 |
| **ZEC/USD** | 45 | 13.30 | 5'563 | 2.74 |

**Nach Richtung**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **long** | 296 | 24.30 | 23'634 | 2.64 |

**Nach Marktphase und Horizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **('Aufwärtstrend, ruhig', 'lang')** | 36 | 33.30 | 11'621 | 4.74 |
| **('Aufwärtstrend, ruhig', 'mittel')** | 63 | 23.80 | -596 | 0.38 |
| **('Aufwärtstrend, wild', 'lang')** | 46 | 21.70 | -318 | 0.89 |
| **('Aufwärtstrend, wild', 'mittel')** | 27 | 22.20 | -244 | 0.68 |
| **('Seitwärts, ruhig', 'kurz')** | 1 | 100 | 55 | – |
| **('Seitwärts, ruhig', 'lang')** | 65 | 23.10 | 14'314 | 4.47 |
| **('Seitwärts, ruhig', 'mittel')** | 9 | 33.30 | 10 | 1.06 |
| **('Seitwärts, wild', 'lang')** | 16 | 18.80 | -711 | 0.16 |
| **('Seitwärts, wild', 'mittel')** | 33 | 21.20 | -495 | 0.66 |

**Nach Ausstiegsgrund**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **Nachlauf-Stop** | 44 | 63.60 | 1'843 | 13.54 |
| **Nachlauf-Stop (Gap)** | 3 | 66.70 | 33 | 38.13 |
| **Not-Aus** | 15 | 46.70 | 10'646 | 7.52 |
| **Phase gekippt** | 6 | 0 | -293 | 0 |
| **Signal** | 177 | 18.10 | 2'249 | 1.22 |
| **Stop-Loss** | 45 | 0 | -2'242 | 0 |
| **Take-Profit** | 3 | 100 | 11'487 | – |
| **Vorrang lang** | 3 | 0 | -90 | 0 |
