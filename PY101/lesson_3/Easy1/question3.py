# Show two different ways to create a new string with "Four score and " prepended to the front of the string referenced by famous_words.

famous_words = "seven years ago..."

# Option 1
new_str = 'Four score and ' + famous_words
print(new_str)

# Option 2
new_str2 = f'Four score and {famous_words}'
print(new_str2)