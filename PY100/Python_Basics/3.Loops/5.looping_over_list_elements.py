# Using the code below as a starting point, write a while loop that prints the elements of lst at each index and terminates after printing the last element of the list.
lst = [1, 3, 7, 15]
# lst = []
index = 0

while index < len(lst):
    print(f'List element at index {index} is {lst[index]}')
    index += 1

# Further Exploration
# What would the code output if lst is empty? Why is that?
# There is no output as the condition index < len(lst) evaluates as falsy and the block is never executed
