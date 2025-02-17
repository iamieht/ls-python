# Problem
# Build a program that displays when the user will retire and how many years she has to work till retirement.

# input
#   - age: a String
#   - retirement_age = a String
# output
#   - a String with current year and retirement year
#   - a String with future years of work

# Examples / Test Cases
# What is your age? 30
# At what age would you like to retire? 70

# It's 2024. You will retire in 2064.
# You have only 40 years of work to go!

# Data Structure
# - String

# Algorithm
# 1. import datetime module
# 2. Create a datetime object to calculate current year
# 3. Create a get_input(prompt) function
# 4. Ask for user's age = get_input("What is your age? ")
# 5. Ask for retirement_age = get_input("At what age would you like to retire? ")
# 6. Initialize a variable retirement_year = current_year + (retirement_age - current_age)
# 7. print(f"It's {current_year}. You will retire in {retirement_year}.")
# 8. print(f"You have only {retirement_age - current_age} years of work to go!"")

from datetime import datetime

def get_current_year():
    return datetime.now().year

def get_input(prompt):
    return input(prompt)

age = int(get_input("What is your age? "))
retirement_age = int(get_input("At what age would you like to retire? "))
current_year = get_current_year()
retirement_year = current_year + (retirement_age - age)

print()
print(f"It's {current_year}. You will retire in {retirement_year}.")
print(f"You have only {retirement_age - age} years of work to go!")

