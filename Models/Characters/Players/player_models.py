from .base_player import Base_Player
from ...Skills import player_skills

class Destitute(Base_Player):
    desc = "Born into poverty, not even the scraps on your back belong to you. Your birth was insignificant and your life a meaningless struggle, but alas you may yet find your worth in the pit."
    class_base_stats = [-1,-1,-1,-1,-1,-1]

    def __init__(self, name: str ,lvl: int = 1):
        super().__init__(name, Destitute.class_base_stats, lvl)
        self.level_stats = ["STR", "INT", "WIS", "END", "GUI", "AGI"]


class Doctor(Base_Player):
    desc = "A healer of men, a combat medic, a learned medicine man. Though you've spent your whole life giving life those who may not even deserve, you seek a weapon that can only take. Your skill with people and bodies will serve you well"
    class_base_stats = [0,4,6,0,2,0]

    def __init__(self, name: str ,lvl: int = 1):
        super().__init__(name, Doctor.class_base_stats, lvl)
        self.level_stats = ["INT", "WIS"]


class Farmer(Base_Player):
    desc = "A man of the earth who finds himself in depths far beyond him, you are strong from years of backbreaking labour and have always been known for your wit"
    class_base_stats = [2,2,2,2,2,2]
    def __init__(self, name: str ,lvl: int = 1):
        super().__init__(name, Farmer.class_base_stats, lvl)
        self.level_stats = ['STR', 'END']


class Ronin(Base_Player):
    desc = "A former samurai who has performed a slight against his lord, whether intentionally or not, whether righteously or not"
    class_base_stats = [6,0,0,2,0,4]

    def __init__(self, name: str ,lvl: int = 1):
        super().__init__(name, Ronin.class_base_stats, lvl)
        self.level_stats = ["STR", "AGI"]
        self.skills = player_skills.ronin_skills


class Shinobi(Base_Player):
    desc = "The shinobi are warriors whose existence is myth. They dance in shadow and attack only when moonlight strikes their targets eyes."
    class_base_stats = [0,4,0,0,0,8]

    def __init__(self, name: str ,lvl: int = 1):
        super().__init__(name, Shinobi.class_base_stats, lvl)
        self.level_stats = ["INT", "AGI"]
        self.skills = player_skills.shinobi_skills
