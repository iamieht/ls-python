# Problem
# Write a function that takes any year greater than 0 as input and returns True if the year is a leap year, or False if it is not.
# use the Julian calendar prior to 1752, and the Gregorian calendar starting in 1752.

# input
#   - integer > 0
# output
#   - Boolean

# Rules
# Julian calendar before 1752 (leap year every 4 years)
# Gregorian calendar from 1752
# f the year is divisible by 400, it is a leap year.
# If the year is divisible by 100 but not by 400, it is not a leap year.
# If the year is divisible by 4 but not by 100, it is a leap year.
# All other years are not leap years.

# Examples / Test Cases
# These examples should all print True
# print(is_leap_year(1) == False)
# print(is_leap_year(2) == False)
# print(is_leap_year(3) == False)
# print(is_leap_year(4) == True)
# print(is_leap_year(1000) == True)
# print(is_leap_year(1100) == True)
# print(is_leap_year(1200) == True)
# print(is_leap_year(1300) == True)
# print(is_leap_year(1751) == False)
# print(is_leap_year(1752) == True)
# print(is_leap_year(1753) == False)
# print(is_leap_year(1800) == False)
# print(is_leap_year(1900) == False)
# print(is_leap_year(2000) == True)
# print(is_leap_year(2023) == False)
# print(is_leap_year(2024) == True)
# print(is_leap_year(2025) == False)

# Data Structures
# - Integer
# - Boolean

# Algorithm
# 1. Create a function is_leap_year that takes a single argument of type integer
# 2. If the year is prior to 1752 follow the julian calendar rules
# 3. AFter 1752 use the Gregorian calendar rules
#   4. Check if integer % 400 == 0 => leap year
#   5. elif Check if integer % 100 == 0 => not a leap year
#   6. elif check integer % 4 == 0 => leap year
#   7. else not a leap year

# Code
def is_leap_year(year):
    if year <= 0:
        return "Year must be greater than 0"
    
    if year < 1752:
        return year % 4 == 0
    else:
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False
    
# These examples should all print True
print(is_leap_year(1) == False)
print(is_leap_year(2) == False)
print(is_leap_year(3) == False)
print(is_leap_year(4) == True)
print(is_leap_year(1000) == True)
print(is_leap_year(1100) == True)
print(is_leap_year(1200) == True)
print(is_leap_year(1300) == True)
print(is_leap_year(1751) == False)
print(is_leap_year(1752) == True)
print(is_leap_year(1753) == False)
print(is_leap_year(1800) == False)
print(is_leap_year(1900) == False)
print(is_leap_year(2000) == True)
print(is_leap_year(2023) == False)
print(is_leap_year(2024) == True)
print(is_leap_year(2025) == False)