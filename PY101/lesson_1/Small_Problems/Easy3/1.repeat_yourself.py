# Problem
# Write a function that takes two arguments, a string and a positive integer, then prints the string as many times as the integer indicates.

# input
#   - string
#   - integer
# output
#   - string

# Examples / Test Cases
# repeat('Hello', 3)
# Hello
# Hello
# Hello

# Data Structure
#   - string
#   - integer

# Algorithm
# 1. Create a function repeat that takes 2 arguments: a string and an integer
# 2. loop integer times and output the string in a new line with each iteration

def repeat(string, repeat):
    for _ in range(repeat):
        print(string)

# def repeat(str, num):
#     print((str + '\n') * num) # This one adds an extra line at the end.


repeat('Hello', 3)
