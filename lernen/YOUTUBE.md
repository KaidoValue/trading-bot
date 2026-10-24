# YouTube-Wissen: was die Videos lehren und was davon im Test taugt

Die Abschriften neuer Videos von **@hkcm**, **@phantombyhkcm** und **@STA_Solutions** holt Hirans PC automatisch
(bei jeder Anmeldung und täglich um 18 Uhr) in den Ordner [youtube/](youtube). Einmal pro Woche werden sie
ausgewertet: Was sich als klare Regel mit Kursdaten prüfen lässt, wird als Strategie gebaut und an Jahren echter
Kurse getestet, und zwar nur auf Daten, die die Regel beim Einstellen nicht gesehen hat (Walk-Forward).
**Übernommen wird nur, was diesen Test besteht.**

## Erste Auswertung (24.10.2026, 45 Videos)

Von 45 Videos drehen sich 14 hauptsächlich um Krypto. Der Rest behandelt Aktien, Edelmetalle, Politik und
Wirtschaft. Die meisten Videos enthalten Einschätzungen («Bitcoin könnte auf 30k fallen», «XRP mit 400 %
Potenzial»), keine festen Regeln. Solche Prognosen lassen sich nicht testen und werden nicht übernommen.
Einige Videos werben für kostenpflichtige Pakete mit Einstiegszonen; das ist Werbung, kein prüfbares Wissen.

### Methoden, die sich in Regeln übersetzen lassen

| Methode (Kanal) | Was in den Videos gesagt wird | Übersetzt in eine Regel | Strategie |
|---|---|---|---|
| Elliott-Wellen und Fibonacci (HKCM, Phantom) | Korrekturen (Welle 2/4) enden oft im Bereich 38,2-61,8 % des vorherigen Anstiegs; unter 78,6 % ist das Szenario ungültig | Im Aufwärtstrend (über der 200er-Linie) nach einem Anstieg kaufen, wenn der Kurs 38,2-61,8 % zurückgesetzt hat und wieder dreht. Verkaufen unter 78,6 % oder bei RSI über 75 | `yt_fib_welle` |
| Zyklen und «im Einkauf liegt der Gewinn» (STA Solutions) | Nach tiefen Bärenmärkten nachkaufen, je tiefer desto mehr; Teilgewinne in die Stärke mitnehmen | Kaufen, wenn der Kurs mehr als 40 % unter dem Jahreshoch ist und der RSI aus dem überverkauften Bereich dreht, oder wenn der Kurs die 200er-Linie zurückerobert. Verkaufen, wenn der Kurs mehr als 60 % über der 200er-Linie liegt | `yt_zyklus` |
| Trendwende-Signale / Divergenzen (HKCM, STA) | Neue Tiefs im Kurs, die der RSI nicht mehr bestätigt, deuten eine Wende an | Kaufen bei bullisher RSI-Divergenz, verkaufen bei bearisher | `yt_divergenz` |

Zusätzlich gibt es zwei neue Bausteine im Strategie-Labor: «Rücksetzer in die Fibonacci-Zone 38,2-61,8 %» und
«Kurs mehr als 40 % unter dem Jahreshoch». Die KI kann sie ab der nächsten Labor-Runde (sonntags) mit den anderen
Bausteinen kombinieren. Die drei Bots, die gerade handeln, werden dadurch nicht verändert.

### Nicht testbar mit Kursdaten

- **On-Chain-Daten** (MVRV, Börsen-Zu- und Abflüsse, Wal-Wallets): bräuchten eine kostenpflichtige Datenquelle.
- **Power-Law-Modell und Kursziele** (200'000 bis 1 Mio. USD): langfristige Prognosen, keine Handelsregel.
- **Makro und Politik** (Ölpreis, Zölle, Zinsen): fliessen beim Hauptbot schon über die Nachrichtenlage ein.

### Testergebnis (24.10.2026)

Geprüft mit echten Kursdaten, Gebühren eingerechnet. Entscheidend ist der Walk-Forward-Test: Er zählt nur Zeiträume,
die die Regel beim Einstellen nicht gesehen hat. Zum Vergleich: Die 200-Tage-Regel des Hauptbots erreicht im
gleichen Test auf Tageskerzen **+15,4 %**, die lernende KI **+0,3 %**.

| Regel | Walk-Forward Tageskerzen (ca. 7 Jahre) | Walk-Forward 4-Stunden-Kerzen (2 Jahre) | Urteil |
|---|---|---|---|
| `yt_fib_welle` (Elliott/Fibonacci) | +4,4 % | −6,0 % | ❌ nicht übernommen |
| `yt_zyklus` (Zyklen, Einkauf bei Panik) | −3,1 % | −4,7 % | ❌ nicht übernommen |
| `yt_divergenz` (RSI-Divergenz) | +9,7 % (nur 7 Trades) | −7,0 % | ❌ nicht übernommen |

**Fazit:** Keine dieser Regeln schlägt die 200-Tage-Regel, die der Hauptbot schon verwendet. Auf kurzen Zeiteinheiten
(4 Stunden, 1 Stunde) verlieren alle Geld, weil Gebühren und Fehlsignale den Vorteil auffressen. Positiv: Sie sind
deutlich weniger oft im Markt und verlieren in fallenden Märkten weniger als die anderen Strategien. Deshalb wird
keine Regel direkt übernommen. Die Bausteine daraus stehen aber im Strategie-Labor, wo die KI sie mit anderen
kombinieren kann. Besteht eine solche Kombination die Prüfung, kommt sie automatisch in den KI-Bot.
Ausführliche Zahlen: [VERGLEICH.md](VERGLEICH.md).

## Alle Videos

| Datum | Kanal | Video | Krypto |
|---|---|---|---|
| 2026-10-23 | @hkcm | [China steht kurz davor, die deutsche Autoindustrie zu demütigen](https://www.youtube.com/watch?v=V6Qu8DpXlGo) | am Rand |
| 2026-10-23 | @hkcm | [Diese Aktie könnte sich vervierfachen!](https://www.youtube.com/watch?v=ka4rOyEy1CU) | nein |
| 2026-10-23 | @phantombyhkcm | [Die Zeit der China Aktien ist gekommen!](https://www.youtube.com/watch?v=kccWYNyGlYI) | am Rand |
| 2026-10-22 | @phantombyhkcm | [Das ist eine der wichtigsten Aktien unserer Zeit!](https://www.youtube.com/watch?v=RuWLpoDbnhs) | am Rand |
| 2026-10-22 | @STA_Solutions | [Bevor du SpaceX nach den Zahlen kaufst, schau dieses Video...](https://www.youtube.com/watch?v=9FfjPL73kyA) | am Rand |
| 2026-10-21 | @hkcm | [Silber: Der Crash geht weiter!](https://www.youtube.com/watch?v=xnBpVoFExoY) | am Rand |
| 2026-10-21 | @hkcm | [„Die USA haben sich völlig verändert!“ - Bodybuilding-Legende JP Fux](https://www.youtube.com/watch?v=u3TlSSrDlSw) | am Rand |
| 2026-10-21 | @phantombyhkcm | [Die nächste große Altcoin Rallye beginnt HIER!](https://www.youtube.com/watch?v=f4i4nUJuQBo) | ja |
| 2026-10-21 | @phantombyhkcm | [Das muss passieren damit der Boden drin ist!](https://www.youtube.com/watch?v=G2SP13fA9k4) | am Rand |
| 2026-10-21 | @STA_Solutions | [Bevor Ethereum in den Bullenzyklus startet, schau dieses Video](https://www.youtube.com/watch?v=DI2bw0z59sw) | ja |
| 2026-10-21 | @phantombyhkcm | [Genauso sah Atlassian vor der Rallye aus!](https://www.youtube.com/watch?v=qhckyjnacpA) | am Rand |
| 2026-10-20 | @hkcm | [Wie geht es weiter nach -40% in einer Nacht?](https://www.youtube.com/watch?v=VeMlMwpnBD4) | nein |
| 2026-10-19 | @phantombyhkcm | [Diese 2 Aktien kaufen wir jetzt nach!](https://www.youtube.com/watch?v=OqLp9kGsih8) | am Rand |
| 2026-10-18 | @hkcm | [XRP mit 400 % Potenzial – aber dieser Altcoin könnte 2.300 % machen!](https://www.youtube.com/watch?v=jLaQiUudQA8) | ja |
| 2026-10-18 | @phantombyhkcm | [Das muss passieren damit Tesla auf $1000 steigt!!](https://www.youtube.com/watch?v=kXpM-gRff6E) | am Rand |
| 2026-10-18 | @hkcm | [„Was jetzt auf Berlin zukommen könnte, ist brandgefährlich!“ – Manuel Ostermann](https://www.youtube.com/watch?v=lWsbrdLqxpc) | am Rand |
| 2026-10-17 | @STA_Solutions | [Jeder Bitcoin-Anleger sollte diesen Chart gesehen haben...](https://www.youtube.com/watch?v=d9ht3uPFMEA) | ja |
| 2026-10-16 | @hkcm | [Die wichtigste Aktie der Welt steht vor einem gewaltigen Absturz!](https://www.youtube.com/watch?v=ILBhdy8Rf6A) | am Rand |
| 2026-10-16 | @hkcm | [Wie lange dauert der Goldzyklus noch?](https://www.youtube.com/watch?v=NPElYcJUess) | am Rand |
| 2026-10-16 | @phantombyhkcm | [Wer hier nicht investiert ist, ist selbst schuld](https://www.youtube.com/watch?v=Bu1UP0HBRGo) | am Rand |
| 2026-10-15 | @phantombyhkcm | [Sind Cannabis Aktien offiziell tot?](https://www.youtube.com/watch?v=5aRrNJlB8_M) | am Rand |
| 2026-10-15 | @hkcm | [Silber: Ich wünschte, wir wären falsch gelegen…](https://www.youtube.com/watch?v=zgAqLD1RsbE) | am Rand |
| 2026-10-15 | @STA_Solutions | [Wer bei AERO zu früh zugreift, riskiert einen teuren Fehler...](https://www.youtube.com/watch?v=x9ImJ4dR4qY) | ja |
| 2026-10-14 | @phantombyhkcm | [Langfristig sind hier +1.200 % drin!](https://www.youtube.com/watch?v=BQHwy8-q_-A) | am Rand |
| 2026-10-14 | @hkcm | [Das könnte jetzt richtig eskalieren!](https://www.youtube.com/watch?v=57d4dsZINSM) | am Rand |
| 2026-10-14 | @STA_Solutions | [Andere Coins werden gegen Solana alt aussehen (20x möglich)](https://www.youtube.com/watch?v=w2wJHNsVB1Y) | ja |
| 2026-10-13 | @STA_Solutions | [Unsere Krypto-Analysen: Die Treffer, die Fehler, die Bilanz...](https://www.youtube.com/watch?v=XYs0WEkGIjc) | ja |
| 2026-10-13 | @phantombyhkcm | [Wer ist der beste Italiener aller Zeiten? 🇮🇹](https://www.youtube.com/watch?v=Tm1Oth0FIbk) | am Rand |
| 2026-10-13 | @hkcm | [Dieses Unternehmen könnte ALLES zum Einsturz bringen!](https://www.youtube.com/watch?v=YXR4ldUXY3A) | am Rand |
| 2026-10-12 | @phantombyhkcm | [Die letzte Chance um bei dieser 1000% Aktie günstig reinzukommen!](https://www.youtube.com/watch?v=XAecgVjJvhU) | am Rand |
| 2026-10-12 | @phantombyhkcm | [+250 % seit Einstieg – und das ist erst der Anfang!](https://www.youtube.com/watch?v=U572vfsoC4A) | am Rand |
| 2026-10-12 | @hkcm | [Neue Kaufzonen für diese Top 2 Altcoins!](https://www.youtube.com/watch?v=wZS0_qr6xgU) | ja |
| 2026-10-12 | @STA_Solutions | [Endlich Entlastung: Trump und Putin senken die Energiepreise!](https://www.youtube.com/watch?v=xL3Bo2-ykQ4) | am Rand |
| 2026-10-11 | @phantombyhkcm | [Die ENTSCHEIDENDE PHASE beginnt an den MÄRKTEN / JETZT handeln!](https://www.youtube.com/watch?v=Nx63xDEv4wY) | ja |
| 2026-10-11 | @hkcm | [Deutschland wird zur Falle? Warum du JETZT einen Plan B brauchst!](https://www.youtube.com/watch?v=sz07MUzPYuc) | am Rand |
| 2026-10-09 | @hkcm | [Über 800 % Kurspotenzial? Hier wollen wir nachkaufen!](https://www.youtube.com/watch?v=Av3MYsngnyQ) | am Rand |
| 2026-10-09 | @phantombyhkcm | [Wir kaufen aggressiv XRP und Solana!](https://www.youtube.com/watch?v=6qr2ibe3HXs) | ja |
| 2026-10-09 | @STA_Solutions | [Die Bitcoin-Strategie der Elite: Was du daraus lernen kannst (Marc Steiner)](https://www.youtube.com/watch?v=7OsIY28a-pg) | ja |
| 2026-10-08 | @STA_Solutions | [KI-Rallye verpasst? Hier liegen Broadcoms nächste Kaufzonen](https://www.youtube.com/watch?v=TiJIFpATXJM) | am Rand |
| 2026-10-05 | @STA_Solutions | [Trump macht Druck auf Ölpreis! Was JETZT jeder wissen muss (5 Min)](https://www.youtube.com/watch?v=kPUbCyDZ9mo) | am Rand |
| 2026-10-01 | @STA_Solutions | [Bitcoin fällt auf 30K? Was hinter der düsteren Prognose steckt...](https://www.youtube.com/watch?v=KYckQW9jUuI) | ja |
| 2026-09-30 | @STA_Solutions | [Bevor du jetzt QUANT und NEAR hinterherläufst, schau dieses Video...](https://www.youtube.com/watch?v=Glx3oLRZSrQ) | ja |
| 2026-09-28 | @STA_Solutions | [Trump sagt wieder Nein: Jetzt droht der nächste Öl-Schock!](https://www.youtube.com/watch?v=uz6wSjfNQUM) | am Rand |
| 2026-09-24 | @STA_Solutions | [Die Apple-Aktie könnte heftig abstürzen! (Verkaufsziele erreicht)](https://www.youtube.com/watch?v=hQcWwqOdIIE) | am Rand |
| 2026-09-23 | @STA_Solutions | [Injective wird viele Personen reich machen ... (+700% möglich)](https://www.youtube.com/watch?v=01xAzYA1NQM) | ja |
