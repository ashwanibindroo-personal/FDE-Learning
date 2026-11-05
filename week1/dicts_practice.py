# Practicing dictionary

# Create a dictionary
road = {"highway": "residential", "name": "Baner Road", "lanes": 2}

# print the value of key 'name'
print(road["name"])

# Changes the value of lanes to 3
road["lanes"] = 3
print(road["lanes"])

# Add new key-value pair
road["surface"] = "asphalt"
print(road["surface"])

# Print an unknown key using .get(), set defaukt vale "not set"
print(road.get("maxspeed", "not set"))

# print(road["maxspeed"])

# Dictionaries + loops
road = {"highway": "primary", "name": "FC Road", "lanes": 4}

for key in road:
    print(key)

# Dictionaries + loops on both key and value
for key, value in road.items():
    print(f"{key} = {value}")

# Count road types
road_types = ["primary", "residential", "primary", "service", "residential", "primary"]

# counts = {}

# for road_type in road_types:
#     if road_type in counts:
#         counts[road_type] = counts[road_type] + 1
#     else:
#         counts[road_type] = 1

# print(counts)

# Hands-on challenge - use .get(), don't use if and else
counts = {}
for road_type in road_types:
    counts[road_type] = counts.get(road_type, 0) + 1
print(counts)




