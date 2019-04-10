
def main():
    numberInput1 = input("First Number? ")
    numberInput2 = input("Second Number? ")
    operatorInput = input("Operator? ")

    try:
        a = int(numberInput1)
        b = int(numberInput2)
    except ValueError:
        print("Invalid Input.")
        return

    if operatorInput == "*" or operatorInput == "times":
        answer = a * b
    elif operatorInput == "+" or operatorInput == "plus":
        answer = a + b
    elif operatorInput == "-" or operatorInput == "minus":
        answer = a - b
    elif operatorInput == "/" or operatorInput == "divided by":
        answer = a / b
    else:
        print("Invlaid Input. Not a number or operator.")
    print("Your answer is " + str(answer) + " .")
    return answer

main()
