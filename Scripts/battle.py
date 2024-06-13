from ..Models import parameters
from ..Models.Characters.Players.base_player import Base_Player
from ..Models.Characters.Enemies.base_enemy import Base_Enemy
from ..Models.Gear.base_gear import Base_Gear
from ..Models.Skills.base_skill import Base_Skill

#todo: add index checks for all Input calls
def battle(player: Base_Player, enemy_array: list[Base_Enemy]):
    turncount = 0
    while (len(enemy_array) > 0):
        turncount += 1
        player.status()
        # todo: add code for displaying player details
        for enemy in enemy_array:
            enemy.status()
            # todo: also add code for displaying enemy details

        # PLAYER TURN
        print('TURN: ', turncount)
        print('---------------PLAYER TURN----------------')
        print('What do you want to do?')
        print('1 - Run\n2 - Item\n3 - Skill\n') #todo: move contents of this to parameters
        action = int(input('? '))

        inst_name = 'Null'

        if action == 1:
            pass #todo: implement 'run' logic
        else:
            # Pick instance
            print(f'What {'skill' if action == 3 else 'item'} do you want to use?') #todo: replace this and next instance of inline logic with updated parameters structure

            for i, j in enumerate(player.skills if action == 3 else player.items, 1):
                print(f'{i} - {j.name}')

            inst = int(input('? '))
            inst_name = player.skills[inst - 1].name

            # Pick target
            print('Who do you want to target?')
            print('1 - Player')
            for i, j in enumerate(enemy_array, 2):
                print(f'{i} - {j.name}')

            target_choice = int(input('? '))
            if target_choice == 1:
                target = player
            else:
                target = enemy_array[target_choice - 2]

            player.act(action, inst_name, target) #!: this won't work because it's written with parameter logic change in mind


        # ENEMY TURN
        print('---------------ENEMY TURN----------------')
        for enemy in enemy_array:
            # Each enemy runs their own predetermined battle script
            enemy.battle_script() #todo: implement enemy battle script
