# Problem
# Write a function that determines the mean (average) of the three scores passed to it, and returns the letter associated with that grade.

# input
#   - 3 positive integers
# output
#   - a char representing the grade

# Numerical score letter grade list:
# 90 <= score <= 100: 'A'
# 80 <= score < 90: 'B'
# 70 <= score < 80: 'C'
# 60 <= score < 70: 'D'
# 0 <= score < 60: 'F'

# Examples / Test Cases
# print(get_grade(95, 90, 93) == "A")      # True
# print(get_grade(50, 50, 95) == "D")      # True

# Data Structure
# - String
# - Integer

# Algorithm
# 1. Create a function get_grade_avg(grade1, grade2, grade3) of type integers
#   - return (grade1 + grade2 + grade3) // 3
# 2. Create a function get_grade(grade1, grade2, grade3):
#   - grade_avg = get_grade_avg(grade1, grade2, grade3)
#   - match:
#       case grade_avg >= 90
#           return 'A'
#       case grade_avg >=80
#           return 'B'
#       case grade_avg  >= 70
#           return 'C'
#       case grade_avg >= 60
#            return 'D'
#       case _
#           return 'F'

# Code
def get_grade_avg(grade1, grade2, grade3):
    return (grade1 + grade2 + grade3) / 3


def get_grade(grade1, grade2, grade3):
    grade_avg = get_grade_avg(grade1, grade2, grade3)
    match grade_avg:
        case _ if grade_avg >= 90:
            return 'A'
        case _ if grade_avg >= 80:
            return 'B'
        case _ if grade_avg >= 70:
            return 'C'
        case _ if grade_avg >= 60:
            return 'D'
        case _:
            return 'F'


print(get_grade(95, 90, 93) == "A")
print(get_grade(50, 50, 95) == "D")
