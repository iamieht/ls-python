# What happens when you run the following program? Why do we get that result?

def set_foo():
    foo = 'bar'

set_foo()   # no output and None returned
print(foo)  # NameError as foo's scope is within the function and not accesible outside of it.

