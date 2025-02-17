# Problem
# Using the multiply function from the "Multiplying Two Numbers" exercise, write a function that computes the square of its argument (the square is the result of multiplying a number by itself).
# Further Exploration: Suppose we want to generalize this function to a "power to the n" type function: cubed, to the 4th power, to the 5th, etc. How would we go about doing so while still using the multiply function?

# input:
#   - an integer or float and an exponent of type int
# output:
#   - an integer of float

# Examples / Test Cases
# print(power(5, 2) == 25)   # True
# print(power(-8, 2) == 64)  # True
# print(power(2,8) == 256)

# Data Structures
# - Integer or/and Float

# Algorithm
# 1. Create a function power that takes a number (int of float) and an exponent (int)
#   - Initialize a variable result to 1
#   - loop exponent times and invoke the multiply function passing the result and number as arguments
#   2. return result

# Code
def multiply(num1, num2):
    return num1 * num2


def power(number, exponent):
    result = 1
    for _ in range(exponent):
        result = multiply(result, number)

    return result


print(power(5, 2) == 25)   # True
print(power(-8, 2) == 64)  # True
print(power(2, 8) == 256)
