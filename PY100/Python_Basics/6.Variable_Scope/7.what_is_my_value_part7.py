# What will the following code do and why? Don't run it until you have tried to answer.
a = 1


def my_function():
    global a
    a = 2


my_function()
print(a)  # 2

# In this code, the global keyword tells the function to assume that a refers to the global variable a. This means that any operation on the variable a inside this function will affect the global variable a, not a local one.

# Initially, the global a is assigned the value 1. When my_function is called, it reassigns the global a to 2. So, after the function call, the value of the global a has been changed to 2.

# Thus, when we call print(a) after invoking my_function, it prints 2
