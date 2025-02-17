# Problem
# Build a program that randomly generates and prints Teddy's age. To get the age, you should generate a random number between 20 and 100, inclusive.

# input
#   - random number between 20 and 100
# output
#   - integer between 20 and 100

# Examples / Test Cases
# Teddy is 69 years old!

# Data Structures
# - Int

# Algorithm
# 1. import random module
# 2. print(f"Teddy is random.rand(20, 101)"")

# Code
import random

# print(f"Teddy is {random.randint(20, 100)} years old!")

# Further exploration
def get_name(prompt):
    return input(prompt)

name = get_name("What is your name? ")
age = random.randint(1, 100)

if name:
    print(f"{name} is {age} years old!")
else:
    print(f"Teddy is {age} years old!")