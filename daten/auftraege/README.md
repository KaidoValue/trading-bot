# Aufträge an die Demo-Bots

Hier liegen Aufträge von Hand an die Demo-Bots. In seinen Stand (`daten/state/`) schreibt nur der Bot selbst: Ein
Auftrag wartet hier, bis der nächste Durchlauf dieses Bots (alle 30 Minuten) ihn ausführt, danach liegt er unter
`erledigt/`. Was der Bot gemacht hat, steht nach dem Lauf in [STATUS.md](../../STATUS.md) unter «Letzte
Entscheidung» und in der Trade-Tabelle.

- Auf GitHub: Actions → «Position schliessen» → Run workflow, Bot-Datei und Coins angeben.
- Lokal: `python -m tradingbot schliessen --config bots/config_daytrading.yaml --symbols TRX/CHF HYPE/CHF`
  (für die Bots auf GitHub die Datei danach hochladen: `git add`, `git commit`, `git push`).

## Format

Dateiname: `<Zeit UTC>_<Name der Bot-Datei>.txt`, die Zeit als Jahr, Monat, Tag, `T`, Stunde, Minute, Sekunde,
z.B. `20261030T201500_config_daytrading.txt` (30.10.2026 20:15:00 UTC, für `bots/config_daytrading.yaml`).
Inhalt: je Zeile ein Befehl, z.B.

```
schliessen TRX/CHF HYPE/CHF
```

- `schliessen <Coins>`: jede offene Position dieser Coins zum dann aktuellen Kurs schliessen (Market-Order zum Geld-
  bzw. Briefkurs, Grund «Von Hand geschlossen»). Ein Coin ohne offene Position wird übersprungen. Hat ein Coin mit
  Position gerade keinen Kurs, wartet der ganze Auftrag auf den nächsten Lauf.
- Unbekannte Befehle überspringt der Bot mit einer Warnung, der Auftrag kommt trotzdem nach `erledigt/`.
- Leere Zeilen und Zeilen, die mit `#` beginnen, zählen nicht.
- Nur Demo-Bots (Paper-Modus) führen Aufträge aus.
