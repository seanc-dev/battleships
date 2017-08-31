import dictionaries
import board
import ships
import shot
from random import randint


def form_styles_list():
    responses = dictionaries.extract_responses()
    style_list = list(responses.keys())
    return style_list


def print_styles_list():
    responses = dictionaries.extract_responses()
    for style in responses:
        print(style.title())


def find_max_int_key(search_dict):
    keyMax = 0
    int_key_found = False
    for key in search_dict:
        if type(key) == int and key >= keyMax:
            keyMax = key
            int_key_found = True
    if int_key_found:
        return keyMax
    else:
        return None


def game_style():
    styles_list = form_styles_list()
    print("What style would you like to play? The options are:")
    print_styles_list()
    while True:
        try:
            return_style = input("Style: ")
        except ValueError:
            print("Sorry that's not one of the options! Please try again.")
            continue
        while return_style not in styles_list:
            print("Sorry that's not one of the options! Please try again.")
            print("What style would you like to play? The options are:")
            print_styles_list()
            return_style = input("Style: ")
        break
    return return_style


def difficulty_response():
    while True:
        try:
            difficulty_x = (input("Do you want the game to be Easy, Medium, or Hard? ")).title()
        except ValueError:
            print("Sorry that's not a valid difficulty! Please try again.")
            continue
        else:
            break
    while difficulty_x not in ["Easy", "Medium", "Hard"]:
        print("Sorry, that's not a valid difficulty! Please try again")
        # print("Do you want the game to be Easy, Medium, or Hard?")
        difficulty_x = input("Do you want the game to be Easy, Medium, or Hard? ")
    print(dictionaries.difficulty_options[difficulty_x][0])
    return difficulty_x


def build_game_variables():
    chosen_style = game_style()
    difficulty = difficulty_response()
    board_dict = dictionaries.board_def[difficulty]
    ship_names = dictionaries.extract_ship_names()
    game_variables = {'guesses': {}, 'difficulty': difficulty, 'ships_remaining': board_dict["ship_count"],
                      'style': chosen_style.lower(), 'misses_remaining': board_dict["misses_allowed"],
                      'board_dimensions': {'min': board_dict["board_min_row"], 'max': board_dict["board_max_row"]}}
    game_variables["board"] = board.generate(game_variables["board_dimensions"]["max"])
    game_variables["ships"] = ships.generate_ships(
        board_dict["ship_count"],
        ship_names[game_variables['style']][randint(
            0, find_max_int_key(ship_names[game_variables['style']]))],
        game_variables["board_dimensions"]["min"],
        game_variables["board_dimensions"]["max"]
    )
    return game_variables


def fire_away(game_variables, coordinate_no):
    game_variables['guesses'][coordinate_no] = shot.request_shot_coordinates(
        game_variables,
        game_variables['board_dimensions']
    )
    outcomes = shot.shot_outcomes(
        game_variables["guesses"][coordinate_no],
        game_variables['ships'],
        game_variables['ships_remaining'],
        game_variables['misses_remaining']
    )
    if outcomes["hit"]:
        shot.shot_hit_flow(outcomes, game_variables)
    return game_variables


def init_game():
    print("Let's play Battleships!")
    game_variables = build_game_variables()
    print(" ")
    print("There are {0} ships somewhere in this ocean..".format(str(game_variables["ships_remaining"])))
    print("Destroy them all to win!")
    print(" ")
    board.display(game_variables["board"])
    print(" ")
    return game_variables
