# Week 2 Weekly Note

## What I built

In week 2, I split my road summary script into modules and functions:

- `roads.py`: `load_roads(path)` loads roads from a JSON file, and `summarize_roads(roads)` returns the counts (total, processed, skipped, unnamed, by type). It logs with `logging` instead of `print`.
- `road_summary.py`: prints the report, inside a `__main__` guard, with the log level read from the `LOG_LEVEL` environment variable.
- `friday_tools.py`: `longest_name(roads)` returns the longest road name, or `None` if there is no name.
- `test_roads.py` and `test_friday_tools.py`: 11 pytest tests that check behaviour, including edge cases, and catch regressions.

## What broke

1. I wrote the `return` statement inside the loop in `count_words`. The expected output was 5, but I got 1.
2. In `summarize_roads`, I named the parameter `load_roads`, which is the name of another function, while the loop used `roads`. The function silently used the `roads` variable from outside the function. The output looked correct, but only by accident.
3. In `longest_name`, starting with `long_name = ""` instead of `None` returned an empty string when there were no names. The main test with real road names still passed.

## How I found the cause

1. The output was 1, which meant the loop stopped after the first iteration. `return` exits the function immediately.
2. An empty-list test exposed it: `summarize_roads([])` returned a total of 428 instead of 0.
3. Only the edge-case tests caught it: the empty-list test and the no-name test both failed with `assert '' is None`. A dry run before running the tests showed why the main test would still pass.

## How I fixed it

1. Moved `return` outside the loop. The output became 5.
2. Renamed the parameter to `roads`, so the function only uses the data it is given. The empty-list test now returns 0 and an empty dictionary.
3. Kept `None` as the starting value. All 3 tests pass. I learned that `""` (an empty string) and `None` (no value) are different.

## What I would do differently

- Write the pseudocode first, in detail, and do a dry run in my mind before writing code.
- Predict the output before every run, and check the prediction against the real output.
- Always write edge-case tests (empty input, missing data), not only the happy path.
- If I can explain a concept to someone else, I have really learned it.
