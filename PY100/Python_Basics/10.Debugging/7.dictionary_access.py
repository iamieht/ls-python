# You are trying to access a value in a dictionary, but the code is giving you an error. Can you change line 4 so that it prints "Unknown" instead of raising an error?
info = {'name': 'Srdjan', 'age': 38}

# print(info['city'])
print(info.get('city', 'Unknown'))
