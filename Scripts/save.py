import json
from datetime import datetime
from os import listdir
from Models import parameters, checks
from Models.utils import dialog_choice
from Models.Characters.Players import base_player
from Models.Characters.Players import player_models

save_folder = 'Saves'
saved_keys = ["name", 'lvl', 'hp', 'sp', 'exp', 'gold', 'mag', "_Base_Character__base_stats"]

def save(player: base_player.Base_Player):
    player_data = {key: player.__dict__[key] for key in saved_keys}

    player_data['class'] = player.__class__.__name__
    player_data['inventory'] = {}
    player_data['gear'] = {}

    for i, j in player.__dict__['gear'].items():
        player_data['gear'].update({i: j.name if j else None})

    for i in player.__dict__["inventory"]:
        player_data["inventory"].update({i.name: i.__class__.__name__})

    save_file = save_folder + '/' + datetime.now().isoformat() + '.json'

    game_state = {
        'player_data': player_data,
        'checks': {i: getattr(checks, i) for i in dir(checks) if not i.startswith('__')}
    }

    with open(save_file, 'w') as s:
        json.dump(game_state, s, indent=4)


def load():
    save_files = listdir(save_folder)
    if len(save_files) == 0:
        print('No save files found')
        return None
    while True:
        x = dialog_choice("What save file do you want to load?", save_files) - 1
        if x < 0:
            return None
        confirm = dialog_choice(f"Confirm", back=False)
        if not confirm:
            continue

        save_file = save_folder + '/' + save_files[x]
        with open(save_file, 'r') as s:
            game_state = json.load(s)

        player_data = game_state['player_data']
        checks_data = game_state['checks']

        for i, j in checks_data.items():
            setattr(checks, i, j)

        for i, j in player_data['gear'].items():
            for k in parameters.gear:
                if k['name'] == j:
                    player_data['gear'][i] = base_player.Base_Gear(k)
                    break


        equipment = parameters.gear + parameters.items
        player_inventory_list = []
        for i, j in player_data['inventory'].items():
            for k in equipment:
                if k['name'] == i:
                    player_inventory_list.append(getattr(base_player, j)(k))
                    break


        player = getattr(player_models, player_data['class'])(player_data['name'])
        player.inventory = player_inventory_list
        player.gear = player_data['gear']

        player_data = {key: player_data[key] for key in saved_keys}

        for i in player_data:
            player.__setattr__(i, player_data[i])
        break

    return player




# def pretty(d: dict, indent=0):
#     for key, value in d.items():
#         print('\t' * indent, key)
#         if isinstance(value, dict):
#             pretty(value, indent=1)
#         else:
#             print('\t' * (indent+1), str(value))