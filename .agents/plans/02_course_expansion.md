# [SEQ-PRO] Plan 02: Wdrożenie Rozszerzenia Kursu v4.0 (Moduły 9-12)

## 1. CEL & SCOPE
Wdrożenie nowej wiedzy z [Konspekt Wiedzy.md](file:///home/tkogut/projects/python-udemy/raw_notes/Konspekt%20Wiedzy.md) w postaci 12 nowych lekcji (Moduły 9-12) w pliku `course_content.py`, przygotowanie szablonów zadań w `exercises/` oraz napisanie pełnych testów pytest w `.agents/tests/`.

---

## 2. KROKI REALIZACJI

### Krok 2.1: Aktualizacja Zależności
- Dopisanie nowych pakietów do `requirements.txt`:
  - `polars`
  - `linearmodels`
  - `arch`
  - `dowhy`
  - `numba`
  - `duckdb`
  - `requests` (dla API NBP)

### Krok 2.2: Uzupełnienie `course_content.py`
- Dodanie definicji dla lekcji 25-36 (Moduły 9-12).
- Każda lekcja musi zawierać:
  - `tytul` (np. "Lekcja 9.1: Integracja z API NBP (NBPy)")
  - `teoria` (opis pojęć, NBPClient, FRED, Polars, linearmodels, arch, DoWhy, Make)
  - `zadanie` (dokładny opis wymagań wejściowych i wyjściowych)
  - `wskazowka` (podpowiedź składniowa)
  - `szablon` (początkowy kod Pythona do uzupełnienia)
  - `rozwiazanie` (wzorcowy kod do wewnętrznej walidacji)

### Krok 2.3: Utworzenie Plików Szablonów Zadań (`exercises/`)
- Stworzenie struktury katalogów:
  - `exercises/module_9/` (task_1.py, task_2.py, task_3.py)
  - `exercises/module_10/` (task_1.py, task_2.py, task_3.py)
  - `exercises/module_11/` (task_1.py, task_2.py, task_3.py)
  - `exercises/module_12/` (task_1.py, task_2.py, task_3.py)
- Zapisanie w każdym z nich odpowiedniego kodu startowego (szablonu).

### Krok 2.4: Wdrożenie Testów Automatycznych (`.agents/tests/`)
- Napisanie testów pytest dla nowych modułów:
  - `.agents/tests/test_module_9.py`
  - `.agents/tests/test_module_10.py`
  - `.agents/tests/test_module_11.py`
  - `.agents/tests/test_module_12.py`
- Testy będą importować funkcje z `exercises/module_*/task_*.py` i sprawdzać ich poprawność.

---

## 3. AUDYT & WERYFIKACJA [Auditor Handshake]
- Uruchomienie `pytest` na wszystkich testach (starych i nowych).
- Uruchomienie `start_course.py` i sprawdzenie czy CLI poprawnie indeksuje nowe moduły.
- Potwierdzenie spójności matematycznej i programistycznej.
