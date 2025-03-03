# What will the following code print and why?
num = 5

def my_func():
    print(num)

my_func()

# Output is 5.
# Variables initialized in the global scope are accesible anywhere in our programs, so on line 5, the print function is able to access the value referenced by global variable num and output its value to the terminal.

# LS Solution:
# This prints 5. The variable num initialized to 5 on line 1 is accessible within the scope of the my_func function. When that function is invoked, 5 is printed.
