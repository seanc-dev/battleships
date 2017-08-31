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
    while True:
        try:
            valid_shot = False
            while not valid_shot:
                guess["col"] = int(input("Guess Column: "))
                guess["row"] = int(input("Guess Row: "))
                valid_shot = validate.coordinates_guess(guess, board_dimensions, guesses)
        except ValueError:
            print("Make sure you enter a number between {0} and {1}.".format(str(board_dimensions["board_min"]),
                                                                             str(board_dimensions["board_max"])))
            continue
        else:
            return guess


def shot_outcomes(shot, ships, ships_remaining, misses_remaining):
    outcomes = {'all_ships_sunk': False, 'all_guesses_used': False, 'hit': False, 'ship': {}, 'section': {}}
    for ship in ships:
        for ship_section in range(ships[ship]["length"]):
            if validate.row_and_col_match(shot, ships[ship][ship_section]):
                outcomes["hit"] = True
                outcomes["ship"]["position"] = ship
                outcomes["ship"]["section"]["position"]: ship_section
                if ships[ship]["SectionsRemaining"] - 1 == 0:
                    # game_variables["ships_remaining"] = game_variables["ships_remaining"] - 1
                    ship_sunk_flow(ships, ship)
                    outcomes["ship"]["sunk"] = True
                    outcomes["ship"]["name"] = ships[ship]["name"]
                    if ships_remaining - 1 == 0:
                        outcomes["all_ships_sunk"] = True
                return outcomes
    if misses_remaining - 1 == 0:
        outcomes["all_guesses_used"] = True
    return outcomes


def ship_sunk_flow(ships, ship_key):
    ships[ship_key]["sunk"] = True
    ships["ships_remaining"] = ships["ships_remaining"] - 1
    return ships


def shot_hit_flow(outcomes, ships, game_variables):
    ship_key = outcomes["ship"]["position"]
    ship_section_key = outcomes["ship"]["section"]["position"]
    ships[ship_key][ship_section_key]["IsHit"] = True
    ships[ship_key]["sections_remaining"] = ships[ship_key]["sections_remaining"] - 1
    if outcomes["ship"]["sunk"]:
        ships = ship_sunk_flow(ships, ship_key)
        if outcomes["all_ships_sunk"]:
            game_variables["all_ships_sunk"] = True
    game_variables["ships"][ship_key] = ships[ship_key]
    return game_variables


def shot_miss_flow(outcomes, game_variables):
    game_variables["misses_remaining"] = game_variables["misses_remaining"] - 1


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
