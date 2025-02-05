# Is there a method to reverse a string, for example turning 'hello' into 'olleh'?

# Option 1
string = 'hello'
print(''.join(list(reversed(string))))

# Option 2
string = 'hello'
string = list(string)
string.reverse()
print(''.join(string))

# Option 3
string = 'hello'
reversed_string = string[::-1]
print(reversed_string)
