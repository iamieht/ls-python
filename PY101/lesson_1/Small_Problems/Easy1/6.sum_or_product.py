# Problem
# Write a program that asks the user to enter an integer greater than 0, then asks whether the user wants to determine the sum or the product of all numbers between 1 and the entered integer, inclusive.
# input
#   - integer > 0
#   - a String 's' to compute sum or a String 'p' to compute the product
# output
#   - The sum of the integers between 1 and input integer is another integer
#   - The product of the integers between 1 and input integer is another integer.

# Examples / Test Cases
# Please enter an integer greater than 0: 5
# Enter "s" to compute the sum, or "p" to compute the product. s

# The sum of the integers between 1 and 5 is 15.

# Please enter an integer greater than 0: 6
# Enter "s" to compute the sum, or "p" to compute the product. p

# The product of the integers between 1 and 6 is 720.

# Data Structures
# - String
# - Integer

# Algorithm
# 1. Create a function get_input(prompt)
# 2. Create a function to validate the input integer. is_valid_integer(input):
#   - return int(input) > 0
# 3. Create a function to valid input for s or p. is_valid_operation(input):
#   - return input == 's' or input == 'p'
# 4. Create a function compute_sum(integer):
#   - return sum(list(range(integer + 1)))
# 5. Create a function compute_product(integer)
#   - list_int = list(range(1, integer + 1))
#   - loop over the list and multiply each element
# 6. Create a main function:
#   while True:
#   - int = get_input('Please enter an integer greater than 0: ')
#   - if is_valid_integer(int):
#   - operation = get_input('Enter "s" to compute the sum, or "p" to compute the product. ')
#   - if is_valid_operation(operation):
#   - if operation == 's':
#       - result = compute_sum(int)
#   - else:
#       - result = compute_product(int)
#   - if input is invalid break
#   - print('The {operation} of the integers between 1 and {int} is {result})

# Code
def get_input(prompt):
    return input(prompt)

def is_valid_integer(integer):
    return int(integer) > 0

def is_valid_operation(input):
    return input == 's' or input == 'p'

def compute_sum(integer):
    return sum(list(range(integer + 1)))

def compute_product(integer):
    product = 1
    for num in range(1, integer + 1):
        product *= num

    return product

def main():
    while True:
        integer = get_input('Please enter an integer greater than 0: ')
        if is_valid_integer(integer):
            break
    
    while True:
        operation = get_input('Enter "s" to compute the sum, or "p" to compute the product. ')
        if is_valid_operation(operation):
            break

    if operation == 's':
        result = compute_sum(int(integer))
        print(f'The sum of the integers between 1 and {integer} is {result}.')
    else:
        result = compute_product(int(integer))
        print(f'The product of the integers between 1 and {integer} is {result}.')

main()