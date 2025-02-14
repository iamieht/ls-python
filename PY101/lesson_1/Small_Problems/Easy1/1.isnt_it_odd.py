# Problem
# Write a function that takes one integer argument and returns True when the number's absolute value is odd, False otherwise.
# inputs:
#   integer
# output:
#   bool (true of false)

# Examples / Test Cases
# isnt_it_odd(2)    # False
# isnt_it_odd(3)    # True
# isnt_it_odd(-9)   # True
# isnt_it_odd(0)    # False

# Data Structure
# - primitives int and bool

# Algorithm
# 1. Define a function isnt_it_odd with a single argument of type integer
# 2. Convert the integer into its absolute value
# 3. Check if the absolute value is divisible by 2 without a remainder and return the boolean.

# Code
def isnt_it_odd(number):
    return abs(number) % 2 == 1

# Test Cases
print(isnt_it_odd(2) == False)
print(isnt_it_odd(3) == True)
print(isnt_it_odd(-9) == True)
print(isnt_it_odd(0) == False)