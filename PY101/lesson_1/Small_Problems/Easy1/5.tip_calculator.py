# Problem
# Create a simple tip calculator. The program should prompt for a bill amount and a tip rate. The program must compute the tip, then print both the tip and the total amount of the bill. You can ignore input validation and assume that the user will enter valid numbers.
# input
#   - a String to represent the bill amount
#   - a String to represent the tip percentage
# output
#   - a String to represent the tip amount
#   - a String to represent the total amount

# Example / Test Cases
# What is the bill? 200
# What is the tip percentage? 20

# The tip is $40.00
# The total is $240.00

# Data Structure
# - String
# - Float

# Algorithm
# 1. Create a function get_input(message) to capture user input
# 2. Create a function calculate_tip(bill, tip%):
#   - return bill * (tip% / 100)
# 3. Create a main function:
#   - bill_amount = float(get_input('What is the bill? '))
#   - tip_percentage = float(get_input('What is the tip percentage? '))
#   - tip = calculate_tip(bill_amount, tip_percentage)
#   - print(f'The tip is ${tip}')
#   - print(f'The total is ${bill_amount + tip}')

# Code
def get_input(message):
    return input(message)

def calculate_tip(bill, tip_percentage):
    return bill * (tip_percentage / 100)

def main():
    bill_amount = float(get_input('What is the bill? '))
    tip_percentage = float(get_input('What is the tip percentage? '))
    tip = calculate_tip(bill_amount, tip_percentage)

    print(f'The tip is ${tip:.2f}')
    print(f'The total is ${bill_amount + tip:.2f}')

main()    
