# Strategie-Vergleich mit echten Kursdaten

Erstellt: 23.10.2026 18:10 UTC. Startkapital je 1000, Gebühren und Slippage eingerechnet.
`adaptive` ist die lernende KI, `regime` die 200-Tage-Regel des Hauptbots.

## Daytrading: 1-Stunden-Kerzen, letzte 365 Tage

```
8760 Kerzen von 23.10.2025 bis 23.10.2026

                 Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %   CRV  Expectancy  Profit Factor  Max. Verlustserie
trend                852.56     -14.74        -27.12          -49.84        12.4           -15.14   -4.26    72.0            23.6  1.14       -1.45           0.35               14.0
mean_reversion       850.60     -14.94        -27.12          -49.84        12.1           -15.05   -3.61    67.0            23.9  1.56       -1.63           0.49                7.0
breakout             853.89     -14.61        -27.12          -49.84        13.0           -15.05   -3.70    92.0            29.3  1.32       -0.99           0.55                8.0
regime               849.33     -15.07        -27.12          -49.84        19.9           -15.07   -3.48    83.0            30.1  1.28       -1.22           0.55                9.0
pullback             957.20      -4.28        -27.12          -49.84         6.9            -5.36   -1.79    34.0            29.4  1.67       -0.62           0.70                8.0
momentum             850.78     -14.92        -27.12          -49.84        11.8           -15.36   -4.13    81.0            27.2  1.19       -1.23           0.44               18.0
price_action         845.44     -15.46        -27.12          -49.84         7.6           -15.46   -5.20    82.0            25.6  1.04       -1.29           0.36               11.0
smc                  880.36     -11.96        -27.12          -49.84        13.7           -12.12   -3.60   100.0            31.0  1.45       -0.58           0.65               10.0
reversal             854.52     -14.55        -27.12          -49.84        14.4           -15.06   -3.39   114.0            32.5  1.36       -0.68           0.65               11.0
range                847.21     -15.28        -27.12          -49.84         8.3           -15.41   -5.20    98.0            34.7  0.83       -0.95           0.44                7.0
ensemble             902.13      -9.79        -27.12          -49.84        14.0            -9.92   -3.10    62.0            29.0  1.35       -0.96           0.55                8.0
adaptive             849.02     -15.10        -27.12          -49.84        12.4           -15.10   -3.81    84.0            26.2  1.28       -1.20           0.45               11.0
adaptive_memory      854.08     -14.59        -27.12          -49.84         8.5           -15.08   -4.99    70.0            21.4  0.93       -1.49           0.25               13.0
```

### Walk-Forward nur KI (Test auf ungesehenen Daten)

```
8760 Kerzen von 23.10.2025 bis 23.10.2026

   Test ab  Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2026-02-10 adaptive            -7.68           -1.87               3.27
2026-03-18 adaptive            -5.10           -5.10               9.48
2026-04-24 adaptive            -5.96           -6.65              -4.81
2026-05-30 adaptive            -7.87           -6.19             -14.85
2026-07-06 adaptive            -9.69           -6.32               0.43
2026-08-11 adaptive           -10.79           -1.22              20.36
2026-09-17 adaptive            -7.00           -2.27               6.60

Gesamt ausserhalb der Trainingsdaten: -26.25 %
```

### Walk-Forward KI mit Gedächtnis

```
8760 Kerzen von 23.10.2025 bis 23.10.2026

   Test ab         Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2026-02-10 adaptive_memory            -7.68           -1.87               3.27
2026-03-18 adaptive_memory            -5.10           -5.10               9.48
2026-04-24 adaptive_memory            -5.96           -6.65              -4.81
2026-05-30 adaptive_memory            -7.87           -6.19             -14.85
2026-07-06 adaptive_memory            -9.69           -6.32               0.43
2026-08-11 adaptive_memory           -10.79           -1.22              20.36
2026-09-17 adaptive_memory            -7.00           -2.27               6.60

Gesamt ausserhalb der Trainingsdaten: -26.25 %
```

## Swing: 4-Stunden-Kerzen, letzte 730 Tage

```
4380 Kerzen von 23.10.2024 bis 23.10.2026

                 Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %   CRV  Expectancy  Profit Factor  Max. Verlustserie
trend                898.84     -10.12         17.44          -53.56        31.3           -15.25   -0.91    90.0            31.1  1.94       -0.49           0.87               13.0
mean_reversion       969.24      -3.08         17.44          -53.56        15.8           -11.46   -0.28    54.0            44.4  1.27        0.07           1.02                7.0
breakout             891.29     -10.87         17.44          -53.56        17.7           -15.11   -1.24    69.0            31.9  1.65       -0.95           0.77                9.0
regime               897.77     -10.22         17.44          -53.56        45.0           -12.94   -0.83    91.0            35.2  1.63       -0.51           0.88                8.0
pullback             954.14      -4.59         17.44          -53.56        10.3            -6.48   -0.78    30.0            30.0  1.77       -0.89           0.76                5.0
momentum             912.99      -8.70         17.44          -53.56        24.9           -15.14   -0.84    94.0            34.0  1.79       -0.28           0.92                8.0
price_action         860.02     -14.00         17.44          -53.56        23.4           -15.18   -1.56   107.0            41.1  1.08       -0.71           0.76                5.0
smc                  926.86      -7.31         17.44          -53.56        18.5            -9.68   -0.93    59.0            32.2  1.74       -0.62           0.83                8.0
reversal             888.91     -11.11         17.44          -53.56        27.2           -15.20   -1.11    90.0            35.6  1.52       -0.61           0.84                7.0
range                851.89     -14.81         17.44          -53.56         9.0           -15.18   -2.07    60.0            35.0  0.94       -1.88           0.51                8.0
ensemble             955.75      -4.43         17.44          -53.56         5.2            -6.88   -1.13    21.0            28.6  1.62       -1.46           0.65                7.0
adaptive             903.92      -9.61         17.44          -53.56        21.8           -15.08   -0.88    97.0            33.0  1.84       -0.36           0.90               10.0
adaptive_memory      911.85      -8.82         17.44          -53.56        23.5           -15.09   -0.78    97.0            37.1  1.56       -0.28           0.92                6.0
```

## Langfrist: Tageskerzen, letzte 2500 Tage

```
2500 Kerzen von 20.12.2019 bis 23.10.2026

                 Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %    CRV  Expectancy  Profit Factor  Max. Verlustserie
trend               1510.08      51.01        699.46          -76.66        56.4           -11.64    0.81    19.0            42.1   5.29       26.32           3.85                4.0
mean_reversion      1046.84       4.68        699.46          -76.66        12.4            -2.67    0.34    14.0            64.3   1.69        3.59           3.04                2.0
breakout            1475.43      47.54        699.46          -76.66        49.4            -9.70    0.92    34.0            44.1   4.15       14.34           3.27                6.0
regime              1465.22      46.52        699.46          -76.66        56.4           -19.57    0.67    12.0            41.7  12.73       37.75           9.09                3.0
pullback            1175.02      17.50        699.46          -76.66        28.4            -7.77    0.57     9.0            55.6   3.49       19.30           4.37                2.0
momentum            1239.21      23.92        699.46          -76.66        49.7           -12.75    0.68    52.0            36.5   3.27        4.90           1.88                6.0
price_action         993.93      -0.61        699.46          -76.66        49.1           -16.55   -0.00    56.0            39.3   1.59        0.15           1.03                7.0
smc                 1073.09       7.31        699.46          -76.66        32.2            -4.70    0.34    26.0            50.0   1.73        3.07           1.73                6.0
reversal            1073.57       7.36        699.46          -76.66        48.3           -13.11    0.24    46.0            43.5   1.69        1.91           1.30                4.0
range                986.02      -1.40        699.46          -76.66        10.3            -5.22   -0.10    29.0            48.3   0.99       -0.23           0.93                4.0
ensemble            1029.44       2.94        699.46          -76.66         3.1            -2.00    0.39     1.0           100.0   0.00       29.70           0.00                0.0
adaptive            1352.48      35.25        699.46          -76.66        50.4           -12.12    0.64    35.0            40.0   4.83       10.41           3.22                6.0
adaptive_memory     1402.17      40.22        699.46          -76.66        57.1           -13.06    0.68    38.0            36.8   4.66       10.30           2.72                9.0
```

### Walk-Forward KI gegen 200-Tage-Regel

KI (adaptive):
```
2500 Kerzen von 20.12.2019 bis 23.10.2026

   Test ab  Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-08 adaptive             1.27           -1.58             -51.47
2022-09-15 adaptive             0.77           -0.46              36.39
2023-05-23 adaptive            -0.72            0.96              54.72
2024-01-28 adaptive             0.12            1.19              44.54
2024-10-04 adaptive             0.22            2.93              77.66
2025-06-11 adaptive             0.77           -2.95             -36.70
2026-02-16 adaptive            -0.42            0.67              18.24

Gesamt ausserhalb der Trainingsdaten: 0.65 %
```

200-Tage-Regel (regime):
```
2500 Kerzen von 20.12.2019 bis 23.10.2026

   Test ab Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-08  regime             0.91            0.00             -51.47
2022-09-15  regime            -0.78            3.44              36.39
2023-05-23  regime             0.26            4.15              54.72
2024-01-28  regime             1.00            2.69              44.54
2024-10-04  regime             0.59            3.38              77.66
2025-06-11  regime             0.43           -0.26             -36.70
2026-02-16  regime             0.21            1.12              18.24

Gesamt ausserhalb der Trainingsdaten: 15.35 %
```

