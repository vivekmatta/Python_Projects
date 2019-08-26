
def quotient():
    print("What two numbers would you like to divide? ")
    
    answer1 = int(input())
    answer2 = int(input())

    quotient = answer1 / answer2

    print(str(answer1) + " / " + str(answer2) + " = " + str(quotient))

def subtraction():
    print("What two numbers would you like to subtract? ")
    
    answer1 = int(input())
    answer2 = int(input())

    subtraction = answer1 - answer2

    print(str(answer1) + " - " + str(answer2) + " = " + str(subtraction))

def addition():
    print("What two numbers would you like to add? ")
    
    answer1 = int(input())
    answer2 = int(input())

    addition = answer1 + answer2

    print(str(answer1) + " + " + str(answer2) + " = " + str(addition))

def multiplication():
    print("What two numbers would you like to subtract? ")
    
    answer1 = int(input())
    answer2 = int(input())

    multiplication = answer1 * answer2

    print(str(answer1) + " * " + str(answer2) + " = " + str(multiplication))

def run():
    print("What operation would you like to do? ")
    operator = input()

    if operator == "addition" or operator == "Addition":
        addition()
    if operator == "subtraction" or operator == "Subtraction":
        subtraction()
    if operator == "division" or operator == "Division":
        division()
    if operator == "muliplication" or operator == "Multiplication":
        multiplication()
"""
    print("Would you like to do another operation? yes or no? ")
    answer = input()
    if answer == "yes":
        run()
    if answer == "no":
        break
"""
run()
