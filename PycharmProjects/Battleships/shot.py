import validate
import dictionaries
import game
from random import randint


def request_coordinates(guesses, board_dimensions):
    guess = {}
    valid_shot = False
    while not valid_shot:
        try:
            guess["col"] = int(input("Guess Column: "))
            guess["row"] = int(input("Guess Row: "))
            valid_shot = validate.coordinates_guess(guess, board_dimensions, guesses)
        except ValueError:
            print('Sorry, those co-ordinates aren''t on the board!')
    return guess


def outcomes_and_update(guess_number, game_variables):
    game_variables['outcomes'] = {'hit': False, 'sunk': False, 'all_ships_sunk': False, 'all_guesses_used': False}
    for ship in game_variables['ships']:
        for ship_section in range(game_variables['ships'][ship]['length']):
            # print('guess_number: {}'.format(str(guess_number)))
            # print('game_variables[''guesses''[guess_number]]: {}'
            #       .format(str(game_variables['guesses'][guess_number])))
            if validate.row_and_col_match(
                    game_variables['guesses'][guess_number], game_variables['ships'][ship][ship_section]):
                game_variables['ships'][ship][ship_section]['is_hit'] = True
                game_variables['outcomes']['hit'] = True
                game_variables['ships'][ship]["sections_remaining"] -= 1
                if game_variables['ships'][ship]["sections_remaining"] == 0:
                    print("ship sunk: {}".format(str(game_variables['ships'][ship])))
                    game_variables['ships'][ship]["sunk"] = True
                    game_variables['outcomes']['sunk'] = True
                    game_variables['outcomes']['name'] = game_variables['ships'][ship]['name']
                    game_variables['ships_remaining_afloat'] -= 1
                    print('outcomes after ships sunk: {}'.format(game_variables['outcomes']))
                    if game_variables['ships_remaining_afloat'] == 0:
                        game_variables['outcomes']['all_ships_sunk'] = True
                return game_variables
    if not game_variables['outcomes']['hit']:
        game_variables['misses_remaining'] -= 1
        if game_variables['misses_remaining'] == 0:
            game_variables['outcomes']["all_guesses_used"] = True
    return game_variables


def print_response(outcomes):
    return outcomes
