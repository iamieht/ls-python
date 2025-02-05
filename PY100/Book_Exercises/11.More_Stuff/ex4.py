# Write a function called increment_counter that increments a counter variable every time it is called.
def increment_counter():
    global counter
    counter += 1


counter = 0
print(counter)                # 0

increment_counter()
print(counter)                # 1

increment_counter()
print(counter)                # 2

counter = 100
increment_counter()
print(counter)                # 101
