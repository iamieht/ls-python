# Problem
# Write a function that takes a number as an argument. If the argument is a positive number, return the negative of that number. If the argument is a negative number, return it as-is.

# input
# - a number
# output
# - a negative number

# Examples / Test Cases
# print(negative(5) == -5)      # True
# print(negative(-3) == -3)     # True
# print(negative(0) == 0)       # True

# Data Structure
# - Numbers

# ALgorithm
# 1. Create a function negative that takes a single number as an argument
# 2. return num if num < 0 else num * -1

# Code
def negative(number):
    return number if number < 0 else -number
    # return -abs(number)

print(negative(5) == -5)      # True
print(negative(-3) == -3)     # True
print(negative(0) == 0)       # True