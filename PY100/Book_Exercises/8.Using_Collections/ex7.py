# Write Python code to replace all the : characters in the string below with +.
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# Option 1
new_info = ''
for char in info:
    if char == ':':
        new_info += '+'
    else:
        new_info += char

print(new_info)

# Option 2
new_info2 = '+'.join(info.split(':'))
print(new_info2)

# Option 3
new_info3 = info.replace(':', '+')
print(new_info3)
