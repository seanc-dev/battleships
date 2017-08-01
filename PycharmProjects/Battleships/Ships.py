from random import randint
import Validate


# Define random row function to gen ship row for ship positions fun
def random_row(board_len):
    return randint(1, board_len)


# Define random col function to gen ship col for ship positions fun
def random_col(board_len):
    return randint(1, board_len)


# Define random binary int to determine whether ship stretches along row or col
def row_or_col():
    if randint(0, 1) == 0:
        return "row"
    else:
        return "col"


# Define random binary int to define whether ship grows pos or neg
def pos_or_neg():
    if randint(0, 1) == 0:
        return -1
    else:
        return 1


# This function determines whether a shadow_ship's set of co-ordinates are valid.
def validate_shadow_ship_coordinates(shadow_ship, ships_dict, board_min, board_max):
    valid = True
    for shadow_section in range(shadow_ship["ShipLength"]):
        valid = Validate.coordinates_on_board(board_min, board_max, shadow_ship[shadow_section])
        # print(f"validate_shadow_ship_coordinates function, coordinates_on_board value = {str(valid)}")
        if len(ships_dict) > 0 and valid:
            valid = not Validate.coordinate_crossover_check(ships_dict, shadow_ship[shadow_section])
        if not valid:
            return valid
    return valid


def extend_shadow_ship(shadow_ship, row_col=row_or_col(), growth_direction=pos_or_neg()):
    for j in range(1, shadow_ship["SectionsRemaining"]):
        shadow_ship[j] = {"IsHit": False, "col": shadow_ship[j - 1]["col"], "row": shadow_ship[j - 1]["row"]}
        shadow_ship[j][row_col] = shadow_ship[j - 1][row_col] + growth_direction
        shadow_ship["ShipLength"] = shadow_ship["ShipLength"] + 1
    return shadow_ship


def shadow_ship_generate(shadow_ship_len, shadow_ship_name, ships_dict, board_min, board_size):
    while True:
        shadow_ship = {
            "SectionsRemaining": shadow_ship_len,
            "ShipLength": 1,
            "name": shadow_ship_name,
            0: {'IsHit': False, 'col': random_row(board_size), 'row': random_row(board_size)}
        }
        shadow_ship = extend_shadow_ship(shadow_ship)
        valid_position = validate_shadow_ship_coordinates(shadow_ship, ships_dict, board_min, board_size)
        # print(f"shadow_ship validation = {str(valid_position)}")
        if shadow_ship["ShipLength"] == shadow_ship_len and valid_position:
            return shadow_ship


def generate_ships(ship_count_x, ship_names_x, ship_lengths_x, board_min_x, board_size_x):
    ships_x = {}
    for i in range(ship_count_x):
        ships_x[i] = shadow_ship_generate(ship_lengths_x[i], ship_names_x[i], ships_x, board_min_x, board_size_x)
    return ships_x
