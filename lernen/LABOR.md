# Strategie-Labor

Letzter Lauf: 15.11.2026 10:59 UTC · Daten: BTC/USD, 1h-Kerzen, 15.11.2024 bis 15.11.2026

Die KI erfindet aus den vorhandenen Bausteinen (Indikatoren, Kerzenmuster, Marktstruktur) neue Strategien. Standard: Suche auf den älteren 50 %; danach zwei getrennte Validierungsfenster und ein späterer Holdout. Prüfung mit Trader/PaperBroker, Gebühren, Slippage, Stops und Risikolimits. Erforderlich: mindestens 30 abgeschlossene Trades insgesamt, positive Rendite und Profit Factor >=1,2 in jedem Fenster, höchstens 15 % Drawdown und insgesamt besser als kostenbereinigtes Halten. Ein Bestehen startet nur die Paper-Probe: mindestens 14 Tage nach Fund und 20 regulär geschlossene Trades. Erst Status active darf im KI-Bot mitstimmen.

## Kandidaten dieses Laufs

| Regel | Training | Prüfung | Trades (Prüfung) | Bitcoin halten (Prüfung) | Ergebnis |
|---|---|---|---|---|---|
| Kaufen, wenn Kurs unter dem unteren Bollinger-Band UND Trendwechsel nach unten (CHoCH). Verkaufen, wenn MACD-Histogramm negativ UND Strukturbruch nach oben (BOS). | +16.1 % | +0.0 % | 0 | -35.0 % | durchgefallen |
| Kaufen, wenn Trendwechsel nach unten (CHoCH) UND Kurs unter dem unteren Bollinger-Band. Verkaufen, wenn Kurs unter der 200er-Linie UND Strukturbruch nach oben (BOS). | +7.0 % | +0.0 % | 0 | -35.0 % | durchgefallen |
| Kaufen, wenn Kurs unter dem unteren Bollinger-Band. Verkaufen, wenn MACD-Histogramm negativ UND Strukturbruch nach oben (BOS). | -21.9 % | +0.0 % | 0 | -35.0 % | durchgefallen |
| Kaufen, wenn Trendwechsel nach unten (CHoCH). Verkaufen, wenn MACD-Histogramm negativ UND Strukturbruch nach oben (BOS). | -31.3 % | +0.0 % | 0 | -35.0 % | durchgefallen |
| Kaufen, wenn MACD-Histogramm negativ UND Trendwechsel nach unten (CHoCH). Verkaufen, wenn MACD-Histogramm negativ UND Strukturbruch nach oben (BOS). | -31.4 % | +0.0 % | 0 | -35.0 % | durchgefallen |

## Strategie-Bibliothek und Freigabestatus

| Name | Regel | Prüfung | Gefunden am | Status |
|---|---|---|---|---|
| labor_3 | Kaufen, wenn Kurs unter der 200er-Linie UND Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn Marktstruktur abwärts UND bullishe RSI-Divergenz. | +21.0 % | 2026-10-23 | legacy |
| labor_4 | Kaufen, wenn Kurs unter der 200er-Linie UND Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn bullishe RSI-Divergenz. | +17.9 % | 2026-10-23 | legacy |
| labor_2 | Kaufen, wenn Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn Kurs im oberen Teil der Range (Premium) UND bullishe RSI-Divergenz. | +14.8 % | 2026-10-23 | legacy |
| labor_1 | Kaufen, wenn Kurs unter der 200er-Linie UND bearishes Kerzenmuster UND Kurs unter dem unteren Bollinger-Band. Verkaufen, wenn Kurs im oberen Teil der Range (Premium) UND bullishe RSI-Divergenz. | +10.4 % | 2026-10-23 | legacy |
| labor_5 | Kaufen, wenn bullishe RSI-Divergenz UND Kurs im unteren Teil der Range (Discount). Verkaufen, wenn bullishe RSI-Divergenz. | +8.6 % | 2026-11-01 | legacy |

Grenzen: isolierte virtuelle Konten pro Regel, keine historischen News oder Orderbücher. Die Paper-Probe ist eine Simulation auf später hinzugekommenen Kursen. Wiederholte Forschung auf ähnlichen Zeiträumen kann weiterhin überanpassen. Ein Bestehen beweist keine künftigen Gewinne.