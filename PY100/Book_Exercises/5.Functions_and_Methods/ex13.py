# Without running the following code, what do you think it will do?
def foo(first, second=3, third):
    print(first)
    print(second)
    print(third)

foo(42) # raises an error as an argument is missing. Once Python sees a positional parameter with a default value, all subsequent parameters must have default values.

