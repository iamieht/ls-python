# Problem
# Write a function that takes a string argument and returns a new string that contains the value of the original string with all consecutive duplicate characters collapsed into a single character.

# input
# - string
# output
# - string

# Examples / Test Cases
# These examples should all print True
# print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
# print(crunch('4444abcabccba') == '4abcabcba')
# print(crunch('ggggggggggggggg') == 'g')
# print(crunch('abc') == 'abc')
# print(crunch('a') == 'a')
# print(crunch('') == '')

# Data Structures
# - String

# Algorithm
# 1. Create a function crunch that takes a single argument of type string
# 2. Initialize a variable result = ""
# 3. Loop over each char of the original string an concatenate it to the result variable if the char is not equal to the last element of the result variable.
# 4. return result

# Code
def crunch(string):
    result = ""
    for char in string:
        if not result.endswith(char):
            result += char

    return result


print(crunch('ddaaiillyy ddoouubbllee') == 'daily double')
print(crunch('4444abcabccba') == '4abcabcba')
print(crunch('ggggggggggggggg') == 'g')
print(crunch('abc') == 'abc')
print(crunch('a') == 'a')
print(crunch('') == '')
