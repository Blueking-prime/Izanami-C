from Models.parameters import moves
from Models.utils import random, dialog_choice
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
    print(f'ATK:{entity.ATK} | DEF:{entity.DEF}')

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
        if player.status_effect != 'Stunned':
            # Checks for valid input
            action = dialog_choice('What do you want to do?', moves) - 1

            inst_name = 'Null'

            if action == len(moves) - 1:
                if escape_chance >= 1 or random() < escape_chance:
                    print('You ran away successfully!')
                    break
                else:
                    print("You couldn't run!")
            else:
                # Pick instance
                attr = player.__getattribute__(moves[action].lower())
                inst = dialog_choice(f'What {moves[action]} do you want to use?', [i.name for i in attr])
                inst_name = attr[inst - 1].name

                target_choice = dialog_choice('Who do you want to target?', [player.name, *[i.name for i in enemy_array]])
                if target_choice == 1:
                    target = player
                else:
                    target = enemy_array[target_choice - 2]

                print('----------------------')
                player.act(moves[action], inst_name, target)
                print('----------------------')
        else:
            print("You are stunned, you can't move")

        for enemy in enemy_array:
            if enemy.status_effect == 'Death':
                enemy.die()
            if not enemy.alive:
                enemy_array.remove(enemy)

        # # ENEMY TURN
        # print('---------------ENEMY TURN----------------')
        # for enemy in enemy_array:
        #     # Each enemy runs their own predetermined battle script
        #     enemy.battle_script() #todo: implement enemy battle script

    player.status_effect = None
    player.ATK = 1
    player.DEF = 1





if __name__ == '__main__':
    pass
