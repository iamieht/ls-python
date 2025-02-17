# Problem
# Write a function that returns the middle word of a phrase or sentence. It should handle all of the edge cases you thought of.


# input:
#   - a String
# output:
#   - a String 

# Examples / Test Cases
# These examples should print True
# print(middle_word("last word") == "word")
# print(middle_word("Launch School is great!") == "is")
# print(middle_word("Launch School is really great!") == "is")
# print(middle_word("")) == ""
# print(middle_word("hello")) == "hello"

# Data Structures
# - String
# - List

# Algorithm
# 1. Create a function middle_word that takes a String as an argument
# 2. Initialize a variable list_of_words = string.split()
# 3. Find the middle character = len(list_of_words) // 2
# 3. Return list_of_words[middle_char]

# Code
def middle_word(a_string):
    if a_string.isspace() or len(a_string) == 0:
        return a_string
    else:
        list_of_words = a_string.split()
        middle_idx = len(list_of_words) // 2
        return list_of_words[middle_idx]


print(middle_word("last word") == "word")
print(middle_word("Launch School is great!") == "is")
print(middle_word("Launch School is really great!") == "is")
print(middle_word("") == "")
print(middle_word(" ") == " ")
print(middle_word("hello") == "hello")