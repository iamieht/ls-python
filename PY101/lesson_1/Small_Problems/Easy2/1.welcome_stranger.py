# Problem
# Create a function that takes 2 arguments, a list and a dictionary. The list will contain 2 or more elements that, when joined with spaces, will produce a person's name. The dictionary will contain two keys, "title" and "occupation", and the appropriate values. Your function should return a greeting that uses the person's full name, and mentions the person's title.

# input:
#   - list with 2 or more elements that represents a person's name.
#   - dictionary: 2 keys: title and occupation
# output:
#   - a String that represents a person's full name and the person's title.

# Example / Test Cases
# greeting = greetings(
#     ["John", "Q", "Doe"],
#     {"title": "Master", "occupation": "Plumber"},
# )
# print(greeting)
# Hello, John Q Doe! Nice to have a Master Plumber around.

# Data Structures:
# - a list with 2 or more elements
# - a dictionary with 2 keys: title and occupation

# Algorithm
# 1. Create a function greetings that takes 2 arguments, a list and a dictionary
# 2. Initialize a variable full_name with the join elements of the list.
# 3. return a string: Hello, {full_name}! Nice to have a {dict['title]} {dict['occupation']} around.

# Code
def greetings(a_list, a_dict):
    full_name = ' '.join(a_list)
    return (f'Hello, {full_name}! Nice to have a '
            f'{a_dict["title"]} {a_dict["occupation"]} '
            'around.')


greeting = greetings(
    ["John", "Q", "Doe"],
    {"title": "Master", "occupation": "Plumber"},
)
print(greeting)
