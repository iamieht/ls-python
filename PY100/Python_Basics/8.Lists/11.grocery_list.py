# Write code that removes the items from grocery_list, one by one, until it is empty. If you print the elements you remove, the expected behavior would look as follows.
grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']

grocery_list.reverse()
for element in range(len(grocery_list) -1, -1, -1):
    print(grocery_list.pop())



print(grocery_list)

# Better Solution
# while grocery_list:
#     checked_item = grocery_list.pop(0)
#     print(checked_item)