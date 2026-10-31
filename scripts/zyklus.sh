#!/usr/bin/env bash
# Ein Durchlauf aller Demo-Bots: handeln, Übersicht schreiben, Stand ins Repository speichern.
set -u
mkdir -p daten/logs
# Fehler sichtbar machen (die Job-Logs sind von aussen nicht lesbar): ins Job-Protokoll und als Zeile
# «Zeit UTC | Schritt | Meldung» nach daten/logs/fehler_zyklus.txt (letzte 100 Zeilen), die Übersicht warnt 2 Std. lang
fehler() {
  local f=daten/logs/fehler_zyklus.txt
  echo "$1: $2"
  echo "$(date -u '+%Y-%m-%d %H:%M') UTC | $1 | $2" >> "$f"
  tail -n 100 "$f" > "$f.tmp" && mv "$f.tmp" "$f"
}
# Ein fehlgeschlagener Durchlauf endet mit Exit-Code 1; die Einzelheiten stehen in daten/logs/fehler_<Config>.txt
python -m tradingbot paper --config bots/config_langfrist.yaml --once || fehler "Langfrist-Bot" "Durchlauf fehlgeschlagen"
python -m tradingbot paper --config bots/config_daytrading.yaml --once || fehler "KI-Bot" "Durchlauf fehlgeschlagen"
python -m tradingbot paper --config bots/config_risiko.yaml --once || fehler "Risiko-Bot" "Durchlauf fehlgeschlagen"

# Fehlermeldungen der Übersicht landen in daten/logs/uebersicht_fehler.txt. Die Nachrichtenlage kommt nur an eine neu
# geschriebene STATUS.md (sonst stünde sie in der alten ein zweites Mal)
if python -m tradingbot dashboard --bots bots/config_langfrist.yaml bots/config_daytrading.yaml bots/config_risiko.yaml \
    --chef daten/state/chef.json > /dev/null 2> daten/logs/uebersicht_fehler.txt; then
  { echo; python -m tradingbot news --config bots/config_langfrist.yaml; } >> STATUS.md
else
  fehler "Übersicht" "STATUS.md nicht erneuert: $(tail -n 1 daten/logs/uebersicht_fehler.txt | cut -c1-200)"
fi

# Chart-Bilder in den Branch «charts» ohne Verlauf (nur die neueste Version, damit das Repository klein bleibt)
if [ -d daten/charts ] && ls daten/charts/*.png > /dev/null 2>&1; then
  export GIT_INDEX_FILE="$(mktemp -u)"
  git --work-tree=daten/charts add -A . && commit=$(git commit-tree "$(git write-tree)" -m "Charts $(date -u '+%Y-%m-%d %H:%M')") \
    && git push -q -f origin "$commit:refs/heads/charts" || fehler "Charts" "nicht gespeichert (Trading-Oberfläche veraltet)"
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
fehler "Speichern" "Stand nicht ins Repository übertragen"
# die Fehlerzeile gleich mit festhalten: der nächste Durchlauf überträgt sie mit (sauberer Stand für git pull)
git add daten/logs/fehler_zyklus.txt && git commit -q -m "Bot-Lauf $(date -u '+%Y-%m-%d %H:%M'): Speichern fehlgeschlagen" || true
