from ..Skills.base_skill import Base_Skill

class Base_Character:
    def __init__(self, base_stats: list, lvl: int):
        self.base_stats = base_stats
        self.stats = self.base_stats
        self.lvl = lvl
        self.hp = self.max_hp
        self.ATK = 1
        self.DEF = 1

    @property
    def base_stats(self):
        return self.__base_stats

    @base_stats.setter
    def base_stats(self, value: list):
        self.__base_stats = {
                'STR': 0,
                'INT': 0,
                'WIS': 0,
                'END': 0,
                'GUI': 0,
                'AGI': 0
            }
        if type(value) == list:
            self.__base_stats.update({
                'STR': value[0],
                'INT': value[1],
                'WIS': value[2],
                'END': value[3],
                'GUI': value[4],
                'AGI': value[5]
            })

    @property
    def max_hp(self):
        return (self.base_stats['END'] * 10) + (self.base_stats['WIS'] * 3) + (self.lvl * 15)

    @property
    def skills(self):
        return self.__skills

    @skills.setter
    def skills(self, skills: list):
        if not self.__skills:
            #todo: Add basic attack
            self.__skills = []
        self.__skills += [x for x in skills if isinstance(x, Base_Skill) and x not in self.__skills]


    def damage(self, value: int):
        value /= self.DEF
        if value < self.hp:
            self.hp -= value
        else:
            self.hp = 0
            self.die()

    def heal(self, value: int):
        self.hp += value
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def die(self):
        pass
