from Models.Characters.Players.base_player import Base_Player
from Models.Gear.base_gear import Base_Gear
from Models.Maps.dungeon import Dungeon

dummy = Base_Player('mark',[1, 1, 1, 1, 1, 1], 1)
sword = Base_Gear([0, 1, 0, 3, 1, 1], 'weapon')

print(sword.slot)
print(sword.stats)

print(dummy.lvl)
print(dummy.stats)
print(dummy.hp)

dummy.equip_gear(sword)

print(dummy.stats)
print(dummy.hp)
print(dummy.sp)

dummy.level_up(1)
print(dummy.lvl)
print(dummy.hp)

dun = Dungeon()
print(dun.__dict__)
dun.display_dungeon()

print('-------------------------------------')
dummy.move(dun, 'u')
dun.display_dungeon()
