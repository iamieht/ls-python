# Ask the user for the first number.
# Ask the user for the second number.
# Ask the user for an operation to perform.
# Perform the operation on the two numbers.
# Print the result to the terminal.
def prompt(message):
    print(f'==> {message}')


prompt("Welcome to Calculator!")

prompt("What's the first number?")
number1 = input()
prompt("What's the second number?")
number2 = input()

prompt("What operation would you like to perform?\n"
       "1) Add 2) Subtract 3) Multiply 4) Divide")

operation = input()

match operation:
    case '1':
        output = int(number1) + int(number2)
    case '2':
        output = int(number1) - int(number2)
    case '3':
        output = int(number1) * int(number2)
    case '4':
        output = int(number1) / int(number2)

prompt(f"The result is : {output}")
