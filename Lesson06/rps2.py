import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:
    print("")
    playerchoice = input(
        "Enter...\n 1 for Rock, \n2 for Pape, or \n3 for Scissors:\n\n"
    )

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3")

    computer = random.choice("123")
    computerchoice = int(computer)

    print("")
    print("Your choice " + str(RPS(player)).replace("RPS.", ""))
    print("Python choice " + str(RPS(computerchoice)).replace("RPS.", ""))

    if player == 1 and computerchoice == 3:
        print("You Win")
    elif player == 2 and computerchoice == 1:
        print("Youn Win")
    elif player == 3 and computerchoice == 2:
        print("Youn Win")
    elif player == computerchoice:
        print("Its a draw")
    else:
        print("Python wins")
    playagain = input("\nPlay again? \n Y for Yes or \n Q to Quit")

    if playagain.lower() == "y":
        continue
    else:
        print("thanks for playing!\n")
        playagain = False
sys.exit("Bye!")
