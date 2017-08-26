# DEFINE LISTS & DICTIONARIES
board_def = dict()

board_def["Easy"] = {}
board_def["Easy"]["board_min"] = 1
board_def["Easy"]["board_size"] = 4
board_def["Easy"]["ship_count"] = 2
board_def["Easy"]["ship_max_size"] = 3
board_def["Easy"]["misses_allowed"] = 8

board_def["Medium"] = {}
board_def["Medium"]["board_min"] = 1
board_def["Medium"]["board_size"] = 6
board_def["Medium"]["ship_count"] = 3
board_def["Medium"]["ship_max_size"] = 4
board_def["Medium"]["misses_allowed"] = 10

board_def["Hard"] = {}
board_def["Hard"]["board_min"] = 1
board_def["Hard"]["board_size"] = 8
board_def["Hard"]["ship_count"] = 4
board_def["Hard"]["ship_max_size"] = 5
board_def["Hard"]["misses_allowed"] = 12

game_styles = {
    "Standard"
}

ship_names = {
    # "optionCount": 0,
    "key_lookup": {
        "standard": 0
    },
    0: {
        0: "Frigate",
        1: "Destroyer",
        2: "Battleship",
        3: "Supercarrier"
    }
}

responses = {
    "difficulty": {
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
    },
    "outcomes": {
        "hit": {
            "standard": ""
        },
        "game_won": {
            "standard": "This is bullshit! You shouldn't be able to beat me! I can think at the speed of light!"
        },
        "game_lost": "Hahaha sucker! You're no match for my light-speed information transmission and advanced\
         algorithms!"
    }
}
