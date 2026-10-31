# Was der Bot aus deiner Liste kennt

✅ = im Bot umgesetzt · 🟡 = teilweise / vereinfacht · ➖ = für einen Krypto-Bot nicht nötig oder nicht programmierbar (mit Begründung)

## Kerzen und Price Action

| Thema | Stand | Wo / wie |
|---|---|---|
| Candlestick-Charts, OHLC | ✅ | Alle Daten sind OHLCV-Kerzen (`data.py`) |
| Kerzenkörper und Dochte | ✅ | `patterns.py` misst Körper, oberen und unteren Docht |
| Hammer, Shooting Star, Doji | ✅ | `patterns.py` |
| Bullish / Bearish Engulfing | ✅ | `patterns.py` |
| Inside Bar, Outside Bar | ✅ | `patterns.py` |
| Price Action | ✅ | Strategie `price_action` |

## Marktstruktur

| Thema | Stand | Wo / wie |
|---|---|---|
| Aufwärts-, Abwärtstrend, Seitwärtsmarkt | ✅ | `structure.market_structure` → `trend` (+1 / -1 / 0) |
| Higher Highs, Higher Lows, Lower Highs, Lower Lows | ✅ | Spalten `HH`, `HL`, `LH`, `LL` |
| Swing Highs und Swing Lows | ✅ | `structure.swings`, erst nach Bestätigung sichtbar (kein Blick in die Zukunft) |
| Break of Structure (BOS) | ✅ | `BOS_up`, `BOS_down` |
| Change of Character (CHoCH), Trendwechsel | ✅ | `CHoCH_up`, `CHoCH_down`; Pullback- und SMC-Strategie steigen bei CHoCH aus |
| Support, Resistance | ✅ | Letzte bestätigte Swing-Tiefs/-Hochs |
| Angebots- und Nachfragezonen | 🟡 | Über Order Blocks und Fair Value Gaps abgebildet |
| Breakouts, Retests, Fehlausbrüche | ✅ | `structure.breakout_events`; Strategien `breakout`, `price_action` |
| Pullbacks und Retracements | ✅ | Strategie `pullback` |
| Trendlinien | 🟡 | Als Verbindung der Swing-Punkte (Dreiecke, Keile); keine frei gezeichneten Linien |
| Range-Trading | ✅ | Strategie `range` |
| Multi-Timeframe-Analyse | ✅ | `structure.htf_trend`: Pullback-Strategie handelt nur in Richtung des 4h-Trends |
| Zeiteinheiten 1m bis 1W | ✅ | `timeframe` in `bots/config.yaml` frei wählbar |

## Chartmuster

| Thema | Stand | Wo / wie |
|---|---|---|
| Doppelboden, Doppeltop | ✅ | `structure.chart_patterns`, Signal beim Bruch der Nackenlinie |
| Kopf-Schulter, inverse Kopf-Schulter | ✅ | dito |
| Dreiecke | ✅ | Zusammenlaufende Swings, Signal beim Ausbruch |
| Keile | ✅ | Steigender und fallender Keil |
| Flaggen und Wimpel | 🟡 | Vereinfacht: starker Impuls, enge Konsolidierung, Ausbruch in Impulsrichtung |
| Strategie dazu | ✅ | `reversal` |

## Indikatoren und Volumen

| Thema | Stand | Wo / wie |
|---|---|---|
| RSI, MACD, MA, EMA, Bollinger, ATR | ✅ | `indicators.py` |
| Fibonacci-Retracements und -Extensions | ✅ | `indicators.fibonacci`; Pullback-Strategie kauft in der Zone 50–78,6 % |
| Momentum | ✅ | Rate of Change; Strategie `momentum` |
| Volatilität | ✅ | ATR bestimmt Stop-Abstand und Positionsgrösse |
| Divergenzen | ✅ | RSI-Divergenzen an Swing-Punkten (`structure.divergences`) |
| Volumenanalyse, Volumenspitzen | ✅ | `indicators.volume_spike`; Momentum verlangt erhöhtes Volumen |
| VWAP | ✅ | `indicators.vwap` (täglich) |
| Volume Profile | 🟡 | Point of Control (`indicators.volume_profile_poc`), noch nicht in einer Strategie |
| Relative Stärke | 🟡 | RSI vorhanden; Vergleich mehrerer Coins untereinander noch nicht |
| Korrelation zwischen Märkten | ✅ | Bei mehreren Coins: korrelierte Positionen nur halb so gross |

## Smart Money Concepts

| Thema | Stand | Wo / wie |
|---|---|---|
| Fair Value Gaps | ✅ | `structure.smc`, Rücklauf in die Lücke als Einstieg |
| Order Blocks | ✅ | Letzte Gegenkerze vor einem Strukturbruch |
| Liquidity Sweeps | ✅ | Docht über Swing-Hoch/-Tief mit Schluss zurück in der Range |
| Inducement | 🟡 | Über Liquidity Sweeps angenähert |
| Premium- und Discount-Bereiche | ✅ | Position in der Swing-Range; Longs nur im Discount |
| Strategie dazu | ✅ | `smc` |

## Orders, Markt und Ausführung

| Thema | Stand | Wo / wie |
|---|---|---|
| Orderbuch, Markttiefe, Bid, Ask, Spread, Liquidität | ✅ | Vor jedem Einstieg wird das Orderbuch geprüft; bei zu grossem Spread kein Trade |
| Slippage, Gebühren | ✅ | In Backtest und Demo eingerechnet |
| Market-Orders | ✅ | Live-Ausführung |
| Limit-, Stop-, Stop-Limit-Orders | 🟡 | Stops und Ziele überwacht der Bot selbst. Im Demo-Betrieb spielt er alle 30 Minuten die Minutenkerzen seit dem letzten Lauf durch wie eine Stop-Order an der Börse (Ausführung an der Marke minus Slippage), live schliesst er per Market-Order. Echte Stop-Orders an der Börse folgen in einer späteren Version |
| Stop-Loss, Take-Profit | ✅ | Bei jedem Trade, aus der ATR berechnet |
| Handelszeiten, London- und New-York-Session | ✅ | Jeder Trade wird einer Sitzung zugeordnet; `report` zeigt, wann der Bot am besten handelt |

## Nachrichten und Fundamentales

| Thema | Stand | Wo / wie |
|---|---|---|
| Nachrichten | ✅ | 4 Krypto-Portale, ein Thema zählt erst ab 2 Quellen |
| Wirtschaftsdaten, Zinsentscheide, Inflation | ✅ | Wirtschaftskalender: ±30 Minuten um wichtige US-Termine keine neuen Trades |
| Aussagen wichtiger Personen (Trump, Powell, Musk …) | ✅ | `events.py`: Alarm, Pause oder Handel nur in die klare Richtung |
| Marktstimmung | ✅ | Fear & Greed Index |
| Unternehmensberichte, Fundamentalanalyse | ➖ | Für Kryptowährungen kaum anwendbar; relevant wird es bei Aktien |
| Marktphasen und Marktzyklen | 🟡 | Die lernende Gewichtung erkennt, welche Strategie in der aktuellen Phase funktioniert |

## Risikomanagement

| Thema | Stand | Wo / wie |
|---|---|---|
| Positionsgrössenberechnung, Kontorisiko pro Trade | ✅ | 1 % Risiko pro Trade |
| Gesamtrisiko offener Positionen | ✅ | max. 3 % Summe aller Stop-Abstände, max. 3 Positionen |
| Risikobegrenzung bei korrelierten Positionen | ✅ | Halbe Grösse bei Korrelation > 0,8 |
| Chance-Risiko-Verhältnis | ✅ | Standard 2:1 (Ziel 4 × ATR, Stop 2 × ATR) |
| Drawdown, Kapitalerhalt | ✅ | Tageslimit 3 %, Not-Aus bei 15 % |
| Verlustserien | ✅ | Nach 3 Verlusten in Folge 12 Stunden Pause |
| Hebel, Margin, Liquidationsrisiko | ➖ | Bewusst kein Hebel. Shorts nur im Demo-Modus |

## Psychologie

Ein Bot hat keine Gefühle, aber die typischen Fehler lassen sich als Regeln verhindern:

| Thema | Stand | Wo / wie |
|---|---|---|
| FOMO | ✅ | Kein Einstieg ohne Signal; bei Ereignissen und Wirtschaftsterminen Pause |
| Revenge Trading | ✅ | Pause nach Verlustserie |
| Overtrading | ✅ | max. 6 Trades pro Tag |
| Disziplin und Geduld | ✅ | Feste Regeln, die der Bot immer einhält |

## Testen, Auswerten, Verbessern

| Thema | Stand | Wo / wie |
|---|---|---|
| Backtesting | ✅ | `backtest`, `compare` |
| Forward Testing, Demokonto | ✅ | `paper` |
| Walk-Forward-Analyse, Vermeidung von Overfitting | ✅ | `walkforward`: Strategie wird nur auf alten Daten gewählt und auf neuen getestet |
| Trefferquote, Expectancy, Profit Factor, CRV, Drawdown | ✅ | In jeder Backtest-Auswertung |
| Trading-Journal, Dokumentation | ✅ | `daten/logs/trades*.csv` mit Nachrichtenlage und Sitzung |
| Kontinuierliche Verbesserung | ✅ | Lernende Gewichtung + `report` |
| Handelsstrategie entwickeln | ✅ | Neue Strategien als Klasse in `strategies.py`, Tests prüfen automatisch auf Blick in die Zukunft |

## Strategietypen

| Thema | Stand |
|---|---|
| Trendfolge, Breakout, Pullback, Momentum, Mean Reversion, Range | ✅ (je eigene Strategie, alle in der lernenden KI) |
| Daytrading, Swingtrading, Positionstrading | ✅ über die Zeiteinheit: 15m–1h ≈ Daytrading, 4h ≈ Swing, 1D ≈ Position |
| Scalping | ➖ Mit 0,2–0,8 % Gebühr pro Order (Kraken: 0,8 % in der kleinsten Stufe) bei Privatkonten nicht profitabel |

## Märkte und Plattformen

| Thema | Stand |
|---|---|
| Kryptowährungen | ✅ über ccxt (Kraken, Bitstamp, Coinbase, Binance und über 100 weitere) |
| Aktien, ETFs, Indizes, Forex, Futures, CFDs, Optionen, Rohstoffe | ➖ Nicht im Fokus, da du Krypto gewählt hast. Möglich später über Interactive Brokers oder MetaTrader 5 |
| Währungskonvertierung, Wechselkursrisiko | 🟡 Handel direkt in CHF-Paaren (BTC/CHF) vermeidet das Risiko |
| Broker-Auswahl und Regulierung | ✅ Vergleich im README |
| TradingView, Chartsoftware | ➖ Der Bot braucht keine Charts; zum Nachschauen kannst du TradingView parallel nutzen |

## Steuern in der Schweiz

➖ Kein Code, aber wichtig: Für Privatpersonen sind Kapitalgewinne auf Kryptowährungen in der Schweiz grundsätzlich steuerfrei, das Vermögen muss aber in der Steuererklärung angegeben werden. Wer sehr häufig handelt, mit Fremdkapital arbeitet oder hohe Umsätze im Verhältnis zum Vermögen hat, kann als **gewerbsmässiger Händler** eingestuft werden; dann sind Gewinne als Einkommen steuerpflichtig. Ein automatischer Bot kann dieses Risiko erhöhen. Kläre das vor dem Live-Betrieb mit einer Steuerberatung. `daten/logs/trades*.csv` dient als Nachweis aller Trades.
