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
