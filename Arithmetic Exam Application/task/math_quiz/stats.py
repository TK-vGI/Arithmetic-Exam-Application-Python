def parse_entry_block(lines, start_index):
    return [line.strip() for line in lines[start_index:start_index + 5]]

def is_matching_name(block, name):
    return block[0] == f"Name: {name}"

def update_stats(block, level_stats):
    level = block[1].replace("Level: ", "")
    score_line = block[2].replace("Score: ", "")
    time_line = block[3].replace("Time: ", "").replace(" sec", "")
    try:
        score, max_score = map(int, score_line.split("/"))
        time_val = float(time_line)
    except ValueError:
        return

    stats = level_stats.setdefault(level, {
        "count": 0,
        "total_score": 0,
        "max_score": max_score,
        "best_score": 0,
        "fastest_time": time_val
    })

    stats["count"] += 1
    stats["total_score"] += score
    stats["best_score"] = max(stats["best_score"], score)
    stats["fastest_time"] = min(stats["fastest_time"], time_val)

def show_stats(level_stats):
    print("\n🏆 Leaderboard & Stats:")
    for level, stats in level_stats.items():
        avg = stats["total_score"] / stats["count"]
        print(f"- {level}")
        print(f"  Played: {stats['count']}x")
        print(f"  Best: {stats['best_score']}/{stats['max_score']}")
        print(f"  Avg: {avg:.2f}/{stats['max_score']}")
        print(f"  Fastest: {stats['fastest_time']:.2f}s\n")