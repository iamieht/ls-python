# Problem
# Print all even numbers from 1 to 99, inclusive, with each number on a separate line.
# input:
#   2 integer numbers
# output:
#   all even numbers from 1 to 99

# Example (Test Case)
# even_numbers(1, 99) # 2, 4, 6, 8, 10 ...

# Data Structure
# integer

# Algorithm
# 1. Define a function even_numbers that takes two integer numbers. The start and end (inclusive).
# 2. Iterate over the range function from number 1 to number 2, and check if the number is even and output the result if the condition is truthy.

# Code
def even_numbers(num1, num2):
    for number in range(num1, num2 + 1):
        if number % 2 == 0:
            print(number)

even_numbers(1, 99)
