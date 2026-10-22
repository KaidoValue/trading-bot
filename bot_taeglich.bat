@echo off
REM Startet den Bot einmal (Langfrist-Variante, Demo-Modus) und speichert den Stand.
REM Fuer die Windows-Aufgabenplanung gedacht. Protokoll: logs\bot.log
cd /d %~dp0
if not exist logs mkdir logs
py -3.13 -m tradingbot paper --config config_langfrist.yaml --once >> logs\bot.log 2>&1
