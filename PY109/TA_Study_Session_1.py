# Ex1
exclamation_marks = '!!!'

def shout(text):
    return text.upper() + exclamation_marks

print(shout('hello') + exclamation_marks)

# Ex2
exclamation_marks = '!!!'

def shout(text):
    exclamation_marks += '¡¡¡'
    # exclamation_marks = exclamation_marks 
    exclamation_marks = exclamation_marks + 'iii'
    # my_exclamations = exclamation_marks + 'iii'
    return text.upper() + exclamation_marks

print(shout('hello') + exclamation_marks) # HELLOiii!!!

# Ex3
players = [
  {'name': "Joe", 'age': 25},
  {'name': "Andy", 'age': 31},
  {'name': "Ralph", 'age': 18},
  {'name': "Mark", 'age': 28},
]

def age_players(players):
    for player in players:
        for key, value in player.items():
            if key == 'age':
                value += 1

age_players(players)


# Ex4
players = [
  {'name': "Joe", 'age': 25},
  {'name': "Andy", 'age': 31},
  {'name': "Ralph", 'age': 18},
  {'name': "Mark", 'age': 28},
]

def age_players(players):
    for player in players:
        for key, value in player.items():
            if key == 'age':
                player[key] += 1


new_team = players
last_years_team = players[:]

new_team.append({
    'name': 'Bob',
    'age': 19,
})

age_players(players)
print(players)
print("")
print(new_team)
print("")
print(last_years_team)

# Variables as pointers (the last one)

#Ex5
lst1 = [0, 1, 2, 3]
lst2 = lst1.pop(0) or lst1.pop()

if lst2:
    print(lst2)
else:
    print(lst1)