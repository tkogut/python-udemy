# 📊 Kurs Programowania i Analityki Danych w Pythonie dla Ekonomistów

Witaj w dedykowanym środowisku szkoleniowym CLI dla kierunku **Analityka Gospodarcza / Ekonomia**. Środowisko to łączy naukę składni języka Python, zaawansowanej manipulacji danymi w bibliotece Pandas z pracą w ekosystemie agentowym **Agents-OS v5.0** oraz integracją z systemem kontroli wersji Git/GitHub.

---

## 🚀 Szybki Start

### 1. Klonowanie i przygotowanie środowiska
Jeśli jeszcze tego nie zrobiłeś, sklonuj repozytorium i wejdź do katalogu projektu:
```bash
git clone <adres-repozytorium>
cd python-udemy
```

Zaleca się stworzenie wirtualnego środowiska (virtualenv):
```bash
python3 -m venv .venv
source .venv/bin/activate  # Na Windows: .venv\Scripts\activate
```

Zainstaluj wymagane biblioteki analityczne i testowe:
```bash
pip install -r requirements.txt
```

### 2. Uruchomienie asystenta CLI
Uruchom główny skrypt szkoleniowy, aby pobrać pierwszą lekcję i wygenerować plik zadania:
```bash
python start_course.py
```

### 3. Rozwiązywanie zadań i weryfikacja
* Zadania będą generowane automatycznie w katalogu `exercises/`.
* Po uzupełnieniu kodu w pliku zadania, uruchom weryfikację:
  ```bash
  python start_course.py --verify
  ```
* Aby sprawdzić swój status w kursie i zobaczyć, które moduły masz już zaliczone, uruchom:
  ```bash
  python start_course.py --status
  ```
* Aby zresetować swój stan i zacząć od początku:
  ```bash
  python start_course.py --reset
  ```

---

## 🛠️ Integracja z Git & GitHub (gh cli)

Aby zapisać swoje postępy i zsynchronizować je z repozytorium zdalnym:

1. **Logowanie do GitHub CLI** (jeśli nie jesteś zalogowany):
   ```bash
   gh auth login
   ```
2. **Dodanie i zatwierdzenie zmian**:
   ```bash
   git add .
   git commit -m "feat: completed module 1 data structures"
   ```
3. **Wysłanie kodu i utworzenie Pull Request (PR)**:
   ```bash
   gh pr create --title "Rozwiązanie Modułu 1" --body "Rozwiązania zadań z matematyki finansowej."
   ```

---

## 🤖 Uruchomienie Środowiska Agents-OS v5.0

Ten projekt jest zintegrowany z systemem **Agents-OS**. Pozwala on na współpracę z autonomicznymi agentami AI (takimi jak Antigravity).

* Konfiguracja agentów znajduje się w katalogu `.agents/`.
* Aby rozpocząć współpracę z agentem pomocniczym w tym repozytorium, upewnij się, że masz uruchomiony CLI Antigravity i zainicjuj go w katalogu głównym projektu.
* Agent automatycznie rozpozna plik `.agents/plans/01_data_analytics_course.md` oraz backlog `task.md` i będzie mógł asystować Ci przy trudniejszych zagadnieniach oraz weryfikować poprawność kodu matematyczno-statystycznego.

Powodzenia! 📈
