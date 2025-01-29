# Write a program that uses a multiply function to multiply two numbers and returns the result. Ask the user to enter the two numbers, then output the numbers and result as a simple equation.

def multiply(num1, num2):
    return num1 * num2

num1 = float(input('Enter the first number: '))
num2 = float(input('Enter the second number: '))

result = multiply(num1, num2)
print(f'{num1} * {num2} = {result}')