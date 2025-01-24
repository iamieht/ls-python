# Write a program which reads an integer from input using pancakes = int(input()). If pancakes is more than 3, print out Yum! and if pancakes is not more than 3, print out Still hungry! instead.
pancakes = int(input())

if pancakes > 3:
    print("Yum!")
else:
    print("Still hungry!")

# Write a program that reads an integer from input, then outputs one of the capitalized words Positive, Negative, or Zero according to whether the number is positive, negative, or zero.
x = int(input())

if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Zero")

# Write a program that reads an integer from input, representing someone's age. If the age is 18 or larger, print out You can vote. If the age is between 0 and 17 inclusive, print out Too young to vote. If the age is less than 0, print out You are a time traveller.
age = int(input())

if age > 17:
    print("You can vote")
elif age >= 0:
    print("Too young to vote")
else:
    print("You are a time traveller")
