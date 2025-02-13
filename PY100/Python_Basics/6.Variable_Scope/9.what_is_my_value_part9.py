# What will the following code do and why? Don't run it until you have tried to answer.
a = 7


def my_function(b):
    b += 10


my_function(a)
print(a)  # 7
# In Python, integers are immutable, which means their values cannot be changed. When the my_function function is called with a as an argument, the local variable b within the function scope is set to reference the same value as a, which is 7. During the execution of the += operation inside the my_function function, b += 10 effectively becomes b = b + 10. This operation creates a new integer object 17 and updates b to reference this new object. However, the original variable a remains unaffected and retains its value of 7.
