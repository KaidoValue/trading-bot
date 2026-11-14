# 🕰️ Geschichts-Simulation: alle Bots über die ganze Krypto-Geschichte

Zeitraum: **18.08.2011 bis 11.11.2026**, Startkapital je Bot 100 (USD). Jeder Bot handelt mit allen Zeithorizonten, seinen Coins (sobald es sie gibt), seinen Risikoregeln, Hebel und Zinsen. Ohne historische News. Vergangene Ergebnisse sind keine Garantie.

Kurse von bitstamp (USD), binance (USDT), binanceus (USD), kucoin (USDT). Fingerabdruck der 16 Kursdateien (SHA-256): `1e0e4b19fab31c12fe60f2d8db34c04e2710d4a76c1c6a2a4a8ce0dc8e6dd06e`

Gebühren: Kraken-Gebührenstaffel wie für ein Konto mit dem Startkapital (ab 0,80 % je Order; ein über die Jahre gewachsenes Simulationskonto bekommt keinen Mengenrabatt). Dazu Slippage je Order, Margin-Kosten und Liquidationsgebühr.

## Gesamtergebnis

| | 1️⃣ Langfrist-Bot (Hauptbot) | 2️⃣ KI-Bot (lernend, kurz bis lang) | 3️⃣ Risiko-Bot (aggressiv, Hebel 3×) | 5️⃣ Phasen-Bot (wählt kurz, mittel oder lang selbst) | 4️⃣ Chef-Bot |
|---|---|---|---|---|---|
| **Endkapital** | 31'712.27 | 428 | 5'228.14 | 4'788.66 | 563.42 |
| **Rendite %** | 31'612.27 | 328 | 5'128.14 | 4'688.66 | 463.87 |
| **Buy & Hold %** | 676'027.71 | 676'027.71 | 676'027.71 | 676'027.71 | – |
| **B&H nach Kosten %** | 670'326.40 | 670'326.40 | 670'326.40 | 670'326.40 | – |
| **B&H Drawdown %** | -84.86 | -84.86 | -84.86 | -84.86 | – |
| **Max. Drawdown %** | -43.77 | -23.79 | -65.73 | -61.99 | -47.91 |
| **Sharpe** | 1.20 | 0.93 | 0.79 | 1.03 | – |
| **Trades** | 175 | 245 | 155 | 417 | – |
| **Trefferquote %** | 22.90 | 35.10 | 20 | 22.30 | – |
| **CRV** | 8.21 | 3.09 | 5.93 | 5.23 | – |
| **Expectancy** | 155.38 | 1.35 | 29.25 | 9.81 | – |
| **Profit Factor** | 2.43 | 1.67 | 1.48 | 1.50 | – |
| **Max. Verlustserie** | 21 | 13 | 21 | 24 | – |
| **Not-Aus** | 8 | 5 | 0 | 5 | – |
| **Liquidationen** | 0 | 0 | 0 | 0 | – |

## Entwicklung und Prüfung

Die Einstellungen der Bots wurden nur mit den Jahren **bis 2022** gewählt. Die Jahre **ab 2023** waren dabei weggesperrt und zeigen, wie die Bots auf unbekannten Kursen abschneiden.

Jeder Abschnitt ist ein Ausschnitt aus dem Lauf über die ganze Geschichte. Kosten = Gebühren + Slippage + Zinsen, Umschlag = gehandelter Wert, beide pro Jahr im Verhältnis zum Ø Kapital; Kostenanteil = Kosten in % des Gewinns vor Kosten. «Bitcoin halten nach Kosten»: ein Kauf am ersten Tag mit 0,80 % Gebühr und 0,05 % Slippage, danach nur halten.

### bis 2022

| | pro Jahr % | Max. DD % | Calmar | Treffer % | Trades je Coin/Jahr | Gebühren | Kosten %/Jahr | Umschlag/Jahr | Ø investiert % | Kostenanteil % |
|---|---|---|---|---|---|---|---|---|---|---|
| **1️⃣ Langfrist-Bot (Hauptbot)** | 56.30 | -42.90 | 1.31 | 23.50 | 2.69 | 1'404.49 | 2.95 | 3.47 | 25.60 | 8.60 |
| **2️⃣ KI-Bot (lernend, kurz bis lang)** | 11.90 | -21.50 | 0.55 | 40 | 3.71 | 52.24 | 2.27 | 2.67 | 6.90 | 17.70 |
| **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** | 40.80 | -65.70 | 0.62 | 22.90 | 2.64 | 820.35 | 3.05 | 3.58 | 33.20 | 15.40 |
| **5️⃣ Phasen-Bot (wählt kurz, mittel oder lang selbst)** | 44 | -44.20 | 1 | 22.50 | 2.80 | 564.38 | 2.42 | 2.85 | 20.10 | 8.80 |
| **Bitcoin halten** | 90.40 | -84.90 | 1.07 | – | – | – | – | – | – | – |
| **Bitcoin halten nach Kosten** | 90.30 | -84.90 | 1.06 | – | – | 0.79 | 0 | 0 | 100 | 0 |

### ab 2023

| | pro Jahr % | Max. DD % | Calmar | Treffer % | Trades je Coin/Jahr | Gebühren | Kosten %/Jahr | Umschlag/Jahr | Ø investiert % | Kostenanteil % |
|---|---|---|---|---|---|---|---|---|---|---|
| **1️⃣ Langfrist-Bot (Hauptbot)** | 19.40 | -35.40 | 0.55 | 22.10 | 2.66 | 2'828.34 | 3.20 | 3.76 | 55.30 | 16.10 |
| **2️⃣ KI-Bot (lernend, kurz bis lang)** | 4.70 | -16.50 | 0.29 | 29.10 | 3.80 | 74.79 | 4.99 | 5.86 | 19.60 | 53.10 |
| **3️⃣ Risiko-Bot (aggressiv, Hebel 3×)** | 1.70 | -48.80 | 0.04 | 15.30 | 2.04 | 783.14 | 8.59 | 4.07 | 56.90 | 86.20 |
| **5️⃣ Phasen-Bot (wählt kurz, mittel oder lang selbst)** | -7 | -39 | -0.18 | 22.20 | 10.87 | 2'138.92 | 10.73 | 12.63 | 28 | 315.40 |
| **Bitcoin halten** | 47.10 | -53.10 | 0.89 | – | – | – | – | – | – | – |
| **Bitcoin halten nach Kosten** | 46.80 | -53.10 | 0.88 | – | – | 0.79 | 0.05 | 0.06 | 100 | 0.20 |

## 1️⃣ Langfrist-Bot (Hauptbot)

**Jahr für Jahr**

| | Rendite % | Kapital Ende | Trades | Trefferquote % |
|---|---|---|---|---|
| **2011** | 0 | 100 | 0 | – |
| **2012** | 17.30 | 117 | 0 | – |
| **2013** | 429.80 | 621 | 3 | 66.70 |
| **2014** | -18.80 | 505 | 4 | 25 |
| **2015** | 10.90 | 560 | 1 | 0 |
| **2016** | 37.50 | 770 | 0 | – |
| **2017** | 442.80 | 4'177 | 4 | 25 |
| **2018** | -26.90 | 3'052 | 12 | 16.70 |
| **2019** | 7.40 | 3'276 | 8 | 25 |
| **2020** | 54.40 | 5'058 | 18 | 22.20 |
| **2021** | 321.20 | 21'304 | 28 | 28.60 |
| **2022** | -24.80 | 16'012 | 20 | 15 |
| **2023** | 21.60 | 19'474 | 13 | 15.40 |
| **2024** | 33.20 | 25'935 | 26 | 15.40 |
| **2025** | 47.40 | 38'228 | 27 | 37 |
| **2026** | -17 | 31'712 | 11 | 9.10 |

**Nach Zeithorizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **lang** | 175 | 22.90 | 27'191 | 2.43 |

**Nach Coin**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **BNB/USD** | 26 | 19.20 | 9'770 | 3.30 |
| **BTC/USD** | 25 | 44 | 7'074 | 7.12 |
| **ETH/USD** | 15 | 46.70 | 2'485 | 3.06 |
| **HYPE/USD** | 3 | 0 | -352 | 0 |
| **SOL/USD** | 6 | 33.30 | 3'501 | 6.65 |
| **TRX/USD** | 17 | 23.50 | 4'110 | 3.10 |
| **XRP/USD** | 48 | 12.50 | -4'021 | 0.23 |
| **ZEC/USD** | 35 | 14.30 | 4'624 | 2.09 |

**Nach Richtung**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **long** | 175 | 22.90 | 27'191 | 2.43 |

**Nach Ausstiegsgrund**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **Not-Aus** | 19 | 47.40 | 14'954 | 16.22 |
| **Signal** | 152 | 19.10 | -375 | 0.98 |
| **Stop-Loss** | 2 | 0 | -1'176 | 0 |
| **Take-Profit** | 2 | 100 | 13'788 | – |

## 2️⃣ KI-Bot (lernend, kurz bis lang)

**Jahr für Jahr**

| | Rendite % | Kapital Ende | Trades | Trefferquote % |
|---|---|---|---|---|
| **2011** | 0 | 100 | 0 | – |
| **2012** | 10.80 | 111 | 10 | 30 |
| **2013** | 39.50 | 155 | 13 | 76.90 |
| **2014** | -4.30 | 148 | 5 | 0 |
| **2015** | 6 | 157 | 6 | 50 |
| **2016** | 17.70 | 184 | 6 | 66.70 |
| **2017** | 30.90 | 241 | 10 | 70 |
| **2018** | -1.70 | 237 | 1 | 0 |
| **2019** | 11.70 | 265 | 13 | 30.80 |
| **2020** | -3.30 | 256 | 23 | 21.70 |
| **2021** | 50.70 | 386 | 37 | 48.60 |
| **2022** | -7.30 | 358 | 11 | 0 |
| **2023** | 0.20 | 359 | 15 | 13.30 |
| **2024** | 25.40 | 450 | 42 | 35.70 |
| **2025** | 4.60 | 470 | 40 | 35 |
| **2026** | -9 | 428 | 13 | 7.70 |

**Nach Zeithorizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **lang** | 245 | 35.10 | 331 | 1.67 |

**Nach Coin**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **BNB/USD** | 30 | 30 | 57 | 1.71 |
| **BTC/USD** | 94 | 41.50 | 167 | 2.29 |
| **ETH/USD** | 35 | 31.40 | 9 | 1.08 |
| **HYPE/USD** | 4 | 0 | -8 | 0 |
| **SOL/USD** | 4 | 75 | 1 | 1.07 |
| **TRX/USD** | 36 | 30.60 | 45 | 1.56 |
| **XRP/USD** | 27 | 18.50 | -1 | 0.99 |
| **ZEC/USD** | 15 | 53.30 | 62 | 3.80 |

**Nach Richtung**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **long** | 245 | 35.10 | 331 | 1.67 |

**Nach Ausstiegsgrund**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **Not-Aus** | 15 | 26.70 | -22 | 0.20 |
| **Signal** | 134 | 14.20 | -197 | 0.20 |
| **Stop-Loss** | 33 | 0 | -219 | 0 |
| **Take-Profit** | 63 | 100 | 769 | – |

## 3️⃣ Risiko-Bot (aggressiv, Hebel 3×)

**Jahr für Jahr**

| | Rendite % | Kapital Ende | Trades | Trefferquote % |
|---|---|---|---|---|
| **2011** | 0 | 100 | 0 | – |
| **2012** | 23 | 123 | 0 | – |
| **2013** | 285.90 | 475 | 2 | 100 |
| **2014** | -22.30 | 369 | 4 | 25 |
| **2015** | 23.30 | 454 | 1 | 0 |
| **2016** | 68.10 | 764 | 0 | – |
| **2017** | 690.50 | 6'037 | 4 | 25 |
| **2018** | -43.40 | 3'417 | 11 | 18.20 |
| **2019** | 11.10 | 3'795 | 8 | 37.50 |
| **2020** | 8.60 | 4'120 | 16 | 6.20 |
| **2021** | 75.80 | 7'243 | 27 | 33.30 |
| **2022** | -32.40 | 4'897 | 23 | 13 |
| **2023** | 5.30 | 5'155 | 8 | 25 |
| **2024** | 41.40 | 7'289 | 24 | 16.70 |
| **2025** | -3.30 | 7'049 | 14 | 21.40 |
| **2026** | -25.80 | 5'228 | 13 | 0 |

**Nach Zeithorizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **lang** | 153 | 19 | 4'429 | 1.47 |
| **mittel** | 2 | 100 | 104 | – |

**Nach Coin**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **BNB/USD** | 19 | 21.10 | -864 | 0.26 |
| **BTC/USD** | 23 | 39.10 | 4'007 | 6.09 |
| **ETH/USD** | 15 | 33.30 | 2'448 | 3.56 |
| **HYPE/USD** | 1 | 0 | -106 | 0 |
| **SOL/USD** | 5 | 20 | 247 | 1.40 |
| **TRX/USD** | 16 | 25 | 2'246 | 2.89 |
| **XRP/USD** | 41 | 14.60 | -1'951 | 0.28 |
| **ZEC/USD** | 35 | 5.70 | -1'493 | 0.19 |

**Nach Richtung**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **long** | 155 | 20 | 4'534 | 1.48 |

**Nach Ausstiegsgrund**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **Signal** | 148 | 18.90 | 2'374 | 1.28 |
| **Stop auf Einstand** | 2 | 100 | 104 | – |
| **Stop-Loss** | 4 | 0 | -840 | 0 |
| **Take-Profit** | 1 | 100 | 2'895 | – |

## 5️⃣ Phasen-Bot (wählt kurz, mittel oder lang selbst)

**Jahr für Jahr**

| | Rendite % | Kapital Ende | Trades | Trefferquote % |
|---|---|---|---|---|
| **2011** | 0 | 100 | 0 | – |
| **2012** | 31.70 | 132 | 1 | 0 |
| **2013** | 466.70 | 747 | 4 | 50 |
| **2014** | -6.20 | 700 | 4 | 25 |
| **2015** | 4.50 | 732 | 1 | 0 |
| **2016** | 15.90 | 848 | 0 | – |
| **2017** | 141.90 | 2'052 | 4 | 25 |
| **2018** | -13.30 | 1'780 | 11 | 18.20 |
| **2019** | 10.10 | 1'959 | 8 | 25 |
| **2020** | 43.30 | 2'808 | 19 | 21.10 |
| **2021** | 193.80 | 8'250 | 28 | 28.60 |
| **2022** | -23.10 | 6'341 | 22 | 13.60 |
| **2023** | -2.20 | 6'204 | 124 | 22.60 |
| **2024** | -7.90 | 5'715 | 120 | 24.20 |
| **2025** | -20.60 | 4'538 | 58 | 20.70 |
| **2026** | 5.50 | 4'789 | 13 | 7.70 |

**Nach Zeithorizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **kurz** | 2 | 50 | 15 | 3.53 |
| **lang** | 160 | 23.10 | 5'826 | 2.20 |
| **mittel** | 255 | 21.60 | -1'750 | 0.47 |

**Nach Coin**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **BNB/USD** | 108 | 19.40 | 2'056 | 1.82 |
| **BTC/USD** | 32 | 43.80 | 2'730 | 6.57 |
| **ETH/USD** | 37 | 24.30 | 1'327 | 2.67 |
| **HYPE/USD** | 3 | 0 | -55 | 0 |
| **SOL/USD** | 24 | 20.80 | 793 | 7.86 |
| **TRX/USD** | 58 | 20.70 | -637 | 0.33 |
| **XRP/USD** | 100 | 21 | -1'282 | 0.39 |
| **ZEC/USD** | 55 | 20 | -840 | 0.27 |

**Nach Richtung**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **long** | 417 | 22.30 | 4'091 | 1.50 |

**Nach Marktphase und Horizont**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **('Aufwärtstrend, ruhig', 'lang')** | 41 | 31.70 | 230 | 1.18 |
| **('Aufwärtstrend, ruhig', 'mittel')** | 90 | 24.40 | -660 | 0.45 |
| **('Aufwärtstrend, wild', 'kurz')** | 1 | 0 | -6 | 0 |
| **('Aufwärtstrend, wild', 'lang')** | 40 | 17.50 | -164 | 0.85 |
| **('Aufwärtstrend, wild', 'mittel')** | 103 | 17.50 | -868 | 0.37 |
| **('Seitwärts, ruhig', 'kurz')** | 1 | 100 | 21 | – |
| **('Seitwärts, ruhig', 'lang')** | 64 | 23.40 | 6'023 | 3.88 |
| **('Seitwärts, ruhig', 'mittel')** | 21 | 28.60 | -68 | 0.56 |
| **('Seitwärts, wild', 'lang')** | 15 | 13.30 | -263 | 0.21 |
| **('Seitwärts, wild', 'mittel')** | 41 | 22 | -155 | 0.74 |

**Nach Ausstiegsgrund**

| | Trades | Trefferquote % | Ergebnis | Profit Factor |
|---|---|---|---|---|
| **Nachlauf-Stop** | 70 | 71.40 | 1'358 | 16.44 |
| **Nachlauf-Stop (Gap)** | 3 | 66.70 | 122 | 122.29 |
| **Not-Aus** | 16 | 43.80 | 1'366 | 2.74 |
| **Phase gekippt** | 9 | 0 | -139 | 0 |
| **Signal** | 202 | 14.90 | -955 | 0.78 |
| **Stop-Loss** | 109 | 0 | -2'689 | 0 |
| **Stop-Loss (Gap)** | 1 | 0 | -1 | 0 |
| **Take-Profit** | 3 | 100 | 5'067 | – |
| **Vorrang lang** | 4 | 25 | -39 | 0.03 |
