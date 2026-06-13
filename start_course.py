# -*- coding: utf-8 -*-
import os
import sys
import json
import subprocess
import argparse

# Importujemy dane kursu
try:
    from course_content import COURSE_DATA
except ImportError:
    print("[BŁĄD] Nie można zaimportować course_content.py. Upewnij się, że plik znajduje się w tym samym katalogu.")
    sys.exit(1)

STATE_FILE = ".agents/course_state.json"
LOG_FILE = ".agents/test_run.log"

def load_state():
    if not os.path.exists(STATE_FILE):
        os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
        default_state = {
            "current_module": 1,
            "current_task": 1,
            "completed_tasks": []
        }
        save_state(default_state)
        return default_state
    try:
        with open(STATE_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        # Awaryjny reset w razie uszkodzenia JSON
        return {
            "current_module": 1,
            "current_task": 1,
            "completed_tasks": []
        }

def save_state(state):
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    with open(STATE_FILE, 'w', encoding='utf-8') as f:
        json.dump(state, f, indent=4, ensure_ascii=False)

def check_dependencies():
    missing = []
    for lib in ["pandas", "numpy", "pytest"]:
        try:
            __import__(lib)
        except ImportError:
            missing.append(lib)
    if missing:
        print("\n\033[91m[UWAGA] Brakujące biblioteki wymagane do kursu: {}\033[0m".format(", ".join(missing)))
        print("Uruchom poniższe polecenie w terminalu, aby zainstalować zależności:")
        print("    \033[93mpip install -r requirements.txt\033[0m\n")
        return False
    return True

def get_next_task(module, task):
    # Znajdź następne zadanie w strukturze COURSE_DATA
    if module not in COURSE_DATA:
        return None, None
    
    tasks = sorted(COURSE_DATA[module]["tasks"].keys())
    current_idx = tasks.index(task)
    
    if current_idx + 1 < len(tasks):
        return module, tasks[current_idx + 1]
    
    # Przejdź do kolejnego modułu
    modules = sorted(COURSE_DATA.keys())
    current_mod_idx = modules.index(module)
    
    if current_mod_idx + 1 < len(modules):
        next_mod = modules[current_mod_idx + 1]
        next_tasks = sorted(COURSE_DATA[next_mod]["tasks"].keys())
        if next_tasks:
            return next_mod, next_tasks[0]
            
    return None, None

def display_lesson(state):
    mod = state["current_module"]
    task = state["current_task"]
    
    if mod not in COURSE_DATA or task not in COURSE_DATA[mod]["tasks"]:
        print("\n\033[92m[GRATULACJE] Ukończyłeś wszystkie dostępne zadania w kursie!\033[0m")
        display_git_instructions()
        return

    module_title = COURSE_DATA[mod]["title"]
    task_data = COURSE_DATA[mod]["tasks"][task]
    task_title = task_data["title"]
    lesson_text = task_data["lesson"]
    ex_path = task_data["exercise_path"]
    
    # Generowanie szablonu zadania, jeśli nie istnieje
    if not os.path.exists(ex_path):
        os.makedirs(os.path.dirname(ex_path), exist_ok=True)
        with open(ex_path, 'w', encoding='utf-8') as f:
            f.write(task_data["template"])
        print("\033[94m[INFO] Wygenerowano szablon zadania w: {}\033[0m".format(ex_path))
        
    print("=" * 60)
    print("\033[96m{}\033[0m".format(module_title))
    print("\033[93mZadanie {}.{}: {}\033[0m".format(mod, task, task_title))
    print("=" * 60)
    print(lesson_text.strip())
    print("-" * 60)
    print("Lokalizacja zadania do edycji: \033[94m{}\033[0m".format(ex_path))
    print("Weryfikacja rozwiązania:      \033[93mpython start_course.py --verify\033[0m")
    print("=" * 60)

def verify_solution(state):
    mod = state["current_module"]
    task = state["current_task"]
    
    if mod not in COURSE_DATA or task not in COURSE_DATA[mod]["tasks"]:
        print("[INFO] Brak aktywnych zadań do weryfikacji.")
        return
        
    task_data = COURSE_DATA[mod]["tasks"][task]
    test_path = task_data["test_path"]
    ex_path = task_data["exercise_path"]
    
    print("\n\033[94m[URUCHAMIANIE WERYFIKACJI] Zadanie {}.{}: {}...\033[0m".format(mod, task, task_data["title"]))
    
    if not os.path.exists(ex_path):
        print("\033[91m[BŁĄD] Plik z rozwiązaniem nie istnieje: {}\033[0m".format(ex_path))
        return
        
    # Uruchomienie testów przez pytest
    # Zapisujemy wyjście do logów w celu uproszczenia widoku dla ucznia
    cmd = [sys.executable, "-m", "pytest", test_path, "-v"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    with open(LOG_FILE, 'w', encoding='utf-8') as log_f:
        log_f.write(result.stdout)
        log_f.write(result.stderr)
        
    if result.returncode == 0:
        print("\033[92m[SUKCES] Zadanie zweryfikowane pomyślnie!\033[0m")
        task_str = "{}.{}".format(mod, task)
        if task_str not in state["completed_tasks"]:
            state["completed_tasks"].append(task_str)
            
        next_mod, next_task = get_next_task(mod, task)
        if next_mod is not None:
            state["current_module"] = next_mod
            state["current_task"] = next_task
            print("\033[96mOdblokowano kolejne zadanie: Zadanie {}.{}!\033[0m".format(next_mod, next_task))
        else:
            state["current_module"] = 999  # Oznaczenie końca kursu
            state["current_task"] = 999
            print("\033[92m[SUKCES] Wszystkie moduły ukończone!\033[0m")
            
        save_state(state)
        display_lesson(state)
    else:
        print("\033[91m[BŁĄD] Testy nie przeszły. Sprawdź swój kod w: {}\033[0m".format(ex_path))
        print("Szczegółowe informacje o błędzie zostały zapisane w: \033[93m{}\033[0m".format(LOG_FILE))
        print("\nSkrócony błąd:")
        # Wyciągamy ostatnie kilka linii z raportu pytest
        lines = result.stdout.splitlines()
        failures = [l for l in lines if l.startswith("FAIL") or "AssertionError" in l or "Error:" in l]
        if failures:
            for f_line in failures[-5:]:
                print("  " + f_line)
        else:
            # Pokaż ostatnie 10 linii wyjścia
            for l in lines[-10:]:
                print("  " + l)
        print("-" * 60)

def display_status(state):
    print("\n" + "=" * 60)
    print("\033[95mSTAN POSTĘPU KURSU\033[0m")
    print("=" * 60)
    
    total_tasks = 0
    completed_count = 0
    
    for m_id, m_data in COURSE_DATA.items():
        print("\n\033[96m{} (Moduł {})\033[0m".format(m_data["title"], m_id))
        for t_id, t_data in m_data["tasks"].items():
            task_str = "{}.{}".format(m_id, t_id)
            total_tasks += 1
            is_completed = task_str in state["completed_tasks"]
            if is_completed:
                status_icon = "\033[92m[X]\033[0m"
                completed_count += 1
            elif state["current_module"] == m_id and state["current_task"] == t_id:
                status_icon = "\033[93m[*]\033[0m (Aktualne)"
            else:
                status_icon = "\033[90m[ ]\033[0m"
            print("  {} Zadanie {}: {}".format(status_icon, t_id, t_data["title"]))
            
    print("\n" + "-" * 60)
    progress_pct = (completed_count / total_tasks * 100) if total_tasks > 0 else 0
    print("Postęp ogólny: {:.1f}% ({}/{} zadań)".format(progress_pct, completed_count, total_tasks))
    print("=" * 60)
    display_git_instructions()

def display_git_instructions():
    print("\n\033[95mINSTRUKCJE INTEGRACJI (Git / GitHub / Agents-OS)\033[0m")
    print("-" * 60)
    print("1. Aby sprawdzić status zmian w repozytorium:")
    print("   \033[93mgit status\033[0m")
    print("2. Aby złożyć zmiany i wysłać je na GitHub (wymaga gh cli):")
    print("   \033[93mgit add .\033[0m")
    print("   \033[93mgit commit -m \"feat: completed data analytics module\"\033[0m")
    print("   \033[93mgh pr create --title \"Completed Module\" --body \"Check my solutions\"\033[0m")
    print("3. Integracja z Agents-OS:")
    print("   Po sklonowaniu repozytorium uruchom agenta Antigravity w tym folderze.")
    print("   Używaj poleceń w terminalu repozytorium, aby uczyć się wspólnie z agentem.")
    print("-" * 60 + "\n")

def reset_course():
    state = {
        "current_module": 1,
        "current_task": 1,
        "completed_tasks": []
    }
    save_state(state)
    print("\033[93m[INFO] Stan kursu został zresetowany do Modułu 1 Zadania 1.\033[0m")
    return state

def main():
    parser = argparse.ArgumentParser(description="Asystent Kursu Python dla Ekonomistów CLI")
    parser.add_argument("--verify", action="store_true", help="Uruchamia weryfikację aktualnego zadania")
    parser.add_argument("--status", action="store_true", help="Wyświetla stan postępów ucznia")
    parser.add_argument("--reset", action="store_true", help="Resetuje stan kursu")
    args = parser.parse_args()
    
    state = load_state()
    check_dependencies()
    
    if args.reset:
        state = reset_course()
        display_lesson(state)
    elif args.verify:
        verify_solution(state)
    elif args.status:
        display_status(state)
    else:
        display_lesson(state)

if __name__ == "__main__":
    main()
