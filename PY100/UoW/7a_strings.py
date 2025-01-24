# Write a program which reads a string using input(), and outputs the same string but with the first and last character deleted. (You may assume the input string has length at least 2.) For example, on input Fairy a correct program will print air.
inputStr = input()
print(inputStr[1:-1])

# Write a program which reads a string using input(), and outputs the same string but with the first and last character exchanged. (You may assume the input string has length at least 2.) For example, on input Fairy a correct program will print yairF. Hint: use your solution to the previous program as part of the answer.
inputStr = input()
print(inputStr[-1] + inputStr[1:-1] + inputStr[0])

# Write a program that takes a character as input (a string of length 1), which you should assume is an upper-case character; the output should be the next character in the alphabet. If the input is 'Z', your output should be 'A'.
letter = input()

if letter == "Z":
    print("A")
else:
    print(chr(ord(letter) + 1))
