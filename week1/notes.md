# Week 1 Notes

Reference notes for Week 1. Do not open these during No-AI practice sessions.

## 1. Setup and Git

| Command | What it does |
|---|---|
| `brew install uv git gh` | Install uv, Git and the GitHub tool |
| `uv python install` | Install Python through uv |
| `uv init` | Turn a folder into a Python project (`pyproject.toml`) |
| `uv run file.py` | Run a file inside the project environment |
| `git status` | Show what changed. Always check before and after `git add` |
| `git add .` | Stage all changes in this folder and its subfolders |
| `git commit -m "message"` | Save a snapshot on your laptop |
| `git push` | Send your snapshots to GitHub |

Memory trick: add = packing, commit = sealing the box, push = sending by courier.

Habit: run `pwd` before `git add .`, so you know which folder it will stage.

Commit `uv.lock`. Keep `.env`, `.venv/`, `__pycache__/` and `.DS_Store` in `.gitignore`.

## 2. Terminal

| Command | Meaning |
|---|---|
| `pwd` | Where am I? |
| `ls` / `ls -la` | List files / list all, including hidden |
| `ls -lh file` | Show file size in readable units |
| `cd folder` / `cd ..` / `cd ~` | Go into folder / one level up / home |
| `mkdir name` | Create a folder |
| `touch file` | Create an empty file |
| `cat file` | Show file content |
| `cp a b` | Copy |
| `mv a b` | Move or rename |
| `rm file` | Delete. It does not go to Trash |
| `echo "text"` | Print text |
| `grep "word" file` | Show lines containing the word. `-c` count, `-i` ignore case, `-n` line numbers, `-r` all files in a folder |

Symbols:

- `>` output redirect: write to a file, replacing its content
- `>>` append redirect: add to the end of a file
- `|` pipe: send one command's output to another command
- `~` home folder, `.` this folder, `..` one folder up, a name starting with `.` is a hidden file

`grep` matches text, not meaning. `grep -c "name"` also counts `name:mr`, `old_name` and so on.

## 3. Environment variables

- `export NAME="value"` makes a variable available to programs started from this terminal only.
- A new terminal starts empty. It only reads `~/.zshrc` at startup. Put the `export` line there to have it in every terminal.
- Never put API keys in `.zshrc`. Use a project `.env` file (ignored by Git) or the Mac Keychain.
- In Python: `os.getenv("NAME")`.

## 4. Strings

- Index starts at 0. `road[0:2]` gives index 0 and 1. The end number is not included.
- Strings are immutable. Methods return a new string. Store it: `clean = raw.strip()`.

| Method | Example | Result |
|---|---|---|
| `.strip()` | `"  FC Road  "` | `"FC Road"` |
| `.lower()` / `.upper()` / `.title()` | `"fc road".title()` | `"Fc Road"` |
| `.replace(a, b)` | `"Baner Rd".replace("Rd", "Road")` | `"Baner Road"` |
| `.split()` | `"the  road".split()` | `["the", "road"]` |
| `.split("=", 1)` | `"a=b=c".split("=", 1)` | `["a", "b=c"]` |
| `.endswith(" Rd")` | `"JM Rd".endswith(" Rd")` | `True` |
| `in` | `"Road" in "FC Road"` | `True` |

- f-string: `f"{name} is a {kind} road"`. Without the `f`, braces print as plain text.
- Order matters: `sentence.lower().split()` works, `sentence.split().lower()` fails.

## 5. Lists

- `.append(x)`, `.remove(x)`, `list[0] = x`, `len(list)`
- `list.sort()` changes the list and returns `None`. Never write `roads = roads.sort()`.
- `sorted(list)` returns a new sorted list and leaves the original unchanged.
- Code inside brackets runs first: `print(roads.sort())` sorts the list, then prints `None`.

## 6. Loops and conditions

```python
for road in roads:
    if road.endswith(" Rd"):
        print(road)
```

- The loop variable (`road`) is created by the loop. One item per iteration.
- Indentation (4 spaces) decides what runs inside the loop.
- Counters start outside the loop. Inside, they reset every iteration.
- `=` stores a value. `==` asks "equal?". `>` bigger, `<` smaller.
- `if` / `else`: `else` runs when the `if` is not true.

Patterns:

```python
# Build a result step by step (reverse a string)
reversed_text = ""
for letter in text:
    reversed_text = letter + reversed_text

# Smallest or largest: start from a value in the list, not 0
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
```

## 7. Dictionaries

```python
road = {"highway": "primary", "name": "FC Road"}
```

| Action | Code |
|---|---|
| Get a required key | `road["highway"]` (missing key gives `KeyError`) |
| Get an optional key | `road.get("maxspeed", "not set")` |
| Change or add | `road["lanes"] = 2` |
| Delete | `del road["lanes"]` |
| Key exists? | `"name" in road` |
| Loop over keys | `for key in road:` |
| Loop over keys and values | `for key, value in road.items():` |
| Keys in order | `for key in sorted(road):` then `road[key]` |

- Use `[]` when the key must exist, so missing data fails loudly. Use `.get()` when the key is optional.
- `.get()` only reads. `=` writes.
- Counting pattern:

```python
counts[item] = counts.get(item, 0) + 1
```

- Dictionaries keep insertion order, but you look things up by key, not by position. Lookup by key is instant even with millions of items.

## 8. JSON files

```python
import json

with open("week1/pune_roads.json") as file:
    data = json.load(file)
```

- `with` closes the file automatically.
- The path is relative to where you run the program. Run from the repo root.
- Explore before coding: `data.keys()`, `type(...)`, `len(...)`, first item.
- Metadata (`version`, `generator`, `osm3s`) is data about the data. Real content is in `elements`.
- Nested access: `road["tags"]["highway"]`.

## 9. Errors

Read a traceback from the bottom up: error type, underlined code, line number, file.

| Error | When it happens |
|---|---|
| `KeyError` | Dictionary key missing and `[]` was used |
| `TypeError` | Mixing wrong data types, for example `None + 1` |
| `AttributeError` | Calling a method the object does not have, for example `list.lower()` |
| `ValueError` | Right type, wrong shape or value |
| `IndexError` | List position does not exist, for example `[][0]` |
| `IndentationError` | Wrong or mixed indentation |

## 10. Silent traps (no error, wrong result)

- `.replace()` matches letters, not words: `"ford rd"` became `"foroad road"`.
- `.replace()` with no match returns the string unchanged.
- f-string without `f`.
- `roads = roads.sort()` turns the list into `None`.
- A counter inside the loop resets every iteration.
- Starting "smallest" or "largest" at 0.
- Overwriting a variable with the same name.
- `.split(" ")` creates empty strings on double spaces.
- `"name" not in roads` (the list) instead of `road` (one item).
- `"name" not in road` instead of `road["tags"]`.

Rule: always check the output by hand or with a second method.

## 11. Working habits

- Write pseudocode (English comments) before code, especially on a blank page.
- Change one thing, save, run, check.
- Print intermediate values when the output is wrong.
- Cross-check results with a second method (for example `grep` versus Python).
- Comments must match the code. A wrong comment is worse than none.
- Name variables by what they hold: `sorted_keys`, not `road_list`.
- AI code may work but be more complex than needed. Judge it, simplify it.

## 12. Map domain notes

- Overpass bounding box order: (south, west, north, east), that is lat first. GeoJSON uses lon first.
- 0.01 degrees is about 1.1 km north to south.
- OpenStreetMap roads can have names in many languages: `name`, `name:mr`, `name:en`.
- The `highway` tag also covers footways, steps and platforms. For car navigation, report them separately, but keep them in the data for pedestrian use.
- OpenStreetMap data needs credit: "© OpenStreetMap contributors, ODbL".

## 13. Weekend project result

`road_summary.py` on 428 `highway` features in a 1 km box in Pune:

- Counts by type (residential 127, service 141, footway 76, ...)
- 309 without a `name` tag, confirmed with `grep` (428 minus 119)
