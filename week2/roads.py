# print(f"roads.py says: __name__ = {__name__}")

import json

# Load the list of roads from a JSON file
def load_roads(path):
    try:
        with open(path) as file:
            data = json.load(file)
    except FileNotFoundError:
        print("Could not find the file. Check the path and run from the repo root")
        raise SystemExit(1)
    except json.JSONDecodeError:
        print("Source json file is broken")
        raise SystemExit(1)
    return data["elements"]


# Define a funtion "summarize_roads" and initiate empty dictionay
# for type counts and counters at 0 for unnamed and skipped roads
def summarize_roads(roads):
    highway_types = {}
    unnamed_roads = 0
    skipped_roads = 0

    # Loop through each road:
    #  a. Get its highway type from road["tags"] and add 1 to that type's count
    #  b. If "name" is not in road["tags"], add 1 to the unnamed counter

    for road in roads:
        # Guard clause
        if "tags" not in road:
            skipped_roads = skipped_roads + 1
            continue
            
        road_type = road["tags"]["highway"]
        highway_types[road_type] = highway_types.get(road_type, 0) + 1

        if "name" not in road["tags"]:
            unnamed_roads = unnamed_roads + 1
    return {
        "total": len(roads),
        "processed": sum(highway_types.values()),
        "skipped": skipped_roads,
        "unnamed": unnamed_roads,
        "by_type": highway_types
    }
