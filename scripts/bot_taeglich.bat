@echo off
REM Startet den Bot einmal (Langfrist-Variante, Demo-Modus) und speichert den Stand.
REM Fuer die Windows-Aufgabenplanung gedacht. Protokoll: daten\logs\bot.log
cd /d %~dp0..
if not exist daten\logs mkdir daten\logs
py -3.13 -m tradingbot paper --config bots\config_langfrist.yaml --once >> daten\logs\bot.log 2>&1
