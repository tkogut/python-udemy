# 📊 Kurs Programowania i Analityki Danych w Pythonie dla Ekonomistów (Środowisko WSL)

Witaj w dedykowanym środowisku szkoleniowym CLI dla kierunku **Analityka Gospodarcza / Ekonomia**. Środowisko to łączy naukę składni języka Python, zaawansowanej manipulacji danymi w bibliotece Pandas z pracą w ekosystemie agentowym **Agents-OS v5.0** w środowisku **WSL (Windows Subsystem for Linux)**.

Praca w systemie Linux (przez WSL) jest standardem branżowym w analizie danych i inżynierii oprogramowania. Wszystkie poniższe polecenia należy uruchamiać w terminalu WSL (np. dystrybucji Ubuntu).

---

## 💻 Przygotowanie Środowiska WSL (Windows)

Jeśli jeszcze nie masz przygotowanego środowiska WSL na Windows, wykonaj poniższe kroki w PowerShellu (jako Administrator):

1. **Instalacja WSL i Ubuntu**:
   ```powershell
   wsl --install
   ```
   *Po instalacji uruchom ponownie komputer i skonfiguruj nazwę użytkownika oraz hasło w konsoli Ubuntu.*

2. **Instalacja pakietów systemowych w WSL (Ubuntu)**:
   Uruchom terminal WSL/Ubuntu i zainstaluj Pythona oraz pip:
   ```bash
   sudo apt update && sudo apt install -y python3-pip python3-venv git
   ```

3. **Uruchomienie VS Code w WSL**:
   Zainstaluj w Windows dodatek **WSL** do VS Code. Następnie w terminalu WSL wpisz:
   ```bash
   code .
   ```
   *VS Code otworzy się na systemie Windows, ale będzie połączony bezpośrednio z plikami wewnątrz środowiska WSL.*

---

## 🚀 Szybki Start (w terminalu WSL)

### 1. Klonowanie i przygotowanie repozytorium
W terminalu WSL sklonuj repozytorium do swojego katalogu domowego (np. `~/projects/`):
```bash
mkdir -p ~/projects && cd ~/projects
git clone <adres-repozytorium>
cd python-udemy
```

Utwórz i aktywuj wirtualne środowisko Pythona:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

Zainstaluj wymagane biblioteki analityczne:
```bash
pip install -r requirements.txt
```

### 2. Uruchomienie asystenta CLI
Uruchom główny skrypt szkoleniowy w terminalu WSL:
```bash
python3 start_course.py
```

### 3. Rozwiązywanie zadań i weryfikacja
* Zadania będą generowane automatycznie w katalogu `exercises/`.
* Po uzupełnieniu kodu w pliku zadania, uruchom weryfikację:
  ```bash
  python3 start_course.py --verify
  ```
* Aby sprawdzić status postępów:
  ```bash
  python3 start_course.py --status
  ```
* Aby zresetować stan kursu do początku:
  ```bash
  python3 start_course.py --reset
  ```

---

## 🛠️ Integracja z Git & GitHub w WSL (gh cli)

Aby zapisać swoje postępy i zsynchronizować je z repozytorium zdalnym bezpośrednio z WSL:

1. **Instalacja GitHub CLI w WSL (Ubuntu)**:
   ```bash
   type -p curl >/dev/null || (sudo apt update && sudo apt install curl -y)
   sudo mkdir -p -m 755 /etc/apt/keyrings
   curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/etc/apt/keyrings/githubcli-archive-keyring.gpg
   sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   sudo apt update
   sudo apt install gh -y
   ```
2. **Logowanie do GitHub**:
   ```bash
   gh auth login
   ```
3. **Zapisanie zmian (Commit & PR)**:
   ```bash
   git add .
   git commit -m "feat: completed module 1 data structures"
   gh pr create --title "Rozwiązanie Modułu 1" --body "Rozwiązania zadań z matematyki finansowej."
   ```

---

## 🤖 Uruchomienie Środowiska Agents-OS v5.0 w WSL

Ten projekt jest w pełni zintegrowany z systemem **Agents-OS**.
* Konfiguracja agentów znajduje się w katalogu `.agents/`.
* Aby rozpocząć współpracę z agentem pomocniczym w tym repozytorium, upewnij się, że masz uruchomiony CLI Antigravity i zainicjuj go w katalogu głównym projektu w WSL.
* Agent automatycznie rozpozna plik `.agents/plans/01_data_analytics_course.md` oraz backlog `task.md` i będzie mógł asystować Ci przy trudniejszych zagadnieniach oraz weryfikować poprawność kodu matematyczno-statystycznego.

Powodzenia! 📈
