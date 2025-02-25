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

# Constants
LANG = 'en'
MONTHS_IN_YEAR = 12

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


def is_valid_float(number):
    try:
        number = float(number)
    except ValueError:
        return False

    return number > 0


def is_valid_number(number):
    return is_valid_int(number) or is_valid_float(number)


def is_valid_apr(number):
    return is_valid_float(number) and float(number) <= 100


def loan_term_months(loan_term):
    years = int(loan_term[0])
    months = int(loan_term[1])

    return (years * MONTHS_IN_YEAR) + months


def get_loan_amount():
    while True:
        loan_amount = get_input('input_loan', '$')

        if is_valid_number(loan_amount):
            return float(loan_amount)
        else:
            prompt('valid_number')


def get_apr():
    while True:
        interest_rate = get_input('input_apr', '%')

        if is_valid_number(interest_rate) and is_valid_apr(interest_rate):
            return float(interest_rate)
        else:
            prompt('valid_interest_rate')


def get_loan_term():
    while True:
        try:
            years, months = get_input('input_loan_term', '⌛').split('/')
        except ValueError:
            prompt('valid_loan_term')
            continue

        if is_valid_number(years) and is_valid_number(months):
            return loan_term_months((years, months))
        else:
            prompt('valid_loan_term')


def calculate_mpr(apr):
    return apr / MONTHS_IN_YEAR


def mortgage_calculator(loan_amount, monthly_interest_rate, loan_term):
    return (loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate)**(-loan_term))))

## Main function ##


def main():
    prompt('welcome')

    # User input
    loan_amount = get_loan_amount()
    loan_term = get_loan_term()
    interest_rate = get_apr()

    # Calculations
    annual_interest_rate = interest_rate / 100
    monthly_interest_rate = calculate_mpr(annual_interest_rate)
    monthly_payment = mortgage_calculator(
        loan_amount, monthly_interest_rate, loan_term)
    total_payments = monthly_payment * loan_term
    total_interest = total_payments - loan_amount

    # Output Results
    print(f'Loan Amount = {loan_amount}')
    print(f'Payment Every Month = {monthly_payment}')
    print(f'Total of {loan_term} payments = {total_payments}')
    print(f'Total interest = {total_interest}')


main()
