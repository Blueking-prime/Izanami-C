from Models.Characters.Players.player_models import Ronin
from Models.Characters.Enemies.enemy_models import Goblin
from Models.Gear.base_gear import Base_Gear
from Models.Skills.base_skill import Offensive_Skill, Heal_Skill
from Models.Maps.dungeon import Dungeon
from Models.parameters import gear

dummy = Ronin('mark')
sword = Base_Gear(gear[-1])
enemy1 = Goblin()
enemy2 = Goblin()

print(sword.name)
print(sword.slot)
print(sword.stats)

print(dummy.lvl)
print(dummy.stats)
print(dummy.hp)

dummy.equip_gear(sword)

print(dummy.stats)
print(dummy.hp)
print(dummy.sp)

dummy.level_up(105)
print(dummy.exp)
print(dummy.level_up_exp)
print(dummy.lvl)
print(dummy.hp)
print(dummy.stats)

fire = Offensive_Skill('Fire', 'fire', ['INT', 'STR'])
wind = Offensive_Skill('Wind', 'wind', ['INT', 'WIS'])
heal = Heal_Skill('Heal', ['GUI', 'WIS'])

dummy.skills = [fire, wind, heal]

while True:
    dun = Dungeon(enemy_types=[Goblin])
    print(dun.__dict__)
    dun.display_dungeon()

    print('-------------------------------------')
    while True:
        x = input('direction? ')
        if x == 'res':
            break
        if x == 'close':
            print(dummy.inventory)
            exit()
        dummy.move(dun, x)
