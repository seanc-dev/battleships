import dictionaries
import ships
import validate
import game
import shot


difficulty = "Hard"

board_def = dictionaries.board_def
board_min = 1
board_max = board_def[difficulty]["board_size"]
test_ships_full = {
    0: {
        'SectionsRemaining': 2, 'length': 2, 'name': 'Frigate',
        0: {'col': 1, 'row': 4, 'IsHit': False},
        1: {'col': 2, 'row': 4, 'IsHit': False}
         },
    1: {
        'SectionsRemaining': 3, 'length': 3, 'name': 'Destroyer',
        0: {'col': 6, 'row': 2, 'IsHit': False},
        1: {'col': 5, 'row': 2, 'IsHit': False},
        2: {'col': 4, 'row': 2, 'IsHit': False}
         },
    2: {
        'SectionsRemaining': 4, 'length': 4, 'name': 'Battleship',
        0: {'col': 6, 'row': 6, 'IsHit': False},
        1: {'col': 6, 'row': 5, 'IsHit': False},
        2: {'col': 6, 'row': 4, 'IsHit': False},
        3: {'col': 6, 'row': 3, 'IsHit': False}
        }
}
test_ship = {
    'SectionsRemaining': 2, 'length': 2, 'name': 'Frigate',
    0: {'col': 3, 'row': 4, 'IsHit': False},
    1: {'col': 4, 'row': 4, 'IsHit': False}
}
off_board_coordinates = {"col": -2, "row": 5}
print(" ")

# Validate
print("Test Validate functions")
print(
    f"coordinates_on_board (should return false) = {validate.coordinates_on_board(board_min, board_max, off_board_coordinates)}")  # Should return false
print(
    f"coordinate_crossover_check (check whether test_ship is within test_ships_full) = {validate.coordinate_crossover_check(test_ships_full,test_ship[0])}")
print(f"row_and_col_match (should return false) = {str(validate.row_and_col_match(test_ship[0], test_ship[1]))}")  # Should return false
print(" ")

# Ships
print("Test Ships functions")
print(f"Random row (should be between 1 and {str(board_max)}) = {str(ships.random_row((board_max)))}")
print(f"Random col = {str(ships.random_col((board_max)))}")
print(f"row_or_col = {str(ships.row_or_col())}")
print(f"growth_direction = {str(ships.pos_or_neg())}")
print(
    "validate_shadow_ship_coordinates = {0}"
    .format(str(ships.validate_shadow_ship_coordinates(test_ship, test_ships_full, board_min, board_max))))
extend_ship_test = {
    'SectionsRemaining': 3, 'length': 1, 'name': 'Testy McTestFace',
    0: {'col': 2, 'row': 4, 'IsHit': False}
}
extend_ship_test_full = ships.extend_shadow_ship(extend_ship_test)
extend_ship_name = extend_ship_test_full["name"]
print(f"extend_ship_test_full (a.k.a {str(extend_ship_name)}) = {str(extend_ship_test_full)}")
shadow_ship = ships.shadow_ship_generate(shadow_ship_len=4, shadow_ship_name="Test McTestface II",
                                         ships_dict=test_ships_full, board_min=board_min, board_size=board_max)
print(f"generated shadow ship = {str(shadow_ship)}")

# difficulty = game.difficulty_response()
print("Difficulty = {0}".format(str(difficulty)))

# game_style = game.game_style()

print("Range of ship lengths (should be 1 more than {0}) = {1}"
      .format(board_def[difficulty]["ship_count"], str(ships.build_ship_lengths(board_def[difficulty]["ship_count"]))))

print(game.form_styles_list())
game.print_styles_list()

ship_names = dictionaries.extract_ship_names()
print('ship_names dict: {}'.format(str(ship_names)))
print('max int key of ship_names dict: {}'.format(str(game.find_max_int_key(ship_names['the robots are coming']))))

print("Initiate Game")
print(" ")
game_variables = game.init_game()

#shot.response_selection('ship_sunk', game_variables['style'], 'Shippy McShipface')