from random import randint
import dictionaries
import board
import validate

## DEFINE LISTS & DICTIONARIES ##
board_def = dictionaries.board_def
ship_names = dictionaries.ship_names

ship_lengths = list()
ships_remaining = list()
misses_remaining = list()
guess_coordinates = dict()
board_start = 1
guesses = dict()


## DEFINE FUNCTIONS ##

def generate_board(board_xy):
    board_f = []
    for i in range(board_xy + 1):
        nextrow = []
        if i == 0:
            toprow = []
            for j in range(board_xy + 1):
                if j == 0:
                    toprow.append(" ")
                else:
                    toprow.append(str(j))
            board_f.append(toprow)
        else:
            nextrow.append(str(i))
            for j in range(2, board_xy + 2):
                nextrow.append("-")
            board_f.append(nextrow)
    return board_f


def print_board(board_f):
    for row in board_f:
        print(" ".join(row))


# Define random row function to gen ship row for ship positions fun
def random_row(board_len):
    return randint(1, board_len)


# Define random col function to gen ship col for ship positions fun
def random_col(board_len):
    return randint(1, board_len)


# Define random binary int to determine whether ship stretches along row or col
def row_or_col():
    bin = randint(0, 1)
    if bin == 0:
        return "row"
    else:
        return "col"


# Define random binary int to define whether ship grows pos or neg
def pos_or_neg():
    bin = randint(0, 1)
    if bin == 0:
        return -1
    if bin == 1:
        return 1


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


# This function determines whether a shadow_ship's set of co-ordinates are valid.
def shadow_ship_coordinates_valid(shadow_ship, ships):
    valid = True
    for shadow_section in range(1, shadow_ship["ShipLength"] + 1):
        valid = validate.coordinates_on_board(board_start, board_def[difficulty]["board_size"], shadow_ship[shadow_section])
        if len(ships) > 0 & valid:
            valid = ship_coordinates_valid(ships, shadow_section)
        if not valid:
            return valid
    return valid


def shadow_ship_generate(shadow_ship_len, shadow_ship_name, ships_dict):
    # valid_position = False
    while True:  # Not valid_position
        shadow_ship = {"SectionsRemaining": shadow_ship_len, "ShipLength": 1, "name": shadow_ship_name,
                       1: {"IsHit": False, "row": random_row(board_def[difficulty]["board_size"]), "col":
                           random_row(board_def[difficulty]["board_size"])}}
        # Set starting co-values for this ship
        growth_direction = pos_or_neg()  # Set growth direction for ship from initial co-ordinates
        row_col = row_or_col()  # Set value to define whether ship grows a]long row or up/down col
        # Define loop to generate remainder of shadow_ship:
        for j in range(2, ship_lengths[i] + 1):
            shadow_ship["ShipLength"] = shadow_ship["ShipLength"] + 1
            shadow_ship[j] = {"IsHit": False, "col": shadow_ship[j - 1]["col"], "row": shadow_ship[j - 1]["row"]}
            shadow_ship[j][row_col] = shadow_ship[j - 1][row_col] + growth_direction
        valid_position = shadow_ship_coordinates_valid(shadow_ship, ships_dict)
        if shadow_ship["ShipLength"] == shadow_ship_len and valid_position:
            return shadow_ship
        # else:
        # valid_position = False


def generate_ships(ship_count_x, ship_names_x, ship_lengths_x):
    ships_x = dict()
    for i in range(ship_count_x):
        ships_x[i] = shadow_ship_generate(ship_lengths_x[i], ship_names_x[i], ships_x)
    return ships_x


# Check that coordinates are valid
def coordinates_valid(coordinates, board, previous_coordinates):
    coordinates_valid = True
    if coordinates["row"] < 0 or coordinates["row"] > len(board) or coordinates["col"] < 0 or coordinates["col"] > \
            board_def[difficulty]["board_size"]:
        coordinates_valid = False
        print("Sorry, those co-ordinates aren't on the board! Guess again.")
    for previous_coordinate in previous_coordinates:
        if previous_coordinates[previous_coordinate]["row"] == coordinates["row"]:
            if previous_coordinates[previous_coordinate]["col"] == coordinates["col"]:
                coordinates_valid = False
                print("Sorry, you've guessed these co-ordinates before! Guess again.")
    return coordinates_valid


def hit_miss(coordinates, ships, misses_remaining_f, ships_remaining_f):
    for ship in ships:
        for ship_section in range(1, ships[ship]["ShipLength"] + 1):
            outcomes = dict()
            outcomes["game_over"] = False
            # outcomes["IsHit"] = False
            if coordinates["row"] == ships[ship][ship_section]["row"] and ships[ship][ship_section]["col"] == \
                    coordinates["col"]:
                outcomes["IsHit"] = True
                outcomes["response"] = "That's a direct hit!"
                ships[ship][ship_section]["IsHit"] = True
                ships[ship]["SectionsRemaining"] = ships[ship]["SectionsRemaining"] - 1
                if ships[ship]["SectionsRemaining"] == 0:
                    ships_remaining_f = ships_remaining_f - 1
                    if ships_remaining_f == 1:
                        outcomes["response"] = "That\'s a direct hit, you sunk the {0}! Only 1 ship to go!".format(
                            str(ships[ship]["name"]))
                    else:
                        outcomes["response"] = "That\'s a direct hit, you sunk the {0}! Only {1} ships to go!".format(
                            str(ships[ship]["name"]), str(ships_remaining_f))
                    if ships_remaining_f == 0:
                        outcomes["response"] = "Congratulations! You sunk the {0}!".format(str(
                            ships[ship]["name"]))
                        outcomes["game_over"] = True
            else:
                outcomes["response"] = "Miss! Try again!"
                outcomes["IsHit"] = False
            if outcomes["IsHit"]:
                break
        if outcomes["IsHit"]:
            break
    if not outcomes["IsHit"]:
        misses_remaining_f = misses_remaining_f - 1
        if misses_remaining_f == 1:
            outcomes["response"] = "Miss! Careful, you only have one incorrect guess left!"
        elif misses_remaining_f == 0:
            outcomes["response"] = "Miss! Oh no, you've run out of guesses!"
            outcomes["game_over"] = True
    outcomes["misses_remaining"] = misses_remaining_f
    outcomes["ships_remaining"] = ships_remaining_f
    return outcomes


def update_board(update_coordinates, board_x, value):
    board_x[update_coordinates["row"]][update_coordinates["col"]] = value
    return board_x


# GAME FLOW

play = "Y"

while play == "Y":

    # Open initial loop

    # Setup input:

    print("Let's play Battleships!")

    while True:
        try:
            difficulty = input("Do you want the game to be Easy, Medium, or Hard? ")
        except ValueError:
            print("Sorry that's not a valid difficulty! Please try again.")
            continue
        else:
            break

    while difficulty not in ["Easy", "Medium", "Hard"]:
        print("Sorry, that's not a valid difficulty! Please try again")
        # print("Do you want the game to be Easy, Medium, or Hard?")
        difficulty = input("Do you want the game to be Easy, Medium, or Hard? ")

    if difficulty == "Easy":
        print("Alright, no shame in starting slow. You are just starting.. right?")
    elif difficulty == "Medium":
        print("The Middle Way. What are you, a Buddhist?")
    elif difficulty == "Hard":
        print("Now that's what I'm talkin' bout. Don't fuck it up though.")

    # Define lists now that difficulty is known
    for i in range(board_def[difficulty]["ship_count"]):
        ship_lengths.append(i + 2)

    ships_remaining = board_def[difficulty]["ship_count"]
    misses_remaining = board_def[difficulty]["misses_allowed"]
    board = board.generate(board_def[difficulty]["board_size"])

    print(" ")
    print("There are {0} ships somewhere in this ocean..".format(str(board_def[difficulty]["ship_count"])))
    print("Destroy them all to win!")
    print(" ")
    print_board(board)
    print(" ")
    ships = generate_ships(board_def[difficulty]["ship_count"], ship_names, ship_lengths)
    print(ships)

    # Generate and print board with ship locations
    ship_locations = board.generate(board_def[difficulty]["board_size"])
    for ship in ships:
        for ship_section in range(1, ships[ship]["ShipLength"] + 1):
            # print("ship = {0}".format(str(ship)) + ", ship_section = {0}".format(str(ship_section)))
            # print("{0}{1}".format("row = {0}".format(str(ships[ship][ship_section]["row"])),
            #                       ", col = {0}".format(str(ships[ship][ship_section]["col"])))ww)
            ship_locations = update_board(ships[ship][ship_section], ship_locations, str(ship))

    print("You can play by selecting a row and a column.")
    print(
        "Guess carefully though! You only have {0} misses at this level before YOU\'RE sunk!".format(
            str(misses_remaining)))

    game_over = False
    coordinate_no = 0

    while not game_over:

        coordindate_no = coordinate_no + 1

        valid_coordinates = False

        while not valid_coordinates:

            while True:
                try:
                    while not valid_coordinates:
                        guess_coordinates["col"] = int(input("Guess Column: "))
                        guess_coordinates["row"] = int(input("Guess Row: "))
                        valid_coordinates = coordinates_valid(guess_coordinates, board, guesses)
                except ValueError:
                    print("Make sure you enter a number between {0} and {1}.".format(
                        str(board_start), str(board_def[difficulty]["board_size"])))
                    continue
                else:
                    break

        guesses[coordinate_no] = {}
        guesses[coordinate_no]["row"] = guess_coordinates["row"]
        guesses[coordinate_no]["col"] = guess_coordinates["col"]

        outcomes = hit_miss(guess_coordinates, ships, misses_remaining, ships_remaining)
        print(" ")
        print(outcomes["response"])
        print(" ")
        misses_remaining = outcomes["misses_remaining"]
        ships_remaining = outcomes["ships_remaining"]
        game_over = outcomes["game_over"]

        # print(outcomes)
        # input("Press any key to see the updated board.")

        if outcomes["IsHit"]:
            board = update_board(guess_coordinates, board, "X")
        else:
            board = update_board(guess_coordinates, board, "O")

        # TEST print solution
        #print_board(ship_locations)
        print(" ")

        # Print game board
        print_board(board)
        print(" ")

        if not game_over:
            if outcomes["IsHit"]:
                print("Guess again, wise guy")
            else:
                print("Guess again, sucker!")
        else:
            if ships_remaining == 0:
                print("You\'ve won the game! I bet you're pleased with yourself..")
            else:
                print("Oh God I'm embarrassed for you.")
        print(" ")

    play = input("Play again? (Y/N): ")
