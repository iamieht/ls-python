# What will the following code print and why?
def my_func():
    x = 15

    def inner_func1():
        x = 25
        print("Inner 1:", x)

    def inner_func2():
        print("Inner 2:", x)

    inner_func1()
    inner_func2()

my_func()

# Outputs: Inner 1: 25 and Inner 2: 15
# On line 15 the function `my_funct()` is invoked. Within the function a local variable `x` is initialized to the integer value `15`. Within the function, on line 12, the function `inner_funct1()` is invoked, which initializes a local variable `x` to the integer `25`. On line 7, the print function outputs 'Inner 1: 25 as the value referenced by local variable `x` is 25. On line 13, the function `inner_func2` is invoked, which outputs the string `Inner 2: 15`, as the value referenced by `x` is the one referenced on line 3.

# LS Solution
# Inside my_func, a local variable x is initialized to 15. When inner_func1 is called, it defines its own local variable x with a value of 25 and prints "Inner 1: 25". However, when inner_func2 is called, it doesn't have access to the variable x from the inner_func1 as it is in its peer scope but accesses variable x defined in the scope of my_func.