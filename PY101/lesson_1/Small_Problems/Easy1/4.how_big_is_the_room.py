# Problem
# Build a program that asks the user to enter the length and width of a room, in meters, then prints the room's area in both square meters and square feet.
# input
#   - a String that represents length in meters
#   - a String that represents width in meters
# output
#   - the area (length * width) in meters
#   - the area in square feet. 1 square meter = 10.7639 square feet

# Examples / Test Cases
# area(15, 10) = The area of the room is 150 square meters (1614.585 square feet)
# area(4, 3) = The area of the room is 12 square meters (129.17 square feet)

# Data Structures
# - a String for the input
# - a Float for the output

# Algorithm
# 0. Initialize a constant SQUARE_FEET = 10.7639
# 1. Create a function area that takes two arguments: length and width that returns length * width
# 2. Create a function area_in_sqf(area_in_meters) and returns area_in_meters * SQUARE_FEET
# 3. Create a function get_input(message) that returns the user input.
# 4. Create a main function:
#   - length = float(get_input('Please enter the length of the room in meters'))
#   - width = float(get_input('Please enter the width of the room in meters'))
#   - area_sqm = area(length, width)
#   - area_sqf = area_in_sqf(square_meters)
#   - print(f'The area of the room is {area_sqm} square meters ({area_sqf} square feet.)')

# Code
SQUARE_METERS2FEET = 10.7639

def area(length, width):
    return length * width

def area_in_sqf(area_in_meters):
    return round(area_in_meters * SQUARE_METERS2FEET, 2)

def get_input(message):
     return input(message)

def main():
    length = float(get_input('Please enter the length of the room in meters: '))
    width = float(get_input('Please enter the width of the room in meters: '))
    area_sqm = area(length, width)
    area_sqf = area_in_sqf(area_sqm)

    print(f'The area of the room is {area_sqm} square meters ({area_sqf} square feet).')

main()
