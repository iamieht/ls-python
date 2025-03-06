# Write two different ways to remove all of the elements from the following list:
numbers = [1, 2, 3, 4]

# Option 1
numbers = []
print(numbers)

# Option 2
numbers = [1, 2, 3, 4]
del numbers[:]
print(numbers)

# Option 3
numbers = [1, 2, 3, 4]
numbers.clear()
print(numbers)

# Option 4
numbers = [1, 2, 3, 4]
while numbers:
   numbers.pop()
print(numbers)