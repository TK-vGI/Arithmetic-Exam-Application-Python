# Math Quiz Project

A modular Python app for practicing arithmetic and tracking performance.

## Features
- Multiple levels of difficulty
- Result tracking with timestamps
- Leaderboard metrics and personal statistics

## Modules
- `__init__.py`
- `main.py`: The core entry point that drives the quiz flow.
    Imports from other modules
    Handles level selection & progression
    Invokes corrections, result saving
- `tasks.py` : Task generation per level.
- `evaluator.py` : Answer checking logic.
- `results.py` : Handles saving and displaying results.
- `corrections.py` : Handles loading, saving, and reviewing wrong answers.
- `stats.py` : Level stats and leaderboard printing.
- `config.py` : Centralized constants and messages.