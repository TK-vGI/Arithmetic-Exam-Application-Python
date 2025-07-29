import random

def generate_task(level):
    if level == "1":
        a, b = random.randint(2, 9), random.randint(2, 9)
        sign = random.choice(["+", "-", "*"])
        task_text = f"{a} {sign} {b}"
        answer = eval(task_text)
    elif level == "2":
        a = random.randint(11, 29)
        task_text = f"{a}^2"
        answer = a ** 2
    elif level == "3":
        a = random.randint(-10, 10)
        b = random.randint(1, 3)
        sign = random.choice(["+", "-", "*", "**"])
        task_text = f"{a} {sign} {b}"
        answer = eval(f"{a} {sign} {b}")
    else:
        return None, ""
    return answer, task_text