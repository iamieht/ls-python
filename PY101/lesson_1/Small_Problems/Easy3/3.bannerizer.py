# Problem
# Write a function that takes a short line of text and prints it within a box.

# Examples / Test Cases
# print_in_box('To boldly go where no one has gone before.')
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+
# print_in_box('')
# +--+
# |  |
# |  |
# |  |
# +--+

# Data Structures
# - string

# Algorithm
# 1. Create a function print_in_box that takes a string as an argument
# 2. Initialize a variable horizontal_line = (f"+-{len(str) * '-'}-+)
# 3. Initialize a variable vertical_line = (f"| {len(str) * ''} |)
# 4. Initialize a variable string_line = (f"| {string} |")
# 5. print(horizontal_line)
# 6. print(vertical_line)
# 7. print(string_line)
# 8. print(vertical_line)
# 9. print(horizontal_line)

# Code
def print_in_box(string):
    horizontal_line = (f"+-{len(string) * '-'}-+")
    vertical_line = (f"| {len(string) * ' '} |")
    string_line = (f"| {string} |")

    print(horizontal_line)
    print(vertical_line)
    print(string_line)
    print(vertical_line)
    print(horizontal_line)


print_in_box('')
print_in_box('To boldly go where no one has gone before.')
