import dictionaries
import board
import ships


def difficulty_response():
    while True:
        try:
            difficulty_x = input("Do you want the game to be Easy, Medium, or Hard? ")
        except ValueError:
            print("Sorry that's not a valid difficulty! Please try again.")
            continue
        else:
            break
    while difficulty_x not in ["Easy", "Medium", "Hard"]:
        print("Sorry, that's not a valid difficulty! Please try again")
        # print("Do you want the game to be Easy, Medium, or Hard?")
        difficulty_x = input("Do you want the game to be Easy, Medium, or Hard? ")
    print(dictionaries.responses["difficulty"][difficulty_x][0])
    return difficulty_x


def build_ship_lengths(ship_count):  # board_def[difficulty]["ship_count"]
    for i in range(ship_count):
        lengths = list()
        lengths.append(i + 2)
    return lengths


def build_game_variables(board_dict, ship_names):  # board_def
    ship_lengths = build_ship_lengths(board_dict["ship_count"])
    game_variables = {}
    game_variables["ships_remaining"] = board_dict["ship_count"]
    game_variables["misses_remaining"] = board_dict["misses_allowed"]
    game_variables["board"] = board.generate_board(board_dict["board_size"])
    game_variables["ships"] = ships.generate_ships(board_dict["ship_count"], ship_names, ship_lengths)
    return game_variables


def fire_away():



def init_game():
    print("Let's play Battleships!")
    difficulty = difficulty_response()
    game_variables = build_game_variables(dictionaries.board_def[difficulty], dictionaries.ship_names)
    print(" ")
    print("There are {0} ships somewhere in this ocean..".format(str(game_variables["ships_remaining"])))
    print("Destroy them all to win!")
    print(" ")
    board.display(game_variables["board"])
    print(" ")
