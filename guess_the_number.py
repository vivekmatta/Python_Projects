'''
from random import randint

answer = randint(1, 100)

print("Guess a number between 1 and 3.")
guess = int(input())

count = 0
print(answer)

bob = True

while bob:
    if guess < answer:
        print("Pick a higher number.")
        count += 1
    elif guess > answer:
        print("Pick a lower number.")
        count += 1
    elif guess == answer:
        print("You got it!")
        bob = False
        break
    print("It took you " + str(count) + " tries.")
'''

from random import randint

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
