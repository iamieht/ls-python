# Problem
# write an xor function that takes two arguments, and returns True if exactly one of its arguments is truthy, False otherwise.

# input:
#   - two arguments of any type
# output:
#   - True if exactly one of the argument is truthy / False otherwise.

# Examples / Test Cases
# print(xor(5, 0) == True)
# print(xor(False, True) == True)
# print(xor(1, 1) == False)
# print(xor(True, True) == False)

# Data Structure
# Any type and Boolean

# Algorithm
# 1. Create a function xor that takes two arguments of any type
#   - if arg1 and arg2 are truthy => False
#   - if arg1 and arg2 are falsy => False
#   - if arg1 == truthy and arg2 == falsy => True
#   - if arg2 == truthy and arg1 == falsy => True

# Code:
def xor(arg1, arg2):
    if arg1 and arg2:
        return False
    elif not arg1 and not arg2:
        return False
    elif arg1 and not arg2:
        return True
    else:
        return True

print(xor(5, 0) == True)
print(xor(False, True) == True)
print(xor(1, 1) == False)
print(xor(True, True) == False)
print(xor(False, False) == False)