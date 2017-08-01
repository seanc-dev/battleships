def row_and_col_match(coordinates_1, coordinates_2):
    result = False
    if coordinates_1["row"] == coordinates_2["row"]:
        if coordinates_1["col"] == coordinates_2["col"]:
            result = True
    return result


def coordinate_crossover_check(ships, test_coordinates):
    for ship in ships:
        for ship_section in range(ships[ship]["ShipLength"]):
            match = row_and_col_match(ships[ship][ship_section], test_coordinates)
            if match:
                print(f"ship = {str(ship)}, ship section = {str(ship_section)}, row = {str(ships[ship][ship_section])}")
                return match
    return match


def coordinates_on_board(board_min, board_max, coordinates):
    valid = False
    # print("coordinates on board function: row = {0}, col = {1}".format(
    #     str(coordinates["row"]),
    #     str(coordinates["col"])
    # ))
    if board_min <= coordinates["row"] <= board_max and board_min <= coordinates["col"] <= board_max:
        valid = True
    return valid


