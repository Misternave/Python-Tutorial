import random
import sys


def play_guess_number(name="cenas"):
    gamecount = 0
    winGames = 0

    def guess_number():
        nonlocal name
        nonlocal gamecount
        nonlocal winGames

        welcomeMessage = "Welcome to Guess a Number\n"
        print(welcomeMessage)

        while True:

            playerChoice = input(f"{name}, guess the number i am thinking 1, 2 or 3?\n")

            if playerChoice in ["1", "2", "3"]:
                break
            else:
                print(f"Choose between 1 , 2 or 3\n")

        playerNumber = int(playerChoice)

        guessingNumber = random.choice("123")
        computerNumber = int(guessingNumber)

        while True:
            if playerNumber == computerNumber:
                print(f"Good guess {name}, You win\n")
                gamecount += 1
                winGames += 1
                break
            else:
                print(f"You lost {name}, better luck next time \n")
                gamecount += 1
                break
        print(f"You won {winGames} games\n")
        print(f"Total number of games:  {gamecount}\n")
        print(f"Winning percentage is {(winGames/gamecount)*100}\n")

        active_game = True
        while active_game:

            play_again_input = input(
                "Do you want to play again?\n\nEnter y to play again\nEnter q to quit\n"
            )
            play_again = play_again_input.lower()

            if play_again == "y":
                guess_number()
            elif play_again == "q":
                active_game = False
                sys.exit(f"Bye {name}, thanks for playing\n")
            else:
                print("incorrect input, ")

    return guess_number


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Provides a personal greeting")

    parser.add_argument(
        "-n",
        "--name",
        metavar="name",
        required=True,
        help="The name if the person to greet",
    )

    arg = parser.parse_args()

    play = play_guess_number(arg.name)

    play()
