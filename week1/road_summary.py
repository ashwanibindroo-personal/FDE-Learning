import json

# Open the json file using "with"
try:
    with open("week1/pune_roads.json") as file:
        data = json.load(file)
except FileNotFoundError:
    print("Could not find the file. Check the path and run from the repo root")
    raise SystemExit(1)
except json.JSONDecodeError:
    print("Source json file is broken")
    raise SystemExit(1)


# Print the "type" of data
# print(type(data))

# Print top level keys of the data
# print(data.keys())

# Explore the data and what's inside "elements" key

# elements = data["elements"]
# elements.append({"type": "way", "id": 1})

# Print the "type" of elements
# print(type(elements))

# Print total number of elements
# print(len(elements))

# print elements at index 0
# print(elements[0])

# Print the value of "highway" key
# print(elements[0]["tags"]["highway"])

# 1. Get the list of roads from data["elements"]
elements = data["elements"]

# 2. Print the total number of roads
print(f"Total highway features in file: {len(elements)}")

# 3. Start an empty dictionary for type counts and a counter at 0 for unnamed roads
highway_types = {}
unnamed_roads = 0
skipped_roads = 0

# 4. Loop through each road:
#    a. Get its highway type from road["tags"] and add 1 to that type's count
#    b. If "name" is not in road["tags"], add 1 to the unnamed counter

for road in elements:
    # Guard clause
    if "tags" not in road:
        skipped_roads = skipped_roads + 1
        continue
        
    road_type = road["tags"]["highway"]
    highway_types[road_type] = highway_types.get(road_type, 0) + 1

    if "name" not in road["tags"]:
        unnamed_roads = unnamed_roads + 1

# Print Processed highway types
print(f"Processed: {sum(highway_types.values())}")

# Print the skipped roads
print(f"Roads with no tags: {skipped_roads}")


# Print the type counts
print(f"Roads by type: {highway_types}")

# Print the unnamed count
print(f"Roads with no name: {unnamed_roads}")







