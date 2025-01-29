# Without running the following code, what do you think it will do?
def foo(bar, qux):
    print(bar)
    print(qux)

foo(42, 3.141592, 2.718) # raises an error as 3 arguments were passed in but only 2 parameters are defined in the function.

