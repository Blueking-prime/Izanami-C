from .base_player import Base_Player

class Doctor(Base_Player):
    desc = "A healer of men, a combat medic, a learned medicine man. Though you've spent your whole life giving life those who may not even deserve, you seek a weapon that can only take. Your skill with people and bodies will serve you well"

    def __init__(self, base_stats: list = [0,4,6,0,2,0], lvl: int = 1):
        super().__init__(base_stats, lvl)
