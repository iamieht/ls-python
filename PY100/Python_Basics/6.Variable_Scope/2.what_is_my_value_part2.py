# What will the following code do and why? Don't run it until you have tried to answer.
x = 10


def my_function():
    x = x + 5
    print(x)


my_function()   # raises an UnboundLocalError: cannot access local variable x, as local variable x is not initialized before the re-assignment on line 5
