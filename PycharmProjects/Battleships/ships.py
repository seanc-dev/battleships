from random import randint
import validate


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


def build_ship_lengths(ship_count):  # This list should be appending values in the place of a new list item
    lengths = [(i + 2) for i in range(ship_count)]
    return lengths


# This function determines whether a shadow_ship's set of co-ordinates are valid.
def validate_shadow_ship_coordinates(shadow_ship, ships_dict, board_min, board_max):
    valid = True
    for shadow_section in range(shadow_ship["length"]):
        valid = validate.coordinates_on_board(board_min, board_max, shadow_ship[shadow_section])
        # print(f"validate_shadow_ship_coordinates function, coordinates_on_board value = {str(valid)}")
        if len(ships_dict) > 0 and valid:
            valid = not validate.coordinate_crossover_check(ships_dict, shadow_ship[shadow_section])
        if not valid:
            return valid
    return valid


def extend_shadow_ship(shadow_ship, row_col=row_or_col(), growth_direction=pos_or_neg()):
    for j in range(1, shadow_ship["SectionsRemaining"]):
        shadow_ship[j] = {"is_hit": False, "col": shadow_ship[j - 1]["col"], "row": shadow_ship[j - 1]["row"]}
        shadow_ship[j][row_col] = shadow_ship[j - 1][row_col] + growth_direction
        shadow_ship["length"] = shadow_ship["length"] + 1
    return shadow_ship


def shadow_ship_generate(shadow_ship_len, shadow_ship_name, ships_dict, board_min, board_size):
    while True:
        shadow_ship = {
            "SectionsRemaining": shadow_ship_len,
            "length": 1,
            "name": shadow_ship_name,
            "sunk": False,
            0: {'IsHit': False, 'col': random_row(board_size), 'row': random_row(board_size)}
        }
        shadow_ship = extend_shadow_ship(shadow_ship)
        valid_position = validate_shadow_ship_coordinates(shadow_ship, ships_dict, board_min, board_size)
        # print(f"shadow_ship validation = {str(valid_position)}")
        if shadow_ship["length"] == shadow_ship_len and valid_position:
            return shadow_ship


def generate_ships(ship_count, ship_names, board_min, board_size):
    ships = {}
    ship_lengths = build_ship_lengths(ship_count)
    for i in range(ship_count):
        ships[i] = shadow_ship_generate(ship_lengths[i], ship_names[i], ships, board_min, board_size)
    return ships
