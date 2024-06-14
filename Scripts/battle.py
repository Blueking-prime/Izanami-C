from Models.parameters import moves
from Models.utils import random
from Models.Characters.Players.base_player import Base_Player, Base_Character
from Models.Characters.Enemies.base_enemy import Base_Enemy

def show_status(entity: Base_Character):
    print(f'{entity.name} current stats:    ', end='')

    print(f'HP: {entity.hp}/{entity.max_hp}', end='')
    try:
        print(f'; SP: {entity.sp}/{entity.max_sp}', end='')
    except AttributeError:
        pass

    print('')

    if entity.status_effect:
        print(f'{entity.name} is afflicted with {entity.status_effect}')


def battle(player: Base_Player, enemy_array: list[Base_Enemy]):
    print('=======================BATTLE START========================')
    turncount = 0
    max_enemy_speed =  max([x.stats['AGI'] for x in enemy_array])
    escape_chance = player.stats['AGI'] / max_enemy_speed if max_enemy_speed > 1 else 1
    while (len(enemy_array) > 0):
        turncount += 1
        print('TURN: ', turncount)

        player.status()
        show_status(player)
        for enemy in enemy_array:
            # todo: add way to distiguish between numerous same type enemies
            enemy.status()
            show_status(enemy)

        ########################## PLAYER TURN ############################
        print('---------------PLAYER TURN----------------')

        # Checks for valid input
        while True:
            print('What do you want to do?')
            for i, j in enumerate(moves, 1):
                print(f'{i} - {j}')

            action = int(input('? '))
            if action in range(1, len(moves) + 1):
                action -= 1
                break
            else:
                print('Invalid input!')
                continue

        inst_name = 'Null'

        if action == len(moves) - 1:
            if escape_chance >= 1 or random() < escape_chance:
                print('You ran away successfully!')
                break
            else:
                print("You couldn't run!")
        else:
            # Pick instance
            while True:
                print(f'What {moves[action]} do you want to use?')

                attr = player.__getattribute__(moves[action].lower())

                for i, j in enumerate(attr, 1):
                    print(f'{i} - {j.name}')

                inst = int(input('? '))
                if inst in range(1, len(attr) + 1):
                    inst_name = attr[inst - 1].name
                    break
                else:
                    print('Invalid choice')
                    continue

            # Pick target
            while True:
                print('Who do you want to target?')
                print('1 - Player')
                for i, j in enumerate(enemy_array, 2):
                    print(f'{i} - {j.name}')

                target_choice = int(input('? '))
                if target_choice in range(1, len(enemy_array) + 2):
                    if target_choice == 1:
                        target = player
                    else:
                        target = enemy_array[target_choice - 2]
                    break
                else:
                    print('Invalid target!')
                    continue

            print('----------------------')
            player.act(moves[action], inst_name, target)
            print('----------------------')


        # # ENEMY TURN
        # print('---------------ENEMY TURN----------------')
        # for enemy in enemy_array:
        #     # Each enemy runs their own predetermined battle script
        #     enemy.battle_script() #todo: implement enemy battle script


        for enemy in enemy_array:
            if not enemy.alive:
                enemy_array.remove(enemy)
