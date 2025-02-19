# Problem
# Given a string that consists of some words and an assortment of non-alphabetic characters, write a function that returns that string with all of the non-alphabetic characters replaced by spaces. If one or more non-alphabetic characters occur in a row, you should only have one space in the result (i.e., the result string should never have consecutive spaces).

# input
# - string
# output
# - string

# Examples / Test Case
# print(clean_up("---what's my +*& line?") == " what s my line ")
# True

# Data Structures
# - String

# Algorithm
# 1. Create a function clean_up(string)
#   - Initialize a variable result = ""
#   - loop over the string and compare each char to see if is alphabetic
#       - if so, add it to the result
#       - if not, replace it with space and add it to result only if result doesn't end with space.

# Code
def clean_up(string):
    result = ""
    for char in string:
        if char.isalpha():
            result += char
        else:
            if not result.endswith(" "):
                result += " "

    return result


print(clean_up("---what's my +*& line?") == " what s my line ")
