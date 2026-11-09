# Week 1 Weekly Note

## What I built

I built a Python script that reads OpenStreetMap road features. The scope is limited to about 1 square kilometre of Pune. The script prints a summary of total features in the input file, processed features, skipped features, counts by road type and roads without a name.

## What broke

- The intention was to identify roads without names. The code I wrote was `"name" not in road`, which checked for `name` at the top level of each road instead of inside the `tags` key. It returned 428 unnamed roads instead of 309. Python did not throw any error.
- One incomplete road without a `tags` key crashed the whole report with a `KeyError`, so none of the results were printed.
- Some highway types like `footway` and `steps` were counted as roads, because OpenStreetMap uses the `highway` tag for pedestrian ways too.

## How I found the cause

- Python did not throw any error for the unnamed roads bug. I found the actual count by comparing a `grep` count on the input file (428 minus 119 named roads gives 309) with the Python output.
- For the crash, I read the traceback from the bottom up: error type, line number, file.

## How I fixed it

- Changed the check to `"name" not in road["tags"]`. The Python result now matches the `grep` count of 309.
- Added a guard clause at the top of the loop that skips roads without `tags` and counts them, so the report shows total, processed and skipped.
- Changed the label to "highway features". For car navigation, pedestrian ways should be reported separately, but kept in the data for pedestrian use.

## What I would do differently

- Always write pseudocode before writing the code, and think about edge cases like missing keys.
- Cross-check numbers using a different method.
- Experiment first instead of referring to notes.
