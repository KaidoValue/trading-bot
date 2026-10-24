# Strategie-Vergleich mit echten Kursdaten

Erstellt: 24.10.2026 13:06 UTC. Startkapital je 1000, Gebühren und Slippage eingerechnet.
`adaptive` ist die lernende KI, `regime` die 200-Tage-Regel des Hauptbots.

## Daytrading: 1-Stunden-Kerzen, letzte 365 Tage

```
8760 Kerzen von 24.10.2025 bis 24.10.2026

                    Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %   CRV  Expectancy  Profit Factor  Max. Verlustserie
trend                   849.29     -15.07        -29.74          -49.84        12.0           -15.22   -4.41    72.0            22.2  1.20       -1.49           0.34               14.0
mean_reversion          850.60     -14.94        -29.74          -49.84        12.1           -15.05   -3.61    67.0            23.9  1.56       -1.63           0.49                7.0
breakout                850.23     -14.98        -29.74          -49.84        12.7           -15.00   -3.83    90.0            27.8  1.36       -1.07           0.52                8.0
regime                  849.33     -15.07        -29.74          -49.84        19.9           -15.07   -3.48    83.0            30.1  1.28       -1.22           0.55                9.0
pullback                955.49      -4.45        -29.74          -49.84         6.9            -5.36   -1.87    33.0            27.3  1.76       -0.71           0.66                8.0
momentum                846.13     -15.39        -29.74          -49.84        11.5           -15.39   -4.30    79.0            25.3  1.22       -1.34           0.41               18.0
price_action            845.42     -15.46        -29.74          -49.84         7.6           -15.46   -5.20    82.0            25.6  1.04       -1.29           0.36               11.0
smc                     878.78     -12.12        -29.74          -49.84        13.7           -12.12   -3.65    99.0            30.3  1.46       -0.61           0.64               10.0
reversal                851.88     -14.81        -29.74          -49.84        14.3           -15.06   -3.47   113.0            31.0  1.42       -0.71           0.64               11.0
range                   847.21     -15.28        -29.74          -49.84         8.3           -15.41   -5.20    98.0            34.7  0.83       -0.95           0.44                7.0
ensemble                901.05      -9.90        -29.74          -49.84        13.9            -9.92   -3.14    61.0            27.9  1.39       -1.01           0.54                8.0
adaptive                849.14     -15.09        -29.74          -49.84        12.4           -15.09   -3.82    84.0            26.2  1.28       -1.20           0.46               11.0
adaptive_memory         850.51     -14.95        -29.74          -49.84         9.1           -15.10   -4.93    71.0            19.7  1.06       -1.51           0.26               12.0
yt_fib_welle            945.20      -5.48        -29.74          -49.84         9.1            -5.79   -2.12    37.0            29.7  1.54       -0.85           0.65                6.0
yt_zyklus               993.72      -0.63        -29.74          -49.84         0.8            -1.32   -0.56     1.0             0.0  0.00       -5.63           0.00                1.0
yt_divergenz            926.19      -7.38        -29.74          -49.84        10.3            -9.77   -1.82    44.0            34.1  1.28       -1.05           0.66                7.0
buch_turtle             849.88     -15.01        -29.74          -49.84        18.4           -15.04   -3.74    90.0            28.9  1.31       -1.07           0.53                7.0
buch_triple_screen      849.18     -15.08        -29.74          -49.84         8.1           -15.08   -5.41    66.0            13.6  1.34       -1.69           0.21               23.0
buch_golden_cross       851.53     -14.85        -29.74          -49.84        17.4           -15.14   -3.78    99.0            31.3  1.35       -0.89           0.61                8.0
buch_livermore          862.27     -13.77        -29.74          -49.84        26.1           -14.65   -2.90   117.0            34.2  1.43       -0.57           0.74                8.0
```

### Walk-Forward nur KI (Test auf ungesehenen Daten)

```
8760 Kerzen von 24.10.2025 bis 24.10.2026

   Test ab  Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2026-02-11 adaptive            -7.65           -1.87               1.86
2026-03-19 adaptive            -5.10           -5.61              11.62
2026-04-25 adaptive            -5.73           -6.69              -4.99
2026-05-31 adaptive            -7.53           -6.31             -13.20
2026-07-07 adaptive           -10.03           -5.56               0.78
2026-08-12 adaptive           -10.78           -1.06              21.11
2026-09-18 adaptive            -7.01           -2.27               4.95

Gesamt ausserhalb der Trainingsdaten: -26.06 %
```

### Walk-Forward KI mit Gedächtnis

```
8760 Kerzen von 24.10.2025 bis 24.10.2026

   Test ab         Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2026-02-11 adaptive_memory            -9.13           -2.05               1.86
2026-03-19 adaptive_memory            -5.63           -5.62              11.62
2026-04-25 adaptive_memory            -6.43           -6.44              -4.99
2026-05-31 adaptive_memory            -7.40           -4.27             -13.20
2026-07-07 adaptive_memory            -9.60           -5.38               0.78
2026-08-12 adaptive_memory           -10.25           -0.82              21.11
2026-09-18 adaptive_memory            -6.86           -4.15               4.95

Gesamt ausserhalb der Trainingsdaten: -25.52 %
```

## Swing: 4-Stunden-Kerzen, letzte 730 Tage

```
4380 Kerzen von 24.10.2024 bis 24.10.2026

                    Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %   CRV  Expectancy  Profit Factor  Max. Verlustserie
trend                   905.09      -9.49          17.6          -53.56        31.2           -15.25   -0.85    88.0            30.7  2.01       -0.44           0.89               13.0
mean_reversion          969.24      -3.08          17.6          -53.56        15.8           -11.46   -0.28    54.0            44.4  1.27        0.07           1.02                7.0
breakout                891.31     -10.87          17.6          -53.56        17.7           -15.11   -1.24    69.0            31.9  1.65       -0.95           0.77                9.0
regime                  906.71      -9.33          17.6          -53.56        44.9           -12.94   -0.75    90.0            35.6  1.64       -0.42           0.90                8.0
pullback                954.14      -4.59          17.6          -53.56        10.3            -6.48   -0.78    30.0            30.0  1.77       -0.89           0.76                5.0
momentum                913.05      -8.70          17.6          -53.56        24.9           -15.14   -0.84    94.0            34.0  1.79       -0.28           0.92                8.0
price_action            860.02     -14.00          17.6          -53.56        23.4           -15.18   -1.56   107.0            41.1  1.08       -0.71           0.76                5.0
smc                     924.87      -7.51          17.6          -53.56        18.7            -9.68   -0.96    59.0            32.2  1.74       -0.62           0.83                8.0
reversal                888.94     -11.11          17.6          -53.56        27.2           -15.20   -1.11    90.0            35.6  1.52       -0.61           0.84                7.0
range                   851.89     -14.81          17.6          -53.56         9.0           -15.18   -2.07    60.0            35.0  0.94       -1.88           0.51                8.0
ensemble                955.75      -4.43          17.6          -53.56         5.2            -6.88   -1.13    21.0            28.6  1.62       -1.46           0.65                7.0
adaptive                886.77     -11.32          17.6          -53.56        21.1           -15.19   -1.10    94.0            31.9  1.80       -0.59           0.84               10.0
adaptive_memory         907.60      -9.24          17.6          -53.56        20.9           -15.17   -0.86    91.0            37.4  1.50       -0.39           0.89                6.0
yt_fib_welle            922.55      -7.74          17.6          -53.56         7.9            -9.65   -1.62    20.0            15.0  2.15       -3.25           0.38                8.0
yt_zyklus               960.35      -3.97          17.6          -53.56         3.6            -5.46   -1.01    10.0            20.0  1.80       -3.34           0.45                5.0
yt_divergenz            947.82      -5.22          17.6          -53.56         6.0            -7.34   -0.98    23.0            30.4  1.53       -1.64           0.67                5.0
buch_turtle             975.44      -2.46          17.6          -53.56        20.7            -9.52   -0.25    55.0            38.2  1.70        0.20           1.05                7.0
buch_triple_screen      897.19     -10.28          17.6          -53.56        31.9           -15.08   -0.97   104.0            29.8  2.08       -0.35           0.88               10.0
buch_golden_cross       862.62     -13.74          17.6          -53.56        19.1           -15.27   -1.66    55.0            27.3  1.55       -1.89           0.58               18.0
buch_livermore          870.44     -12.96          17.6          -53.56        23.3           -13.02   -1.51    69.0            31.9  1.50       -1.27           0.70                8.0
```

## Langfrist: Tageskerzen, letzte 2500 Tage

```
2500 Kerzen von 21.12.2019 bis 24.10.2026

                    Endkapital  Rendite %  Buy & Hold %  B&H Drawdown %  Im Markt %  Max. Drawdown %  Sharpe  Trades  Trefferquote %    CRV  Expectancy  Profit Factor  Max. Verlustserie
trend                  1516.24      51.62         741.2          -76.66        56.4           -11.64    0.81    19.0            42.1   5.45       26.71           3.96                4.0
mean_reversion         1046.84       4.68         741.2          -76.66        12.4            -2.67    0.34    14.0            64.3   1.69        3.59           3.04                2.0
breakout               1475.43      47.54         741.2          -76.66        49.4            -9.70    0.92    34.0            44.1   4.15       14.34           3.27                6.0
regime                 1468.13      46.81         741.2          -76.66        56.4           -19.67    0.67    12.0            41.7  12.80       38.10           9.14                3.0
pullback               1174.02      17.40         741.2          -76.66        28.4            -7.77    0.57     9.0            55.6   3.50       19.30           4.37                2.0
momentum               1239.21      23.92         741.2          -76.66        49.7           -12.75    0.68    52.0            36.5   3.27        4.90           1.88                6.0
price_action            993.93      -0.61         741.2          -76.66        49.1           -16.55   -0.00    56.0            39.3   1.59        0.15           1.03                7.0
smc                    1073.15       7.31         741.2          -76.66        32.2            -4.70    0.34    26.0            50.0   1.73        3.08           1.73                6.0
reversal               1072.64       7.26         741.2          -76.66        48.3           -13.11    0.24    46.0            43.5   1.69        1.91           1.30                4.0
range                   986.02      -1.40         741.2          -76.66        10.3            -5.22   -0.10    29.0            48.3   0.99       -0.23           0.93                4.0
ensemble               1029.44       2.94         741.2          -76.66         3.1            -2.00    0.39     1.0           100.0   0.00       29.70           0.00                0.0
adaptive               1352.48      35.25         741.2          -76.66        50.4           -12.12    0.64    35.0            40.0   4.83       10.41           3.22                6.0
adaptive_memory        1406.76      40.68         741.2          -76.66        57.2           -12.77    0.69    38.0            36.8   4.77       10.45           2.78                9.0
yt_fib_welle           1022.57       2.26         741.2          -76.66        16.5            -4.06    0.17     8.0            50.0   1.50        3.08           1.50                2.0
yt_zyklus              1081.32       8.13         741.2          -76.66        61.1            -7.54    0.38     4.0            50.0   3.37       20.53           3.37                1.0
yt_divergenz           1097.72       9.77         741.2          -76.66        26.1            -5.54    0.55     7.0            71.4   0.95       14.21           2.38                1.0
buch_turtle            1281.87      28.19         741.2          -76.66        43.5           -13.55    0.57    18.0            50.0   4.53       16.49           4.53                4.0
buch_triple_screen     1365.21      36.52         741.2          -76.66        47.5           -13.78    0.71    44.0            22.7  11.57        8.51           3.40               15.0
buch_golden_cross      1354.79      35.48         741.2          -76.66        53.9           -21.53    0.52     6.0            66.7   5.56       61.07          11.12                1.0
buch_livermore         1120.56      12.06         741.2          -76.66        18.8            -4.03    0.72     9.0            44.4   5.64       11.69           4.52                3.0
```

### Walk-Forward KI gegen 200-Tage-Regel

KI (adaptive):
```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab  Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09 adaptive             1.27           -1.58             -52.98
2022-09-16 adaptive             0.81           -0.46              37.49
2023-05-24 adaptive            -0.81            0.93              59.64
2024-01-29 adaptive             0.11            0.88              43.36
2024-10-05 adaptive             0.25            2.93              75.11
2025-06-12 adaptive             0.72           -2.95             -34.87
2026-02-17 adaptive            -0.46            0.67              19.64

Gesamt ausserhalb der Trainingsdaten: 0.31 %
```

200-Tage-Regel (regime):
```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09  regime             0.91            0.00             -52.98
2022-09-16  regime            -0.74            3.63              37.49
2023-05-24  regime             0.27            4.54              59.64
2024-01-29  regime             1.00            2.14              43.36
2024-10-05  regime             0.60            3.21              75.11
2025-06-12  regime             0.43            0.05             -34.87
2026-02-17  regime             0.21            1.03              19.64

Gesamt ausserhalb der Trainingsdaten: 15.44 %
```

## Regeln aus YouTube-Videos und Trading-Büchern (Walk-Forward, nur ungesehene Daten)

Herleitung der Regeln: lernen/YOUTUBE.md und lernen/BUECHER.md

### yt_fib_welle, Tageskerzen 2500 Tage

```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab      Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09 yt_fib_welle            -0.51            0.00             -52.98
2022-09-16 yt_fib_welle            -1.27            3.18              37.49
2023-05-24 yt_fib_welle             0.32            0.35              59.64
2024-01-29 yt_fib_welle             0.61            1.74              43.36
2024-10-05 yt_fib_welle             0.59           -0.52              75.11
2025-06-12 yt_fib_welle             0.55           -0.37             -34.87
2026-02-17 yt_fib_welle            -0.29            0.00              19.64

Gesamt ausserhalb der Trainingsdaten: 4.41 %
```

### yt_fib_welle, 4-Stunden-Kerzen 730 Tage

```
4380 Kerzen von 24.10.2024 bis 24.10.2026

   Test ab      Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2025-05-31 yt_fib_welle            -0.97           -0.32              14.49
2025-08-12 yt_fib_welle            -1.52           -1.86              -8.02
2025-10-24 yt_fib_welle            -3.13            0.00             -15.08
2026-01-05 yt_fib_welle            -2.52            0.47             -26.40
2026-03-19 yt_fib_welle            -0.79           -1.36               4.68
2026-05-31 yt_fib_welle            -0.69           -1.27             -13.73
2026-08-12 yt_fib_welle            -1.93           -1.83              27.44

Gesamt ausserhalb der Trainingsdaten: -6.03 %
```

### yt_zyklus, Tageskerzen 2500 Tage

```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab   Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09 yt_zyklus             0.94           -6.01             -52.98
2022-09-16 yt_zyklus            -0.47            3.20              37.49
2023-05-24 yt_zyklus            -0.33            0.00              59.64
2024-01-29 yt_zyklus             0.78            0.00              43.36
2024-10-05 yt_zyklus             0.00            2.96              75.11
2025-06-12 yt_zyklus             0.91           -4.29             -34.87
2026-02-17 yt_zyklus            -0.27            1.43              19.64

Gesamt ausserhalb der Trainingsdaten: -3.05 %
```

### yt_zyklus, 4-Stunden-Kerzen 730 Tage

```
4380 Kerzen von 24.10.2024 bis 24.10.2026

   Test ab   Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2025-05-31 yt_zyklus             0.00            0.00              14.49
2025-08-12 yt_zyklus             0.00            0.00              -8.02
2025-10-24 yt_zyklus             0.00           -2.99             -15.08
2026-01-05 yt_zyklus            -3.28            0.37             -26.40
2026-03-19 yt_zyklus            -1.73           -1.83               4.68
2026-05-31 yt_zyklus            -2.10           -0.31             -13.73
2026-08-12 yt_zyklus            -0.51            0.00              27.44

Gesamt ausserhalb der Trainingsdaten: -4.71 %
```

### yt_divergenz, Tageskerzen 2500 Tage

```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab      Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09 yt_divergenz             0.12           -4.09             -52.98
2022-09-16 yt_divergenz            -0.76            3.11              37.49
2023-05-24 yt_divergenz            -0.18            4.93              59.64
2024-01-29 yt_divergenz             0.58            0.00              43.36
2024-10-05 yt_divergenz             1.50            3.70              75.11
2025-06-12 yt_divergenz             1.97           -2.30             -34.87
2026-02-17 yt_divergenz             0.24            4.37              19.64

Gesamt ausserhalb der Trainingsdaten: 9.73 %
```

### yt_divergenz, 4-Stunden-Kerzen 730 Tage

```
4380 Kerzen von 24.10.2024 bis 24.10.2026

   Test ab      Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2025-05-31 yt_divergenz            -1.67           -0.71              14.49
2025-08-12 yt_divergenz            -2.42           -1.37              -8.02
2025-10-24 yt_divergenz            -0.75           -2.62             -15.08
2026-01-05 yt_divergenz            -1.99           -2.17             -26.40
2026-03-19 yt_divergenz            -2.89           -0.14               4.68
2026-05-31 yt_divergenz            -3.03           -1.99             -13.73
2026-08-12 yt_divergenz            -2.50            1.87              27.44

Gesamt ausserhalb der Trainingsdaten: -6.98 %
```

### buch_turtle, Tageskerzen 2500 Tage

```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab     Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09 buch_turtle             0.99           -1.62             -52.98
2022-09-16 buch_turtle             0.89            0.13              37.49
2023-05-24 buch_turtle            -0.26            1.80              59.64
2024-01-29 buch_turtle             0.01            2.20              43.36
2024-10-05 buch_turtle             0.53            4.04              75.11
2025-06-12 buch_turtle             1.06           -2.40             -34.87
2026-02-17 buch_turtle             0.29           -0.15              19.64

Gesamt ausserhalb der Trainingsdaten: 3.91 %
```

### buch_turtle, 4-Stunden-Kerzen 730 Tage

```
4380 Kerzen von 24.10.2024 bis 24.10.2026

   Test ab     Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2025-05-31 buch_turtle             0.50           -0.09              14.49
2025-08-12 buch_turtle             0.01            0.25              -8.02
2025-10-24 buch_turtle             0.14            0.03             -15.08
2026-01-05 buch_turtle             0.51           -3.16             -26.40
2026-03-19 buch_turtle            -1.39           -2.33               4.68
2026-05-31 buch_turtle            -2.39           -0.24             -13.73
2026-08-12 buch_turtle            -1.80            1.49              27.44

Gesamt ausserhalb der Trainingsdaten: -4.06 %
```

### buch_triple_screen, Tageskerzen 2500 Tage

```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab            Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09 buch_triple_screen             1.24           -0.49             -52.98
2022-09-16 buch_triple_screen             1.14           -2.62              37.49
2023-05-24 buch_triple_screen            -0.67            0.09              59.64
2024-01-29 buch_triple_screen            -0.50            2.24              43.36
2024-10-05 buch_triple_screen             0.18            6.09              75.11
2025-06-12 buch_triple_screen             1.00           -0.41             -34.87
2026-02-17 buch_triple_screen             0.29            0.44              19.64

Gesamt ausserhalb der Trainingsdaten: 5.23 %
```

### buch_triple_screen, 4-Stunden-Kerzen 730 Tage

```
4380 Kerzen von 24.10.2024 bis 24.10.2026

   Test ab            Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2025-05-31 buch_triple_screen             0.28           -1.52              14.49
2025-08-12 buch_triple_screen            -1.55           -1.29              -8.02
2025-10-24 buch_triple_screen            -0.57           -2.13             -15.08
2026-01-05 buch_triple_screen            -2.35           -2.70             -26.40
2026-03-19 buch_triple_screen            -2.29            1.27               4.68
2026-05-31 buch_triple_screen            -1.21           -4.09             -13.73
2026-08-12 buch_triple_screen            -1.41           -1.61              27.44

Gesamt ausserhalb der Trainingsdaten: -11.54 %
```

### buch_golden_cross, Tageskerzen 2500 Tage

```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab           Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09 buch_golden_cross             0.83            0.23             -52.98
2022-09-16 buch_golden_cross            -0.71            1.05              37.49
2023-05-24 buch_golden_cross             0.07            1.92              59.64
2024-01-29 buch_golden_cross             0.44            4.93              43.36
2024-10-05 buch_golden_cross             0.57            0.94              75.11
2025-06-12 buch_golden_cross             0.49           -1.07             -34.87
2026-02-17 buch_golden_cross            -0.04           -0.71              19.64

Gesamt ausserhalb der Trainingsdaten: 7.40 %
```

### buch_golden_cross, 4-Stunden-Kerzen 730 Tage

```
4380 Kerzen von 24.10.2024 bis 24.10.2026

   Test ab           Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2025-05-31 buch_golden_cross            -0.63           -3.69              14.49
2025-08-12 buch_golden_cross            -0.56           -5.27              -8.02
2025-10-24 buch_golden_cross            -2.24            0.00             -15.08
2026-01-05 buch_golden_cross            -4.49           -0.85             -26.40
2026-03-19 buch_golden_cross            -2.30           -2.67               4.68
2026-05-31 buch_golden_cross            -1.33           -3.91             -13.73
2026-08-12 buch_golden_cross            -2.28           -0.39              27.44

Gesamt ausserhalb der Trainingsdaten: -15.73 %
```

### buch_livermore, Tageskerzen 2500 Tage

```
2500 Kerzen von 21.12.2019 bis 24.10.2026

   Test ab        Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2022-01-09 buch_livermore             1.10            0.00             -52.98
2022-09-16 buch_livermore             0.00           -1.73              37.49
2023-05-24 buch_livermore            -1.02            2.18              59.64
2024-01-29 buch_livermore             0.10            0.00              43.36
2024-10-05 buch_livermore             0.31            4.45              75.11
2025-06-12 buch_livermore             0.92           -0.56             -34.87
2026-02-17 buch_livermore             0.87            1.62              19.64

Gesamt ausserhalb der Trainingsdaten: 5.98 %
```

### buch_livermore, 4-Stunden-Kerzen 730 Tage

```
4380 Kerzen von 24.10.2024 bis 24.10.2026

   Test ab        Gewählt  Sharpe Training  Rendite Test %  Buy & Hold Test %
2025-05-31 buch_livermore            -1.99            0.89              14.49
2025-08-12 buch_livermore             0.18            0.12              -8.02
2025-10-24 buch_livermore             0.42           -1.91             -15.08
2026-01-05 buch_livermore            -0.43           -0.43             -26.40
2026-03-19 buch_livermore            -1.30           -1.48               4.68
2026-05-31 buch_livermore            -1.23           -4.14             -13.73
2026-08-12 buch_livermore            -2.14           -0.65              27.44

Gesamt ausserhalb der Trainingsdaten: -7.43 %
```

