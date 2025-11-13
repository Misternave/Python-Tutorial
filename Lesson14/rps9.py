import random
import sys
from enum import Enum


def rps(name="PlayerOne"):

    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        playerchoice = input(
            f"{name}, Enter...\n 1 for Rock, \n2 for Pape, or \n3 for Scissors:\n"
        )

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, You muyst choose 1 , 2 , 3")
            return play_rps()

        player = int(playerchoice)

        computer = random.choice("123")
        computerchoice = int(computer)

        print("")
        print(f"{name}, Your choice {str(RPS(player)).replace("RPS.", "")}.")
        print(f"Python choice { str(RPS(computerchoice)).replace("RPS.", "")}.")

        def decide_winner(player, computerchoice):
            nonlocal player_wins
            nonlocal python_wins

            if player == 1 and computerchoice == 3:
                player_wins += 1
                return f"{name}, You Win"
            elif player == 2 and computerchoice == 1:
                player_wins += 1
                return f"{name}, You Win"
            elif player == 3 and computerchoice == 2:
                player_wins += 1
                return f"{name}, You Win"
            elif player == computerchoice:
                return "Its a draw"
            else:
                python_wins += 1
                return "Python wins"

        game_result = decide_winner(player, computerchoice)
        print(game_result)

        nonlocal game_count
        game_count += 1
        print(f"Game count: {game_count}")
        print(f"{name}, Wins: {player_wins}")
        print(f"Python Wins: {python_wins}")

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
            sys.exit(f"Bye, {name}!")

    return play_rps


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides personalized game experience",
    )

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name of the person playing the game",
    )

    arg = parser.parse_args()

    rock_paper_scissors = rps(arg.name)
    rock_paper_scissors()
