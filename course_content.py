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
        "title": "Moduł 2: Kontrola Przepływu, Słowniki & Serializacja JSON",
        "tasks": {
            1: {
                "title": "Klasyfikacja poziomu dochodów (If-Elif-Else)",
                "lesson": """
Witaj w Module 2!
W pracy analityka często musisz grupować dane na podstawie progów wartościowych.
Twoim zadaniem jest napisanie funkcji `classify_income(income)`, która zwróci klasyfikację tekstową:
- Dla dochodu poniżej 30000 -> "Niski"
- Dla dochodu od 30000 do 85000 (wyłącznie) -> "Średni"
- Dla dochodu 85000 i powyżej -> "Wysoki"

Kod uzupełnij w exercises/module_2/task_1.py.
""",
                "theory": """
=== Instrukcje warunkowe (if-elif-else) ===

Instrukcje warunkowe sterują przepływem programu na podstawie testów logicznych:
```python
if income < 30000:
    return "Niski"
elif income < 85000:
    return "Średni"
else:
    return "Wysoki"
```
""",
                "hint": """
Użyj standardowych operatorów porównania: `<` oraz `>=`. Warunek `elif` sprawdzany jest tylko wtedy, gdy poprzedni `if` był fałszywy.
""",
                "template": """# -*- coding: utf-8 -*-

def classify_income(income: float) -> str:
    \"\"\"
    Klasyfikuje dochód do jednej z trzech kategorii: "Niski", "Średni", "Wysoki".
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_2/task_1.py",
                "test_path": ".agents/tests/test_module_2_1.py"
            },
            2: {
                "title": "Zarządzanie kartoteką klientów (Słowniki)",
                "lesson": """
Witaj w zadaniu 2.2!
Słowniki (`dict`) w Pythonie przechowują pary klucz-wartość. To fundamentalna struktura przy indeksowaniu danych obiektów biznesowych.
Napisz funkcję `manage_clients(clients, client_id, action, name=None)`, która:
- Dla `action` równego "add": dodaje do słownika `clients` klucz `client_id` z wartością `name` i zwraca słownik.
- Dla `action` równego "remove": usuwa klucz `client_id` ze słownika i zwraca go (usuwaj bezpiecznie za pomocą `.pop()`).

Kod uzupełnij w exercises/module_2/task_2.py.
""",
                "theory": """
=== Praca ze słownikami (dict) ===

Słownik to zestaw unikalnych kluczy przypisanych do wartości:
- Dodanie/modyfikacja elementu: `slownik[klucz] = wartosc`
- Bezpieczne usuwanie klucza: `slownik.pop(klucz, domyslna_wartosc)`
""",
                "hint": """
Wskazówki implementacyjne:
```python
if action == "add":
    clients[client_id] = name
elif action == "remove":
    clients.pop(client_id, None)
return clients
```
""",
                "template": """# -*- coding: utf-8 -*-

def manage_clients(clients: dict, client_id: int, action: str, name: str = None) -> dict:
    \"\"\"
    Dodaje lub usuwa klienta ze słownika na podstawie podanej akcji.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_2/task_2.py",
                "test_path": ".agents/tests/test_module_2_2.py"
            },
            3: {
                "title": "Serializacja i Zapis do JSON",
                "lesson": """
Witaj w zadaniu 2.3!
JSON to standardowy format wymiany danych biznesowych w Internecie i API.
Napisz funkcję `serialize_and_save(data, filepath)`, która serializuje słownik `data` do formatu JSON i zapisuje go w pliku o ścieżce `filepath`.

Kod uzupełnij w exercises/module_2/task_3.py.
""",
                "theory": """
=== Praca z modułem json ===

Python posiada wbudowany moduł `json`:
- `json.dumps(obj)` – zamienia obiekt na ciąg znaków w formacie JSON.
- `json.dump(obj, file)` – zapisuje obiekt bezpośrednio do pliku.

Przykład zapisu do pliku:
```python
with open(filepath, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
```
""",
                "hint": """
Zaimportuj `json`. Użyj konstrukcji `with open(filepath, 'w')` do otwarcia pliku w trybie zapisu, a następnie wywołaj `json.dump(data, f)`.
""",
                "template": """# -*- coding: utf-8 -*-
import json

def serialize_and_save(data: dict, filepath: str) -> None:
    \"\"\"
    Zapisuje słownik do pliku w formacie JSON.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_2/task_3.py",
                "test_path": ".agents/tests/test_module_2_3.py"
            }
        }
    },
    3: {
        "title": "Moduł 3: Wprowadzenie do Pandas & NumPy",
        "tasks": {
            1: {
                "title": "Analiza stóp zwrotu akcji (DataFrame & Series)",
                "lesson": """
Witaj w Module 3! Pandas i NumPy to podstawowe narzędzia analityka danych.
Twoim zadaniem jest uzupełnienie funkcji analyze_stock_returns(prices_list) w exercises/module_3/task_1.py.
Funkcja powinna przyjąć listę cen zamknięcia akcji, utworzyć DataFrame, obliczyć stopy zwrotu oraz podstawowe statystyki (średnią i odchylenie standardowe prostych stóp zwrotu).
""",
                "theory": """
=== Podstawy Pandas & NumPy dla Analizy Finansowej ===

1. Tworzenie DataFrame:
   `df = pd.DataFrame({'price': prices})`
2. Metoda .pct_change():
   Oblicza procentową zmianę wartości: `df['price'].pct_change()`
3. Logarytmowanie:
   `np.log(df['price'] / df['price'].shift(1))`
4. Statystyki: `.mean()` oraz `.std()`
""",
                "hint": """
Utwórz DataFrame ze słownika, wylicz pct_change() i log(), a na koniec stopy średnie i odchylenie standardowe.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def analyze_stock_returns(prices: list) -> tuple:
    \"\"\"
    Tworzy DataFrame z cenami akcji i oblicza stopy zwrotu.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_3/task_1.py",
                "test_path": ".agents/tests/test_module_3_1.py"
            },
            2: {
                "title": "Fuzja danych makro- i mikroekonomicznych (Merge/Join)",
                "lesson": """
Witaj w zadaniu 3.2!
Połącz dwa DataFrame'y po kolumnie 'data' z użyciem złączenia typu 'left' (zachowaj wszystkie wiersze z micro_df).

Uzupełnij kod w exercises/module_3/task_2.py.
""",
                "theory": """
=== Łączenie tabel w Pandas (pd.merge) ===

Złączenie lewostronne:
`df_merged = pd.merge(df_lewy, df_prawy, on='klucz', how='left')`
""",
                "hint": """
Użyj funkcji `pd.merge` z parametrami `on='data'` oraz `how='left'`.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def merge_macro_micro(micro_df: pd.DataFrame, macro_df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"
    Łączy micro_df z macro_df po kolumnie 'data' za pomocą left join.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_3/task_2.py",
                "test_path": ".agents/tests/test_module_3_2.py"
            },
            3: {
                "title": "Agregacja i grupowanie portfela inwestycyjnego",
                "lesson": """
Witaj w zadaniu 3.3!
Pogrupuj dane portfela inwestycyjnego po kolumnie 'sektor' i oblicz całkowitą wartość ('wartosc') jako sumę oraz średnią stopę zwrotu ('stopa_zwrotu') w każdym sektorze.

Uzupełnij kod w exercises/module_3/task_3.py.
""",
                "theory": """
=== Grupowanie danych i agregacja ===

Grupowanie i agregacja w Pandas:
`df.groupby('kolumna').agg({'kolumna_A': 'sum', 'kolumna_B': 'mean'})`
""",
                "hint": """
Zastosuj `.groupby('sektor').agg({'wartosc': 'sum', 'stopa_zwrotu': 'mean'})` na obiekcie DataFrame.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def aggregate_portfolio(portfolio_df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"
    Grupuje portfolio_df po 'sektor' i oblicza sumę 'wartosc' oraz średnią 'stopa_zwrotu'.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_3/task_3.py",
                "test_path": ".agents/tests/test_module_3_3.py"
            }
        }
    },
    4: {
        "title": "Moduł 4: Zaawansowane Czyszczenie Danych (Data Wrangling)",
        "tasks": {
            1: {
                "title": "Czyszczenie wskaźników makroekonomicznych",
                "lesson": """
Witaj w Module 4!
Oczyść ramkę danych z braków (NaN), błędnych formatów tekstowych i anomalii.
Musisz wczytać CSV, wyczyścić kolumnę 'PKB_usd' (usuwając '$' i ','), zamienić -999.0 w inflacji na np.nan, uzupełnić te braki średnią, a na koniec usunąć wiersze, które posiadają braki w 'Kraj' lub 'PKB_usd'.

Kod uzupełnij w exercises/module_4/task_1.py.
""",
                "theory": """
=== Czyszczenie i konwersja danych w Pandas ===

Zastępowanie symboli w napisach: `df['col'].astype(str).str.replace('$', '')`
Rzutowanie na typ numeryczny: `pd.to_numeric(df['col'], errors='coerce')`
Usuwanie pustych wierszy: `df.dropna(subset=['col1', 'col2'])`
""",
                "hint": """
Wyczyść tekst, zmień typ, podmień -999.0, fillna średnią, na koniec dropna.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

def clean_macro_data(file_path: str) -> pd.DataFrame:
    \"\"\"
    Wczytuje i oczyszcza dane makroekonomiczne z pliku CSV.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_4/task_1.py",
                "test_path": ".agents/tests/test_module_4_1.py"
            },
            2: {
                "title": "Zaawansowana imputacja braków danych (NaN)",
                "lesson": """
Witaj w zadaniu 4.2!
Uzupełnij brakujące wartości w kolumnie 'PKB' średnią wartością PKB obliczoną w ramach danej grupy 'kontynent'.

Kod uzupełnij w exercises/module_4/task_2.py.
""",
                "theory": """
=== Grupowa imputacja braków ===

Używamy metody transform:
`df['PKB'] = df.groupby('kontynent')['PKB'].transform(lambda x: x.fillna(x.mean()))`
""",
                "hint": """
Pogrupuj po kontynencie, pobierz PKB, wywołaj transform z wyrażeniem lambda i przypisz z powrotem.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def impute_missing_gdp(df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"
    Uzupełnia braki w kolumnie 'PKB' średnią wartością dla danego kontynentu.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_4/task_2.py",
                "test_path": ".agents/tests/test_module_4_2.py"
            },
            3: {
                "title": "Detekcja anomalii (outliers) za pomocą Z-Score",
                "lesson": """
Witaj w zadaniu 4.3!
Znajdź statystyczne outliers w wybranej kolumnie przy użyciu miary Z-Score. Zwróć podzbiór wierszy, dla których |Z-Score| > threshold.

Kod uzupełnij w exercises/module_4/task_3.py.
""",
                "theory": """
=== Obliczanie Z-Score ===

`z = (df[column] - df[column].mean()) / df[column].std()`
Filtrowanie: `df[z.abs() > threshold]`
""",
                "hint": """
Oblicz średnią i odchylenie standardowe kolumny. Wylicz z-score dla każdego wiersza i przefiltruj ramkę za pomocą metody indeksowania warunkowego.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def detect_outliers_zscore(df: pd.DataFrame, column: str, threshold: float = 3.0) -> pd.DataFrame:
    \"\"\"
    Zwraca wiersze df stanowiące wartości odstające (outliers) w kolumnie column.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_4/task_3.py",
                "test_path": ".agents/tests/test_module_4_3.py"
            }
        }
    },
    5: {
        "title": "Moduł 5: Szeregi Czasowe (Time Series) w Finansach",
        "tasks": {
            1: {
                "title": "Filtrowanie i indeksowanie szeregów czasowych",
                "lesson": """
Witaj w Module 5!
Praca z datami to kluczowa umiejętność każdego analityka rynkowego.
Zaimplementuj funkcję `filter_by_date(df, start_date, end_date)`. Funkcja powinna konwertować indeks lub kolumnę 'data' na typ datetime, ustawiać go jako indeks (jeśli nie jest) i zwracać przefiltrowany zakres dat od `start_date` do `end_date` (włącznie).

Kod uzupełnij w exercises/module_5/task_1.py.
""",
                "theory": """
=== Praca z datami w Pandas ===

Konwersja na typ datetime: `df['data'] = pd.to_datetime(df['data'])`
Ustawienie indeksu: `df = df.set_index('data')`
Filtrowanie zakresu: `df.loc[start_date:end_date]`
""",
                "hint": """
Użyj `pd.to_datetime()`, potem `set_index('data')` i wreszcie przefiltruj przy użyciu `.loc[start_date:end_date]`.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def filter_by_date(df: pd.DataFrame, start_date: str, end_date: str) -> pd.DataFrame:
    \"\"\"
    Konwertuje kolumnę 'data' na datetime, ustawia jako indeks i filtruje przedział.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_5/task_1.py",
                "test_path": ".agents/tests/test_module_5_1.py"
            },
            2: {
                "title": "Średnie kroczące w szeregach czasowych",
                "lesson": """
Witaj w zadaniu 5.2!
Średnie kroczące (rolling windows) służą do wygładzania wahań i analizy trendu cen.
Napisz funkcję `calculate_rolling_mean(df, window)`, która zwróci serię (Series) zawierającą średnią kroczącą z kolumny 'price' o oknie wielkości `window`.

Kod uzupełnij w exercises/module_5/task_2.py.
""",
                "theory": """
=== Metoda .rolling() w Pandas ===

Metoda `.rolling(window=N)` pozwala na agregację w oknach przesuwnych.
Przykład:
`df['price'].rolling(window=5).mean()`
Pierwsze `N-1` wartości będą miały wartość NaN.
""",
                "hint": """
Pobierz kolumnę 'price', wywołaj `.rolling(window=window).mean()` i zwróć wynik.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def calculate_rolling_mean(df: pd.DataFrame, window: int) -> pd.Series:
    \"\"\"
    Oblicza średnią kroczącą z kolumny 'price' o rozmiarze okna window.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_5/task_2.py",
                "test_path": ".agents/tests/test_module_5_2.py"
            },
            3: {
                "title": "Resampling danych finansowych (Zmiana częstotliwości)",
                "lesson": """
Witaj w zadaniu 5.3!
Agregacja szeregów czasowych (resampling) pozwala zmienić np. dane dzienne na dane miesięczne lub roczne.
Napisz funkcję `resample_to_monthly(df)`, która przyjmuje DataFrame z DateTimeIndex, oblicza średnie miesięczne z kolumn liczbowych i zwraca DataFrame o częstotliwości miesięcznej (indeksowany na koniec miesiąca).

Kod uzupełnij w exercises/module_5/task_3.py.
""",
                "theory": """
=== Resampling w Pandas ===

Metoda `.resample()` działa podobnie do grupowania, ale po osi czasu:
`df_monthly = df.resample('ME').mean()`
Oznaczenie `'M'` (lub `'ME'`) oznacza agregację miesięczną.
""",
                "hint": """
Użyj metody `.resample('ME').mean()` na wejściowej ramce danych.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def resample_to_monthly(df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"
    Agreguje dzienne dane w DataFrame do średnich miesięcznych.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_5/task_3.py",
                "test_path": ".agents/tests/test_module_5_3.py"
            }
        }
    },
    6: {
        "title": "Moduł 6: Praca z Relacyjnymi Bazami Danych (SQL & SQLite)",
        "tasks": {
            1: {
                "title": "Odczyt danych z SQLite bezpośrednio do Pandas",
                "lesson": """
Witaj w Module 6!
Większość danych firmowych znajduje się w relacyjnych bazach danych (SQL).
Napisz funkcję `read_sql_data(db_path, query)`, która łączy się z bazą danych SQLite w lokalizacji `db_path`, wykonuje zapytanie `query` i zwraca wynik jako Pandas DataFrame. Pamiętaj o zamknięciu połączenia z bazą!

Kod uzupełnij w exercises/module_6/task_1.py.
""",
                "theory": """
=== Odczyt baz danych w Pandas ===

Biblioteka `sqlite3` obsługuje bazy SQLite w Pythonie.
Pandas pozwala odczytać zapytanie bezpośrednio do DataFrame:
```python
import sqlite3
import pandas as pd

conn = sqlite3.connect(db_path)
df = pd.read_sql_query(query, conn)
conn.close()
```
""",
                "hint": """
Zaimportuj `sqlite3` oraz `pandas`. Utwórz połączenie za pomocą `sqlite3.connect()`, odczytaj dane za pomocą `pd.read_sql_query()`, zamknij połączenie i zwróć ramkę.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3

def read_sql_data(db_path: str, query: str) -> pd.DataFrame:
    \"\"\"
    Łączy się z SQLite w db_path, pobiera dane zapytaniem query i zwraca DataFrame.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_6/task_1.py",
                "test_path": ".agents/tests/test_module_6_1.py"
            },
            2: {
                "title": "Eksportowanie danych z Pandas do bazy SQL",
                "lesson": """
Witaj w zadaniu 6.2!
Zapisywanie przetworzonych danych do bazy SQL to standardowy krok w procesach ETL.
Napisz funkcję `write_to_sql(df, db_path, table_name)`. Funkcja powinna zapisać DataFrame do tabeli o nazwie `table_name` w bazie danych SQLite pod ścieżką `db_path`. Jeśli tabela istnieje, ma zostać nadpisana. Nie zapisuj indeksu DataFrame.

Kod uzupełnij w exercises/module_6/task_2.py.
""",
                "theory": """
=== Zapis do SQL w Pandas ===

Do eksportu służy metoda `.to_sql()`:
`df.to_sql(table_name, conn, if_exists='replace', index=False)`
Parametr `if_exists='replace'` nadpisuje tabelę w bazie danych.
""",
                "hint": """
Połącz się z bazą przez `sqlite3.connect()`, wywołaj `df.to_sql(table_name, conn, if_exists='replace', index=False)`, a na koniec zamknij połączenie.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
import sqlite3

def write_to_sql(df: pd.DataFrame, db_path: str, table_name: str) -> None:
    \"\"\"
    Zapisuje DataFrame do tabeli table_name w bazie danych SQLite.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_6/task_2.py",
                "test_path": ".agents/tests/test_module_6_2.py"
            },
            3: {
                "title": "Raport sprzedaży bezpośrednio z bazy danych SQL",
                "lesson": """
Witaj w zadaniu 6.3!
Czasami wydajniej jest agregować dane po stronie silnika SQL zamiast pobierać całą bazę do pamięci Pythona.
Napisz funkcję `get_total_sales_by_product(db_path)`, która łączy się z bazą danych i wykonuje zapytanie SQL sumujące przychody:
`SELECT product, SUM(quantity * price) AS total_sales FROM sales GROUP BY product`
Funkcja ma zwrócić wynik jako listę krotek (wyniki zapytania `cursor.fetchall()`).

Kod uzupełnij w exercises/module_6/task_3.py.
""",
                "theory": """
=== Agregacje i Kursory SQL w Pythonie ===

Bez używania Pandas możemy operować bezpośrednio kursorami `sqlite3`:
```python
conn = sqlite3.connect(db_path)
cursor = conn.cursor()
cursor.execute(query)
results = cursor.fetchall()  # Zwraca listę krotek
conn.close()
```
""",
                "hint": """
Utwórz kursor z połączenia, wykonaj zapytanie SELECT z sumowaniem i grupuj po produkcie, pobierz wyniki za pomocą fetchall(), zamknij bazę i zwróć listę.
""",
                "template": """# -*- coding: utf-8 -*-
import sqlite3

def get_total_sales_by_product(db_path: str) -> list:
    \"\"\"
    Wykonuje zapytanie SQL grupujące i sumujące sprzedaż i zwraca listę krotek.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_6/task_3.py",
                "test_path": ".agents/tests/test_module_6_3.py"
            }
        }
    },
    7: {
        "title": "Moduł 7: Analiza Statystyczna & Ekonometria (Statsmodels/Scipy)",
        "tasks": {
            1: {
                "title": "Obliczanie macierzy korelacji zmiennych",
                "lesson": """
Witaj w Module 7!
Analiza korelacji pozwala sprawdzić, jak silnie powiązane są ze sobą wskaźniki (np. bezrobocie i inflacja).
Napisz funkcję `get_correlations(df)`, która obliczy i zwróci macierz korelacji Pearsona dla wszystkich kolumn liczbowych w DataFrame.

Kod uzupełnij w exercises/module_7/task_1.py.
""",
                "theory": """
=== Korelacja w Pandas ===

Metoda `.corr()` w Pandas automatycznie wylicza współczynniki korelacji liniowej:
`correlation_matrix = df.corr(method='pearson')`
Wartości mieszczą się w przedziale [-1, 1].
""",
                "hint": """
Po prostu wywołaj `df.corr(method='pearson')` i zwróć tę macierz.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def get_correlations(df: pd.DataFrame) -> pd.DataFrame:
    \"\"\"
    Zwraca macierz korelacji Pearsona dla kolumn numerycznych.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_7/task_1.py",
                "test_path": ".agents/tests/test_module_7_1.py"
            },
            2: {
                "title": "Regresja liniowa OLS (Dopasowanie modelu)",
                "lesson": """
Witaj w zadaniu 7.2!
Regresja liniowa (Metoda Najmniejszych Kwadratów - OLS) to podstawowe narzędzie ekonometryczne do badania przyczynowo-skutkowego.
Napisz funkcję `run_regression(df, y_col, x_col)`, która dopasuje model OLS, gdzie `y_col` to zmienna objaśniana (np. 'popyt'), a `x_col` to zmienna objaśniająca (np. 'cena'). Dodaj stałą (wyraz wolny) do zmiennej objaśniającej. Funkcja powinna zwracać krotkę `(rsquared, pvalues)` z dopasowanego modelu.

Kod uzupełnij w exercises/module_7/task_2.py.
""",
                "theory": """
=== Modelowanie OLS w statsmodels ===

Biblioteka `statsmodels` udostępnia zaawansowaną statystykę:
```python
import statsmodels.api as sm

# Musimy dodać stałą (wyraz wolny) do X
X = sm.add_constant(df[x_col])
y = df[y_col]
model = sm.OLS(y, X).fit()

r2 = model.rsquared
p_vals = model.pvalues  # Seria p-value dla stałej i zmiennej X
```
""",
                "hint": """
Użyj `sm.add_constant()` na zmiennej niezależnej, zbuduj model `sm.OLS(y, X)`, wywołaj `.fit()` i zwróć `(model.rsquared, model.pvalues)`.
""",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
import statsmodels.api as sm

def run_regression(df: pd.DataFrame, y_col: str, x_col: str) -> tuple:
    \"\"\"
    Dopasowuje model regresji liniowej OLS i zwraca (R-squared, p-values).
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_7/task_2.py",
                "test_path": ".agents/tests/test_module_7_2.py"
            },
            3: {
                "title": "Test t-Studenta dla dwóch prób niezależnych",
                "lesson": """
Witaj w zadaniu 7.3!
Test t-Studenta służy do weryfikacji hipotezy, czy średnie w dwóch grupach są statystycznie równe (np. czy nowa strategia marketingowa zwiększyła sprzedaż).
Napisz funkcję `run_t_test(sample1, sample2)`, która przeprowadzi dwustronny test t-Studenta dla dwóch prób niezależnych i zwróci statystykę t oraz wartość p (p-value) jako krotkę `(t_stat, p_value)`.

Kod uzupełnij w exercises/module_7/task_3.py.
""",
                "theory": """
=== Testy statystyczne w scipy ===

Moduł `scipy.stats` zawiera implementacje testów:
```python
from scipy import stats

t_stat, p_value = stats.ttest_ind(sample1, sample2)
```
""",
                "hint": """
Użyj funkcji `stats.ttest_ind(sample1, sample2)` i zwróć jej wynik.
""",
                "template": """# -*- coding: utf-8 -*-
from scipy import stats

def run_t_test(sample1: list, sample2: list) -> tuple:
    \"\"\"
    Przeprowadza test t-Studenta dla dwóch prób niezależnych i zwraca (t_stat, p_value).
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_7/task_3.py",
                "test_path": ".agents/tests/test_module_7_3.py"
            }
        }
    },
    8: {
        "title": "Moduł 8: Automatyzacja & Integracja AI (Swarm)",
        "tasks": {
            1: {
                "title": "Cykliczne sprawdzanie i logowanie danych (Scheduler)",
                "lesson": """
Witaj w Module 8!
Zaimplementuj prosty harmonogram zadań w Pythonie.
Funkcja `schedule_data_check(check_func, interval_sec, max_iterations)` powinna cyklicznie wywoływać przekazaną funkcję `check_func` co określony czas (`interval_sec`), maksymalnie `max_iterations` razy, i zwracać listę z wynikami tych uruchomień.

Kod uzupełnij w exercises/module_8/task_1.py.
""",
                "theory": """
=== Harmonogram z time.sleep ===

`time.sleep(seconds)` zawiesza działanie wątku na podany czas.
""",
                "hint": """
W pętli for wywołaj check_func(), dodaj wynik do listy, a jeśli to nie jest ostatnia iteracja – wywołaj `time.sleep(interval_sec)`.
""",
                "template": """# -*- coding: utf-8 -*-
import time

def schedule_data_check(check_func, interval_sec: int, max_iterations: int) -> list:
    \"\"\"
    Cyklicznie wywołuje check_func co interval_sec, max_iterations razy.
    Zwraca listę wyników.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_8/task_1.py",
                "test_path": ".agents/tests/test_module_8_1.py"
            },
            2: {
                "title": "Delegowanie zadań do wyspecjalizowanych subagentów",
                "lesson": """
Witaj w zadaniu 8.2!
Zaimplementuj prosty router żądań w architekturze wieloagentowej. Funkcja `delegate_to_subagent(user_request)` analizuje tekst:
- Jeśli żądanie zawiera słowa 'statystyka' lub 'analiza': zwraca "Delegowano do: Agent Statystyczny".
- Jeśli żądanie zawiera słowa 'wykres' lub 'wizualizacja': zwraca "Delegowano do: Agent Wizualizacji".
- W pozostałych przypadkach: zwraca "Delegowano do: General Agent".

Kod uzupełnij w exercises/module_8/task_2.py.
""",
                "theory": """
=== Rutowanie intencji ===

Używamy `.lower()` oraz dopasowania cząstkowego w tekście (operator `in`).
""",
                "hint": """
Sprawdź obecność "statyst" lub "analiz", a także "wykres" lub "wizualiz".
""",
                "template": """# -*- coding: utf-8 -*-

def delegate_to_subagent(user_request: str) -> str:
    \"\"\"
    Kieruje żądanie user_request do odpowiedniego agenta pomocniczego.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_8/task_2.py",
                "test_path": ".agents/tests/test_module_8_2.py"
            },
            3: {
                "title": "Automatyczny Report Builder",
                "lesson": """
Witaj w zadaniu 8.3!
Ostatnim krokiem analizy jest sformułowanie i zapisanie raportu końcowego do pliku.
Napisz funkcję `build_economic_report(data_summary, filepath)`. Funkcja powinna utworzyć tekstowy raport na podstawie słownika `data_summary` i zapisać go w pliku `filepath`.
Słownik `data_summary` zawiera klucze: 'tytul', 'autor', 'wynik'.
Plik powinien mieć format dokładnie taki:
Raport: <tytul>
Autor: <autor>
Wynik: <wynik>

Kod uzupełnij w exercises/module_8/task_3.py.
""",
                "theory": """
=== Zapis tekstowy i szablony ===

Zapis pliku w Pythonie:
```python
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(report_string)
```
""",
                "hint": """
Sformatuj ciąg znaków pobierając wartości ze słownika:
`report = f"Raport: {data_summary['tytul']}\\nAutor: {data_summary['autor']}\\nWynik: {data_summary['wynik']}"`
Zapisz go do pliku `filepath`.
""",
                "template": """# -*- coding: utf-8 -*-

def build_economic_report(data_summary: dict, filepath: str) -> None:
    \"\"\"
    Tworzy sformatowany raport tekstowy na podstawie data_summary i zapisuje go w pliku.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_8/task_3.py",
                "test_path": ".agents/tests/test_module_8_3.py"
            }
        }
    },
    9: {
        "title": "Moduł 9: Zaawansowane APIs i Jakość Danych w Ekonomii",
        "tasks": {
            1: {
                "title": "Integracja z API NBP (NBPy)",
                "lesson": """
Witaj w zadaniu 9.1!
Twoim zadaniem jest pobranie średniego kursu waluty (tabela A) z oficjalnego API NBP (np. NBPClient) na zadaną datę.
Napisz funkcję `get_nbp_exchange_rate(currency_code, date_str)`.
Powinna ona wysłać zapytanie pod adres:
`http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/{date_str}/?format=json`
i zwrócić kurs średni (`mid`) jako float.
Jeśli wystąpi błąd HTTP (np. brak danych na ten dzień), zwróć `-1.0`.

Kod uzupełnij w exercises/module_9/task_1.py.
""",
                "theory": """
=== API NBP i NBPClient ===
NBP udostępnia API w formacie JSON. Użyj modułu `requests` do pobrania danych:
`response = requests.get(url)`
`data = response.json()`
Kurs znajduje się w `data['rates'][0]['mid']`.
""",
                "hint": "Użyj bloków try-except do obsługi requests.exceptions.RequestException lub sprawdzania status_code.",
                "template": """# -*- coding: utf-8 -*-
import requests

def get_nbp_exchange_rate(currency_code: str, date_str: str) -> float:
    \"\"\"
    Pobiera kurs średni (mid) z tabeli A API NBP dla danej waluty i daty.
    W przypadku błędu (np. 404 brak danych) zwraca -1.0.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_9/task_1.py",
                "test_path": ".agents/tests/test_module_9_1.py"
            },
            2: {
                "title": "Analiza Real-time i Vintages (FRED)",
                "lesson": """
Witaj w zadaniu 9.2!
W analizie ekonomicznej kluczowa jest reprodukowalność – analizowanie danych dokładnie w takiej wersji, w jakiej były one dostępne w wybranym momencie w przeszłości (tzw. Vintages z ALFRED/FRED).
Zaimplementuj funkcję `parse_fred_vintage(vintage_data, target_date)`, która ze słownika rewizji wybierze najbardziej aktualną wartość wskaźnika opublikowaną do dnia `target_date` włącznie.
Słownik `vintage_data` ma postać: `{"obserwacja": {"data_publikacji": wartosc, ...}}`.
Zwróć wartość dla zadanej obserwacji. Jeśli brak publikacji przed tą datą, zwróć `None`.

Kod uzupełnij w exercises/module_9/task_2.py.
""",
                "theory": """
=== Vintages (ALFRED/FRED) ===
Pozwala to uniknąć błędu look-ahead w badaniach historycznych (backtestach).
""",
                "hint": "Filtruj klucze publikacji, które są mniejsze lub równe target_date, i wybierz najnowszą z nich.",
                "template": """# -*- coding: utf-8 -*-

def parse_fred_vintage(vintage_data: dict, observation_date: str, target_date: str) -> float:
    \"\"\"
    Zwraca wartość obserwacji z daty 'observation_date', która była opublikowana
    najpóźniej do dnia 'target_date' włącznie. Jeśli brak danych, zwraca None.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_9/task_2.py",
                "test_path": ".agents/tests/test_module_9_2.py"
            },
            3: {
                "title": "Ewaluacja Jakości Danych (Data Quality Audit)",
                "lesson": """
Witaj w zadaniu 9.3!
Jakość danych (Data Quality) w ekonomii oceniamy na podstawie 5 kryteriów: Accuracy, Completeness, Consistency, Timeliness, Accessibility.
Zaimplementuj funkcję `audit_data_quality(df)` oceniającą DataFrame posiadający kolumny `Data` i `Wartosc`. Zwróć słownik z metrykami:
- `Completeness`: udział niepustych wierszy (float od 0.0 do 1.0).
- `Consistency`: czy wszystkie wartości w kolumnie 'Wartosc' są typu numerycznego (bool).
- `Accuracy`: udział wartości dodatnich w kolumnie 'Wartosc' (float od 0.0 do 1.0).

Kod uzupełnij w exercises/module_9/task_3.py.
""",
                "theory": """
=== Metryki Jakości Danych ===
Wysoka jakość danych to podstawa każdego wnioskowania statystycznego.
""",
                "hint": "Użyj `.notnull().mean()`, `pd.api.types.is_numeric_dtype()`, oraz sumy wartości > 0.",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def audit_data_quality(df: pd.DataFrame) -> dict:
    \"\"\"
    Przeprowadza audyt jakości danych na DataFrame i zwraca słownik z metrykami.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_9/task_3.py",
                "test_path": ".agents/tests/test_module_9_3.py"
            }
        }
    },
    10: {
        "title": "Moduł 10: Nowoczesny Stos Wydajnościowy i Bazy",
        "tasks": {
            1: {
                "title": "Przetwarzanie w bibliotece Polars",
                "lesson": """
Witaj w zadaniu 10.1!
Polars to niezwykle szybki silnik analizy danych napisany w Rust.
Zaimplementuj funkcję `aggregate_with_polars(csv_path)`, która wczyta plik CSV za pomocą Polars, pogrupuje dane według kolumny `Kategoria` i obliczy średnią z kolumny `Wynik`.
Wynik zwróć jako zwykły słownik w Pythonie `{kategoria: srednia}`.

Kod uzupełnij w exercises/module_10/task_1.py.
""",
                "theory": """
=== Polars DataFrame ===
Polars jest często znacznie szybszy od Pandas. Używaj `pl.read_csv`, `.group_by`, `.agg` i `.mean()`.
""",
                "hint": "Użyj `df.group_by('Kategoria').agg(pl.col('Wynik').mean())` i przekształć na słownik za pomocą `.to_dicts()` lub zip.",
                "template": """# -*- coding: utf-8 -*-
import polars as pl

def aggregate_with_polars(csv_path: str) -> dict:
    \"\"\"
    Wczytuje plik CSV za pomocą Polars, grupuje po 'Kategoria' i wylicza średnią z 'Wynik'.
    Zwraca słownik.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_10/task_1.py",
                "test_path": ".agents/tests/test_module_10_1.py"
            },
            2: {
                "title": "Regresja Out-of-Core z DuckDB",
                "lesson": """
Witaj w zadaniu 10.2!
DuckDB pozwala na błyskawiczne zapytania analityczne na dużych plikach bez ładowania ich w całości do pamięci RAM.
Napisz funkcję `duckdb_query_and_regression(db_path)`, która połączy się z bazą DuckDB, pobierze dane z tabeli `ekonomia` i wyliczy parametry regresji liniowej (slope, intercept) dla modelu Y ~ X.
Zwróć krotkę `(slope, intercept)`.

Kod uzupełnij w exercises/module_10/task_2.py.
""",
                "theory": """
=== DuckDB i Out-of-Core ===
DuckDB świetnie sprawdza się w scenariuszach analitycznych na jednym komputerze.
""",
                "hint": "Możesz wyliczyć współczynniki bezpośrednio zapytaniem SQL lub pobrać dane za pomocą `.df()` i użyć NumPy.",
                "template": """# -*- coding: utf-8 -*-
import duckdb

def duckdb_query_and_regression(db_path: str) -> tuple:
    \"\"\"
    Łączy się z bazą DuckDB, pobiera X i Y, i wylicza współczynniki regresji liniowej.
    Zwraca (slope, intercept).
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_10/task_2.py",
                "test_path": ".agents/tests/test_module_10_2.py"
            },
            3: {
                "title": "Kompilacja JIT (Numba)",
                "lesson": """
Witaj w zadaniu 10.3!
Numba pozwala kompilować kod Pythona bezpośrednio do natywnego kodu maszynowego przy użyciu dekoratora `@jit`.
Napisz funkcję `monte_carlo_option_pricing(s0, k, r, sigma, t, simulations)` obliczającą cenę europejskiej opcji call metodą Monte Carlo.
Funkcja musi być udekorowana `@jit(nopython=True)` w celu optymalizacji.

Kod uzupełnij w exercises/module_10/task_3.py.
""",
                "theory": """
=== Kompilacja JIT i Numba ===
Metody Monte Carlo w czystym Pythonie są powolne. Numba pozwala przyspieszyć pętle tysiąckrotnie.
""",
                "hint": "Użyj numpy wewnątrz funkcji skompilowanej przez numba do wygenerowania kroków rozkładu normalnego.",
                "template": """# -*- coding: utf-8 -*-
from numba import jit
import numpy as np

@jit(nopython=True)
def monte_carlo_option_pricing(s0: float, k: float, r: float, sigma: float, t: float, simulations: int) -> float:
    \"\"\"
    Wycenia opcję call metodą Monte Carlo przy użyciu kompilacji JIT.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_10/task_3.py",
                "test_path": ".agents/tests/test_module_10_3.py"
            }
        }
    },
    11: {
        "title": "Moduł 11: Zaawansowana Ekonometria i Szeregi Czasowe",
        "tasks": {
            1: {
                "title": "Regresja Panelowa (linearmodels)",
                "lesson": """
Witaj w zadaniu 11.1!
Dane panelowe (wielowymiarowe) są powszechne w ekonomii.
Zaimplementuj funkcję `estimate_panel_ols(df)`, która przyjmie DataFrame z indeksem typu MultiIndex (entity, time) i dopasuje model PanelOLS z efektami stałymi dla obiektów (Entity Effects).
Zwróć współczynnik kierunkowy (parametr) dla zmiennej 'X'.

Kod uzupełnij w exercises/module_11/task_1.py.
""",
                "theory": """
=== Modele Panelowe ===
Biblioteka `linearmodels` rozszerza `statsmodels` o regresje panelowe.
Użyj: `PanelOLS(y, x, entity_effects=True).fit()`
""",
                "hint": "Dodaj stałą do zmiennej objaśniającej używając statsmodels.api.add_constant.",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
from linearmodels.panel import PanelOLS
from statsmodels.api import add_constant

def estimate_panel_ols(df: pd.DataFrame) -> float:
    \"\"\"
    Estymuje model regresji panelowej PanelOLS z efektami stałymi dla obiektów.
    Zwraca współczynnik przy zmiennej 'X'.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_11/task_1.py",
                "test_path": ".agents/tests/test_module_11_1.py"
            },
            2: {
                "title": "Modelowanie Zmienności GARCH (arch)",
                "lesson": """
Witaj w zadaniu 11.2!
Model GARCH służy do modelowania zmienności warunkowej szeregów finansowych.
Napisz funkcję `fit_garch_model(returns)`, która dopasuje model GARCH(1,1) do podanej listy stóp zwrotu.
Zwróć parametry modelu: omega, alpha[1] i beta[1] jako krotkę `(omega, alpha, beta)`.

Kod uzupełnij w exercises/module_11/task_2.py.
""",
                "theory": """
=== Model GARCH ===
Użyj pakietu `arch`:
`am = arch_model(returns, vol='Garch', p=1, q=1)`
`res = am.fit(disp='off')`
""",
                "hint": "Parametry odczytasz z `res.params['omega']`, `res.params['alpha[1]']` oraz `res.params['beta[1]']`.",
                "template": """# -*- coding: utf-8 -*-
from arch import arch_model

def fit_garch_model(returns: list) -> tuple:
    \"\"\"
    Dopasowuje model GARCH(1,1) do stóp zwrotu i zwraca (omega, alpha, beta).
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_11/task_2.py",
                "test_path": ".agents/tests/test_module_11_2.py"
            },
            3: {
                "title": "Filtry i Dekompozycja Szeregów Czasowych",
                "lesson": """
Witaj w zadaniu 11.3!
Filtr Hodricka-Prescotta (HP) jest standardowym narzędziem do dekompozycji szeregu czasowego na trend i cykl koniunkturalny.
Napisz funkcję `decompose_macro_series(series, lamb)`, która podzieli szereg za pomocą filtra HP.
Zwróć krotkę `(trend, cycle)` jako listy.

Kod uzupełnij w exercises/module_11/task_3.py.
""",
                "theory": """
=== Filtr HP ===
Statsmodels udostępnia filtr HP w module `statsmodels.tsa.filters.hp_filter.hpfilter`.
""",
                "hint": "Zwracane wartości z hpfilter to cykl i trend. Zwróć je przekonwertowane na listy.",
                "template": """# -*- coding: utf-8 -*-
from statsmodels.tsa.filters.hp_filter import hpfilter

def decompose_macro_series(series: list, lamb: float) -> tuple:
    \"\"\"
    Dekonponuje szereg czasowy na trend i cykl za pomocą filtra HP.
    Zwraca (trend, cycle) jako listy.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_11/task_3.py",
                "test_path": ".agents/tests/test_module_11_3.py"
            }
        }
    },
    12: {
        "title": "Moduł 12: Text as Data, Przyczynowość i Reprodukowalność",
        "tasks": {
            1: {
                "title": "Analiza Sentymentu Raportów Finansowych",
                "lesson": """
Witaj w zadaniu 12.1!
W nowoczesnej ekonomii tekst jest traktowany jako źródło danych.
Zaimplementuj funkcję `calculate_sentiment_score(text, positive_words, negative_words)` tokenizującą tekst po spacjach, usuwającą znaki interpunkcyjne i wyliczającą indeks sentymentu:
`(pos_count - neg_count) / (pos_count + neg_count + 1e-6)`.

Kod uzupełnij w exercises/module_12/task_1.py.
""",
                "theory": """
=== Sentyment w Ekonomii ===
Używa się słowników specyficznych dla finansów w celu określenia tonu komunikatów.
""",
                "hint": "Sprowadź słowa do małych liter i usuń znaki interpunkcyjne za pomocą `.strip('.,?!;')`.",
                "template": """# -*- coding: utf-8 -*-

def calculate_sentiment_score(text: str, positive_words: list, negative_words: list) -> float:
    \"\"\"
    Wylicza wskaźnik sentymentu dla podanego tekstu na podstawie list słów.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_12/task_1.py",
                "test_path": ".agents/tests/test_module_12_1.py"
            },
            2: {
                "title": "Wnioskowanie Przyczynowe",
                "lesson": """
Witaj w zadaniu 12.2!
Ekonomia opiera się na wnioskowaniu przyczynowym.
Napisz funkcję `estimate_causal_effect(df)`, która przy użyciu biblioteki `dowhy` oszacuje wpływ zmiennej binarnej `T` na zmienną `Y` z uwzględnieniem zmiennej zakłócającej `W`.
Zwróć oszacowany średni efekt traktowania (ATE).

Kod uzupełnij w exercises/module_12/task_2.py.
""",
                "theory": """
=== DoWhy i Modele Przyczynowe ===
DoWhy dzieli wnioskowanie na 4 kroki: Model, Identify, Estimate, Refute.
""",
                "hint": "Zbuduj model przyczynowy podając graph='digraph { W -> T; W -> Y; T -> Y; }'. Użyj metody regresji liniowej do estymacji.",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd
import dowhy
from dowhy import CausalModel

def estimate_causal_effect(df: pd.DataFrame) -> float:
    \"\"\"
    Szacuje ATE (Average Treatment Effect) za pomocą DoWhy.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_12/task_2.py",
                "test_path": ".agents/tests/test_module_12_2.py"
            },
            3: {
                "title": "Automatyzacja Potoku Badawczego (DAG)",
                "lesson": """
Witaj w zadaniu 12.3!
Reprodukowalne potoki analityczne modelowane są jako Directed Acyclic Graph (DAG).
Zaimplementuj funkcję `run_research_pipeline(raw_data_path, clean_data_path)`, która odczyta surowe dane z `raw_data_path`, usunie wiersze z ujemną wartością w kolumnie `Wartosc`, zapisze wyczyszczony plik CSV do `clean_data_path` i zwróci `True`.

Kod uzupełnij w exercises/module_12/task_3.py.
""",
                "theory": """
=== DAG i Potoki Danych ===
Dobre zaprojektowanie potoku danych gwarantuje, że wyniki analizy można odtworzyć jedną komendą.
""",
                "hint": "Użyj pandas do odczytu, filtracji i zapisu do CSV.",
                "template": """# -*- coding: utf-8 -*-
import pandas as pd

def run_research_pipeline(raw_data_path: str, clean_data_path: str) -> bool:
    \"\"\"
    Wczytuje, czyści i zapisuje dane, symulując krok potoku DAG.
    Zwraca True przy sukcesie.
    \"\"\"
    # TWÓJ KOD TUTAJ
    pass
""",
                "exercise_path": "exercises/module_12/task_3.py",
                "test_path": ".agents/tests/test_module_12_3.py"
            }
        }
    }
}

