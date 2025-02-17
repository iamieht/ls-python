# Problem
# Write a function that takes a non-empty string argument and returns the middle character(s) of the string. If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

# input:
#   - a non-empty String
# output
#   - a string of characters: If the string has an odd length, you should return exactly one character. If the string has an even length, you should return exactly two characters.

# Examples / Test Cases
# print(center_of('I Love Python!!!') == "Py")    # True
# print(center_of('Launch School') == " ")        # True
# print(center_of('Launchschool') == "hs")        # True
# print(center_of('Launch') == "un")              # True
# print(center_of('Launch School is #1') == "h")  # True
# print(center_of('x') == "x")                    # True

# Data Structures
# - String

# ALgorithm
# 1. Create a function center_of that takes a single string as an argument
# 2. Check whether the string has a length of odd or even number
# 3. If odd calculate the middle char = len // 2 and return that char
# 4. If even calculate the middle char = len // 2 and return together with the previous char (2 chars in total)

# Code
def center_of(a_string):
    middle_char = len(a_string) // 2
    is_odd = len(a_string) % 2 == 1

    if is_odd:
        return a_string[middle_char]
    else:
        return a_string[middle_char -1: middle_char + 1]
    

print(center_of('I Love Python!!!') == "Py")    # True
print(center_of('Launch School') == " ")        # True
print(center_of('Launchschool') == "hs")        # True
print(center_of('Launch') == "un")              # True
print(center_of('Launch School is #1') == "h")  # True
print(center_of('x') == "x")                    # True