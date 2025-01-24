# Ex1: Write a program that prints out the maximum weight that can be transported along this road. Your code should assume that the variables a, b, and c already contain the bridge weight limits.
a = 187
b = 277
c = 379
print(min(a, b, c))

# Ex2: Write a program that prints out the maximum weight that can be transported between the two cities. Assume that the variables a, b, c, d, and e contain the bridge weight limits.
a = 127
b = 221
c = 338
d = 64
e = 78
print(max(min(a, b, c), min(d, e)))
