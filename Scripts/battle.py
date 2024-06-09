from ..Models import parameters
from ..Models.Characters import Players, Enemies
from ..Models.Gear import base_gear

def battle():
    enemy_array = []
    turncount = 0
    while (len(enemy_array) > 0):
        turncount += 1
        