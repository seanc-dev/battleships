import Dictionaries
import Ships
import Validate

difficulty = "Hard"

board_def = Dictionaries.board_def
board_min = 1
board_max = board_def[difficulty]["board_size"]
test_ships_full = {
    0:
        {'SectionsRemaining': 2, 'ShipLength': 2, 'name': 'Frigate',
         0: {'col': 1, 'row': 4, 'IsHit': False},
         1: {'col': 2, 'row': 4, 'IsHit': False}
         },
    1:
        {'SectionsRemaining': 3, 'ShipLength': 3, 'name': 'Destroyer',
         0: {'col': 6, 'row': 2, 'IsHit': False},
         1: {'col': 5, 'row': 2, 'IsHit': False},
         2: {'col': 4, 'row': 2, 'IsHit': False}
         },
    2: {'SectionsRemaining': 4, 'ShipLength': 4, 'name': 'Battleship',
        0: {'col': 6, 'row': 6, 'IsHit': False},
        1: {'col': 6, 'row': 5, 'IsHit': False},
        2: {'col': 6, 'row': 4, 'IsHit': False},
        3: {'col': 6, 'row': 3, 'IsHit': False}
        }
}
test_ship = {
    'SectionsRemaining': 2, 'ShipLength': 2, 'name': 'Frigate',
    0: {'col': 2, 'row': 4, 'IsHit': False},
    1: {'col': 1, 'row': 4, 'IsHit': False}
}
off_board_coordinates = {"col": -2, "row": 5}
print(" ")

# Validate
print("Test Validate functions")
print(
    f"coordinates_on_board = {Validate.coordinates_on_board(board_min, board_max, off_board_coordinates)}")  # Should return false
print(
    f"coordinate_crossover_check = {Validate.coordinate_crossover_check(test_ships_full,test_ship[0])}")  # Should return..?
print(f"row_and_col_match = {str(Validate.row_and_col_match(test_ship[0], test_ship[1]))}")  # Should return false
print(" ")

# Ships
print("Test Ships functions")
print(f"Random row = {str(Ships.random_row((board_max)))}")
print(f"Random col = {str(Ships.random_col((board_max)))}")
print(f"row_or_col = {str(Ships.row_or_col())}")
print(f"growth_direction = {str(Ships.pos_or_neg())}")
print(
    f"validate_shadow_ship_coordinates = {str(Ships.validate_shadow_ship_coordinates(test_ship, test_ships_full, board_min, board_max))}")
extend_ship_test = {
    'SectionsRemaining': 3, 'ShipLength': 1, 'name': 'Testy McTestFace',
    0: {'col': 2, 'row': 4, 'IsHit': False}
}
extend_ship_test_full = Ships.extend_shadow_ship(extend_ship_test)
extend_ship_name = extend_ship_test_full["name"]
print(f"extend_ship_test_full (a.k.a {str(extend_ship_name)}) = {str(extend_ship_test_full)}")
shadow_ship = Ships.shadow_ship_generate(shadow_ship_len=4, shadow_ship_name="Test McTestface II",
                                         ships_dict=test_ships_full, board_min=board_min, board_size=board_max)
print(f"generated shadow ship = {str(shadow_ship)}")
