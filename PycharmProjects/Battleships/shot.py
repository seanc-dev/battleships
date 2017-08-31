import validate
import dictionaries
from random import randint


def response_selection(response_type, game_style, ship_name=None):
    responses = dictionaries.extract_responses()
    option_count = responses[game_style][response_type]["optionCount"]
    randint_key = randint(0, option_count)
    if 'ship_sunk' in response_type:
        response_type_a = response_type + '_1'
        response_type_b = response_type + '_2'
        response_a = responses[game_style][response_type_a][randint_key]
        response_b = responses[game_style][response_type_b][randint_key]
        response = response_a + ship_name + response_b
    else:
        response = responses[game_style][response_type][randint_key]
    return response


def request_shot_coordinates(guesses, board_dimensions):
    guess = {}
    try:
        valid_shot = False
        while not valid_shot:
            guess["col"] = int(input("Guess Column: "))
            guess["row"] = int(input("Guess Row: "))
            valid_shot = validate.coordinates_guess(guess, board_dimensions, guesses)
            print(valid_shot)
    except ValueError:
        print("Make sure you enter a number between {0} and {1}.".format(str(board_dimensions["board_min"]),
                                                                         str(board_dimensions["board_max"])))
    return guess


def shot_outcomes(coordinate_number, game_variables):
    game_variables['outcomes'] = {}
    for ship in game_variables['ships']:
        for ship_section in range(game_variables['ships'][ship]['length']):
            if validate.row_and_col_match(
                    game_variables['guesses'][coordinate_number], game_variables['ships'][ship][ship_section]):
                game_variables['ships'][ship][ship_section]['is_hit'] = True
                game_variables['outcomes']['hit'] = True
                if game_variables['ships'][ship]["SectionsRemaining"] - 1 == 0:
                    game_variables['ships']["sunk"] = True
                    game_variables['outcomes']['sunk'] = True
                    game_variables['outcomes']['name'] = game_variables['ships'][ship]['name']
                    game_variables['remaining_afloat'] -= 1
                    if game_variables['remaining_afloat'] == 0:
                        game_variables['outcomes']['all_sunk'] = True
                return game_variables
    if not game_variables['outcomes']['hit']:
        game_variables['misses_remaining'] -= 1
        if game_variables['misses_remaining'] == 0:
            game_variables['outcomes']["all_guesses_used"] = True
    return game_variables


def shot_hit_flow(outcomes, ships, game_variables):
    # set local variables
    ship_key = outcomes["ship"]["position"]
    ship_section_key = outcomes["ship"]["section"]["position"]
    # change relevant data values and print responses
    ships[ship_key][ship_section_key]["IsHit"] = True
    ships[ship_key]["sections_remaining"] -= 1
    if outcomes["ship"]["sunk"]:
        ships['remaining_afloat'] -= 1
        if outcomes["all_ships_sunk"]:
            game_variables["all_ships_sunk"] = True
    game_variables["ships"][ship_key] = ships[ship_key]
    return game_variables


def shot_miss_flow(outcomes, game_variables):
    game_variables["misses_remaining"] -= 1


def hit_miss(coordinates, ships, misses_remaining_f, ships_remaining_f):
    outcomes = dict()
    outcomes["game_over"] = False
    for ship in ships:
        for ship_section in range(1, ships[ship]["length"] + 1):
            # outcomes["IsHit"] = False
            if coordinates["row"] == ships[ship][ship_section]["row"] and ships[ship][ship_section]["col"] == \
                    coordinates["col"]:
                outcomes["IsHit"] = True
                outcomes["response"] = "That's a direct hit!"
                ships[ship][ship_section]["IsHit"] = True
                ships[ship]["SectionsRemaining"] = ships[ship]["SectionsRemaining"] - 1
                if ships[ship]["SectionsRemaining"] == 0:
                    ships_remaining_f = ships_remaining_f - 1
                    if ships_remaining_f == 1:
                        outcomes["response"] = "That\'s a direct hit, you sunk the {0}! Only 1 ship to go!".format(
                            str(ships[ship]["name"]))
                    else:
                        outcomes["response"] = "That\'s a direct hit, you sunk the {0}! Only {1} ships to go!".format(
                            str(ships[ship]["name"]), str(ships_remaining_f))
                    if ships_remaining_f == 0:
                        outcomes["response"] = "Congratulations! You sunk the {0}!".format(str(ships[ship]["name"]))
                        outcomes["game_over"] = True
            else:
                outcomes["response"] = "Miss! Try again!"
                outcomes["IsHit"] = False
            if outcomes["IsHit"]:
                break
        if outcomes["IsHit"]:
            break
    if not outcomes["IsHit"]:
        misses_remaining_f = misses_remaining_f - 1
        if misses_remaining_f == 1:
            outcomes["response"] = "Miss! Careful, you only have one incorrect guess left!"
        elif misses_remaining_f == 0:
            outcomes["response"] = "Miss! Oh no, you've run out of guesses!"
            outcomes["game_over"] = True
    outcomes["misses_remaining"] = misses_remaining_f
    outcomes["ships_remaining"] = ships_remaining_f
    return outcomes
