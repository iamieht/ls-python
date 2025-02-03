# Use slicing to write Python code to print a 6-character substring of 'Launch School' that begins with the first c.
string = 'Launch School'
substring = string[string.find('c'): string.find('c') + 6]
print(substring)

print(string[4:10])
