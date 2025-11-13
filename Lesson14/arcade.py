import rps9
import guess_number

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


while True:
    game = input(
        "Choose 1 to play Guess a Number\nChoose 2 to play Rock Paper Scissors\n"
    )

    gamechoosed = int(game)

    if gamechoosed == 1:
        play1 = guess_number.play_guess_number(arg.name)
        play1()
        # print(arg.name)
        print("Choosed play_guess_number")
        break
    elif gamechoosed == 2:
        play2 = rps9.rps(arg.name)
        play2()
        print("Choosed Rock Paper Scissors")
        break
    else:
        print("Game choosed not available")
