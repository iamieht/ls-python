# How can you determine whether a given string ends with an exclamation mark (!)? Write some code that prints True or False depending on whether the string ends with an exclamation mark.
str1 = "Come over here!"  # True
str2 = "What's up, Doc?"  # False

# Option 1
print(str1.endswith('!'))
print(str2.endswith('!'))

# Option 2
print(str1[-1] == '!')
print(str2[-1] == '!')