# What will the following code do and why? Don't run it until you have tried to answer.
b = [1, 2, 3]


def my_function():
    b[0] = 10


my_function()
print(b)

# This example shows how lists, being mutable objects, can be modified within a function, affecting the original list in the global scope.

# The list b is initialized on line 1 outside the function my_function. Inside the function, on line 4, the first element of b is changed to 10. Since b is not a local variable within my_function() but we are directly referencing b from the global scope, the change b[0] = 10 impacts the global variable b. Consequently, after the execution of my_function(), the global list b reflects this modification, and printing b will display [10, 2, 3].
