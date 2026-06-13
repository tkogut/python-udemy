# -*- coding: utf-8 -*-

COURSE_DATA = {
    1: {
        "title": "Moduł 1: Składnia Python w Modelach Ekonomicznych",
        "tasks": {
            1: {
                "title": "Kalkulator NPV i Wartości Pieniądza w Czasie",
                "lesson": """
Witaj w Module 1! W ekonomii kluczowym pojęciem jest wartość pieniądza w czasie (Time Value of Money - TVM).
Wzory:
1. Future Value (FV): FV = PV * (1 + r)^n
2. Present Value (PV): PV = FV / (1 + r)^n
3. Net Present Value (NPV): NPV = suma_{t=0}^{N} (CF_t / (1 + r)^t)
   gdzie CF_0 to zazwyczaj nakład początkowy (wartość ujemna).

Twoim zadaniem jest zaimplementowanie tych trzech funkcji w pliku exercises/module_1/task_1.py.
""",
                "template": """# -*- coding: utf-8 -*-

def calculate_fv(pv: float, r: float, n: int) -> float:
    \"\"\"
    Oblicza Future Value (Wartość Przyszłą).
    pv - Present Value (Wartość Obecna)
    r  - roczna stopa procentowa (np. 0.05 dla 5%)
    n  - liczba okresów (lat)
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass

def calculate_pv(fv: float, r: float, n: int) -> float:
    \"\"\"
    Oblicza Present Value (Wartość Obecną).
    fv - Future Value (Wartość Przyszła)
    r  - roczna stopa procentowa (np. 0.05 dla 5%)
    n  - liczba okresów (lat)
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass

def calculate_npv(cash_flows: list, r: float) -> float:
    \"\"\"
    Oblicza Net Present Value (Wartość Bieżącą Netto).
    cash_flows - lista przepływów pieniężnych (indeks 0 to nakład początkowy, np. -1000)
    r          - stopa dyskontowa (np. 0.08 dla 8%)
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_1/task_1.py",
                "test_path": ".agents/tests/test_module_1.py"
            }
        }
    },
    2: {
        "title": "Moduł 2: Wprowadzenie do Pandas & NumPy",
        "tasks": {
            1: {
                "title": "Analiza stóp zwrotu akcji (DataFrame & Series)",
                "lesson": """
Witaj w Module 2! Pandas i NumPy to fundamenty analizy danych w Pythonie.
DataFrame reprezentuje tabelę danych, a Series to pojedyncza kolumna.
W analizie rynków finansowych kluczowe są stopy zwrotu (returns):
1. Prosta stopa zwrotu: R_t = (P_t - P_{t-1}) / P_{t-1} (w Pandas: .pct_change())
2. Logarytmiczna stopa zwrotu: r_t = ln(P_t / P_{t-1}) (w NumPy: np.log(P_t / P_{t-1}))

Twoim zadaniem jest uzupełnienie funkcji analyze_stock_returns(prices_list) w exercises/module_2/task_1.py.
Funkcja powinna przyjąć listę cen zamknięcia akcji, utworzyć DataFrame, obliczyć stopy zwrotu oraz podstawowe statystyki (średnią i odchylenie standardowe prostych stóp zwrotu).
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def analyze_stock_returns(prices: list) -> tuple:
    \"\"\"
    Tworzy DataFrame z cenami akcji i oblicza stopy zwrotu.
    Wejście: prices - lista cen akcji (kolejne dni)
    Wyjście: tuple (df, mean_return, volatility)
       - df: DataFrame z kolumnami: 'price', 'simple_return', 'log_return'
       - mean_return: średnia prosta stopa zwrotu (ignorując wartość NaN na początku)
       - volatility: odchylenie standardowe prostej stopy zwrotu (ignorując wartość NaN)
    
    Uwaga: Pierwszy wiersz stóp zwrotu będzie NaN (brak ceny z dnia poprzedniego).
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_2/task_1.py",
                "test_path": ".agents/tests/test_module_2.py"
            }
        }
    },
    3: {
        "title": "Moduł 3: Pozyskiwanie & Czyszczenie Danych (Data Wrangling)",
        "tasks": {
            1: {
                "title": "Czyszczenie wskaźników makroekonomicznych",
                "lesson": """
Witaj w Module 3! Rzeczywiste dane rzadko są idealne. Często zawierają braki (NaN), niepoprawne formaty typów danych (np. liczby zapisane jako tekst) oraz błędy grubego błędu (anomalie rynkowe).
W tym zadaniu wyczyścisz tabelę makroekonomiczną.
Musisz:
1. Wczytać plik CSV wskazany w argumencie.
2. Zmienić typ kolumny 'PKB_usd' na float. Usuń znaki '$' oraz przecinki/spacje.
3. Zidentyfikować anomalie w kolumnie 'Inflacja'. Czasami błędne wartości są kodowane jako -999.0. Zastąp je wartością NaN.
4. Uzupełnić brakujące wartości w kolumnie 'Inflacja' średnią wartością z tej kolumny.
5. Usunąć wiersze, które nadal posiadają braki (NaN) w kolumnie 'Kraj' lub 'PKB_usd'.
6. Zwrócić oczyszczony DataFrame.

Kod uzupełnij w exercises/module_3/task_1.py.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def clean_macro_data(file_path: str) -> pd.DataFrame:
    \"\"\"
    Wczytuje i oczyszcza dane makroekonomiczne z pliku CSV.
    1. Wczytaj CSV.
    2. Oczyść kolumnę 'PKB_usd' (usuń '$', ',', spacje i rzutuj na float).
    3. Zastąp wartości inflacji równe -999.0 wartością np.nan.
    4. Uzupełnij braki w kolumnie 'Inflacja' średnią z tej kolumny.
    5. Usuń wiersze z brakującą wartością (NaN) w 'Kraj' lub 'PKB_usd'.
    6. Zwróć oczyszczony DataFrame.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_3/task_1.py",
                "test_path": ".agents/tests/test_module_3.py"
            }
        }
    }
}
