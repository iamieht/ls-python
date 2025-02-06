# Determine what the following code snippet prints.
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)    # True

# Bonus question: Do we need the parentheses in the boolean expression or could we have written the following?: Parentheses not needed
is_moving = braking_force < acceleration and speed > 0 or acceleration > 0
print(is_moving)    # True
