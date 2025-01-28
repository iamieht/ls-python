# extract the individual digits of 4936:

# One place is 6.
# Tens place is 3.
# Hundreds place is 9.
# Thousands place is 4.

number = 4936
one_place = number % 10
number = number // 10
tens_place = number % 10
number = number // 10
hundreds_place = number % 10
thousands_place = number // 10


print(f'One place is {one_place}')
print(f'Tens place is {tens_place}')
print(f'Hundreds place is {hundreds_place}')
print(f'Thousands place is {thousands_place}')
