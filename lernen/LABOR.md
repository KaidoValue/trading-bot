# Strategie-Labor

Letzter Lauf: 01.11.2026 10:32 UTC · Daten: BTC/USD, 1h-Kerzen, 01.11.2024 bis 01.11.2026

Die KI erfindet aus den vorhandenen Bausteinen (Indikatoren, Kerzenmuster, Marktstruktur) neue Strategien. Sie werden auf den älteren 70 % der Kurse entwickelt und auf den neuesten 30 % geprüft, die das Labor nie gesehen hat. Nur wer dort nach Gebühren Gewinn macht und mindestens 10 Trades hat (sonst wäre es eher Glück), kommt in die Bibliothek.

## Kandidaten dieses Laufs

| Regel | Training | Prüfung | Trades (Prüfung) | Bitcoin halten (Prüfung) | Ergebnis |
|---|---|---|---|---|---|
| Kaufen, wenn bullishe RSI-Divergenz UND Kurs im unteren Teil der Range (Discount). Verkaufen, wenn bullishe RSI-Divergenz. | +10.2 % | +8.6 % | 10 | +17.0 % | ✅ aufgenommen |
| Kaufen, wenn bullishe RSI-Divergenz UND Kurs im unteren Teil der Range (Discount). Verkaufen, wenn RSI unter 30 (überverkauft). | +3.7 % | -11.6 % | 16 | +17.0 % | ❌ durchgefallen |
| Kaufen, wenn Kurs im unteren Teil der Range (Discount) UND bullishe RSI-Divergenz. Verkaufen, wenn Kurs über der 200er-Linie. | -7.9 % | -19.7 % | 13 | +17.0 % | ❌ durchgefallen |
| Kaufen, wenn bullishe RSI-Divergenz UND Kurs im unteren Teil der Range (Discount). Verkaufen, wenn schneller EMA (20) über langsamem EMA (50). | -27.6 % | -23.4 % | 14 | +17.0 % | ❌ durchgefallen |
| Kaufen, wenn bullishe RSI-Divergenz UND Marktstruktur abwärts. Verkaufen, wenn bullishe RSI-Divergenz. | -28.1 % | +0.7 % | 11 | +17.0 % | ✅ aufgenommen |

## Strategie-Bibliothek (wird vom KI-Bot benutzt)

| Name | Regel | Prüfung | Gefunden am |
|---|---|---|---|
| labor_3 | Kaufen, wenn Kurs unter der 200er-Linie UND Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn Marktstruktur abwärts UND bullishe RSI-Divergenz. | +21.0 % | 2026-10-23 |
| labor_4 | Kaufen, wenn Kurs unter der 200er-Linie UND Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn bullishe RSI-Divergenz. | +17.9 % | 2026-10-23 |
| labor_2 | Kaufen, wenn Kurs unter dem unteren Bollinger-Band UND bearishes Kerzenmuster. Verkaufen, wenn Kurs im oberen Teil der Range (Premium) UND bullishe RSI-Divergenz. | +14.8 % | 2026-10-23 |
| labor_1 | Kaufen, wenn Kurs unter der 200er-Linie UND bearishes Kerzenmuster UND Kurs unter dem unteren Bollinger-Band. Verkaufen, wenn Kurs im oberen Teil der Range (Premium) UND bullishe RSI-Divergenz. | +10.4 % | 2026-10-23 |
| labor_5 | Kaufen, wenn bullishe RSI-Divergenz UND Kurs im unteren Teil der Range (Discount). Verkaufen, wenn bullishe RSI-Divergenz. | +8.6 % | 2026-11-01 |

Hinweis: Auch eine bestandene Prüfung ist keine Garantie. Deshalb gewichtet der KI-Bot diese Strategien danach live weiter nach ihrem tatsächlichen Erfolg, wie alle anderen.