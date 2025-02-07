# What will the following code do and why? Don't run it until you have tried to answer.
a = 1


def my_function():
    print(a)
    a = 2


my_function()
# UnboundLocalError: local variable 'a' referenced before assignment
# Python detects that a is being assigned within the my_function function and therefore treats it as a local variable. However, since we are trying to print the local a variable's value before it has been assigned a value, we get an error.
