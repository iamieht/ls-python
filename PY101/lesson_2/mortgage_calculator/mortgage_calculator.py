# Problem
# build a mortgage calculator (or car payment calculator -- it's the same thing) that determines the monthly payment assuming that interest is compounded monthly.

# input
#   - loan amount
#   - APR = Annual Percentage Rate
#   - loan duration
# output
#   - Monthly payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-loan_duration_months)))
# calculate
#   - monthly_interest_rate (APR / 12)
#   - loan duration in months

# Examples / Test Cases
# print(is_valid_int(1))
# print(is_valid_int(-1))
# print(is_valid_int('abc'))

# Data Structures
# - float
# - strings

# Algorithm
# Create a .json file for the messages with internationalization support (en / es)
# Create a function prompt to define a user prompt
#   - use a message key to retrieve msg from .json file
# Create a function to capture user input
#   - get_input()
# Create a function to check user input (amounts)
#   - is_valid_amount()
# Create a function to check user input (APR)
#   - Ask for a %
#   - is_valid_apr()
# Create a function to check user input (loan duration)
#   - is_valid_loan()
# Create a function to calculate interest rate (monthly)
#   - calculate_interest_rate()
# Crete a function to calculate loan duration in months
#   - calculate_loan_duration()
# Create a function to calculate the mortgage (monthly payment)
#   - calculate_mortgage()
# Create a main function
#   - print Welcome Screen
#   - Ask for loan amount ($)
#   - Ask for loan term (Years / Months)
#   - Ask for Interest Rate (%)

# Code
import os
import json

LANG = 'en'

# Load the messages from the JSON file
with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)

### Helper Functions ####


def messages(message, lang='en'):
    return MESSAGES[lang][message]


def prompt(key):
    message = messages(key, LANG)
    print(f'==> {message}')


def get_input(key, symbol):
    message = messages(key, LANG)
    return input(f"==> {message} {symbol}")


def is_valid_int(number):
    try:
        number = int(number)
    except ValueError:
        return False

    return number > 0


def is_valid_float(float):
    try:
        number = float(number)
    except ValueError:
        return False

    return number > 0


def is_valid_number(number):
    return is_valid_int or is_valid_float


def main():
    prompt('welcome')
    # prompt('input_loan')
    loan_amount = get_input('input_loan', '$')
    print(loan_amount)


# main()
