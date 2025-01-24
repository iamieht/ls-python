def lowerChar(char):
    upCaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerCaseLetters = 'abcdefghijklmnopqrstuvwxyz'

    for idx in range(len(upCaseLetters)):
        if char == upCaseLetters[idx]:
            return lowerCaseLetters[idx]

    return char


def lowerString(string):
    result = ""
    for i in string:
        result += lowerChar(i)

    return result


print(lowerChar('Z'))
print(lowerChar('a'))
print(lowerString('Gr3aT!'))
print(lowerString('This string has 9 CAPITAL letters (& Punctuation)!'))
