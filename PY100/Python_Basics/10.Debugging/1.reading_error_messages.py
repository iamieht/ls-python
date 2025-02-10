# What errors does it raise for the given examples and what exactly do the error messages mean?
def find_first_nonzero_among(numbers):
    for n in numbers:
        if n != 0:
            return n


find_first_nonzero_among(0, 0, 1, 0, 2, 0)
find_first_nonzero_among(1)

# TypeError: one argument is expected but 6 were given to the function. The function expects a list of elements and 6 integers were provided.
# The second function invocation (line 7) receives the correct number of arguments, so no error is raised on line 1. However, as soon as the program tries to evaluate line 2 with the given argument, it raises another TypeError: TypeError: 'int' object is not iterable
