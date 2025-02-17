# Problem
# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).

# input:
#   - an integer or float
# output:
#   - an integer of float

# Examples / Test Cases
# print(square(5) == 25)   # True
# print(square(-8) == 64)  # True

# Data Structures
# - Integer or/and Float

# Algorithm
# 1. Create a function square that takes a single argument of type in or float
#   2. return multiply(num, num)

# Code
def multiply(num1, num2):
    return num1 * num2


def square(number):
    return multiply(number, number)


print(square(5) == 25)   # True
print(square(-8) == 64)  # True
