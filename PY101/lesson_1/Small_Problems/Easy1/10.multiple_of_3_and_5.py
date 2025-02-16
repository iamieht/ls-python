# Problem
# Write a function that computes the sum of all numbers between 1 and some other number, inclusive, that are multiples of 3 or 5. For instance, if the supplied number is 20, the result should be 98 (3 + 5 + 6 + 9 + 10 + 12 + 15 + 18 + 20).

# input:
# - integer > 1
# output:
# - integer

# Rules:
# numbers must be unique. So if a number is multiple of 3 and 5 is considered only once.

# Examples / Test Cases
# These examples should all print True
# print(multisum(3) == 3)
# print(multisum(5) == 8)
# print(multisum(10) == 33)
# print(multisum(1000) == 234168)

# Data Structure
# - integer
# - range
# - set

# Algorithm
# 1. Create a function multisum that takes a single argument of type integer
# 2. Initialize an empty list to store the multiples
# 3. Loop over the range from 1 until integer (inclusive)
# 4. Check if the number is multiple of 3 and add it to the list
# 5. Check if the number is multiple of 5 and add it to the list
# 6. return the sum of the elements of the list

# Code
def multisum(integer):
    numbers = []

    for num in range(1, integer + 1):
        if num % 3 == 0 or num % 5 == 0:
            numbers.append(num)

    return sum(numbers)

# These examples should all print True
print(multisum(3) == 3)
print(multisum(5) == 8)
print(multisum(10) == 33)
print(multisum(20) == 98)
print(multisum(1000) == 234168)