# task 1: clean the road name
raw = "   mg road   "
step1 = raw.strip()
# print(step1)
step2 = step1.title()
# print(step2)
clean = step2.replace("Mg", "MG")
# print(clean)
single_line_version = raw.strip().title().replace("Mg", "MG")
print(single_line_version)


# task 2: split the tag into key and value
tag = "highway=residential"
parts = tag.split("=")
key = parts[0]
value = parts[1]
print(key)
print(value)

# task 2: split the tag into key and value (alternative method)
# key, value = tag.split("=")
# print(key)
# print(value)

# task 3: expand the short form
name = "Baner Rd"
full_name = name.replace("Rd", "Road")
print(full_name)

# task 3: challenge
# name = "ford rd"
# full_name = name.replace("rd", "road")
# print(full_name)

# task 4: build the sentence
print(f"{full_name} is a {value} road")