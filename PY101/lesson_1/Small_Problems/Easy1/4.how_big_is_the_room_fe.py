# Problem
# Build a program that asks the user to enter the length and width of a room, and the measurement type (meters or feet), then prints the room's area in both measurements.
# input
#   - a String that represents length in meters
#   - a String that represents width in meters
#   - a String that represents the measurement unit (meters or feet)
# output
#   - the area (length * width) in the user specified unit
#   - the area in the second unit:
#       - 1 square meter = 10.7639 square feet
#       - 1 square feet = 0.092903 square meters

# Examples / Test Cases
# Unit: feet = area(12, 10) = The area of the room is 120 square feet (11.5 square meters)
# Unit: Meters = area(4, 3) The area of the room is 12 square meters (129.17 square feet)

# Data Structures
# - a String for the inputs
# - a Float for the outputs

# Algorithm
# 0. Initialize a constant SQUARE_METERS_2_FEET = 10.7639
# 0. Initialize a constant SQUARE_FEET_2_METERS = 0.092903
# 1. Create a function area that takes two arguments: length and width that returns length * width
# 2. Create a function area_in_sqf(area_in_meters) and returns area_in_meters * SQUARE_METERS_2_FEET
# 3. Create a function area_in_sqm(area_in_feet) and returns area_in_feet * SQUARE_FEET_2_METERS
# 4. Create a function get_input(message) that returns the user input.
# 5. Create a main function:
#   - uom = get_input('Please enter the unit of measurement you want to use: (meters (m)) or feet(f))): ')
#   - length = float(get_input(f'Please enter the length of the room in {uom}: '))
#   - width = float(get_input(f'Please enter the width of the room in {uom}: '))
#   - Check the uom: if m:
#       - area_sqm = area(length, width)
#       - area_sqf = area_in_sqf(square_meters)
#       - print(f'The area of the room is {area_sqm} square {uom} ({area_sqf} square feet.)')
#   - if f:
#       - area_sqf = area(lenght, width)
#       - area_sqm = area_in_sqm(area_sqf)
#       - print(f'The area of the room is {area_sqf} square {uom} ({area_sqm} square meters.)')

# Code
SQUARE_METERS_2_FEET = 10.7639
SQUARE_FEET_2_METERS = 0.092903

def area(length, width):
    return length * width

def area_in_sqf(area_in_meters):
    return round(area_in_meters * SQUARE_METERS_2_FEET, 2)

def area_in_sqm(area_in_feet):
    return round(area_in_feet * SQUARE_FEET_2_METERS, 2)

def get_input(message):
     return input(message)

def unit_translation(uom):
    match uom:
        case 'm' | 'meters':
            return 'meters'
        case 'f' | 'feet':
            return 'feet'
        case _:
            return 'Invalid Input'
    

def main():
    uom = get_input(
        'Please enter the unit of measurement you want to use: (m)eters or (f)eet: ').lower()
    
    length = float(get_input(
            f'Please enter the length of the room in {unit_translation(uom)}: '))
    
    width = float(get_input(
            f'Please enter the width of the room in {unit_translation(uom)}: '))

    if unit_translation(uom) == 'meters':
        area_sqm = area(length, width)
        area_sqf = area_in_sqf(area_sqm)
        print(
            f'The area of the room is {area_sqm} square meters ({area_sqf} square feet).')
    elif uom == 'f' or uom == 'feet':
        area_sqf = area(length, width)
        area_sqm = area_in_sqm(area_sqf)
        print(
            f'The area of the room is {area_sqf} square feet ({area_sqm} square meters).')
    else:
        print(
            'Error. Invalid input!. Please choose between m(meters) or f(feet).')

main()
