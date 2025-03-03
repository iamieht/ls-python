# What will the following code do?
def my_func():
    num = 10

my_func()
print(num)

# This code raises a NameError exception as the variable `num` is not accesible in the global scope, as the variable initialized within the function `my_funct()` is local to the function.

# LS Solution
# This code raises a NameError since the variable num is defined within the function my_func and is not accessible outside of its scope.