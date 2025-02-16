# Problem
# Write a function that takes two strings as arguments, determines the length of the two strings, and then returns the result of concatenating the shorter string, the longer string, and the shorter string once again. You may assume that the strings are of different lengths.

# input
#   - 2 strings
# output
#   - 1 string with the format shorter+longer+shorter

# Example / Test Cases
# These examples should all print True
# print(short_long_short('abc', 'defgh') == "abcdefghabc")
# print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
# print(short_long_short('', 'xyz') == "xyz")

# Data Structure
# - String

# Algorithm
# 1. Create a function short_long_short that takes 2 strings as arguments
# 2. Compute the length of the strings
# 3. Compare the length of the strings
# 4. Concatenate the shorter string + longer string + shorter string
# 5. Return the new string

# Code
def short_long_short(string1, string2):
    if len(string1) > len(string2):
        return string2 + string1 + string2
    else:
        return string1 + string2 + string1
    
print(short_long_short('abc', 'defgh') == "abcdefghabc")
print(short_long_short('abcde', 'fgh') == "fghabcdefgh")
print(short_long_short('', 'xyz') == "xyz")