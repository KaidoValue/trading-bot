#!/usr/bin/env bash
# Ein Durchlauf aller Demo-Bots: handeln, Übersicht schreiben, Stand ins Repository speichern.
set -u
python -m tradingbot paper --config bots/config_langfrist.yaml --once || echo "Langfrist-Bot: Fehler"
python -m tradingbot paper --config bots/config_daytrading.yaml --once || echo "Daytrading-Bot: Fehler"
python -m tradingbot paper --config bots/config_risiko.yaml --once || echo "Risiko-Bot: Fehler"

mkdir -p daten/logs
# Fehlermeldungen landen in daten/logs/uebersicht_fehler.txt (die Job-Logs sind von aussen nicht lesbar)
python -m tradingbot dashboard --bots bots/config_langfrist.yaml bots/config_daytrading.yaml bots/config_risiko.yaml \
  --chef daten/state/chef.json > /dev/null 2> daten/logs/uebersicht_fehler.txt || echo "Übersicht konnte nicht erstellt werden"
{ echo; python -m tradingbot news --config bots/config_langfrist.yaml; } >> STATUS.md

# Chart-Bilder in den Branch «charts» ohne Verlauf (nur die neueste Version, damit das Repository klein bleibt)
if [ -d daten/charts ] && ls daten/charts/*.png > /dev/null 2>&1; then
  export GIT_INDEX_FILE="$(mktemp -u)"
  git --work-tree=daten/charts add -A . && commit=$(git commit-tree "$(git write-tree)" -m "Charts $(date -u '+%Y-%m-%d %H:%M')") \
    && git push -q -f origin "$commit:refs/heads/charts" || echo "Charts konnten nicht gespeichert werden"
  rm -f "$GIT_INDEX_FILE"; unset GIT_INDEX_FILE
fi

git add -A STATUS.md daten lernen || true
git diff --cached --quiet || git commit -q -m "Bot-Lauf $(date -u '+%Y-%m-%d %H:%M')"
# Falls inzwischen Code-Änderungen hochgeladen wurden: zuerst übernehmen, dann speichern
for i in 1 2 3; do
  git pull -q --rebase -X theirs origin main && git push -q && exit 0
  git rebase --abort 2>/dev/null || true    # Konflikt: nicht in einem halben Rebase stecken bleiben
  sleep 5
done
echo "Speichern fehlgeschlagen"
