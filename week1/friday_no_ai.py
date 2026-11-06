# Problem 1: Reverse the string without using[::-1]
city = "Pune"
reversed_city = ""

for letter in city:
    reversed_city = letter + reversed_city

print(reversed_city)

# Problem 2: Identify the smallest number without using .min()
elevations = [12, -3, 45, -10, 7]
# Start by assuming the first value is the smallest
smallest_elevation = elevations[0]

# Check every elevation
for elevation in elevations:
    # If it is smaller than the current smallest, replace it
    if elevation < smallest_elevation:
        smallest_elevation = elevation

# Print the result
print(smallest_elevation)

# Problem 3: Get the keys in alphabetical order
road = {"name": "FC Road", "highway": "primary", "lanes": 4, "surface": "asphalt", "oneway": "yes"}

sorted_keys = sorted(road)
print(sorted_keys)

for key in sorted_keys:
    print(f"{key} = {road[key]}")

