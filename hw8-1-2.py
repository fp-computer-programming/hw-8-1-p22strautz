# Author: SCT (AMDG) 12/9/21

def grade_calculate(grade):
    if grade < 60:
        print("You get an F")
    elif grade < 65:
        print("You get a D")
    elif grade < 70:
        print("You get a D+")
    elif grade < 73:
        print("You get a C-")
    elif grade < 77:
        print("You get a C")
    elif grade < 80:
        print("You get a C+")
    elif grade < 83:
        print("You get a B-")
    elif grade < 87:
        print("You get a B")
    elif grade < 90:
        print("You get a B+")
    elif grade < 93:
        print("You get a A-")
    else:
        print("You get an A!")


grade_calculate(70)
grade_calculate(95)
grade_calculate(100)
