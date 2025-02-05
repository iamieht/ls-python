# What does the following function do? Be sure to identify the output value.
def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()


my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

# Step 1. Get the dict keys and sort them
# ['Antonina', 'Chris', 'Clare', 'Karis', 'Karl', 'Trevor']
# Retrieve the second element of the list and transform it into uppercase and return it. CHRIS
print(do_something(my_dict))
