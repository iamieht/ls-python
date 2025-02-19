# Problem
# Write a function that takes a year as input and returns the century.

# The return value should be a string that begins with the century number, and ends with 'st', 'nd', 'rd', or 'th' as appropriate for that number.
# New centuries begin in years that end with 01. So, the years 1901 - 2000 comprise the 20th century.

# input
#   - positive integer
# output
#   - string: {century_number}{sufix}
# where {sufix} is one of: th, st, nd, rd

# Examples / Test Cases
# print(century(2000) == "20th")          # True
# print(century(2001) == "21st")          # True
# print(century(1965) == "20th")          # True
# print(century(256) == "3rd")            # True
# print(century(5) == "1st")              # True
# print(century(10103) == "102nd")        # True
# print(century(1052) == "11th")          # True
# print(century(1127) == "12th")          # True
# print(century(11201) == "113th")        # True

# Data Structures
# - String

# Algorithm
# 1. Create a helper function get_century_sufix(year)
#   -
# 2. Create a function get_century(year):
#   - if year % 100 != 0 => return (year // 100) + 1
#   - else: return year // 100


# Code
def get_century(year):
    if year % 100 != 0:
        return (year // 100) + 1
    else:
        return year // 100


def get_century_sufix(century):
    last_two = century % 100
    last_digit = century % 10

    match last_two:
        case 11 | 12 | 13:
            return 'th'

    match last_digit:
        case 1:
            return 'st'
        case 2:
            return 'nd'
        case 3:
            return 'rd'
        case _:
            return 'th'


def century(year):
    century = get_century(year)
    sufix = get_century_sufix(century)
    return f"{century}{sufix}"


print(century(2000) == "20th")          # True
print(century(2001) == "21st")          # True
print(century(1965) == "20th")          # True
print(century(256) == "3rd")            # True
print(century(5) == "1st")              # True
print(century(10103) == "102nd")        # True
print(century(1052) == "11th")          # True
print(century(1127) == "12th")          # True
print(century(11201) == "113th")        # True
