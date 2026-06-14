# [SEQ-PRO] Plan 04: Integracja Zadania SciPy (Zadanie 7.4) w Module 7

## 1. CEL
Wdrożenie zadania 4.1 z pliku `Zestawienie Ćwiczeń: Python w Badaniach Ekonomicznych i Biznesowych.md` (całkowanie numeryczne i gęstość rozkładu z SciPy) jako zadanie 7.4 w Module 7.

---

## 2. KROKI REALIZACJI

### Krok 2.1: Rozszerzenie Modułu 7 w `course_content.py`
- Dodanie zadania 4 w słowniku pod kluczem `7`:
  - Tytuł: "Gęstość i całkowanie numeryczne (SciPy)"
  - lesson, theory, hint, template
  - Szablon funkcji: `integrate_normal_density(a: float, b: float) -> float` i `get_normal_pdf(z: float) -> float`
  - Ścieżki: `exercises/module_7/task_4.py` oraz `.agents/tests/test_module_7_4.py`

### Krok 2.2: Stworzenie Szablonu Zadania `exercises/module_7/task_4.py`
- Pusty plik szablonu z `pass`.

### Krok 2.3: Utworzenie Testów w `.agents/tests/test_module_7_4.py`
- Testy sprawdzające poprawność funkcji `get_normal_pdf` oraz całki `integrate_normal_density` w zadanym przedziale.

---

## 3. AUDYT & WERYFIKACJA [Auditor Handshake]
- Uruchomienie testów i potwierdzenie 100% poprawności.
