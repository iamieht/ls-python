# Problem
# Write a function that determines and returns the UTF-16 string value of a string passed in as an argument.

# input:
# - a String
# output:
# - Integer

# Rules
# The UTF-16 string value is the sum of the UTF-16 values of every character in the string. (You may use ord to determine the UTF-16 value of a character.)

# Examples / Test Cases
# These examples should all print True
# print(utf16_value('Four score') == 984)
# print(utf16_value('Launch School') == 1251)
# print(utf16_value('a') == 97)
# print(utf16_value('') == 0)

# # The next three lines demonstrate that the code
# # works with non-ASCII characters from the UTF-16
# # character set.
# OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
# print(utf16_value(OMEGA) == 937)
# print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)

# Data Structure
# - String
# - Integer

# Algorithm
# 1. Create a function utf16_value that takes a string as an argument
# 2. Create a helper function char_to_value that takes a string char as an argument and returns its value using `ord` function
#   3. return ord(char)
# 4. Initialize a variable result = 0
# 5. Loop over each string character and invoke the function char_to_value and do augmented assignment with addition to get the sum of all the values.

# Code
def char_to_value(char):
    return ord(char)

def utf16_value(string):
    result = 0
    for char in string:
        result += char_to_value(char)

    return result

print(utf16_value('Four score') == 984)
print(utf16_value('Launch School') == 1251)
print(utf16_value('a') == 97)
print(utf16_value('') == 0)
OMEGA = "\u03A9"              # UTF-16 character 'Ω' (omega)
print(utf16_value(OMEGA) == 937)
print(utf16_value(OMEGA + OMEGA + OMEGA) == 2811)