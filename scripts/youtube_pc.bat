@echo off
chcp 65001 > nul
set PYTHONUTF8=1
REM Holt die Abschriften neuer YouTube-Videos und laedt sie ins Projekt hoch (laeuft automatisch).
cd /d %~dp0..
if not exist lernen mkdir lernen
git pull -q --rebase -X theirs origin main
if "%1"=="show" (
  py -m tradingbot youtube
) else (
  py -m tradingbot youtube >> lernen\youtube_pc.log 2>&1
)
git add -A lernen/youtube
git diff --cached --quiet && exit /b
git commit -q -m "YouTube-Wissen vom PC"
for /l %%i in (1,1,3) do (
  git pull -q --rebase -X theirs origin main && git push -q && exit /b
  git rebase --abort 2> nul
  timeout /t 5 > nul
)
