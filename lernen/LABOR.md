# Strategie-Labor

Letzter Lauf: 25.10.2026 08:29 UTC · Daten: BTC/USD, 1h-Kerzen, 25.10.2024 bis 25.10.2026

Die KI erfindet aus den vorhandenen Bausteinen (Indikatoren, Kerzenmuster, Marktstruktur) neue Strategien. Sie werden auf den älteren 70 % der Kurse entwickelt und auf den neuesten 30 % geprüft, die das Labor nie gesehen hat. Nur wer dort nach Gebühren Gewinn macht und mindestens 10 Trades hat (sonst wäre es eher Glück), kommt in die Bibliothek.

## Kandidaten dieses Laufs

| Regel | Training | Prüfung | Trades (Prüfung) | Bitcoin halten (Prüfung) | Ergebnis |
|---|---|---|---|---|---|
| Kaufen, wenn Kurs unter der 200er-Linie UND bearishes Kerzenmuster UND Kurs unter dem unteren Bollinger-Band. Verkaufen, wenn MACD-Histogramm steigt UND RSI unter 30 (überverkauft). | +84.4 % | -2.2 % | 10 | +13.8 % | ❌ durchgefallen |
| Kaufen, wenn bearishes Kerzenmuster UND Kurs unter dem unteren Bollinger-Band. Verkaufen, wenn MACD-Histogramm steigt UND RSI unter 30 (überverkauft). | +77.6 % | -6.1 % | 13 | +13.8 % | ❌ durchgefallen |
| Kaufen, wenn Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster UND Kurs unter der 200er-Linie. Verkaufen, wenn RSI unter 30 (überverkauft). | +49.5 % | -3.7 % | 19 | +13.8 % | ❌ durchgefallen |
| Kaufen, wenn Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster UND Kurs unter der 200er-Linie. Verkaufen, wenn MACD-Histogramm negativ UND RSI unter 30 (überverkauft). | +49.5 % | -4.3 % | 19 | +13.8 % | ❌ durchgefallen |
| Kaufen, wenn schneller EMA (20) über langsamem EMA (50) UND bearishes Kerzenmuster UND Kurs unter der 200er-Linie. Verkaufen, wenn MACD-Histogramm steigt UND RSI unter 30 (überverkauft). | +42.8 % | -9.2 % | 12 | +13.8 % | ❌ durchgefallen |

## Strategie-Bibliothek (wird vom KI-Bot benutzt)

| Name | Regel | Prüfung | Gefunden am |
|---|---|---|---|
| labor_3 | Kaufen, wenn Kurs unter der 200er-Linie UND Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn Marktstruktur abwärts UND bullishe RSI-Divergenz. | +21.0 % | 2026-10-23 |
| labor_4 | Kaufen, wenn Kurs unter der 200er-Linie UND Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn bullishe RSI-Divergenz. | +17.9 % | 2026-10-23 |
| labor_2 | Kaufen, wenn Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn Kurs im oberen Teil der Range (Premium) UND bullishe RSI-Divergenz. | +14.8 % | 2026-10-23 |
| labor_1 | Kaufen, wenn Kurs unter der 200er-Linie UND bearishes Kerzenmuster UND Kurs unter dem unteren Bollinger-Band. Verkaufen, wenn Kurs im oberen Teil der Range (Premium) UND bullishe RSI-Divergenz. | +10.4 % | 2026-10-23 |

Hinweis: Auch eine bestandene Prüfung ist keine Garantie. Deshalb gewichtet der KI-Bot diese Strategien danach live weiter nach ihrem tatsächlichen Erfolg, wie alle anderen.