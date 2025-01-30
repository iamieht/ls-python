# In the code shown below, identify all of the function names and parameters present in the code. Include the line numbers for each item identified.

def multiply(left, right):
    return left * right

def get_num(prompt):
    return float(input(prompt))

first_number = get_num('Enter the first number: ')
second_number = get_num('Enter the second number: ')
product = multiply(first_number, second_number)
print(f'{first_number} * {second_number} = {product}')

# Function names:
# multiply: defined on line 1, used on line 9.
# get_num: defined on line 4, used on lines 7 and 8.
# float: built-in function used on line 5.
# input: built-in function used on line 5.
# print: built-in function used on line 10.

# Parameters:
# left and right are defined on line 1 and then used on line 2.
# prompt is defined on line 4 and then used on line 5.