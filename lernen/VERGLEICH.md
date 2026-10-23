# Strategie-Vergleich mit echten Kursdaten

Erstellt: 23.10.2026 00:01 UTC. Startkapital je 1000, Gebühren und Slippage eingerechnet.
`adaptive` ist die lernende KI, `regime` die 200-Tage-Regel des Hauptbots.

## Daytrading: 1-Stunden-Kerzen, letzte 365 Tage

```
8760 Kerzen von 23.10.2025 bis 23.10.2026

                Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %   CRV  Expectancy  Profit Factor  Max. Verlustserie
trend               854.34     -14.57        -27.26          -49.84        12.4           -15.07   -4.23    72.0            23.6  1.17       -1.42           0.36               14.0
mean_reversion      850.60     -14.94        -27.26          -49.84        12.1           -15.05   -3.61    67.0            23.9  1.56       -1.63           0.49                7.0
breakout            853.92     -14.61        -27.26          -49.84        13.0           -15.05   -3.70    92.0            29.3  1.32       -0.99           0.55                8.0
regime              849.33     -15.07        -27.26          -49.84        19.9           -15.07   -3.48    83.0            30.1  1.28       -1.22           0.55                9.0
pullback            957.21      -4.28        -27.26          -49.84         6.9            -5.36   -1.79    34.0            29.4  1.67       -0.62           0.70                8.0
momentum            850.81     -14.92        -27.26          -49.84        11.8           -15.36   -4.13    81.0            27.2  1.19       -1.23           0.44               18.0
price_action        845.44     -15.46        -27.26          -49.84         7.6           -15.46   -5.20    82.0            25.6  1.04       -1.29           0.36               11.0
smc                 880.37     -11.96        -27.26          -49.84        13.7           -12.12   -3.60   100.0            31.0  1.45       -0.58           0.65               10.0
reversal            854.54     -14.55        -27.26          -49.84        14.4           -15.06   -3.39   114.0            32.5  1.36       -0.68           0.65               11.0
range               847.21     -15.28        -27.26          -49.84         8.3           -15.41   -5.20    98.0            34.7  0.83       -0.95           0.44                7.0
ensemble            901.05      -9.90        -27.26          -49.84        13.9            -9.92   -3.14    61.0            27.9  1.39       -1.01           0.54                8.0
adaptive            849.86     -15.01        -27.26          -49.84        12.7           -15.09   -3.81    83.0            26.5  1.27       -1.21           0.46               11.0
```

### Walk-Forward nur KI (Test auf ungesehenen Daten)

```
8760 Kerzen von 23.10.2025 bis 23.10.2026

   Test ab  Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2026-02-09 adaptive            -7.28           -1.36               7.79
2026-03-18 adaptive            -4.61           -5.78               5.12
2026-04-23 adaptive            -5.61           -6.61              -5.36
2026-05-30 adaptive            -7.70           -4.85             -14.79
2026-07-05 adaptive            -9.31           -5.96               1.97
2026-08-11 adaptive           -10.86           -2.10              18.58
2026-09-16 adaptive            -7.49           -2.27               7.49

Gesamt ausserhalb der Trainingsdaten: -25.69 %
```

## Swing: 4-Stunden-Kerzen, letzte 730 Tage

```
4380 Kerzen von 23.10.2024 bis 23.10.2026

                Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %   CRV  Expectancy  Profit Factor  Max. Verlustserie
trend               894.96     -10.50         16.46          -53.56        31.3           -15.25   -0.95    90.0            30.0  2.01       -0.54           0.86               13.0
mean_reversion      969.24      -3.08         16.46          -53.56        15.8           -11.46   -0.28    54.0            44.4  1.27        0.07           1.02                7.0
breakout            891.29     -10.87         16.46          -53.56        17.7           -15.11   -1.24    69.0            31.9  1.65       -0.95           0.77                9.0
regime              889.81     -11.02         16.46          -53.56        45.1           -12.94   -0.89    92.0            34.8  1.62       -0.59           0.86                8.0
pullback            954.14      -4.59         16.46          -53.56        10.3            -6.48   -0.78    30.0            30.0  1.77       -0.89           0.76                5.0
momentum            913.00      -8.70         16.46          -53.56        24.9           -15.14   -0.84    94.0            34.0  1.79       -0.28           0.92                8.0
price_action        860.02     -14.00         16.46          -53.56        23.4           -15.18   -1.56   107.0            41.1  1.08       -0.71           0.76                5.0
smc                 926.39      -7.36         16.46          -53.56        18.4            -9.68   -0.94    59.0            32.2  1.74       -0.62           0.83                8.0
reversal            881.40     -11.86         16.46          -53.56        27.3           -15.20   -1.18    91.0            35.2  1.51       -0.68           0.82                7.0
range               851.89     -14.81         16.46          -53.56         9.0           -15.18   -2.07    60.0            35.0  0.94       -1.88           0.51                8.0
ensemble            955.75      -4.43         16.46          -53.56         5.2            -6.88   -1.13    21.0            28.6  1.62       -1.46           0.65                7.0
adaptive            891.78     -10.82         16.46          -53.56        21.9           -15.15   -1.05    96.0            32.3  1.82       -0.51           0.87               10.0
```

## Langfrist: Tageskerzen, letzte 2500 Tage

```
2500 Kerzen von 20.12.2019 bis 23.10.2026

                Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %   CRV  Expectancy  Profit Factor  Max. Verlustserie
trend              4215.04     321.50        697.83          -76.66        56.4           -32.97    0.94    19.0            42.1  3.55      161.54           2.58                4.0
mean_reversion     1201.05      20.11        697.83          -76.66        12.4           -13.00    0.33    14.0            64.3  1.40       15.65           2.52                2.0
breakout           3834.80     283.48        697.83          -76.66        49.4           -31.57    0.99    34.0            44.1  2.78       87.38           2.20                6.0
regime             4346.57     334.66        697.83          -76.66        56.3           -40.40    0.94    11.0            45.5  7.43      287.57           6.19                3.0
pullback           1858.26      85.83        697.83          -76.66        28.4           -25.32    0.61     9.0            55.6  3.13       93.94           3.91                2.0
momentum           2122.93     112.29        697.83          -76.66        48.1           -43.57    0.67    52.0            36.5  2.67       23.88           1.54                6.0
price_action        817.67     -18.23        697.83          -76.66        48.0           -60.31   -0.07    56.0            39.3  1.42       -2.07           0.92                7.0
smc                1261.97      26.20        697.83          -76.66        32.2           -21.58    0.31    26.0            50.0  1.49       11.50           1.49                6.0
reversal           1233.68      23.37        697.83          -76.66        46.6           -48.84    0.25    47.0            42.6  1.58        6.98           1.17                4.0
range               936.85      -6.32        697.83          -76.66        10.3           -22.52   -0.07    29.0            48.3  0.99       -1.08           0.92                4.0
ensemble           1147.20      14.72        697.83          -76.66         3.1            -8.40    0.43     1.0           100.0  0.00      148.50           0.00                0.0
adaptive           2735.48     173.55        697.83          -76.66        50.4           -33.21    0.74    35.0            40.0  3.15       52.89           2.10                6.0
```

### Walk-Forward KI gegen 200-Tage-Regel

KI (adaptive):
```
2500 Kerzen von 20.12.2019 bis 23.10.2026

   Test ab  Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-08 adaptive             1.60           -7.02             -51.47
2022-09-15 adaptive             0.90           -2.07              36.39
2023-05-23 adaptive            -0.69            4.52              54.72
2024-01-28 adaptive             0.16            4.46              44.54
2024-10-04 adaptive             0.27           15.04              77.66
2025-06-11 adaptive             0.87          -14.40             -36.70
2026-02-16 adaptive            -0.42            3.09              18.00

Gesamt ausserhalb der Trainingsdaten: 0.92 %
```

200-Tage-Regel (regime):
```
2500 Kerzen von 20.12.2019 bis 23.10.2026

   Test ab Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-08  regime             1.31            0.00             -51.47
2022-09-15  regime            -0.73           17.20              36.39
2023-05-23  regime             0.32           20.53              54.72
2024-01-28  regime             1.12            8.62              44.54
2024-10-04  regime             0.69           17.21              77.66
2025-06-11  regime             0.54           -1.22             -36.70
2026-02-16  regime             0.27            5.50              18.00

Gesamt ausserhalb der Trainingsdaten: 87.42 %
```

