from Models.Characters.Players.player_models import Ronin
from Models.Characters.Enemies.enemy_models import Goblin
from Models.Gear.base_gear import Base_Gear
from Models.Skills.base_skill import Offensive_Skill, Heal_Skill
from Models.Maps.dungeon import Dungeon
from Scripts.battle import battle

dummy = Ronin('mark')
sword = Base_Gear([0, 1, 0, 3, 1, 1], 'weapon')
enemy1 = Goblin()
enemy2 = Goblin()

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


dun = Dungeon()
print(dun.__dict__)
dun.display_dungeon()

print('-------------------------------------')
dummy.move(dun, 'u')
dun.display_dungeon()


print('-------------------------------------')
enemies = [enemy1, enemy2]
battle(dummy, enemies)