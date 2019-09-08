
from random import randint

def again():
    answer = input("Would you like to play again? ")
    if answer == "Yes" or answer == "yes":
        run()
    elif answer == "No" or answer == "no":
        exit

        
def guess_100():
    answer = randint(1, 100)

    count = 0
    keep_loop = True

    prompt = "Guess a number between 1 and 100."

    while keep_loop:
        print(prompt)
        guess = int(input())
        if guess < answer:
            prompt = "Pick a higher number."
            count += 1
        elif guess > answer:
            prompt = "Pick a lower number."
            count += 1
        elif guess == answer:
            print("You got it!")
            keep_loop = False
    print("It took you " + str(count) + " tries.")
    again()

def guess_50():
    answer = randint(1, 50)

    count = 0
    keep_loop = True

    prompt = "Guess a number between 1 and 50."

    while keep_loop:
        print(prompt)
        guess = int(input())
        if guess < answer:
            prompt = "Pick a higher number."
            count += 1
        elif guess > answer:
            prompt = "Pick a lower number."
            count += 1
        elif guess == answer:
            print("You got it!")
            keep_loop = False
    print("It took you " + str(count) + " tries.")
    again()
    
def guess_10():
    answer = randint(1, 10)

    count = 0
    keep_loop = True

    prompt = "Guess a number between 1 and 10."

    while keep_loop:
        print(prompt)
        guess = int(input())
        if guess < answer:
            prompt = "Pick a higher number."
            count += 1
        elif guess > answer:
            prompt = "Pick a lower number."
            count += 1
        elif guess == answer:
            print("You got it!")
            keep_loop = False
    print("It took you " + str(count) + " tries.")
    again()
    
def run():
    print("Please pick a level of difficulty: ")
    answer = input("Easy, Medium, or Hard: ")

    if answer == "Easy":
        guess_10()
    elif answer == "Medium":
        guess_50()
    elif answer == "Hard":
        guess_100()

run()
    

