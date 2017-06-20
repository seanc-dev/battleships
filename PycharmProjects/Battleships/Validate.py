def row_and_col_match(coordinates_1, coordinates_2):
    result = False
    if coordinates_1["row"] == coordinates_2["row"]:
        if coordinates_1["col"] == coordinates_2["col"]:
            result = True
    return result


def ship_coordinates_valid(ships, test_coordinates):
    for ship in ships:
        for ship_section in range(1, ships[ship]["ShipLength"] + 1):
            match = row_and_col_match(ships[ship][ship_section], test_coordinates)
            if match:
                return not match
    return not match


def coordinates_on_board(board_min, board_max, coordinates):
    valid = False
    if coordinates["row"] >= board_min:
        if coordinates["row"] <= board_max:
            if coordinates["col"] >= board_min:
                if coordinates["row"] <= board_max:
                    valid = True
    return valid
