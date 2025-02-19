# Problem
# Write a function that takes a positive integer, n, as an argument and prints a right triangle whose sides each have n stars. The hypotenuse of the triangle (the diagonal side in the images below) should have one end at the lower-left of the triangle, and the other end at the upper-right.

# input:
#   - positive integer
# output
#   - string representing a right triangle

# Examples/Test Cases
# triangle(5)
#     *
#    **
#   ***
#  ****
# *****
# triangle(9)
#         *
#        **
#       ***
#      ****
#     *****
#    ******
#   *******
#  ********
# *********

# Data Structures
# - string

# Algorithm
# 1. Create a function triangle(integer)
# 2. loop integer times starting with 1 until integer + 1:
#   - print(f'{integer - iter} * " "{iter * "*"}')

# Code
def triangle(integer):
    for i in range(1, integer + 1):
        print(f"{(integer - i) * ' '}{i * '*'}")


triangle(5)
triangle(9)
