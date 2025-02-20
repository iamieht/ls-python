# New features
# Ask the user for another calculation
# Extracting messages in the program to a configuration file.
# Internationalization
import os
import json

LANG = 'en'

# Load the messages from the JSON file
with open('calculator_messages.json', 'r') as file:
    MESSAGES = json.load(file)

def prompt(message_key):
    message = messages(message_key, LANG)
    print(f'==> {message}')

def messages(message, lang='en'):
    return MESSAGES[lang][message]


def invalid_number(number_str):
    try:
        int(number_str)
    except ValueError:
        return True

    return False


prompt('welcome')
print()

while True:
    prompt('number1')
    number1 = input()

    while invalid_number(number1):
        prompt('invalid_number')
        number1 = input()

    prompt('number2')
    number2 = input()

    while invalid_number(number2):
        prompt('invalid_number')
        number2 = input()

    prompt('operation')

    operation = input()

    while operation not in ['1', '2', '3', '4']:
        prompt('invalid_operation')
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

    prompt('result') 
    print(f"{output}")
    print()
    prompt('calculation')
    another_calculation = input()

    if another_calculation == 'n' or another_calculation == 'N':
        break
    else:
        os.system('clear')

