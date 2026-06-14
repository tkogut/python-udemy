# [SEQ-PRO] Plan 01: Kompleksowy Kurs Programowania i Analityki Danych w Pythonie v3.0

## 1. STRATEGIA & CEL
Przygotowanie kompletnego, zautomatyzowanego środowiska szkoleniowego CLI dla analityków gospodarczych, pozwalającego opanować język Python, biblioteki Pandas/NumPy, pracę z relacyjnymi bazami danych SQL, analizę statystyczną i szeregi czasowe, a także automatyzację zadań (Swarm/Agents-OS).

## 2. TOPOLOGIA I STRUKTURA MODUŁÓW

### Moduł 1: Podstawy Pythona w Ekonomii
- **Zadanie 1.1: Hello World & Zmienne** – podstawowe typy danych (`int`, `float`, `str`), instrukcja `return` i zmienne.
- **Zadanie 1.2: Model PKB / Operacje Arytmetyczne** – obliczanie tożsamości PKB (C + I + G + X - M) z nawiasowaniem.
- **Zadanie 1.3: Kalkulator NPV / Listy i Pętle** – pętla `for` z `enumerate()`, listy i potęgowanie do dyskontowania przepływów.

### Moduł 2: Kontrola Przepływu, Słowniki & Serializacja JSON
- **Zadanie 2.1: Klasyfikacja Dochodu (Instrukcje Warunkowe)** – klasyfikacja podatkowa/dochodowa przy użyciu `if-elif-else`.
- **Zadanie 2.2: Kartoteka Klientów (Słowniki)** – operacje dodawania, modyfikacji i odczytu par klucz-wartość w strukturze `dict`.
- **Zadanie 2.3: Serializacja i Zapis do JSON** – odczyt i zapis słowników do formatu JSON.

### Moduł 3: Wprowadzenie do Pandas & NumPy
- **Zadanie 3.1: Tworzenie DataFrame i stóp zwrotu** – budowanie DataFrame z serii cenowych i obliczanie stóp prostych oraz logarytmicznych.
- **Zadanie 3.2: Fuzja danych makro- i mikroekonomicznych (Merge)** – łączenie baz danych za pomocą `pd.merge` z kluczem złączenia.
- **Zadanie 3.3: Agregacja i grupowanie portfela** – agregacja portfela inwestycyjnego z wykorzystaniem `.groupby()` i `.agg()`.

### Moduł 4: Zaawansowane Czyszczenie Danych (Data Wrangling)
- **Zadanie 4.1: Czyszczenie wskaźników z pliku CSV** – wczytywanie plików, usuwanie znaków walut, czyszczenie spacji i konwersja typów.
- **Zadanie 4.2: Grupowa imputacja braków danych (NaN)** – zaawansowane uzupełnianie braków w grupach metodą `.transform()` z lambdą.
- **Zadanie 4.3: Statystyczna detekcja anomalii (Z-Score)** – filtrowanie i identyfikacja odchyleń od średniej (Z-Score).

### Moduł 5: Szeregi Czasowe (Time Series) w Finansach
- **Zadanie 5.1: Datetime Index & Filtrowanie Czasowe** – parsowanie dat (`pd.to_datetime`), ustawianie indeksu czasowego i filtrowanie przedziałów.
- **Zadanie 5.2: Przesunięcia (Shifts) i Średnie Kroczące (Rolling)** – obliczanie stóp zwrotu za pomocą przesunięć oraz wygładzanie wykresów średnią kroczącą.
- **Zadanie 5.3: Resampling danych finansowych** – agregacja częstotliwości czasowych (np. zmiana interwału z dziennego na miesięczny/roczny).

### Moduł 6: Praca z Relacyjnymi Bazami Danych (SQL & SQLite)
- **Zadanie 6.1: Odczyt danych z SQLite do Pandas** – łączenie z bazą `sqlite3` i odczyt zapytań SQL bezpośrednio do DataFrame za pomocą `pd.read_sql_query`.
- **Zadanie 6.2: Zapis i aktualizacja tabel SQL** – eksportowanie danych z Pandas z powrotem do bazy za pomocą `df.to_sql`.
- **Zadanie 6.3: Agregacja i filtry SQL (Zadania biznesowe)** – wykonywanie transakcji i zapytań agregujących bezpośrednio w bazie SQLite.

### Moduł 7: Analiza Statystyczna & Ekonometria (Statsmodels/Scipy)
- **Zadanie 7.1: Statystyki Opisowe & Korelacja** – obliczanie macierzy korelacji Pearsona i podstawowych miar statystycznych.
- **Zadanie 7.2: Regresja Liniowa OLS** – dopasowanie modelu regresji liniowej za pomocą `statsmodels` (zależność popytu od ceny, interpretacja R2 i p-value).
- **Zadanie 7.3: Testowanie Hipotez (T-Test)** – porównanie średnich z dwóch prób (np. stóp zwrotu przed i po zmianie stóp procentowych) za pomocą testu t-Studenta.

### Moduł 8: Automatyzacja & Integracja AI (Swarm)
- **Zadanie 8.1: Harmonogram Zadań (Scheduler)** – implementacja cyklicznego pobierania i analizowania danych.
- **Zadanie 8.2: Routing i delegacja zapytań do subagentów** – podział zadań w architekturze wieloagentowej.
- **Zadanie 8.3: Automatyczny Report Builder** – generowanie zsyntetyzowanych raportów analitycznych do plików tekstowych na podstawie wyczyszczonych danych.

## 4. HARMONOGRAM WDROŻENIA ŚRODOWISKA
1. **Plan & Backlog**: Aktualizacja topologii w planie oraz centralnym `task.md`.
2. **Implementacja Bazy Lekcji**: Uzupełnienie `course_content.py` o teorię, zadania, wskazówki i szablony dla wszystkich 24 lekcji.
3. **Zestaw Testów (pytest)**: Napisanie 24 plików testowych w `.agents/tests/` do automatycznej walidacji kodu.
4. **Weryfikacja CLI**: Testy poprawności działania interaktywnego asystenta `start_course.py`.
