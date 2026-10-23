#!/usr/bin/env bash
# Ein Durchlauf aller Demo-Bots: handeln, Übersicht schreiben, Stand ins Repository speichern.
set -u
python -m tradingbot paper --config config_langfrist.yaml --once || echo "Langfrist-Bot: Fehler"
python -m tradingbot paper --config config_daytrading.yaml --once || echo "Daytrading-Bot: Fehler"
python -m tradingbot paper --config config_risiko.yaml --once || echo "Risiko-Bot: Fehler"

mkdir -p logs
# Fehlermeldungen landen in logs/uebersicht_fehler.txt (die Job-Logs sind von aussen nicht lesbar)
python -m tradingbot dashboard --bots config_langfrist.yaml config_daytrading.yaml config_risiko.yaml \
  > /dev/null 2> logs/uebersicht_fehler.txt || echo "Übersicht konnte nicht erstellt werden"
{ echo; python -m tradingbot news --config config_langfrist.yaml; } >> STATUS.md

git add STATUS.md charts state logs || true
git diff --cached --quiet || git commit -q -m "Bot-Lauf $(date -u '+%Y-%m-%d %H:%M')"
# Falls inzwischen Code-Änderungen hochgeladen wurden: zuerst übernehmen, dann speichern
for i in 1 2 3; do
  git pull -q --rebase -X theirs origin main && git push -q && exit 0
  sleep 5
done
echo "Speichern fehlgeschlagen"
