import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


print("")
playerchoice = input("Enter...\n 1 for Rock, \n2 for Pape, or \n3 for Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 2:
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

# print("")

# papper = "Papper"
# rock = "Rock"
# scissor = "Scissor"

# playerChoice = input("Choose Rock, Papper, Scissor \n")

# print(playerChoice != papper)
# print(playerChoice != rock)
# print(playerChoice != scissor)

# if playerChoice != papper and playerChoice != rock and playerChoice != scissor:
#     print("invalid input")
#     playerChoice = input("Choose Rock, Papper, Scissor \n")

# random_choice = random.randint(1, 3)
# computerChoice = ""
# if random_choice == 1:
#     computerChoice = papper
# elif random_choice == 2:
#     computerChoice = rock
# else:
#     computerChoice = scissor

# if playerChoice == computerChoice:
#     print("is a draw")
# elif playerChoice == papper and computerChoice == rock:
#     print("Player Wins")
# elif playerChoice == papper and computerChoice == scissor:
#     print("Player Loses")
# elif playerChoice == rock and computerChoice == scissor:
#     print("Player Wins")
# elif playerChoice == rock and computerChoice == papper:
#     print("Player Loses")
# elif playerChoice == scissor and computerChoice == papper:
#     print("Player Wins")
# elif playerChoice == scissor and computerChoice == rock:
#     print("Player Loses")
# else:
#     print("not expecting")
