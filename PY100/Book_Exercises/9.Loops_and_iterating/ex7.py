# Write a find_integers function that returns a list of all the integers from my_tuple
# Option 1 (simple for loop)
def find_integers(tuple):
    integers = []
    for element in tuple:
        if type(element) is int:
            integers.append(element)

    return integers

# Option 2 (list comprehensions)


def find_integers2(things):
    return [element
            for element in things
            if type(element) is int]


my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

integers = find_integers(my_tuple)
integers2 = find_integers2(my_tuple)

print(integers)                    # [1, 3, -4]
print(integers2)                    # [1, 3, -4]
