# Problem
# Write a function that returns a list that contains every other element of a list that is passed in as an argument. The values in the returned list should be those values that are in the 1st, 3rd, 5th, and so on elements of the argument list.

# input:
#   - list
# output
# - list

# Examples / Test Cases
# print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
# print(oddities([1, 2, 3, 4]) == [1, 3])        # True
# print(oddities(["abc", "def"]) == ['abc'])     # True
# print(oddities([123]) == [123])                # True
# print(oddities([]) == [])                      # True

# Data Structures
# - list

# Algorithm
# 1. Create a function oddities that takes a list as an argument
#   - initialize an empty list
#   - loop over the len of the list and append each element on an odd index  to the empty list

# Code
def oddities(a_list):
    result = []
    for idx in range(0, len(a_list), 2):
        result.append(a_list[idx])

    return result

def oddities2(a_list):
    return a_list[::2]

def evens(a_list):
    return a_list[1::2]

print(oddities([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities([1, 2, 3, 4]) == [1, 3])        # True
print(oddities(["abc", "def"]) == ['abc'])     # True
print(oddities([123]) == [123])                # True
print(oddities([]) == [])                      # True

print(oddities2([2, 3, 4, 5, 6]) == [2, 4, 6])  # True
print(oddities2([1, 2, 3, 4]) == [1, 3])        # True
print(oddities2(["abc", "def"]) == ['abc'])     # True
print(oddities2([123]) == [123])                # True
print(oddities2([]) == [])                      # True

print(evens([2, 3, 4, 5, 6]) == [3, 5])
print(evens([1, 2, 3, 4]) == [2, 4])
print(evens(["abc", "def"]) == ['def'])
print(evens([123]) == [])
print(evens([]) == []) 