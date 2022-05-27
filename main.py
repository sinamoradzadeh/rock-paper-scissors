from random import randint

print('rock paper scissors game...')
finalAnswer = True
while finalAnswer == True:

    playermove = input("what's your move? \nvalid answers:[rock,paper,scissors]...\n").lower()

    validanswers = ["rock", "paper", "scissors"]

    if playermove in validanswers:
        # pc move start
        rannum = randint(1, 3)
        if rannum == 1:
            pcchoice = "rock"
        elif rannum == 2:
            pcchoice = "paper"
        else:
            pcchoice = "scissors"
        # pc move done
        print(f"your choice is {playermove} & PCs choice was {pcchoice}... So:\n")

        # result of game
        if playermove == pcchoice:
            print("No one won the game.")
        else:
            if playermove == "rock" and pcchoice == "paper":
                print("PC 🏆 🥇 ")
            elif playermove == "rock" and pcchoice == "scissors":
                print("you 🏆 🥇 ")
            elif playermove == "scissors" and pcchoice == "paper":
                print("you 🏆 🥇 ")
            elif playermove == "scissors" and pcchoice == "rock":
                print("PC 🏆 🥇 ")
            elif playermove == "paper" and pcchoice == "scissors":
                print("PC 🏆 🥇 ")
            elif playermove == "paper" and pcchoice == "rock":
                print("you 🏆 🥇 ")
        # result done
        # ask player if he/she wants to play again
        answer = input("do you want to play again?").lower()
        fanswer = list(answer)
        if fanswer[0] == "n":
            print("you said no ...so bye")
            finalAnswer = False
        elif fanswer[0] == "y":
            finalAnswer = True
    else:
        print(f"you must choose one of these values: {validanswers}")
        answer = input("do you want to Try again?").lower()
        fanswer = list(answer)
        if fanswer[0] == "n":
            print("you said no ...so bye")
            finalAnswer = False
        elif fanswer[0] == "y":
            finalAnswer = True
