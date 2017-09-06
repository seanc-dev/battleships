
import game
import dictionaries

play = "Y"

while play == "Y":

    game_variables = game.init_game()

    game_variables["game_over"] = False

    guess_number = 0

    while not game_variables["game_over"]:

        game_variables = game.fire_away(
            game_variables,
            guess_number
        )

        guess_number += 1

    play = input("Play again? (Y/N): ")