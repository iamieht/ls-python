# Problem
# Write a function that returns the next to last word in the string argument.


# input:
#   - a String with at least two words
# output:
#   - a String 

# Assumptions:
# - Words are any sequence of non-blank characters.

# Examples / Test Cases
# These examples should print True
# print(penultimate("last word") == "last")
# print(penultimate("Launch School is great!") == "is")

# Data Structures
# - String
# - List

# Algorithm
# 1. Create a function penultimate that takes a String as an argument
# 2. Initialize a variable list_of_words = string.split()
# 3. Return list_of_words[-2]

# Code
def penultimate(a_string):
    list_of_words = a_string.split()
    return list_of_words[-2]

print(penultimate("last word") == "last")
print(penultimate("Launch School is great!") == "is")