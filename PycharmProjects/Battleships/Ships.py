from random import randint
import Dictionaries
board_def = Dictionaries.board_def


# Define random row function to gen ship row for ship positions fun
def random_row(board_len):
    return randint(1, len(board_len))


# Define random col function to gen ship col for ship positions fun
def random_col(board_len):
    return randint(1, len(board_len))


# Define random binary int to determine whether ship stretches along row or col
def row_or_col():
    if randint(0, 1) == 0:
        return "row"
    else:
        return "col"


# Define random binary int to define whether ship grows pos or neg
def pos_or_neg():
    bin = randint(0, 1)
    if bin == 0:
        return -1
    if bin == 1:
        return 1


def shadow_ship_generate(shadow_ship_len, shadow_ship_name, ships_dict, game_difficulty):
    # valid_position = False
    while True:  # Not valid_position
        shadow_ship = {"SectionsRemaining": shadow_ship_len, "ShipLength": 1, "name": shadow_ship_name,
                       1: {"IsHit": False, "row": random_row(board_def[game_difficulty]["board_size"]), "col":
                           random_row(board_def[game_difficulty]["board_size"])}}
        # Set starting co-values for this ship
        growth_direction = pos_or_neg()  # Set growth direction for ship from initial co-ordinates
        row_col = row_or_col()  # Set value to define whether ship grows a]long row or up/down col
        # Define loop to generate remainder of shadow_ship:
        for j in range(2, ship_lengths[i] + 1):
            shadow_ship["ShipLength"] = shadow_ship["ShipLength"] + 1
            shadow_ship[j] = {"IsHit": False, "col": shadow_ship[j - 1]["col"], "row": shadow_ship[j - 1]["row"]}
            shadow_ship[j][row_col] = shadow_ship[j - 1][row_col] + growth_direction
        valid_position = shadow_ship_coordinates_valid(shadow_ship, ships_dict)
        if shadow_ship["ShipLength"] == shadow_ship_len and valid_position:
            return shadow_ship
        # else:
        # valid_position = False


def generate_ships(ship_count_x, ship_names_x, ship_lengths_x):
    ships_x = dict()
    for i in range(ship_count_x):
        ships_x[i] = shadow_ship_generate(ship_lengths_x[i], ship_names_x[i], ships_x)
    return ships_x
