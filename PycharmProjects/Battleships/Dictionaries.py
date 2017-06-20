
## DEFINE LISTS & DICTIONARIES ##
board_def = dict()

board_def["Easy"] = {}
board_def["Easy"]["board_size"] = 4
board_def["Easy"]["ship_count"] = 2
board_def["Easy"]["ship_max_size"] = 3
board_def["Easy"]["misses_allowed"] = 8

board_def["Medium"] = {}
board_def["Medium"]["board_size"] = 6
board_def["Medium"]["ship_count"] = 3
board_def["Medium"]["ship_max_size"] = 4
board_def["Medium"]["misses_allowed"] = 10

board_def["Hard"] = {}
board_def["Hard"]["board_size"] = 8
board_def["Hard"]["ship_count"] = 4
board_def["Hard"]["ship_max_size"] = 5
board_def["Hard"]["misses_allowed"] = 12

ship_names = {}
ship_names[2] = "Frigate"
ship_names[3] = "Destroyer"
ship_names[4] = "Battleship"
ship_names[5] = "Supercarrier"
