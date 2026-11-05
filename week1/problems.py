# Problem 1: Reverse the string without using [::-1]
road_name = "FC Road"
reversed_road_name = ""
for letter in road_name:
    reversed_road_name = letter + reversed_road_name
print(reversed_road_name)

# Problem 2: Print the largest number from the list without using max() function
lengths = [120, 450, 80, 900, 300]

largest_length = lengths[0]

for length in lengths:
    if length > largest_length:
        largest_length = length

print(largest_length)

# Problem 3: Count the repetitive words
sentence = "The road near the river and the bridge"
words = sentence.lower().split()
# print(words)

counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)

# Problem 4: Dictionaries inside a List
roads = [
    {"highway": "primary", "name": "FC Road"},
    {"highway": "residential"},
    {"highway": "primary", "name": "JM Road"},
    {"highway": "service"},
    {"highway": "residential", "name": "Baner Lane"},
]

highway_counts = {}
no_name_count = 0

for road in roads:
    road_type = road["highway"]
    highway_counts[road_type] = highway_counts.get(road_type, 0) + 1
    if "name" not in road:
        no_name_count = no_name_count + 1

print(highway_counts)
print(f"{no_name_count} roads have no name")