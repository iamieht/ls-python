# Write some code that iterates through and prints all the words, one per line.
vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]

# happy
# cheerful
# merry
# glad
# tired
# sleepy
# etc...

for nested_list in vocabulary:
    for word in nested_list:
        print(word)