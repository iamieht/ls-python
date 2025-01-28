# What happens when you run the following code? Why?

NAME = 'Victor'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

NAME = 'Nina'
print('Good Morning, ' + NAME)
print('Good Afternoon, ' + NAME)
print('Good Evening, ' + NAME)

# The program first greets Victor 3 times. It then greets Nina 3 times.Unfortunately, Python doesn't have real constants. There's no way to prevent the reassignment of NAME.