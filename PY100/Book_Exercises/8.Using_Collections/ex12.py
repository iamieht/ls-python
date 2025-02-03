# Write some code that determines and prints whether the number 3 appears inside each of these lists:
numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']


def is_3_in_list(list):
    return 3 in list


print(is_3_in_list(numbers1))
print(is_3_in_list(numbers2))
print(is_3_in_list(numbers3))
print(is_3_in_list(numbers4))
print(is_3_in_list(numbers5))
