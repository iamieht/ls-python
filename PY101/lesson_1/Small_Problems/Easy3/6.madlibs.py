# Problem
# Create a simple madlib program that prompts for a noun, a verb, an adverb, and an adjective, and injects them into a story that you create.

# input:
#   - noun: string
#   - verb: string
#   - adjective: string
#   - adverb: string
# output:
#   - a story: string

# Example / Test Case
# Enter a noun: dog
# Enter a verb: walk
# Enter an adjective: blue
# Enter an adverb: quickly
# Do you walk your blue dog quickly? That's hilarious!
# The blue dog walks quickly over the lazy dog.
# The dog quickly walks up to Joe's blue turtle.

# Data Structure
# - string

# Algorithm
# 1. Create a function get_input(prompt)
#   - return input(prompt)
# 2. Create a function madlibs():
#   noun = get_input("Enter a noun: ")
#   verb = get_input("Enter a verb: ")
#   adjective = get_input("Enter an adjective: ")
#   adverb = get_input("Enter an adverb: ")
#   print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!"")
#   print(f"The {adjective} {noun} {verb}s {adverb} over the lazy dog.")
#   print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.)

# Code
def get_input(prompt):
    return input(prompt)


def madlibs():
    noun = get_input("Enter an noun: ")
    verb = get_input("Enter a verb: ")
    adjective = get_input("Enter an adjective: ")
    adverb = get_input("Enter an adverb: ")

    print(f"Do you {verb} your {adjective} {noun} {adverb}? That's hilarious!")
    print(f"The {adjective} {noun} {verb}s {adverb} over the lazy dog.")
    print(f"The {noun} {adverb} {verb}s up to Joe's {adjective} turtle.")


madlibs()
