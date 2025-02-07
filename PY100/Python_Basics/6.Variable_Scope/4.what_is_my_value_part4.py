# What will the following code do and why? Don't run it until you have tried to answer.
a = 1


def my_function():
    print(a)


my_function()
# The variable a is initialized at the top level of our code and is initialized with the value 1. This makes it globally accessible throughout the code, including within the body of the my_function. When we invoke my_function, it prints the value of the global variable a, which is 1.
