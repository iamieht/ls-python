# New features
# Ask the user for another calculation
# Extracting messages in the program to a configuration file.
import os
import json

# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message):
    print(f'==> {message}')


def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False


prompt(MESSAGES['welcome'])
print()

while True:
    prompt(MESSAGES['number1'])
    number1 = input()

    while invalid_number(number1):
        prompt(MESSAGES['invalid_number'])
        number1 = input()

    prompt(MESSAGES['number2'])
    number2 = input()

    while invalid_number(number2):
        prompt(MESSAGES['invalid_number'])
        number2 = input()

    prompt("What operation would you like to perform?\n"
        "1) Add 2) Subtract 3) Multiply 4) Divide")

    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt(MESSAGES['operation'])
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
    print()
    prompt(MESSAGES['calculation'])
    another_calculation = input()

    if another_calculation == 'n' or another_calculation == 'N':
        break
    else:
        os.system('clear')

