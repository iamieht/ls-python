# The absolute value of a number is defined as follows. For a number x that is positive or zero, the absolute value of x is x. Otherwise, when x is a negative number, the absolute value of x is -x, or in other words the same as x but without the minus sign. For example the absolute value of 5 is 5, and the absolute value of -10 is 10. Using if and else, write a program that reads an integer as input, and prints its absolute value.

x = int(input())

if x >= 0:
    print(x)
else:
    print(-x)

# The words 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th are called ordinal adjectives. Write a program which reads an integer x between 1 and 9 from input. The program should output the ordinal adjective corresponding to x.

num = int(input())

if num == 1:
    print(str(num) + 'st')
elif num == 2:
    print(str(num) + 'nd')
elif num == 3:
    print(str(num) + 'rd')
else:
    print(str(num) + 'th')
