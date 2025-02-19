# Problem
# Write a function that takes one argument, a positive integer, and returns a string of alternating '1's and '0's, always starting with a '1'. The length of the string should match the given integer.

# input:
# - positive integer: length of the string
# output:
# - a string of '1' and '0'. Always starting with '1'

# Examples / Test Cases
# print(stringy(6) == "101010")           # True
# print(stringy(9) == "101010101")        # True
# print(stringy(4) == "1010")             # True
# print(stringy(7) == "1010101")          # True

# Data Structure
# - integer
# - string

# Algorithm
# 1. Create a function stringy that takes a single argument of type integer
# 2. Initialize a variable result = ''
# 3. Loop integer times and check if result == '' or result.endswith('0') then concatenate '1' else concatenate '0'
# 4. return result

# Code
def stringy(integer):
    result = ''
    for _ in range(integer):
        result += '1' if result == '' or result.endswith('0') else '0'

    return result


print(stringy(6) == "101010")           # True
print(stringy(9) == "101010101")        # True
print(stringy(4) == "1010")             # True
print(stringy(7) == "1010101")          # True
