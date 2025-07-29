import random
import os

MSG1 = "Which level do you want? Enter a number:\n\
1 - simple operations with numbers 2-9\n\
2 - integral squares of 11-29\n"


def generate_task(level: str) -> int | None:
    def generate_task_easy():
        sign = random.choice(("+", "-", "*"))
        operands = [random.randint(2, 9) for _ in range(2)]
        print(operands[0], sign, operands[1])
        if sign == "+":
            return operands[0] + operands[1]
        elif sign == "-":
            return operands[0] - operands[1]
        else:
            return operands[0] * operands[1]

    def generate_task_medium():
        operand = random.randint(11, 29)
        correct_answer = operand * operand
        print(operand)
        return correct_answer

    match level:
        case "1":
            return generate_task_easy()
        case "2":
            return generate_task_medium()
    return None


def check_answer(answer: int, correct: int) -> bool:
    return answer == correct


def save_to_file(name: str, marks: dict):
    correct = marks["correct"]
    lvl = marks["level"]
    desc_lvl = marks["description"]
    result = f"{name}: {correct}/5 in level {lvl} ({desc_lvl})."

    file_path = "results.txt"
    # Check if file exists
    if os.path.exists(file_path):
        # Append to the file
        with open(file_path, 'a', encoding='utf-8') as file:
            file.write(result)
    else:
        # Create and write to the file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(result)

    print('The results are saved in "results.txt".')


def output_result(marks: dict) -> None:
    print(f"Your mark is {marks["correct"]}/5. Would you like to save the result? Enter yes or no.")
    save = input().lower()
    if save in ["yes", "y"]:
        print("What is your name?")
        name = input()
        save_to_file(name, marks)
    else:
        return


def main():
    marks = {"correct": 0, "wrong": 0}

    while True:
        user = input(MSG1)
        if user == "1" or user == "2":
            marks.update({"level": user})
            description = "simple operations with numbers 2-9" if user == "1" else "integral squares of 11-29"
            marks.update({"description": description})
            break
        else:
            print("Incorrect format.")

    for i in range(5):
        correct_answer = generate_task(user)
        while True:
            try:
                answer = int(input())
                break
            except ValueError:
                print("Wrong format! Try again.")

        if check_answer(answer, correct_answer):
            print("Right!")
            marks["correct"] += 1
        else:
            print("Wrong!")
            marks["wrong"] += 1

    output_result(marks)


if __name__ == '__main__':
    main()