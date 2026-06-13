# [SEQ-PRO] Plan 01: Kurs Analityki Danych dla Ekonomistów

## 1. STRATEGIA & CEL
Przygotowanie interaktywnego CLI do nauki Pythona i Pandas pod kątem analizy danych ekonomicznych i finansowych dla studenta Analityki Gospodarczej.

## 2. MODUŁY KURSU
### Moduł 1: Składnia Python w Modelach Ekonomicznych
- **Temat**: Zmienne, listy, pętle i warunki w kontekście modeli finansowych.
- **Teoria**: Podstawowe typy, list comprehensions, wyliczanie odsetek (prosty i składany).
- **Zadanie**: Implementacja kalkulatora wartości przyszłej (FV) i obecnej (PV) dla strumienia płatności.

### Moduł 2: Wprowadzenie do Pandas & NumPy (DataFrame & Series)
- **Temat**: Tworzenie i indeksowanie struktur DataFrame i Series.
- **Teoria**: NumPy arrays, wektoryzacja, indeksowanie `.loc` i `.iloc`.
- **Zadanie**: Budowa DataFrame z wskaźnikami giełdowymi i wyliczanie stóp zwrotu.

### Moduł 3: Pozyskiwanie & Czyszczenie Danych (Data Wrangling)
- **Temat**: Import danych i obsługa brakujących wartości (NaN), anomalie.
- **Teoria**: `pd.read_csv`, `pd.read_excel`, czyszczenie braków (`fillna`, `dropna`), zmiana typów (`astype`).
- **Zadanie**: Oczyszczenie rzeczywistego zestawu danych makroekonomicznych z brakami i błędnymi formatami.

### Moduł 4: Transformacja & Agregacja Danych
- **Temat**: Grupowanie, tabele przestawne (pivot) i łączenie tabel.
- **Teoria**: `groupby`, `pivot_table`, `merge`, `join`.
- **Zadanie**: Połączenie danych o PKB i bezrobociu krajów OECD, a następnie agregacja roczna.

### Moduł 5: Raportowanie, Analiza Statystyczna & Wskaźniki Biznesowe
- **Temat**: Wyliczanie ROI, CAGR, elastyczności popytu oraz szeregi czasowe.
- **Teoria**: `describe()`, korelacje (`corr()`), datetime index, resampling.
- **Zadanie**: Analiza szeregów czasowych indeksu giełdowego, CAGR i elastyczności cenowej popytu.

## 3. HARMONOGRAM WDROŻENIA ŚRODOWISKA
1. **Plan & Backlog**: Utworzenie `task.md` i planu szkolenia.
2. **Architektura CLI**: `start_course.py` do nawigacji po lekcjach i zadaniach.
3. **Stan Kursu**: Obsługa stanu w `.agents/course_state.json`.
4. **Zadania & Testy**: Implementacja szablonów zadań i testów jednostkowych (pytest) dla modułów 1-3.
5. **Instrukcje Uruchomienia**: README.md z instrukcjami gh/git oraz integracji z Agents-OS.
