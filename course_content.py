# -*- coding: utf-8 -*-

COURSE_DATA = {
    1: {
        "title": "Moduł 1: Składnia Python w Modelach Ekonomicznych",
        "tasks": {
            1: {
                "title": "Witaj w Pythonie (Hello World & Zmienne)",
                "lesson": """
Witaj w Module 1! Zaczynamy od absolutnych podstaw programowania.
Pierwszym krokiem każdego programisty jest napisanie programu, który wita się ze światem ("Hello, World!").
Dodatkowo poznasz pojęcie zmiennych – to jak szufladki w pamięci komputera, w których przechowujemy dane, np. wartości ekonomiczne.

Twoim zadaniem jest zaimplementowanie dwóch funkcji w pliku exercises/module_1/task_1.py:
1. `hello_world()` - funkcja ma zwracać tekst "Hello, World!".
2. `get_gdp_value()` - funkcja ma tworzyć zmienną `gdp` o wartości 1500.0 (liczba zmiennoprzecinkowa) i ją zwracać.
""",
                "theory": """
=== Podstawy programowania w Pythonie ===

1. Funkcja print() i zwracanie wartości (return):
   Funkcje to wydzielone fragmenty kodu. Słowo kluczowe `return` przekazuje wynik działania funkcji na zewnątrz.
   W Pythonie teksty zapisujemy w cudzysłowach (np. "Hello, World!" lub 'Hello, World!').
   Przykład funkcji zwracającej tekst:
   def przywitanie():
       return "Witaj!"

2. Zmienne (Variables) i Typy Danych:
   Zmienna to nazwa, pod którą przechowujemy dane. Nazwę zmiennej piszemy małymi literami (np. `gdp` lub `inflacja`).
   W Pythonie mamy różne typy danych:
   - int (liczby całkowite, np. `rok = 2026`)
   - float (liczby rzeczywiste/zmiennoprzecinkowe, np. `gdp = 1500.0`)
   - str (tekst, np. `kraj = "Polska"`)

   Aby przypisać wartość do zmiennej, używamy znaku `=`:
   inflacja = 2.5
   return inflacja
""",
                "hint": """
Wskazówki implementacyjne:
- `hello_world()`: Wpisz linijkę `return "Hello, World!"`.
- `get_gdp_value()`:
  1. Stwórz zmienną: `gdp = 1500.0`
  2. Zwróć ją: `return gdp`
""",
                "template": """# -*- coding: utf-8 -*-

def hello_world() -> str:
    \"\"\"
    Zwraca tekst "Hello, World!".
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass

def get_gdp_value() -> float:
    \"\"\"
    Tworzy zmienną gdp o wartości 1500.0 i ją zwraca.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_1/task_1.py",
                "test_path": ".agents/tests/test_module_1.py"
            },
            2: {
                "title": "Podstawowe Operacje Matematyczne (Model PKB)",
                "lesson": """
Wspaniale! Teraz poćwiczymy podstawowe operacje matematyczne.
W ekonomii jednym z podstawowych modeli jest tożsamość PKB (metoda wydatkowa):
PKB = C + I + G + (X - M)
Gdzie:
- C: Konsumpcja (Consumption)
- I: Inwestycje (Investment)
- G: Wydatki rządowe (Government spending)
- X: Eksport (Exports)
- M: Import (Imports)
Różnica (X - M) to eksport netto.

Twoim zadaniem jest uzupełnienie funkcji `calculate_gdp(c, i, g, x, m)` w exercises/module_1/task_2.py, która obliczy i zwróci wartość PKB na podstawie przekazanych parametrów.
""",
                "theory": """
=== Operacje matematyczne w Pythonie ===

Python pozwala wykonywać standardowe działania matematyczne:
- dodawanie: `+`
- odejmowanie: `-`
- mnożenie: `*`
- dzielenie: `/`

Kolejność wykonywania działań jest taka sama jak w matematyce. Możesz używać nawiasów okrągłych `()`, aby kontrolować kolejność operacji:
wynik = a + b + c + (d - e)
""",
                "hint": """
Wskazówki implementacyjne:
Wewnątrz funkcji `calculate_gdp(c, i, g, x, m)` wpisz linijkę:
`return c + i + g + (x - m)`
""",
                "template": """# -*- coding: utf-8 -*-

def calculate_gdp(c: float, i: float, g: float, x: float, m: float) -> float:
    \"\"\"
    Oblicza PKB ze wzoru: C + I + G + (X - M)
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_1/task_2.py",
                "test_path": ".agents/tests/test_module_1_2.py"
            },
            3: {
                "title": "Kalkulator NPV i Wartości Pieniądza w Czasie",
                "lesson": """
Teraz jesteś gotowy na trudniejsze zadanie! Wykorzystamy pętle i listy w modelu wartości pieniądza w czasie.
Wzory:
1. Future Value (FV): FV = PV * (1 + r)^n
2. Present Value (PV): PV = FV / (1 + r)^n
3. Net Present Value (NPV): NPV = suma_{t=0}^{N} (CF_t / (1 + r)^t)
   gdzie CF_0 to nakład początkowy (wartość ujemna).

Twoim zadaniem jest zaimplementowanie tych trzech funkcji w pliku exercises/module_1/task_3.py.
""",
                "theory": """
=== Podstawy składni Pythona dla Modelu NPV ===

1. Pętle (Loops) i Listy (Lists):
   Pętla `for` pozwala powtarzać czynności.
   Funkcja `enumerate(lista)` zwraca pary: (indeks, wartość).
   Przykład:
   for t, cf in enumerate(cash_flows):
       # t to rok (0, 1, 2...), cf to przepływ w tym roku.

2. Potęgowanie:
   W Pythonie potęgowanie zapisujemy jako podwójną gwiazdkę `**`:
   mnożnik = (1 + r) ** n
""",
                "hint": """
Wskazówki implementacyjne:
- `calculate_fv(pv, r, n)`: Zwróć `pv * ((1 + r) ** n)`.
- `calculate_pv(fv, r, n)`: Zwróć `fv / ((1 + r) ** n)`.
- `calculate_npv(cash_flows, r)`: 
  1. Stwórz zmienną sumującą: `npv_sum = 0.0`.
  2. Użyj pętli: `for t, cf in enumerate(cash_flows):`
  3. Dodaj zdyskontowaną wartość do sumy: `npv_sum += cf / ((1 + r) ** t)`.
  4. Zwróć `npv_sum`.
""",
                "template": """# -*- coding: utf-8 -*-

def calculate_fv(pv: float, r: float, n: int) -> float:
    \"\"\"
    Oblicza Future Value (Wartość Przyszłą).
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass

def calculate_pv(fv: float, r: float, n: int) -> float:
    \"\"\"
    Oblicza Present Value (Wartość Obecną).
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass

def calculate_npv(cash_flows: list, r: float) -> float:
    \"\"\"
    Oblicza Net Present Value (Wartość Bieżącą Netto).
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_1/task_3.py",
                "test_path": ".agents/tests/test_module_1_3.py"
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
                "theory": """
=== Podstawy Pandas & NumPy dla Analizy Finansowej ===

1. Co to jest DataFrame?
   Tabela dwuwymiarowa z kolumnami. Tworzenie DataFrame ze słownika:
   df = pd.DataFrame({'nazwa_kolumny': lista_wartosci})

2. Metoda .pct_change():
   Wbudowana funkcja Pandas do obliczania procentowej zmiany wiersz do wiersza:
   df['simple_return'] = df['price'].pct_change()
   Uwaga: Pierwsza wartość stopy zwrotu zawsze będzie równa NaN (brak wcześniejszego punktu odniesienia).

3. Funkcja przesunięcia .shift(1):
   Pozwala pobrać wartość z poprzedniego okresu (wiersza):
   poprzednie_ceny = df['price'].shift(1)

4. Logarytmowanie i NumPy:
   W analizie ilościowej często stosuje się stopy logarytmiczne: log(cena_t / cena_t-1).
   Używamy numpy:
   df['log_return'] = np.log(df['price'] / df['price'].shift(1))

5. Metody statystyczne:
   - Średnia stóp zwrotu: `df['simple_return'].mean()`
   - Odchylenie standardowe (zmienność / zmienność historyczna): `df['simple_return'].std()`
   Funkcje te automatycznie ignorują wartości NaN.
""",
                "hint": """
Wskazówki implementacyjne:
1. Zainicjuj DataFrame z kolumną 'price':
   `df = pd.DataFrame({'price': prices})`
2. Oblicz prostą stopę zwrotu:
   `df['simple_return'] = df['price'].pct_change()`
3. Oblicz logarytmiczna stopę zwrotu za pomocą NumPy:
   `df['log_return'] = np.log(df['price'] / df['price'].shift(1))`
4. Wylicz statystyki:
   `mean_return = df['simple_return'].mean()`
   `volatility = df['simple_return'].std()`
5. Zwróć krotkę: `return df, mean_return, volatility`
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
                "theory": """
=== Podstawy Data Wrangling w Pandas ===

1. Wczytywanie danych:
   `df = pd.read_csv(file_path)`

2. Praca na łańcuchach tekstowych w kolumnach:
   Można używać metod tekstowych za pomocą akcesora `.str`:
   `df['PKB_usd'] = df['PKB_usd'].astype(str).str.replace('$', '').str.replace(',', '').str.strip()`
   Po usunięciu niechcianych znaków konwertujemy na liczby:
   `df['PKB_usd'] = pd.to_numeric(df['PKB_usd'], errors='coerce')`
   `errors='coerce'` sprawi, że błędne wartości (np. puste) staną się wartościami NaN.

3. Zamiana wartości (zastępowanie anomalii):
   `df['Inflacja'] = df['Inflacja'].replace(-999.0, np.nan)`

4. Uzupełnianie braków:
   Obliczamy średnią z kolumny, a następnie używamy `.fillna()`:
   `srednia = df['Inflacja'].mean()`
   `df['Inflacja'] = df['Inflacja'].fillna(srednia)`

5. Usuwanie wierszy z brakami w kluczowych kolumnach:
   `df = df.dropna(subset=['Kraj', 'PKB_usd'])`
""",
                "hint": """
Wskazówki implementacyjne:
1. Wczytaj dane: `df = pd.read_csv(file_path)`
2. Oczyść kolumnę 'PKB_usd' za pomocą metod `.str.replace` dla znaku dolara i przecinka, a następnie wywołaj `pd.to_numeric(..., errors='coerce')`.
3. Zastąp anomalne inflacje -999.0 wartością `np.nan` (użyj `df['Inflacja'].replace(-999.0, np.nan)`).
4. Oblicz średnią i uzupełnij: `mean_inf = df['Inflacja'].mean()` oraz `df['Inflacja'] = df['Inflacja'].fillna(mean_inf)`.
5. Przefiltruj braki za pomocą: `df = df.dropna(subset=['Kraj', 'PKB_usd'])`.
6. Zwróć `df`.
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
