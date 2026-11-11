# def say_hello():
#     print("Hello, Ashwani")

# say_hello()
# say_hello()

# Print print_city before defining the function and learn the error
# print_city()


# Print a city "Pune" by defining a function
# def print_city():
#     print("Pune")

# print_city()
# print_city()
# print_city()

# Define a function that prints a new city in the same function
# def print_city(city):
#     print(f"City: {city}")

# print_city("Mumbai")
# print_city("Pune")

# # Practicing "return"
# def double(number):
#     return number * 2

# result = double(5)
# print(result)

# Common trap print vs return

def double_print(number):
    print(number * 2)

def double_return(number):
    return number * 2

# a = double_print(5)
# print(a)
# b = double_return(5)
# print(b)

# Test 1
# x = double_print(3)

# Test 2
# y = double_return(3)

# Test 3
# z = double_return(3) + 1
# print(z)

# Test 4
# w = double_print(3) + 1

# write a function that returns the count of words
# def count_words(sentence):
#     # split the sentence
#     words = sentence.split()
#     # Add a counter
#     word_count = 0
#     # write a for loop which counts the words in the sentence
#     for word in words:
#         word_count = word_count + 1
#     return word_count

# total = count_words("the road near the river")
# print(total)

# variation of the above code
# def count_words(sentence):
#     return len(sentence.split())
# total = count_words("the road near the river")
# print(total)






