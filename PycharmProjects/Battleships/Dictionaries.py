# DEFINE LISTS & DICTIONARIES
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

ship_names = {
    2: "Frigate",
    3: "Destroyer",
    4: "Battleship",
    5: "Supercarrier"
}

responses = {
    "difficulty_selection": {
        "Easy": {
            "option_count": 1,
            0: "Alright, no shame in starting slow. You are just starting.. right?",
            1: "Baby steps? Are you a baby?"
        },
        "Medium": {
            "option_count": 0,
            0: "The Middle Way. What are you, a Buddhist?"
        },
        "Hard": {
            "option_count": 0,
            0: "Now that's what I'm talkin' bout. Don't fuck it up though."
        }
    }
}
