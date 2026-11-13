# 1. Import necessary libraries
import logging

logger = logging.getLogger(__name__)

# 2. Define a function which does the following:
def longest_name(roads):
    # a. Within the function, define a variable to store the longest name as text. Start with None
    long_name = None 
    # b. Inside the loop, identify the roads with no "tags" and use "continue" to keep the program running and log WARNING
    for road in roads:
        if "tags" not in road:
            logger.warning("Skipped road id %s: no tags", road.get("id"))
            continue
        

        # c. Inside the loop, skip the road that has no name
        if "name" not in road["tags"]:
            continue
        # d. Inside the loop, iterate through the first valid name of a road and consider that name as the
        # longest name, then compare the len of names on each road and keep the longest one only
        name = road["tags"]["name"]

        if long_name is None:
            long_name = name
        elif len(name) > len(long_name): # on a tie, the first name found wins
            long_name = name
    # e. After the loop, return the variable
    return long_name

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    ROADS = [
        {"id": 1, "tags": {"highway": "primary", "name": "FC Road"}},
        {"id": 2, "tags": {"highway": "residential", "name": "Senapati Bapat Road"}},
        {"id": 3, "tags": {"highway": "service"}},
        {"id": 4},
    ]
    print(longest_name(ROADS))

    

