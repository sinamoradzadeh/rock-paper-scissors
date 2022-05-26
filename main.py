from random import randint

print('hey!!\n welcome to rock paper scissors game...')
playermove=input("what's your move? \nvalid answers:[rock,paper,scissors]...\n").lower()
validanswers=["rock","paper","scissors"]
if playermove in validanswers:
    rannum=randint(1,3)
    if rannum == 1:
        pcchoice="rock"
    elif rannum==2:
        pcchoice="paper"
    else:pcchoice="scissors"
    print(f"your choice is {playermove} & PCs choice was {pcchoice}... So:\n")
    if playermove == pcchoice:
        print("No one won the game.")
    else:
        if playermove == "rock" and pcchoice =="paper":
            print("PC 🏆 🥇 ")
        elif playermove== "rock"and pcchoice=="scissors":
            print("you 🏆 🥇 ")
        elif playermove== "scissors"and pcchoice=="paper":
            print("you 🏆 🥇 ")
        elif playermove== "scissors"and pcchoice=="rock":
            print("PC 🏆 🥇 ")
        elif playermove== "paper"and pcchoice=="scissors":
            print("PC 🏆 🥇 ")
        elif playermove== "paper"and pcchoice=="rock":
            print("you 🏆 🥇 ")
else:print(f"you must choose one of these values: {validanswers}")
