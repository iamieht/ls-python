# Problem
# Print all odd numbers from a range of 2 numbers , last one inclusive, with each number on a separate line.
# input:
#   2 integer numbers
# output:
#   all odd numbers from 1 to 99

# Example (Test Case)
# odd_numbers(1, 99) # 1, 3, 5, 7, 9......99

# Data Structure
# integer

# Algorithm
# 1. Define a function odd_numbers that takes two integer numbers. The start and end (inclusive).
# 2. Iterate over the range function from number 1 to number 2, and check if the number is odd and output the result if the condition is truthy.

# Code
def odd_numbers(num1, num2):
    for num in range(num1, num2 + 1):
        if num % 2 != 0:
            print(num)


odd_numbers(1, 99)