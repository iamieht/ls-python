# Take your code from the previous Check the Weather exercise and rewrite it as a match-case statement.
# weather = 'windy'

# if weather == 'sunny':
#     print("It's a beautiful day!")
# elif weather == 'rainy':
#     print("Grab your umbrella.")
# else:
#     print("Let's stay inside.")
weather = 'windy'

match weather:
    case 'sunny':
        print("It's a beautiful day!")
    case 'rainy':
        print("Grab your umbrella.")
    case _:
        print("Let's stay inside.")
