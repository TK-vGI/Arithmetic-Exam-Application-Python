from config import MSG1, LEVELS
from tasks import generate_task
from evaluator import check_answer
from results import save_result, show_previous_results
from corrections import save_corrections, correction_stage
import time

def run_level(level, marks, wrong_tasks):
    print(f"\n🧪 Starting level {level} - {LEVELS[level]}")
    correct = 0
    start = time.time()

    for _ in range(5):
        answer, task_text = generate_task(level)
        print(f"\nTask: {task_text}")
        while True:
            user_input = input("Your answer: ").strip()
            if user_input.lstrip("-").isdigit():
                user_answer = int(user_input)
                break
            print("⚠️ Wrong format! Try again.")

        if check_answer(user_answer, answer):
            print("✅ Correct!")
            correct += 1
        else:
            print(f"❌ Wrong! Correct answer was {answer}")
            wrong_tasks.append((level, task_text, answer))

    elapsed = round(time.time() - start, 2)
    marks[level] = {
        "description": LEVELS[level],
        "correct": correct,
        "time_taken": elapsed
    }

    print(f"\n🏁 You scored {correct}/5 in level {level}. Time: {elapsed}s")
    return correct >= 4

def main():
    open("corrections.txt", "w", encoding="utf-8").close()

    marks = {}
    wrong_tasks = []

    level = input(MSG1).strip()
    while level not in LEVELS:
        print("Invalid level.")
        level = input(MSG1).strip()

    while run_level(level, marks, wrong_tasks):
        level = str(int(level) + 1)
        if level not in LEVELS:
            break
        print(f"\n🎉 Great job! Advancing to level {level}.")

    print("\n📊 Level results:")
    for lvl in marks:
        print(f"Level {lvl}: {marks[lvl]['correct']}/5")

    save_prompt = input("Do you want to save the result? (yes/no): ").strip().lower()
    if save_prompt in ["yes", "y"]:
        name = input("Enter your name: ").strip()
        save_result(name, marks)
        save_corrections(wrong_tasks)
        show_previous_results(name)
    else:
        print("Result not saved.")

    correction_stage()

if __name__ == "__main__":
    main()