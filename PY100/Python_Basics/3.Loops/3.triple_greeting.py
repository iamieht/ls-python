# Write a loop that prints the value of the greeting variable three times.
greeting = 'Aloha!'

counter = 3

print('while')
while counter > 0:
    print(greeting)
    counter -= 1

print()
print('for loop')
for _ in range(3):
    print(greeting)
