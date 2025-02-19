# Problem
# Write a function that returns the number provided as an argument multiplied by two, unless the argument is a double number. If the argument is a double number, return the double number as-is.
# A double number is an even-length number whose left-side digits are exactly the same as its right-side digits. For example, 44, 3333, 103103, and 7676 are all double numbers, whereas 444, 334433, and 107 are not.

# input:
#   - a positive integer
# output
#   - integer: number * 2 if number is not a double number
#   - integer: double number if number is a double number

# Examples / Test Cases
# print(twice(37) == 74)                  # True
# print(twice(44) == 44)                  # True
# print(twice(334433) == 668866)          # True
# print(twice(444) == 888)                # True
# print(twice(107) == 214)                # True
# print(twice(103103) == 103103)          # True
# print(twice(3333) == 3333)              # True
# print(twice(7676) == 7676)              # True

# Data Structure
# - Integer
# - String

# Algorithm
# 1. Create is_double(integer):
#   - number = str(integer)
#   - middle_char = len(number) // 2
#   - return number[0:middle_char] == number[middle_char:-1]
# 2. Create a function twice(integer)
#   - return (integer if is_double(integer) else integer * 2)

# Code:
def is_double(integer):
    number = str(integer)
    middle_char = len(number) // 2
    return number[:middle_char] == number[middle_char:]


def twice(integer):
    return (integer if is_double(integer) else integer * 2)


print(twice(37) == 74)                  # True
print(twice(44) == 44)                  # True
print(twice(334433) == 668866)          # True
print(twice(444) == 888)                # True
print(twice(107) == 214)                # True
print(twice(103103) == 103103)          # True
print(twice(3333) == 3333)              # True
print(twice(7676) == 7676)              # True
