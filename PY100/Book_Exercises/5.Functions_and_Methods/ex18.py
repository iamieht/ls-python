# Use this function to determine which of the following lists contains at least one number that is not evenly divisible by 3 (that is, the remainder is not 0):

def remainders_3(numbers):
    return [number % 3 for number in numbers]

numbers_1 = [0, 1, 2, 3, 4, 5, 6]
numbers_2 = [1, 2, 4, 5]
numbers_3 = [0, 3, 6]
numbers_4 = []

print(f'List {numbers_1} contains at least one number that is not divisible by 3: {any(remainders_3(numbers_1))}')
print(f'List {numbers_2} contains at least one number that is not divisible by 3: {any(remainders_3(numbers_2))}')
print(f'List {numbers_3} contains at least one number that is not divisible by 3: {any(remainders_3(numbers_3))}')
print(f'List {numbers_4} contains at least one number that is not divisible by 3: {any(remainders_3(numbers_4))}')