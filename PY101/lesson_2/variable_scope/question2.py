# What will the following code print and why?
num = 5

def my_func():
    num = 10

my_func()
print(num)

# This code outputs 5
# On line 7, when invoking the function `mu_funct()` a local variable `num` is initialized to the integer value 10. This local variable is a different variable than `num` initialized in the global scope. So when invoking the print function on line 8, the value referenced by `num` is `5`.

# LS Solution
#$ This prints 5. The variable num initialized to 5 on line 1 and the variable num initialized on line 4 within the function my_func are two different variables. We can't reassign variable num initialized on line 1 within the function.