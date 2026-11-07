@echo off
setlocal
chcp 65001 > nul
set PYTHONUTF8=1
REM Profi-Bot-Pruefung auf dem Windows-PC (lernen/PROFI_PLAN.md): rechnet denselben Stand des Profi-Zweigs wie
REM GitHub, aber mit den Kursen von Binance (auf GitHub gesperrt). Das ist der zweite Cache fuer alle Entscheide.
REM Start in der Eingabeaufforderung, die Angaben wie in lernen/PROFI_PLAN.md, zum Beispiel:
REM   scripts\profi_pc.bat E0
REM   scripts\profi_pc.bat E0 --gebuehren alt
REM   scripts\profi_pc.bat E1 --varianten bots/profi/varianten/e1_kb5.yaml
REM Mit Doppelklick fragt das Skript nach dem Schritt. Gerechnet wird in einer eigenen Kopie des Projekts
REM (%USERPROFILE%\trading-bot-profi), damit die Demo-Bots und das YouTube-Skript auf diesem PC unberuehrt bleiben.
REM Der erste Lauf laedt die Kurse und friert sie als Zip mit Fingerabdruck ein (data\profi_cache.zip, Fingerabdruck
REM in lernen\profi\cache_pc.txt); danach rechnet jeder Lauf nur mit diesen Kursen.

REM Aus einer Kopie in %TEMP% laufen, denn git pull kann diese Datei waehrend des Laufs aendern
if not defined PROFI_KOPIE (
  set PROFI_KOPIE=1
  copy /y "%~f0" "%TEMP%\profi_pc.bat" > nul
  call "%TEMP%\profi_pc.bat" %*
  exit /b
)
set ZWEIG=claude/project-thread-usz8e3
set REPO=%USERPROFILE%\trading-bot-profi
set ZIP=data\profi_cache.zip
echo.
echo === Profi-Bot-Pruefung auf diesem PC, mit Binance-Kursen ===
echo.

set SCHRITT=%~1
set REST=
:angaben
shift
if "%~1"=="" goto angaben_fertig
set REST=%REST% %1
goto angaben
:angaben_fertig
if "%SCHRITT%"=="" (
  echo Welcher Schritt? Die genauen Angaben stehen in lernen/PROFI_PLAN.md unter "Befehle".
  set /p SCHRITT=Schritt, zum Beispiel E0: 
  set /p REST=Weitere Angaben, sonst leer lassen: 
)
set OK=
for %%s in (E0 E1 E2 E3 E4 E5 E6) do if /i "%SCHRITT%"=="%%s" (set SCHRITT=%%s& set OK=1)
if not defined OK (
  echo Unbekannter Schritt "%SCHRITT%". Erlaubt sind E0 bis E6.
  goto fehler
)

where py > nul 2>&1
if errorlevel 1 (
  echo Python fehlt, wird jetzt installiert ...
  winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
  echo.
  echo Python ist installiert. Bitte diese Datei jetzt NOCHMALS starten.
  pause
  exit /b
)
where git > nul 2>&1
if errorlevel 1 (
  echo Git fehlt, wird jetzt installiert ...
  winget install -e --id Git.Git --accept-package-agreements --accept-source-agreements
  echo.
  echo Git ist installiert. Bitte diese Datei jetzt NOCHMALS starten.
  pause
  exit /b
)

if not exist "%REPO%\.git" (
  echo Lade das Trading-Bot-Projekt nach %REPO%, nur beim ersten Mal ...
  git clone -q -b %ZWEIG% https://github.com/KaidoValue/trading-bot.git "%REPO%" || goto fehler
)
cd /d "%REPO%" || goto fehler
git config user.name "trading-bot-pc"
git config user.email "trading-bot@users.noreply.github.com"
echo Hole den neuesten Stand des Profi-Zweigs %ZWEIG% ...
git fetch -q origin %ZWEIG% || goto fehler
git checkout -q %ZWEIG% || goto fehler
git pull -q --rebase --autostash -X theirs origin %ZWEIG% || goto fehler
echo Installiere die noetigen Python-Bausteine, dauert 1-2 Minuten ...
py -m pip install -q --disable-pip-version-check -r requirements.txt || goto fehler

if not exist data mkdir data
if not exist lernen\profi mkdir lernen\profi
if exist %ZIP% goto auspacken
if exist lernen\profi\cache_pc.txt goto zip_fehlt
echo.
echo Erster Lauf: lade die Kurse von den Boersen, dauert 10-30 Minuten ...
if exist data\historie rmdir /s /q data\historie
py -m tradingbot profi --schritt E0 --laden > nul || goto fehler
py -m tradingbot profi --schritt E1 --varianten bots/profi/varianten/e1_kbe.yaml --laden > nul || goto fehler
if not exist data\historie\binance_*.csv goto ohne_binance
echo Friere die Kurse ein: %REPO%\%ZIP%
powershell -NoProfile -Command "Compress-Archive -Path 'data\historie\*' -DestinationPath '%ZIP%' -Force" || goto fehler
goto pruefen

:auspacken
echo Nehme die eingefrorenen Kurse aus %ZIP% ...
if exist data\historie rmdir /s /q data\historie
powershell -NoProfile -Command "Expand-Archive -Path '%ZIP%' -DestinationPath 'data\historie' -Force" || goto fehler

:pruefen
set FINGER=
for /f %%f in ('py -c "from tradingbot.auswertung import cache_id; print(cache_id())"') do set FINGER=%%f
if not defined FINGER goto fehler
if not exist lernen\profi\cache_pc.txt (> lernen\profi\cache_pc.txt echo %FINGER%)
set /p SOLL=<lernen\profi\cache_pc.txt
if not "%FINGER%"=="%SOLL%" goto falscher_cache
echo Kurse eingefroren, Fingerabdruck %FINGER%

echo.
echo Rechne: profi --schritt %SCHRITT% %REST%
echo Das kann mehrere Stunden dauern: den PC eingeschaltet lassen und dieses Fenster nicht schliessen.
echo.
set MELDUNG=Profi-Bot %SCHRITT%: Ergebnisse vom PC (Binance)
set DANACH=fertig
py -m tradingbot profi --schritt %SCHRITT% %REST% --cache-fest || goto abgebrochen

:hochladen
echo.
echo Lade die Ergebnisse hoch. Beim ersten Mal oeffnet sich ein GitHub-Anmeldefenster: bitte dort anmelden.
git add lernen/profi lernen/PROFI_ERGEBNISSE.md lernen/PROFI_PRUEFPROTOKOLL.md
git diff --cached --quiet && goto %DANACH%
git commit -q -m "%MELDUNG%"
for /l %%i in (1,1,3) do (
  git pull -q --rebase -X theirs origin %ZWEIG% && py -m tradingbot profi --zusammenfassen > nul && git add lernen/PROFI_ERGEBNISSE.md && (git diff --cached --quiet || git commit -q -m "Profi-Bot: Bericht neu zusammengefasst") && git push -q origin HEAD:%ZWEIG% && goto %DANACH%
  git rebase --abort 2> nul
  timeout /t 5 > nul
)
goto fehler

:abgebrochen
REM Auch nach einem Abbruch kommen der Eintrag im Pruefprotokoll (mit --pruefung vor der Rechnung geschrieben) und die
REM fertigen Teilergebnisse auf den Zweig, wie auf GitHub
echo.
echo Die Rechnung ist abgebrochen. Eintrag im Pruefprotokoll und fertige Teilergebnisse kommen trotzdem hoch.
set MELDUNG=Profi-Bot %SCHRITT%: abgebrochen (PC), Pruefprotokoll und Teilergebnisse
set DANACH=fehler
goto hochladen

:fertig
echo.
echo === Fertig. Der Bericht steht in lernen/PROFI_ERGEBNISSE.md auf dem Zweig %ZWEIG%. ===
echo Dieses Fenster kann geschlossen werden.
pause
exit /b

:zip_fehlt
echo.
echo Die eingefrorenen Kurse dieses PCs fehlen: %REPO%\%ZIP%
echo Neu laden wuerde die Kurse aendern, darum wird nicht gerechnet.
goto fehler

:ohne_binance
echo.
echo Binance war nicht erreichbar. Ohne Binance-Kurse waere dieser Cache derselbe wie bei GitHub.
echo Bitte spaeter nochmals starten.
rmdir /s /q data\historie
goto fehler

:falscher_cache
echo.
echo Die Kurse in %ZIP% passen nicht zum Fingerabdruck in lernen\profi\cache_pc.txt:
echo   gerechnet %FINGER%
echo   erwartet  %SOLL%
goto fehler

:fehler
echo.
echo Es gab einen Fehler. Bitte ein Foto dieses Fensters an Claude schicken.
pause
exit /b 1
