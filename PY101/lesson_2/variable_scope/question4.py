# What will the following code print and why?
def outer():
    outer_var = 'Hello'

    def inner():
        inner_var = 'World'
        print(outer_var, inner_var)

    inner()

outer()

# Ouputs 'Hello World'
# On line 11, we invoke the function `outer()`. Within the function a local variable `outer_var` is initialized to the String object with value `Hello`. On line 9, whithin the function, the function `inner()` is invoked, which initializes a local variable `inner_var` to the String object with value `World`. On line 7, the print function outputs the values of the variables `outer_var` and `inner_var`. Both variables are accessible from within the function `inner()`

# LS Solution
# This prints Hello World. The outer() function defines a local variable outer_var with the value 'Hello'. Inside it, the inner() function is defined, which has its own local variable inner_var with the value 'World'. When inner() is called within outer(), both outer_var and inner_var are printed using print(outer_var, inner_var), which outputs Hello World.