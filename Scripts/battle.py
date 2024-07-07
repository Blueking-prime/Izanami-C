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
    turncount = 1
    max_enemy_speed =  max([x.stats['AGI'] for x in enemy_array])
    escape_chance = player.stats['AGI'] / max_enemy_speed if max_enemy_speed > 1 else 1

    player.status()
    show_status(player)
    for enemy in enemy_array:
        # todo: add way to distiguish between numerous same type enemies
        enemy.status()
        show_status(enemy)

    while True:
        print('TURN: ', turncount)
        player.DEF = 1
        ########################## PLAYER TURN ############################
        print('---------------PLAYER TURN----------------')
        if player.status_effect != 'Stunned':
            # Checks for valid input
            action = dialog_choice('What do you want to do?', moves, back=False) - 1

            match action:
                case 0: # Run
                    if escape_chance >= 1 or random() < escape_chance:
                        print('You ran away successfully!')
                        break
                    else:
                        print("You couldn't run!")
                case 1: # Defend
                    player.DEF *= 2
                    print("You brace for the enemy's attack")
                case _: # Skills, Items
                    attr = player.__getattribute__(moves[action].lower())
                    inst = dialog_choice(f'What {moves[action]} do you want to use?', [i.name for i in attr])
                    match inst:
                        case 0:
                            continue
                        case -1:
                            print('None found')
                            continue
                        case _:
                            inst_name = attr[inst - 1].name

                    target_choice = dialog_choice('Who do you want to target?', [player.name, *[i.name for i in enemy_array]])
                    match target_choice:
                        case 0:
                            continue
                        case 1:
                            target = player
                        case _:
                            target = enemy_array[target_choice - 2]

                    print('----------------------')
                    x = player.act(moves[action], inst_name, target)
                    print(x)
                    if not x:
                        continue
                    print('----------------------')
        else:
            print("You are stunned, you can't move")

        player.ATK = 1

        for enemy in enemy_array:
            if enemy.status_effect == 'Death':
                player.gold += enemy.gold_drop
                player.level_up(enemy.exp_drop)
                enemy.die()

        if len(enemy_array) < 1:
            print("You've defeated all the enemies!")
            break

        # ENEMY TURN
        print('---------------ENEMY TURN----------------')
        for enemy in enemy_array:
            # Each enemy runs their own predetermined battle script
            enemy.battle_script(player) #todo: implement enemy battle script

        turncount += 1
        player.restore()

        player.status()
        show_status(player)
        for enemy in enemy_array:
            # todo: add way to distiguish between numerous same type enemies
            enemy.status()
            show_status(enemy)

    player.status_effect = None
    player.ATK = 1
    player.DEF = 1
    player.sp = player.max_sp

    return 0




if __name__ == '__main__':
    pass
