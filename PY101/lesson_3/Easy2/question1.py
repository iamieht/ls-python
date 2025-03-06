# Write two distinct ways of reversing the list without mutating the original list.
numbers = [1, 2, 3, 4, 5]     # [5, 4, 3, 2, 1]

# Option 1
print(numbers[-1::-1])
print(numbers)

# Option 2
print(list(reversed(numbers)))
print(numbers)