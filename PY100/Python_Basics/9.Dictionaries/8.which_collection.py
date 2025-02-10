# Rewrite car as a list of lists in which each nested list contains two elements that represent the corresponding key/value pairs.
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}

car_list = [
    ['type', 'sedan'],
    ['color', 'blue'],
    ['year', 2003]
]
print(car_list)
