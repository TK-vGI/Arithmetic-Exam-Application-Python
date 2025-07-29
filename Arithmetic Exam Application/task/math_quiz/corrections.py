from config import CORRECTIONS_FILE
from evaluator import check_answer

def save_corrections(wrong_tasks):
    with open(CORRECTIONS_FILE, 'a') as f:
        for level, task_text, correct in wrong_tasks:
            f.write(f"{level}|{task_text}|{correct}\n")

def load_corrections():
    tasks = []
    try:
        with open(CORRECTIONS_FILE) as f:
            for line in f:
                parts = line.strip().split("|")
                if len(parts) == 3:
                    tasks.append((parts[0], parts[1], int(parts[2])))
    except FileNotFoundError:
        pass
    return tasks

def correction_stage():
    corrections = load_corrections()
    if corrections:
        print("\n🔁 Correction Practice:")
        for lvl, task_text, correct in corrections:
            print(f"\nTask: {task_text}")
            while True:
                user_input = input("Your answer: ").strip()
                if user_input.lstrip("-").isdigit():
                    if check_answer(int(user_input), correct):
                        print("✅ Correct!")
                        break
                print("❌ Try again.")