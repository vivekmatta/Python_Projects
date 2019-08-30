from random import randint

def run():
    print("Let's play Rock, Paper, Scissiors!")

    print("When you want to stop playing, type 'exit' to end it.")


    choices = ["Rocks", "Paper", "Scissor"]

    computer = choices[randint(0,2)]

    player = False

    player_score = 0

    computer_score = 0

    while player == False:
        player = input("Rock, Paper, or Scissor? ")
        if player == computer:
            print("It's a tie!")
        elif player == "Rock":
            if computer == "Paper":
                print("You lose. " + computer + " covers " + player)
                computer_score += 1
            else:
                print("You won. " + player + " smashes " + computer)
                player_score += 1
        elif player == "Scissors":
            if computer == "Paper":
                print("You won. " + player + " cuts " + computer)
                player_score += 1
            else:
                print("You lost. " + computer + " smashes " + player)
                computer_score += 1
        elif player == "Paper":
            if computer == "Rock":
                print("You won. " + player + " covers " + computer)
                player_score += 1
            else:
                print("You lost. " + computer + " cuts " + player)
                computer_score += 1
        elif player == "exit":
            print("\nPlayer Score: " + str(player_score))
            print("Computer Score: " + str(computer_score))
            if player_score > computer_score:
                print("You won.")
            elif player_score == computer_score:
                print("You tied.")
            else:
                print("You lost.")
            break
        else:
            print("That's not a valid play. Check your spelling!")

        player = False
        computer = choices[randint(0,2)]

run()
