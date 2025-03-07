# What do you expect to happen when the greeting variable is referenced in the last line of the code below?
if False:
    greeting = "hello world"

print(greeting)

# I would expect a NameError exception as the greeting variable is never initialized as the if condition always evaluates as falsy