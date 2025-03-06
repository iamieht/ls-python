# Will the following functions return the same results?
def first():
    return {
        'prop1': "hi there",
    }

def second():
    return
    {
        'prop1': "hi there",
    }

print(first())
print(second())

# No, the second() function returns None, while the first() function returns a dictionary. In Python, if there's nothing after a return statement, the function will return None. The indented block after the return statement in second function is unreachable and doesn't affect the return value.