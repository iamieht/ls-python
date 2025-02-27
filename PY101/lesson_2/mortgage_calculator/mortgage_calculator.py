import os
import json

# Constants
LANG = 'en'
MONTHS_IN_YEAR = 12

# Load the messages from the JSON file
with open('mortgage_messages.json', 'r') as file:
    MESSAGES = json.load(file)

### Helper Functions ####


def clear():
    os.system('clear')


def set_language(lang='en'):
    global LANG
    if lang == 's':
        LANG = 'es'
    else:
        LANG = 'en'


def messages(message, lang='en'):
    return MESSAGES[lang][message]


def prompt(key):
    message = messages(key, LANG)
    print(f'==> {message}')


def get_input(key):
    message = messages(key, LANG)
    return input(f"==> {message}")


def is_valid_int(number):
    try:
        int(number)
    except ValueError:
        return False

    # return number > 0
    return True


def is_valid_float(number):
    try:
        float(number)
    except ValueError:
        return False

    # return number > 0
    return True


def is_valid_number(number):
    return is_valid_int(number) or is_valid_float(number)


def is_valid_amount(number):
    return is_valid_number(number) and float(number) > 0


def is_valid_loan_term(number):
    return is_valid_number(number) and int(number) >= 0


def is_valid_apr(number):
    return is_valid_float(number) and 0 <= float(number) <= 100


def loan_term_months(loan_term):
    years = int(loan_term[0])
    months = int(loan_term[1])

    return (years * MONTHS_IN_YEAR) + months


def get_loan_amount():
    while True:
        loan_amount = get_input('input_loan')

        if is_valid_amount(loan_amount):
            return float(loan_amount)

        prompt('valid_amount')


def get_apr():
    while True:
        interest_rate = get_input('input_apr')

        if is_valid_number(interest_rate) and is_valid_apr(interest_rate):
            return float(interest_rate)

        prompt('valid_interest_rate')


def get_loan_term():
    while True:
        try:
            years, months = get_input('input_loan_term').split('/')
        except ValueError:
            prompt('valid_loan_term')
            continue

        if is_valid_loan_term(years) and is_valid_loan_term(months):
            return loan_term_months((years, months))

        prompt('valid_loan_term')


def calculate_mpr(apr):
    return apr / MONTHS_IN_YEAR


def calculate_monthly_payment(loan_amount, monthly_interest_rate, loan_term):
    if monthly_interest_rate > 0:
        return (loan_amount * (monthly_interest_rate /
                               (1 - (1 + monthly_interest_rate) **
                                (-loan_term))))
    else:
        return (loan_amount / loan_term)


def mortgage_calculator(interest_rate, loan_amount, loan_term):
    annual_interest_rate = interest_rate / 100
    monthly_interest_rate = calculate_mpr(annual_interest_rate)
    monthly_payment = calculate_monthly_payment(
        loan_amount, monthly_interest_rate, loan_term)
    total_payments = monthly_payment * loan_term
    total_interest = total_payments - loan_amount

    display_results(loan_amount, monthly_payment,
                    loan_term, interest_rate,
                    monthly_interest_rate, total_payments,
                    total_interest)


def display_results(loan_amount, monthly_payment,
                    loan_term, interest_rate,
                    monthly_interest_rate, total_payments,
                    total_interest):

    print()
    print(messages('results', LANG))
    print(f'''{messages("label_loan_amount", LANG).ljust(30)}'
          '= ${loan_amount: , .2f}''')
    print(f'''{messages("label_loan_term", LANG).ljust(30)}'
          '={loan_term}''')
    print(f'''{messages("label_apr", LANG).ljust(30)}'
          '= % {interest_rate}''')
    print(f'''{messages("label_mpr", LANG).ljust(30)}'
          '=% {monthly_interest_rate: .4f}''')
    print(f'''{messages("label_m_payment", LANG).ljust(30)}'
          '= ${monthly_payment: , .2f}''')
    print(f'''{messages("label_t_payments", LANG).ljust(30)}'
          '= ${total_payments: , .2f}''')
    print(f'''{messages("label_interests", LANG).ljust(30)}'
          '= ${total_interest: , .2f}''')
    print(messages('hr'))


def get_answer():
    def is_valid_answer(answer):
        valid_answers = ['y', 'yes', 'Y', 'YES', 'n', 'no', 'N', 'NO']
        return answer in valid_answers

    while True:
        answer = get_input('another_calculation')

        if is_valid_answer(answer):
            return answer
        else:
            prompt('valid_answer')


def another_calculation(answer):
    return answer == 'y' or answer == 'yes'


def get_language():
    while True:
        lang = get_input('input_language')

        if is_valid_language(lang):
            return lang.lower()

        prompt('valid_language')


def is_valid_language(lang):
    return lang in ['E', 'e', 'S', 's']


## Main function ##


def main():
    clear()
    prompt('welcome')
    print(messages('hr', LANG))
    print()

    while True:
        lang = get_language()
        set_language(lang)
        break

    while True:
        # User input
        loan_amount = get_loan_amount()
        loan_term = get_loan_term()
        interest_rate = get_apr()

        # Calculations
        mortgage_calculator(interest_rate, loan_amount, loan_term)

        # Ask for another calculation
        answer = get_answer()

        if not another_calculation(answer):
            break
        clear()

    prompt('goodbye')


main()
