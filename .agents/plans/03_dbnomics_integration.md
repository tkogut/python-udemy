# [SEQ-PRO] Plan 03: Integracja Wiedzy DBnomics w Module 9

## 1. CEL
Wdrożenie nowej wiedzy o platformie DBnomics z dokumentu `.agents/specs/knowledge/DBnomics.md` poprzez zastąpienie dotychczasowego zadania 9.1 (API NBP) zadaniem zintegrowanym bezpośrednio z API DBnomics.

---

## 2. KROKI REALIZACJI

### Krok 2.1: Zmiana Zadania 9.1 w `course_content.py`
- Nowa nazwa zadania: "Integracja z API DBnomics".
- Funkcja do zaimplementowania: `get_dbnomics_series(api_url: str) -> list`
- Teoria: Wyjaśnienie architektury DBnomics, proweniencji danych, rygoru "non-opinionated" (zachowanie wartości NA/None).
- Szablon i wskazówki: Przetwarzanie odpowiedzi JSON z API DBnomics:
  `https://api.dbnomics.world/v22/series/...`

### Krok 2.2: Aktualizacja Zadania w `exercises/module_9/task_1.py`
- Zastąpienie starego szablonu NBP nowym szablonem DBnomics.

### Krok 2.3: Aktualizacja Testów w `.agents/tests/test_module_9_1.py`
- Mockowanie odpowiedzi HTTP z serwera DBnomics (`https://api.dbnomics.world/`).
- Weryfikacja poprawnego parsowania okresów i wartości, w tym poprawne zachowanie wartości pustych (`None`).

---

## 3. AUDYT & WERYFIKACJA [Auditor Handshake]
- Uruchomienie testów jednostkowych za pomocą `pytest`.
- Sprawdzenie CLI `start_course.py`.
