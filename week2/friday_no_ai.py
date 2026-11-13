# 1. Import os, logging
import os
import logging

# 2. From friday_tools import longest_name
from friday_tools import longest_name
# 3. From roads import load_roads
from roads import load_roads


# 4. define a function "print_longest_name" whose primary work is to print the info
def print_longest_name(long_name):
    print(f"Longest name on a road: {long_name}")

# 5. inside if __name__ == "__main__"
if __name__ == "__main__":
    # a. Read LOG_LEVEL from the environment, default INFO
    logging.basicConfig(
        level=os.getenv("LOG_LEVEL", "INFO"),
        format="%(asctime)s %(levelname)s %(name)s: %(message)s",
    )
    # b. Load roads from week1/pune_roads.json, store in a variable
    roads = load_roads("week1/pune_roads.json")
    # c. Find the longest name from those roads, store in a variable
    long_name = longest_name(roads)
    # d. Print it using print_longest_name
    print_longest_name(long_name)
