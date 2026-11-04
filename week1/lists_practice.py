road_types = ["primary", "residential", "service"]
print(road_types)

print(road_types[0])

print(road_types[-1])

print(road_types[0:2])

print(len(road_types))

# Append and print
road_types.append("motorway")
print(road_types)

# Replace and Print
road_types[0] = "trunk"
print(road_types)

# Remove and print
road_types.remove("service")
print(road_types)

# Sort and Print
road_types.sort()
print(road_types)

# Hands-on

# Step 1: Create a list
roads = ["FC Road", "MG Road", "Baner Road"]
print(roads)

# Step 2: Add "JM Road" at the end
roads.append("JM Road")
print(roads)

# Step 3: Print first and last item in the list
print(roads[0])
print(roads[-1])

# Step 4: remove "MG Road"
roads.remove("MG Road")
print(roads)

# Step 5: print len of list
print(len(roads))

# Step 6: 
print(roads.sort())
print(roads)