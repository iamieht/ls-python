# Without running the following code, what do you think it will do?
def foo(first, second=3, third=2):
    print(first)
    print(second)
    print(third)

foo() # raises an error as the function is invoked without arguments and the first parameter has no default value
