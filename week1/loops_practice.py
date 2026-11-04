# basic for loop
roads = ["FC Road", "MG Road", "Baner Road"]

for road in roads:
    print(road)


# Andar kya hai, bahar kya hai
for road in roads:
    print(road)
print("Done")

# Map wala example

roads = ["FC Road", "Baner Rd", "MG Road", "JM Rd"]

for road in roads:
    if road.endswith(" Rd"):
        print(f"Fix Needed: {road}")

# Loops me ginti karna
roads = ["FC Road", "Baner Rd", "MG Road", "JM Rd"]
count = 0

for road in roads:
    if road.endswith(" Rd"):
        count = count + 1

print(f"{count} roads need fixing")

# Hands-on
road_types = ["primary", "residential", "primary", "service", "residential", "primary"]
# Print all road types using loop
for road_type in road_types:
    print(road_type)

# Print only "primary" using loop
for road_type in road_types:
    if road_type == "primary":
        print(road_type)

# Count the primary raods and print "3 primary roads" using f string
count = 0
for road_type in road_types:
    if road_type == "primary":
        count = count + 1
print(f"{count} primary roads")


