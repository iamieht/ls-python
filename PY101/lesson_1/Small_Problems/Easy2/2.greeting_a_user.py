# Write a program that asks for user's name, then greets the user. If the user appends a ! to their name, the computer will yell the greeting (print it using all uppercase).

# input:
#   - a String: user's name with a ! as optional character
# output:
#   - a String: a greeting

# Examples / Test Cases
# What is your name? Sue
# Hello Sue.

# What is your name? Bob!
# HELLO BOB! WHY ARE WE YELLING?

# Data Structures
# - Strings

# Algorithm
# 1. Create a function get_user_name(prompt)
#   2. returns input(prompt)
# 3. Create a function greeting(user_name)
#   4. Check input is not empty
#   5. Check the last character of the user_name.
#   6. If last char is "!": print(f"HELLO {user_name.upper()} WHY ARE WE YELLING?")
#   7. else: print(f"Hello {user_name[1:-1]}")
#

# Code
def get_user_name(prompt):
    return input(prompt)


def is_valid_user_name(user_name):
    return len(user_name) > 0


def greeting(user_name):
    if not is_valid_user_name(user_name):
        print("Invalid Input")
        exit

    if user_name[-1] == "!":
        print(f"HELLO {user_name.upper()} WHY ARE WE YELLING?")
    else:
        print(f"Hello {user_name}")


def main():
    user_name = get_user_name("What is your name? ")
    greeting(user_name)


main()
