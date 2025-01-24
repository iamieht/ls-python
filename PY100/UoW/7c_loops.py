# Modify the example above to give a program where we count up starting from 1 and going up until 10, and then print Blastoff!

counter = 1
while counter < 11:
    print(counter)
    counter += 1
print("Blastoff!")

# Ex1: The square numbers are the integers of the form K × K, e.g. 9 is a square number since 3 × 3 = 9. Write a program that reads an integer n from input and outputs all the positive square numbers less than n, one per line in increasing order. For example, if the input is 16, then the correct output would be
# 1
# 4
# 9

n = int(input())

for num in range(1, n):
    if num * num < n:
        print(num * num)
