# DEFINE LISTS & DICTIONARIES

from csv import DictReader

board_def = dict()

board_def['Easy'] = {}
board_def['Easy']['board_min_dim'] = 1
board_def['Easy']['board_max_dim'] = 4
board_def['Easy']['ship_count'] = 2
board_def['Easy']['ship_max_size'] = 3
board_def['Easy']['misses_allowed'] = 8

board_def['Medium'] = {}
board_def['Medium']['board_min_dim'] = 1
board_def['Medium']['board_max_dim'] = 6
board_def['Medium']['ship_count'] = 3
board_def['Medium']['ship_max_size'] = 4
board_def['Medium']['misses_allowed'] = 10

board_def['Hard'] = {}
board_def['Hard']['board_min_dim'] = 1
board_def['Hard']['board_max_dim'] = 8
board_def['Hard']['ship_count'] = 4
board_def['Hard']['ship_max_size'] = 5
board_def['Hard']['misses_allowed'] = 12


difficulty_options = {
    'Easy': {
        'option_count': 1,
        0: 'Alright, no shame in starting slow. You are just starting.. right?',
        1: 'Baby steps? Are you a baby?'
    },
    'Medium': {
        'option_count': 0,
        0: 'The Middle Way. What are you, a Buddhist?'
    },
    'Hard': {
        'option_count': 0,
        0: 'Now that''s what I''m talkin'' bout. Don''t fuck it up though.'
    }
}


def boolify(s):
    if s == 'True' or s == 'true':
            return True
    if s == 'False' or s == 'false':
            return False
    raise ValueError('Not Boolean Value!')


def typeCast(var):
    if type(var) not in (dict, list):
        tempVar = var
        for caster in (boolify, int, float):
                try:
                        return caster(tempVar)
                except ValueError:
                        pass
        if type(var) is not type(tempVar):
            var = tempVar
    return var


def append_new_dict(new_item, housing_dict, item_to_append):
    if new_item is not None:
        new_item_x = typeCast(new_item)
        item_to_append_x = typeCast(item_to_append)
        if new_item_x not in housing_dict:
            housing_dict[new_item_x] = item_to_append_x
    return housing_dict


def unpack_csv(filename, headers):
    delimiter = ','
    with open(filename, 'r') as data_file:
        data = DictReader(data_file, delimiter=delimiter,
                          fieldnames=headers)
        temp_dict = {}
        i = 0
        for row in data:
            #print(row)
            row_dict = {}
            for item in row:
                row_dict[item] = typeCast(row[item])
            temp_dict[i] = row_dict
            i += 1
    return temp_dict


def extract_ship_names():
    data = unpack_csv('ship_names.csv', (['game_style', 'randomiser', 'ship_ID', 'name']))
    ship_names = {}
    for row in data:
        append_new_dict(data[row]['game_style'], ship_names, {})
        append_new_dict(data[row]['randomiser'], ship_names[data[row]['game_style']], {})
        append_new_dict(
            data[row]['ship_ID'], ship_names[data[row]['game_style']][data[row]['randomiser']], data[row]['name']
        )
    return ship_names


def extract_responses():
    data = unpack_csv('responses.csv', (['style', 'response_type', 'column_4', 'column_5']))
    responses = {}
    for row in data:
        append_new_dict(data[row]['style'], responses, {})
        append_new_dict(data[row]['response_type'], responses[data[row]['style']], {})
        append_new_dict(
            data[row]['column_4'], responses[data[row]['style']][data[row]['response_type']], data[row]['column_5']
        )
    return responses

# print(extract_ship_names())


ships = {
    0: {
        'sections_remaining': 2,
        'length': 2,
        'name': 'Frigate',
        'sunk': False,
        0: {
            'is_hit': False,
            'col': 7,
            'row': 6
        },
        1: {
            'is_hit': False,
            'col': 8,
            'row': 6
        }
    },
    1: {
        'sections_remaining': 0,
        'length': 3,
        'name': 'Destroyer',
        'sunk': False,
        0: {
            'is_hit': False,
            'col': 1,
            'row': 8
        },
        1: {
            'is_hit': True,
            'col': 2,
            'row': 8
        },
        2: {
            'is_hit': True,
            'col': 3
            , 'row': 8
        }
    },
    2: {
        'sections_remaining': 2,
        'length': 4,
        'name': 'Battleship',
        'sunk': False,
        0: {
            'is_hit': False,
            'col': 4,
            'row': 1
        },
        1: {
            'is_hit': False,
            'col': 5,
            'row': 1
        }, 2: {
            'is_hit': False,
            'col': 6,
            'row': 1
        }, 3: {
            'is_hit': True,
            'col': 7,
            'row': 1
        }
    },
    3: {
        'sections_remaining': 3,
        'length': 5,
        'name': 'Supercarrier',
        'sunk': False,
        0: {
            'is_hit': False,
            'col': 1,
            'row': 4
        },
        1: {
            'is_hit': False,
            'col': 2,
            'row': 4
        }, 2: {
            'is_hit': False,
            'col': 3,
            'row': 4
        },
        3: {
            'is_hit': False,
            'col': 4,
            'row': 4
        },
        4: {
            'is_hit': True,
            'col': 5,
            'row': 4
        }
    },
    'sunk': True
}
