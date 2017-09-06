import dictionaries
from random import randint

def response_selection(response_type, game_style, ship_name=None):
    responses = dictionaries.extract_responses()
    option_count = responses[game_style][response_type]["optionCount"]
    randint_key = randint(0, option_count)
    if 'ship_sunk' in response_type:
        response_type_a = response_type + '_1'
        response_type_b = response_type + '_2'
        response_a = responses[game_style][response_type_a][randint_key]
        response_b = responses[game_style][response_type_b][randint_key]
        response = response_a + ship_name + response_b
    else:
        response = responses[game_style][response_type][randint_key]
    return response

