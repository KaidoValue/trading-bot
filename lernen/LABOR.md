# Strategie-Labor

Letzter Lauf: 08.11.2026 10:28 UTC · Daten: BTC/USD, 1h-Kerzen, 08.11.2024 bis 08.11.2026

Die KI erfindet aus den vorhandenen Bausteinen (Indikatoren, Kerzenmuster, Marktstruktur) neue Strategien. Standard: Suche auf den älteren 50 %; danach zwei getrennte Validierungsfenster und ein späterer Holdout. Prüfung mit Trader/PaperBroker, Gebühren, Slippage, Stops und Risikolimits. Erforderlich: mindestens 30 abgeschlossene Trades insgesamt, positive Rendite und Profit Factor >=1,2 in jedem Fenster, höchstens 15 % Drawdown und insgesamt besser als kostenbereinigtes Halten. Ein Bestehen startet nur die Paper-Probe: mindestens 14 Tage nach Fund und 20 regulär geschlossene Trades. Erst Status active darf im KI-Bot mitstimmen.

## Kandidaten dieses Laufs

| Regel | Training | Prüfung | Trades (Prüfung) | Bitcoin halten (Prüfung) | Ergebnis |
|---|---|---|---|---|---|
| Kaufen, wenn MACD-Histogramm steigt. Verkaufen, wenn Kurs unter dem unteren Bollinger-Band UND bullishes Kerzenmuster. | +4.2 % | +0.0 % | 0 | -29.7 % | durchgefallen |
| Kaufen, wenn bearishes Kerzenmuster. Verkaufen, wenn Kurs unter dem unteren Bollinger-Band UND bullishes Kerzenmuster. | +3.0 % | +0.0 % | 0 | -29.7 % | durchgefallen |
| Kaufen, wenn Marktstruktur aufwärts (höhere Hochs/Tiefs). Verkaufen, wenn Kurs unter dem unteren Bollinger-Band UND bullishes Kerzenmuster. | +2.0 % | +0.0 % | 0 | -29.7 % | durchgefallen |
| Kaufen, wenn MACD-Histogramm positiv. Verkaufen, wenn Kurs unter dem unteren Bollinger-Band UND bullishes Kerzenmuster. | -0.9 % | +0.0 % | 0 | -29.7 % | durchgefallen |
| Kaufen, wenn Kurs im oberen Teil der Range (Premium). Verkaufen, wenn Kurs unter dem unteren Bollinger-Band UND bullishes Kerzenmuster. | -3.3 % | +0.0 % | 0 | -29.7 % | durchgefallen |

## Strategie-Bibliothek und Freigabestatus

| Name | Regel | Prüfung | Gefunden am | Status |
|---|---|---|---|---|
| labor_3 | Kaufen, wenn Kurs unter der 200er-Linie UND Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn Marktstruktur abwärts UND bullishe RSI-Divergenz. | +21.0 % | 2026-10-23 | legacy |
| labor_4 | Kaufen, wenn Kurs unter der 200er-Linie UND Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn bullishe RSI-Divergenz. | +17.9 % | 2026-10-23 | legacy |
| labor_2 | Kaufen, wenn Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn Kurs im oberen Teil der Range (Premium) UND bullishe RSI-Divergenz. | +14.8 % | 2026-10-23 | legacy |
| labor_1 | Kaufen, wenn Kurs unter der 200er-Linie UND bearishes Kerzenmuster UND Kurs unter dem unteren Bollinger-Band. Verkaufen, wenn Kurs im oberen Teil der Range (Premium) UND bullishe RSI-Divergenz. | +10.4 % | 2026-10-23 | legacy |
| labor_5 | Kaufen, wenn bullishe RSI-Divergenz UND Kurs im unteren Teil der Range (Discount). Verkaufen, wenn bullishe RSI-Divergenz. | +8.6 % | 2026-11-01 | legacy |

Grenzen: isolierte virtuelle Konten pro Regel, keine historischen News oder Orderbücher. Die Paper-Probe ist eine Simulation auf später hinzugekommenen Kursen. Wiederholte Forschung auf ähnlichen Zeiträumen kann weiterhin überanpassen. Ein Bestehen beweist keine künftigen Gewinne.