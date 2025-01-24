'''
Exercise #1
Write a code fragment (a short part of a Python program) to count heads, shoulders, knees, and toes at a party. The grader will automatically define a variable people for you, counting the number of people at the party. Your code must define four variables, one called heads, one called shoulders, one called knees, and one called toes, equal to the number of heads, shoulders, knees, and toes in total at the party. Your program does not need to print any output. The grader will select a new random value for people each time your code runs.
'''
people = 19
heads = people
shoulders = people * 2
knees = people * 2
toes = people * 10

print(
    f"In a party of {people} people, there are {heads} heads, {shoulders} shoulders, {knees} knees and {toes} toes.")

'''
Exercise #2
You are in a bike race which goes up and down a hill. The grader will pre-define four variables for you: uphillDistance and downhillDistance give the distance (in km) of both parts of the race, and uphillTime and downhillTime give the time (in minutes) of how long it took you to complete each part of the race. Write a program that will print out your average speed (in km/min) for the entire race.
'''
uphillDistance = 9
uphillTime = 78
downhillDistance = 4
downhillTime = 50

totalDistance = uphillDistance + downhillDistance
totalTime = uphillTime + downhillTime
averageSpeed = totalDistance / totalTime

print(averageSpeed)

'''
Exercise #3
Write a program to swap the values of two variables. The grader will automatically define variables x and y for you, with numerical values. You must write code that exchanges their values: the value of x after your code runs must equal the value that y had before your code ran, and the value of y after your code runs must equal the value that x had before your code ran. 
'''
x = 13
y = 12

x, y = y, x

print(f'X = {x} and Y = {y}')
