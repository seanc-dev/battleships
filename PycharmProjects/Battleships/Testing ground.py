import Dictionaries
board_def = Dictionaries.board_def
ship_names = Dictionaries.ship_names



def row_and_col_match(coordinates_1,coordinates_2):
    result = False
    if  coordinates_1["row"] == coordinates_2["row"]:
        if coordinates_1["col"] == coordinates_2["col"]:
            result = True
    return result

def ship_coordinate_match(ships,test_coordinates):
    for ship in ships:
        for ship_section in range(1, ships[ship]["ShipLength"]+1):
            match = row_and_col_match(ships[ship][ship_section],test_coordinates)
            if match:
                break
        if match:
            break
    return match