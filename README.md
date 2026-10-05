# PLP Python Week 6

## Assignment: Error Handling with try / except

### Files

- `safe_tools.py` — Contains safe functions that handle common Python errors.
- `unbreakable.py` — Contains the Week 6 error-handling exercise.
- `README.md` — Describes the assignment and explains the use of error handling.

### Why can't the `if` check catch `abc` on its own?

An `if` check can test a condition, but `int("abc")` causes Python to raise a `ValueError` when the conversion is attempted. The `try / except` block is used to catch that error and keep the program from crashing.