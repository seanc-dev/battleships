
import game

play = "Y"

while play == "Y":

    game.init_game()

    while not game_over:

        game_over = game.fire_away()

    play = input("Play again? (Y/N): ")