# Lernende KI: nachvollziehbare Vorwärtstests

Der KI-Bot sammelt ab Aktivierung eigene neue Lernfälle. Ein Modell wird nicht allein
durch den Einbau profitabel. Die bisherigen Kontostände, Positionen und Strategiegedächtnisse
werden nicht zurückgesetzt. Die neue Forschung ist nur für ungehebeltes Long-Paper-Trading aktiviert.

## Was jetzt automatisch geschieht

1. Je Coin und abgeschlossener Kerze werden Marktmerkmale, ursprüngliches Signal,
   Modellversion, Wahrscheinlichkeit und die spätere Ausführungsentscheidung protokolliert.
   Auch neutrale Signale und abgewiesene Einstiege werden erfasst.
2. Pro Coin und Horizont läuft höchstens ein isolierter Testtrade gleichzeitig.
   Sein Einstieg erfolgt frühestens zur nächsten Kerzeneröffnung nach der Beobachtung.
   Der Vergleich verwendet eine feste Testposition von höchstens 25 % des Startkapitals,
   zusätzlich begrenzt durch die konfigurierte Positionsobergrenze und Mindestorder.
3. Erst später eintreffende, abgeschlossene Kerzen liefern das Ergebnis. Berücksichtigt werden
   die beobachtete Gebührenstufe, Slippage, der beobachtete Spread (bei fehlendem Spread vorsichtig 1 %),
   Stop, Ziel, Teilverkauf und Nachlaufstop der Produktion. Bei gleichzeitiger Berührung wird der
   Stop zuerst verarbeitet. Bei Datenlücken wird kein Ergebnis erfunden.
4. Die Testposition endet spätestens nach zwölf Kerzen, bei Tageskerzen nach sechs Kerzen.
   Die Zielgrösse ist **positiver Nettoertrag dieses Testtrades**, nicht eine sichere Kursprognose.
5. Ab 200 ausgewerteten Fällen, darunter mindestens 30 positive und 30 nichtpositive,
   wird eine regularisierte logistische Regression trainiert. Standardisierung erfolgt nur auf
   den Trainingsdaten. Ältere Fälle verlieren Gewicht (Halbwertszeit 90 Tage, Trainingsfenster 180 Tage).
   Gleichzeitige Coins erhalten im Training zusammen nur ein Zeitblockgewicht.
6. Modell und Prognosen werden für die Forward-Probe eingefroren. In dieser Phase handeln weiter
   die bisherigen Regeln. Ein Kandidat darf erst nach mindestens 30 Tagen, 200 neuen Fällen,
   20 Zeitblöcken und 40 gewählten Testtrades als zusätzlicher Paper-Einstiegsfilter dienen.

## Voraussetzungen für eine Übernahme

- Untere statistische Schranke des Nettoertrags und des paarweisen Vorteils zum bisherigen
  Filter muss positiv sein (zeitblockweise Mittelwerte, konservativer Faktor 2,58).
- Brier-Fehler der Wahrscheinlichkeiten muss besser sein als die feste Trefferhäufigkeit
  des Trainingsdatensatzes.
- Untere Wilson-Schranke der Trefferquote muss mit den trainierten mittleren Gewinnen und
  Verlusten einen positiven Erwartungswert ergeben.
- Kein ausgewerteter Zeitblock darf durchschnittlich mehr als 10 % Verlust je Standard-Testposition aufweisen.
- Der Kandidat wird einmal am vorab festgelegten Mindestumfang beurteilt; unzureichende
  Daten verfallen nach mindestens 90 Tagen bzw. 30 Test-Zeitblöcken.

Ein akzeptiertes Modell darf nur neue, bereits von der bisherigen Strategie vorgeschlagene
Paper-Einstiege herausfiltern. Es erzeugt keine zusätzlichen Kaufsignale, erhöht keinen Einsatz
und verändert keine Ausstiege. Die normalen Nachrichten-, Trend-, Kosten- und Risikoregeln
gelten weiterhin. Bei einer Vorhersage unter 60 %, negativem geschätztem Nettovorteil oder
Merkmalen mehr als vier Trainings-Standardabweichungen ausserhalb des Datenbereichs wartet der Filter.

Weitere Kandidaten treten gegen den zuletzt akzeptierten Filter an. Bei negativen Ergebnissen
über die letzten zehn ausgewerteten Zeitblöcke, einem schlechten Einzelblock oder nach
180 Tagen wird ein aktiver Filter pausiert; die bisherige Strategie übernimmt wieder.
Ein gleichzeitiger Kandidatenvergleich mit geänderter Vergleichsbasis wird verworfen.

## Was die Zahlen nicht beweisen

Die Testtrades sind isolierte Was-wäre-wenn-Fälle, **keine Portfoliosimulation**. Sie dürfen
auch eine von Nachrichten oder Gebührenfiltern abgelehnte Gelegenheit untersuchen. Sie
teilen nicht das tatsächliche Kapital und enthalten keine echten zukünftigen Orderbücher.
Ihre Renditen dürfen nicht addiert und als erzielter Gewinn dargestellt werden.

Zeitblöcke vermindern die Abhängigkeit ähnlicher Coins, beseitigen sie aber nicht vollständig.
Die Prüfschranken sind Auswahlregeln, keine garantierten Konfidenzaussagen unter beliebigen
Marktverhältnissen. Wiederholte Modellgenerationen bleiben ein Risiko für Überanpassung.
Lange Horizonte benötigen unter Umständen Monate, bevor genug neue Ergebnisse vorliegen.

## Dateien und Bedienung

- Aktivierung: `research_enabled: true` in `bots/config_daytrading.yaml`.
- Arbeitsstand: `daten/research/<Bot>_<Horizont>_<Konfigurationshash>.json`.
- Nachvollziehbares Journal: `daten/research/journal/<Bot>_<Monat>.jsonl`.
  Die `id` verbindet Beobachtung, Entscheidung und späteres Ergebnis; Wiederholungen nach
  einem Prozessabbruch können anhand dieser ID und des Datensatztyps dedupliziert werden.
- Änderungen an Kosten, Risiko oder Horizont erzeugen einen getrennten Forschungsstand.
  Alte Forschungsdateien werden erhalten, aber nicht stillschweigend vermischt.
- Das Dashboard zeigt Status, ausgewertete, offene und ungültige Fälle pro Horizont.
  Wahrscheinlichkeiten erscheinen erst, wenn tatsächlich ein Modell trainiert wurde.

## Optionale Sprachanalyse der Nachrichten: ausgeschaltet

Der gesamte Kurs-Lernbetrieb funktioniert lokal mit NumPy und ohne Sprachmodell-API.
Die vorbereitete zusätzliche Nachrichtenanalyse ist standardmässig aus und beeinflusst keine Orders.
Sie klassifiziert öffentliche Schlagzeilen, nennt betroffene Coins, gruppiert mutmasslich gleiche
Ereignisse und unterscheidet Meldungen, Kommentare und historische Berichte. Originalquellen
bleiben erhalten; ungültige oder unvollständige Antworten werden verworfen.

Nur bei späterer bewusster Aktivierung in GitHub Actions:

- Secret `NEWS_OPENAI_API_KEY`: eigener OpenAI-API-Schlüssel, niemals in Code oder Chat speichern.
- Variable `NEWS_LLM_MODEL`: ein im eigenen API-Projekt verfügbares Modell mit Structured Outputs.
- Variable `NEWS_LLM_ENABLED`: `1`.
- Variable `NEWS_LLM_MAX_CALLS_PER_DAY`: standardmässig `1`, technische Obergrenze `24`.

Es werden höchstens zwölf öffentliche Schlagzeilen je Aufruf übertragen, keine Kontostände,
Trades oder Schlüssel. Auch fehlgeschlagene Aufrufe zählen gegen das Tageslimit. Gleiche
Nachrichten werden aus dem Cache gelesen. Ein Aufruflimit ist kein Geldbetrag-Limit; zusätzlich
ein Kostenlimit beim Anbieter einrichten. Ohne Zugang bleibt die bestehende Regelprüfung aktiv.

API-Grundlage: [OpenAI Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs?api-mode=responses).
