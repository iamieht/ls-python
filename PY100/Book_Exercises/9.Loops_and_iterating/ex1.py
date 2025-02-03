# The following code causes an infinite loop (a loop that never stops iterating). Why?
counter = 0

while counter < 5:
    print(counter)

# Because the counter variable is not modified inside of the block, so it remains with the value 0, so the conditional expression always returns a truthy value.