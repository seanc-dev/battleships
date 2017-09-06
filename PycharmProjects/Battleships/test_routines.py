import dictionaries
import ships
import validate
import game
from game import test_print
import shot
import board


difficulty = "Hard"

board_def = dictionaries.board_def
board_min = 1
board_max = board_def[difficulty]["board_max_dim"]
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

'''
print(" ")

# Validate
print("Test Validate functions")
print(
    f"coordinates_on_board (should return false) = {validate.coordinates_on_board(board_min, board_max, off_board_coordinates)}")  # Should return false
#print('test_ship[0]: '.format(str(test_ship[0])))
print(
    f"coordinate_crossover_check (check whether test_ship is within test_ships_full) = {validate.coordinate_crossover_check(test_ships_full,test_ship[0])}")
print(f"row_and_col_match (should return false) = {str(validate.row_and_col_match(test_ship[0], test_ship[1]))}")  # Should return false
game_variables = game.build_game_variables()

print('coordinates on board (true): {}'.format(str(validate.coordinates_on_board(board_min, board_max, test_ship[1]))))
print(validate.coordinates_guess(test_ship[0], game_variables['board_dimensions'], game_variables['guesses']))


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

'''
print("Initiate Game")
print(" ")

game_variables = game.init_game()

print(game_variables)

game_variables = game.fire_away(game_variables, guess_number=0)

# difficulty = "Hard"
#game_variables = {'guesses': {}, 'difficulty': 'Hard', 'style': 'the robots are coming', 'misses_remaining': 12, 'ships_remaining_afloat': 4, 'board_dimensions': {'min': 1, 'max': 8}, 'board': [[' ', '1', '2', '3', '4', '5', '6', '7', '8'], ['1', '-', '-', '-', '-', '-', '-', '-', '-'], ['2', '-', '-', '-', '-', '-', '-', '-', '-'], ['3', '-', '-', '-', '-', '-', '-', '-', '-'], ['4', '-', '-', '-', '-', '-', '-', '-', '-'], ['5', '-', '-', '-', '-', '-', '-', '-', '-'], ['6', '-', '-', '-', '-', '-', '-', '-', '-'], ['7', '-', '-', '-', '-', '-', '-', '-', '-'], ['8', '-', '-', '-', '-', '-', '-', '-', '-']], 'ships': {0: {'sections_remaining': 2, 'length': 2, 'name': 'Frigate', 'sunk': False, 0: {'is_hit': False, 'col': 7, 'row': 6}, 1: {'is_hit': False, 'col': 6, 'row': 6}}, 1: {'sections_remaining': 3, 'length': 3, 'name': 'Destroyer', 'sunk': False, 0: {'is_hit': False, 'col': 7, 'row': 4}, 1: {'is_hit': False, 'col': 6, 'row': 4}, 2: {'is_hit': False, 'col': 5, 'row': 4}}, 2: {'sections_remaining': 4, 'length': 4, 'name': 'Battleship', 'sunk': False, 0: {'is_hit': False, 'col': 6, 'row': 5}, 1: {'is_hit': False, 'col': 5, 'row': 5}, 2: {'is_hit': False, 'col': 4, 'row': 5}, 3: {'is_hit': False, 'col': 3, 'row': 5}}, 3: {'sections_remaining': 5, 'length': 5, 'name': 'Supercarrier', 'sunk': False, 0: {'is_hit': False, 'col': 8, 'row': 1}, 1: {'is_hit': False, 'col': 7, 'row': 1}, 2: {'is_hit': False, 'col': 6, 'row': 1}, 3: {'is_hit': False, 'col': 5, 'row': 1}, 4: {'is_hit': False, 'col': 4, 'row': 1}}}}



#
# game_counter = 0
# game_outcomes = {}
#
# game_won = False
# game_lost = False
#
# while not game_won or not game_lost:
#
#     difficulty = 'Hard'
#     board_dict = dictionaries.board_def[difficulty]
#     ship_names = dictionaries.extract_ship_names()
#     game_variables = {'guesses': {}, 'difficulty': difficulty, 'style': 'the robots are coming',
#                       'misses_remaining': board_dict["misses_allowed"],
#                       'ships_remaining_afloat': board_dict["ship_count"],
#                       'board_dimensions': {'min': board_dict["board_min_dim"], 'max': board_dict["board_max_dim"]}}
#     game_variables["board"] = board.generate(game_variables["board_dimensions"]["max"])
#     game_variables["ships"] = ships.generate_ships(board_dict["ship_count"],
#         ship_names[game_variables['style']][ships.randint(0, game.find_max_int_key(ship_names[game_variables['style']]))],
#         game_variables["board_dimensions"]["min"], game_variables["board_dimensions"]["max"]
#                                                    )
#     game_variables['outcomes'] = {}
#     game_variables['outcomes']['all_ships_sunk'] = False
#     game_variables['outcomes']['all_guesses_used'] = False
#     game_variables['misses_remaining'] = 30
#
#     guess_counter = 0
#
#     while not game_variables['outcomes']['all_ships_sunk'] and not game_variables['outcomes']['all_guesses_used']:
#
#         game_variables['guesses'][guess_counter] = {
#             'row': ships.randint(1, 8),
#             'col': ships.randint(1, 8)
#         }
#
#         # game_variables['guesses'][coordinate_no] = shot.request_coordinates(
#         #     game_variables['guesses'], game_variables['board_dimensions'])
#         game_variables = shot.outcomes_and_update(guess_counter, game_variables)
#         test_print('outcomes', game_variables['outcomes'])
#         if game_variables['outcomes']['sunk']:
#             test_print('sunk ship ships:', game_variables['ships'])
#
#         # for ship in game_variables['ships']:
#         #     for ship_section in range(game_variables['ships'][ship]['length']):
#         #         if game_variables['ships'][ship][ship_section]['is_hit']:
#         #             print('hit ship: {}'.format(str(game_variables['ships'][ship])))
#
#         guess_counter += 1
#
#         if game_variables['outcomes']['all_ships_sunk']:
#             print('Game won, all ships sunk')
#             game_won = True
#         if game_variables['outcomes']['all_guesses_used']:
#             print('Game Lost, all guesses used')
#             game_lost = True
#
#     game_outcomes[game_counter] = {
#         'won': game_won,
#         'lost': game_lost,
#         'guesses': guess_counter
#     }
#
#     test_print('game over ships', game_variables['ships'])
#     test_print('game over outcomes', game_variables['outcomes'])
#
#     game_counter += 1
#
# print(game_outcomes)
#
# # shot.response_selection('ship_sunk', game_variables['style'], 'Shippy McShipface')
#
