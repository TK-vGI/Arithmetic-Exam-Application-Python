from config import RESULTS_FILE
from stats import parse_entry_block, is_matching_name, update_stats, show_stats

def save_result(name, marks):
    with open(RESULTS_FILE, 'a', encoding='utf-8') as f:
        for level in marks:
            f.write(
                f"Name: {name}\n"
                f"Level: {level} - {marks[level]['description']}\n"
                f"Score: {marks[level]['correct']}/5\n"
                f"Time: {marks[level]['time_taken']} sec\n"
                f"{'-'*40}\n"
            )

def show_previous_results(name):
    print(f"\n🔍 Previous results for {name}:")
    level_stats = {}

    try:
        with open(RESULTS_FILE, "r", encoding="utf-8") as f:
            lines = f.readlines()
            total = len(lines)

            for i in range(0, total, 5):
                if i + 4 < total:
                    block = parse_entry_block(lines, i)
                    if is_matching_name(block, name):
                        for line in block[1:]:
                            print(line)
                        update_stats(block, level_stats)

        if level_stats:
            show_stats(level_stats)

    except FileNotFoundError:
        print("⚠️ Results file not found.")
