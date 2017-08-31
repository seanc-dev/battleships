
import game
import dictionaries

play = "Y"

while play == "Y":

    game_variables = game.init_game()

    game_variables["game_over"] = False

    coordinate_no = 0

    while not game_variables["game_over"]:

        game_variables = game.fire_away(
            game_variables['guesses'],
            game_variables['board_dimensions'],
            coordinate_no
        )

        coordinate_no = coordinate_no + 1

    play = input("Play again? (Y/N): ")