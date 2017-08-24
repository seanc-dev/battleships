

def row_and_col_match(coordinates_1, coordinates_2):
    result = False
    if coordinates_1["row"] == coordinates_2["row"]:
        if coordinates_1["col"] == coordinates_2["col"]:
            result = True
    return result


def coordinate_crossover_check(ships, test_coordinates):
    for ship in ships:
        for ship_section in range(ships[ship]["length"]):
            match = row_and_col_match(ships[ship][ship_section], test_coordinates)
            if match:
                return match
    return match


def coordinates_on_board(board_min, board_max, coordinates):
    valid = False
    if board_min <= coordinates["row"] <= board_max and board_min <= coordinates["col"] <= board_max:
        valid = True
    return valid


# Check that coordinates are valid
def coordinates_guess(coordinates, board_dict, previous_coordinates):
    valid = coordinates_on_board(board_dict["board_min"], board_dict["board_max"], coordinates)
    if not valid:
        print("Sorry, those co-ordinates aren't on the board! Guess again.")
        return valid  # This is more efficient and has no downside
    for previous_coordinate in previous_coordinates:
        valid = not row_and_col_match(coordinates, previous_coordinate)
        if not valid:
            print("Sorry, you've guessed these co-ordinates before! Guess again.")
            return valid
