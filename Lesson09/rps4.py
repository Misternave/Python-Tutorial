import random
import sys
from enum import Enum

game_count = 0


def play_rps():

    class RPS(Enum):
        ROCK = 1
        PAPER = 2
        SCISSORS = 3

    playerchoice = input("Enter...\n 1 for Rock, \n2 for Pape, or \n3 for Scissors:\n")

    if playerchoice not in ["1", "2", "3"]:
        print("You muyst choose 1 , 2 , 3")
        return play_rps()

    player = int(playerchoice)

    computer = random.choice("123")
    computerchoice = int(computer)

    print("")
    print("Your choice " + str(RPS(player)).replace("RPS.", ""))
    print("Python choice " + str(RPS(computerchoice)).replace("RPS.", ""))

    def decide_winner(player, computerchoice):
        if player == 1 and computerchoice == 3:
            return "You Win"
        elif player == 2 and computerchoice == 1:
            return "Youn Win"
        elif player == 3 and computerchoice == 2:
            return "Youn Win"
        elif player == computerchoice:
            return "Its a draw"
        else:
            return "Python wins"

    game_result = decide_winner(player, computerchoice)
    print(game_result)

    global game_count
    game_count += 1
    print("Game_count: " + str(game_count))

    print("\nPlay again?")

    while True:
        playagain = input("\n Y for Yes or \n Q to Quit 2\n")
        if playagain.lower() not in ["y", "q"]:
            continue
        else:
            break

    if playagain.lower() == "y":
        return play_rps()
    else:
        print("thanks for playing!\n")
        sys.exit("Bye!")


play_rps()
