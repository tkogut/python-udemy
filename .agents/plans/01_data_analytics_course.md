# [SEQ-PRO] Plan 01: Kurs Analityki Danych dla Ekonomistów v2.0 (WSL & Swarm Integration)

## 1. STRATEGIA & CEL
Przygotowanie interaktywnego CLI do nauki Pythona i Pandas pod kątem analizy danych ekonomicznych i finansowych dla studenta Analityki Gospodarczej, z pełnym wykorzystaniem środowiska WSL oraz integracją z koncepcjami Swarm & AI Automation.

## 2. MODUŁY KURSU
### Moduł 1: Składnia Python w Modelach Ekonomicznych
- **Zadanie 1.1: Witaj w Pythonie (Hello World & Zmienne)** – nauka zmiennych, instrukcji `return` i typów danych.
- **Zadanie 1.2: Podstawowe Operacje Matematyczne (Model PKB)** – operacje arytmetyczne i nawiasowanie.
- **Zadanie 1.3: Kalkulator NPV i Wartości Pieniądza w Czasie** – pętle, listy, enumerate i potęgowanie.

### Moduł 2: Wprowadzenie do Pandas & NumPy (DataFrame & Series)
- **Zadanie 2.1: Analiza stóp zwrotu akcji** – wektoryzacja rynkowa, stopy procentowe proste oraz logarytmiczne.
- **Zadanie 2.2: Fuzja danych makro- i mikroekonomicznych (Merge/Join)** – łączenie tabel rynkowych metodą `pd.merge`.
- **Zadanie 2.3: Agregacja i grupowanie portfela inwestycyjnego** – grupowanie `groupby` i agregacja `agg` sumarycznych statystyk.

### Moduł 3: Pozyskiwanie & Czyszczenie Danych (Data Wrangling)
- **Zadanie 3.1: Czyszczenie wskaźników makroekonomicznych** – wczytywanie CSV, czyszczenie znaków tekstowych, podstawowa obsługa braków NaN.
- **Zadanie 3.2: Zaawansowana imputacja braków danych (NaN)** – uzupełnianie braków w grupach przy użyciu `.transform()`.
- **Zadanie 3.3: Detekcja anomalii (outliers) za pomocą Z-Score** – statystyczna filtracja anomalii rynkowych.

### Moduł 4: Swarm & AI Automation
- **Zadanie 4.1: Cykliczne sprawdzanie i logowanie danych (Scheduler)** – implementacja harmonogramu zadań z `time.sleep`.
- **Zadanie 4.2: Delegowanie zadań do wyspecjalizowanych subagentów** – implementacja routera zadań do agentów pomocniczych na podstawie słów kluczowych.

## 3. HARMONOGRAM WDROŻENIA ŚRODOWISKA
1. **Plan & Centralny Backlog**: Aktualizacja topologii w planie oraz `task.md`.
2. **Generowanie Zadań**: Przygotowanie szablonów `.py` w katalogu `exercises/` dla wszystkich modułów.
3. **Automatyczne Testy (pytest)**: Implementacja zestawu testów jednostkowych w `.agents/tests/` dla wszystkich zadań.
4. **Rozbudowa CLI**: Uruchomienie interaktywnego przewodnika (`start_course.py`) dla wszystkich 8 zadań.
