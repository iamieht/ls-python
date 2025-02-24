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


def prompt(key):
    message = messages(key, LANG)
    print(f'==> {message}')


def messages(message, lang='en'):
    return MESSAGES[lang][message]


def main():
    prompt('welcome')


main()
