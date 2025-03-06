# For this practice problem, write a program that outputs The Flintstones Rock! 10 times, with each line prefixed by one more hyphen than the line above it. The output should start out like this:
# -The Flintstones Rock!
# --The Flintstones Rock!
# ---The Flintstones Rock!
#     ...

str1 = "The Flintstones Rock!"
counter = 1

while counter <= 10:
    print(f'{'-' * counter}{str1}')
    counter +=1
