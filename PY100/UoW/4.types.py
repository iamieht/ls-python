# Write a program to help you feed your friends at a party by doing some math about square pizzas. Assume the grader defines a string inputStr for you, which is a decimal string meaning the side length L of the pizza in cm. The area of the pizza should be computed using the formula A = L*L. Then, assuming that each person needs to eat 100 cm2 of pizza, compute the number of people it can feed, rounded down to the nearest integer.
# Example: if inputStr is "17.5", the area will be 306.25 cm2, so 3 is the correct output.

inputStr = float("17.5")
areaOfPizza = inputStr * inputStr
numberOfPeopleFeed = areaOfPizza / 100

print(f"{int(numberOfPeopleFeed)}")
