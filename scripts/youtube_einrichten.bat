@echo off
chcp 65001 > nul
REM Einmalige Einrichtung auf dem Windows-PC: holt die Abschriften neuer YouTube-Videos fuer den KI-Bot.
REM Einfach doppelklicken. Danach laeuft es bei jeder Anmeldung am PC und taeglich um 18 Uhr automatisch.
setlocal
set REPO=%USERPROFILE%\trading-bot
echo.
echo === Trading-Bot: YouTube-Wissen einrichten ===
echo.

where py > nul 2>&1
if errorlevel 1 (
  echo Python fehlt, wird jetzt installiert ...
  winget install -e --id Python.Python.3.12 --accept-package-agreements --accept-source-agreements
  echo.
  echo Python ist installiert. Bitte diese Datei jetzt NOCHMALS doppelklicken.
  pause
  exit /b
)
where git > nul 2>&1
if errorlevel 1 (
  echo Git fehlt, wird jetzt installiert ...
  winget install -e --id Git.Git --accept-package-agreements --accept-source-agreements
  echo.
  echo Git ist installiert. Bitte diese Datei jetzt NOCHMALS doppelklicken.
  pause
  exit /b
)

if not exist "%REPO%\.git" (
  echo Lade das Trading-Bot-Projekt nach %REPO% ...
  git clone https://github.com/KaidoValue/trading-bot.git "%REPO%" || goto fehler
)
cd /d "%REPO%"
git config user.name "trading-bot-pc"
git config user.email "trading-bot@users.noreply.github.com"
git pull -q origin main

echo Installiere die noetigen Python-Bausteine (dauert 1-2 Minuten) ...
py -m pip install -q --disable-pip-version-check -r requirements.txt || goto fehler

echo Richte die automatische Ausfuehrung ein ...
schtasks /create /tn "TradingBot YouTube (Anmeldung)" /tr "\"%REPO%\scripts\youtube_pc.bat\"" /sc onlogon /f > nul
schtasks /create /tn "TradingBot YouTube (18 Uhr)" /tr "\"%REPO%\scripts\youtube_pc.bat\"" /sc daily /st 18:00 /f > nul

echo.
echo Erster Lauf. Beim ersten Hochladen oeffnet sich ein GitHub-Anmeldefenster: bitte dort anmelden.
echo.
call "%REPO%\scripts\youtube_pc.bat" show
echo.
echo === Fertig. Ab jetzt laeuft es automatisch. Dieses Fenster kann geschlossen werden. ===
pause
exit /b

:fehler
echo.
echo Es gab einen Fehler. Bitte ein Foto dieses Fensters an Claude schicken.
pause
