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

## Testergebnis (24.10.2026)

Geprüft mit echten Kursdaten, Gebühren eingerechnet. Entscheidend ist der Walk-Forward-Test: Er zählt nur Zeiträume,
die die Regel beim Einstellen nicht gesehen hat. Zum Vergleich: Die 200-Tage-Regel des Hauptbots erreicht im
gleichen Test auf Tageskerzen **+15,4 %**, die lernende KI **+0,3 %**.

| Regel | Walk-Forward Tageskerzen (ca. 7 Jahre) | Walk-Forward 4-Stunden-Kerzen (2 Jahre) | Urteil |
|---|---|---|---|
| `buch_turtle` (Turtle) | +3,9 % | −4,1 % | ❌ nicht übernommen |
| `buch_triple_screen` (Elder) | +5,2 % | −11,5 % | ❌ nicht übernommen |
| `buch_golden_cross` (Murphy) | +7,4 % | −15,7 % | ❌ nicht übernommen |
| `buch_livermore` (Livermore) | +6,0 % | −7,4 % | ❌ nicht übernommen |

**Fazit:** Keine dieser Regeln schlägt die 200-Tage-Regel, die der Hauptbot schon verwendet. Auf kurzen Zeiteinheiten
(4 Stunden, 1 Stunde) verlieren alle Geld, weil Gebühren und Fehlsignale den Vorteil auffressen. Positiv: Sie sind
deutlich weniger oft im Markt und verlieren in fallenden Märkten weniger als die anderen Strategien. Deshalb wird
keine Regel direkt übernommen. Die Bausteine daraus stehen aber im Strategie-Labor, wo die KI sie mit anderen
kombinieren kann. Besteht eine solche Kombination die Prüfung, kommt sie automatisch in den KI-Bot.
Ausführliche Zahlen: [VERGLEICH.md](VERGLEICH.md).

## Eigene Bücher

Bücher, die Hiran schickt (z.B. als PDF), werden genauso ausgewertet. Der Buchtext selbst kommt nicht ins
öffentliche Repository, nur die Regeln daraus in eigenen Worten.
