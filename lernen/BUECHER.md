# Wissen aus Trading-Büchern: was die Klassiker lehren und was davon im Test taugt

Aus bekannten Trading-Büchern werden die konkreten Regeln herausgezogen, als Strategie gebaut und an Jahren echter
Kurse getestet, und zwar nur auf Daten, die die Regel beim Einstellen nicht gesehen hat (Walk-Forward).
**Übernommen wird nur, was diesen Test besteht.** Hier stehen nur die Regeln in eigenen Worten, kein Buchtext.

## Regeln, die als Strategie getestet werden

| Buch | Kernidee | Übersetzt in eine Regel | Strategie |
|---|---|---|---|
| **Way of the Turtle** (Curtis Faith), Turtle-Regeln von Richard Dennis | Trendfolge mit festen Ausbruchsregeln; jeder Trade gleich viel Risiko, gemessen an der Schwankung (ATR) | Kaufen über dem 55-Kerzen-Hoch, verkaufen unter dem 20-Kerzen-Tief | `buch_turtle` |
| **Trading for a Living** (Alexander Elder) | «Triple Screen»: mit dem Trend der höheren Zeiteinheit handeln, aber gegen kurze Rücksetzer einsteigen | Langer EMA steigt (Trend), Force Index kurz negativ (Rücksetzer), Einstieg über dem Hoch der Vorkerze; raus, wenn der Trend dreht | `buch_triple_screen` |
| **Technische Analyse der Finanzmärkte** (John Murphy) | Gleitende Durchschnitte zeigen den Trend; Golden Cross / Death Cross; Indikatoren als Bestätigung | Investiert, solange die 50er- über der 200er-Linie liegt und der MACD bestätigt; raus beim Death Cross | `buch_golden_cross` |
| **Reminiscences of a Stock Operator / How to Trade in Stocks** (Jesse Livermore) | Nur mit dem Trend; am «Pivotal Point» kaufen, also beim Ausbruch aus einer ruhigen Phase; Verluste sofort begrenzen | Ausbruch auf ein neues 20-Kerzen-Hoch nach enger Seitwärtsphase, über der 200er-Linie; raus 10 % unter dem letzten Hoch | `buch_livermore` |

Schon im Bot enthalten: Die Ausbruchsstrategie des Risiko-Bots ist im Kern die Turtle-Methode (System 1 mit
kürzeren Fristen), die 200-Tage-Regel des Hauptbots stammt aus Meb Fabers Studie «A Quantitative Approach to
Tactical Asset Allocation».

## Regeln für das Risikomanagement (kein Kauf-Signal, sondern Schutz)

| Buch | Kernidee | Wo im Bot |
|---|---|---|
| **Trading in the Zone** (Mark Douglas) | Jeder einzelne Trade ist Zufall, nur die Regeln über viele Trades zählen. Risiko vor dem Einstieg festlegen und nie davon abweichen | Fester Stop-Loss bei jedem Trade, festes Risiko pro Trade, der Bot handelt ohne Gefühle |
| **Way of the Turtle** (Curtis Faith) | Positionsgrösse nach Schwankung: in wilden Märkten kleiner | Stop-Loss und Positionsgrösse richten sich nach der ATR |
| **Fooled by Randomness / The Black Swan** (Nassim Taleb) | Seltene Extremereignisse kommen öfter als gedacht; nie so handeln, dass ein einzelnes Ereignis alles vernichtet | Not-Aus bei grossem Kontoverlust, Hebel nur im Demo-Bot, Notbremse beim Chef-Bot |
| **Market Wizards** (Jack Schwager) | Fast alle erfolgreichen Trader nennen dasselbe: Verluste klein halten, Gewinner laufen lassen | Chance-Risiko-Verhältnis mit Take-Profit beim 2- bis 3-Fachen des Risikos |

## Testergebnis

Die vier Strategien werden im [Strategie-Vergleich](VERGLEICH.md) mit echten Kursdaten geprüft (Abschnitt «Regeln
aus YouTube-Videos und Trading-Büchern»). Das Ergebnis wird hier nachgetragen.

## Eigene Bücher

Bücher, die Hiran schickt (z.B. als PDF), werden genauso ausgewertet. Der Buchtext selbst kommt nicht ins
öffentliche Repository, nur die Regeln daraus in eigenen Worten.
