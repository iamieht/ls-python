# Assignment: Rock, Paper, Scissors, Lizard, Spock
# Author: Iván E. Hernández T.
# Launch School: PY101

# Game rules
# Scissors beats Paper, Lizard
# Paper beats Rock, Spock
# Rock beats Lizard, Scissors
# Lizard beats Spock, Paper
# Spock beats Scissors, Rock

import random
import json
import os

# CONSTANTS
# Load the messages from the JSON file
with open('rpsls.json', 'r') as file:
    MESSAGES = json.load(file)

LANG = 'en'

RPSLS_RULES = {
    'rock': ['lizard', 'scissors'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': [ 'spock', 'paper'],
    'spock': ['scissors', 'rock']    
}

VALID_CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock' ]
VALID_SHORT_CUTS = ['r', 'p', 's', 'l', 'sp']
WINS = 3

# Helper Functions
def clear():
    os.system('clear')

def messages(lang, msg_key):
    return MESSAGES[lang][msg_key]

def prompt(msg_key):
    message = messages(LANG, msg_key)
    print(f'==> {message}')

def get_user_input(msg_key):
    message = messages(LANG, msg_key)
    return input(f'==> {message}')

def get_player_choice():
    while True:
        choice = get_user_input('choice')

        if is_valid_choice(choice):
            return choice

        prompt('invalid_choice')

def get_computer_choice():
    return random.choice(VALID_CHOICES)

def is_valid_choice(choice):
    return choice in VALID_CHOICES or choice in VALID_SHORT_CUTS

def shortcut_to_choice(choice):
    match choice:
        case 'r':
            return VALID_CHOICES[0]
        case 'p':
            return VALID_CHOICES[1]
        case 's':
            return VALID_CHOICES[2]
        case 'l':
            return VALID_CHOICES[3]
        case 'sp':
            return VALID_CHOICES[4]
        case _:
            return choice

def display_choices(player, computer):
    print()
    print(f'You chose: {shortcut_to_choice(player)}'
          f' and Computer chose: {computer}')
    print()

def display_winner(player, computer):
    pass

def set_score(winner):
    pass

def display_score():
    pass

def rpsls():
    clear()
    prompt("welcome")

    player_choice = get_player_choice()
    computer_choice = get_computer_choice()

    display_choices(player_choice, computer_choice)

rpsls()

