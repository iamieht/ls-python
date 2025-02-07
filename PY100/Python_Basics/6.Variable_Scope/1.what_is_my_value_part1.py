# What will the following code do and why? Don't run it until you have tried to answer.
if True:
    my_value = 20

# 20 because the if block doesn't create a local scope, so the variable my_value is accessible by the print function.
print(my_value)

# In Python, variables initialized inside an if, match, while, for, with, or try statement are accessible outside of that block of code. Thus, the variable my_value initialized inside the if block on line 2 can be accessed and printed on line 4. The output of the print(my_value) statement is 20.

# What do you think will happen if we run the following code instead:
if False:
    my_new_value = 42

# a NameError is raised as the variable my_new_value is not initialized as the block code is never executed.
# print(my_new_value)
