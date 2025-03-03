# What will the following code print and why?
num = 5

def my_func():
    global num
    num = 10

my_func()
print(num)

# Outputs 10
# The global variable `num` is initialized on line 1 to the integer `5`. On line 8, we invoke the function `my_func()` which reassigns the global variable `num` to the integer `10` as the global keyword with the variable `num` is used, making it accessible within the function. On line 9 the print function outputs the value of `num` which is `10`.

# LS Solution
# This prints 10. The variable num is initialized to 5 on line 1. On line 4 we use global keyword inside the function to reference the global variable num initialized on line 1. For that reason, on line 5 we are reassigning global variable num to 10 and on line 8 printing that value.

