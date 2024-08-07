from ..Skills.base_skill import Base_Skill
from .. import parameters

class Base_Character:
    def __init__(self, name, base_stats: list, lvl: int):
        self.name = name
        self.base_stats = base_stats
        self.stats = self.base_stats
        self.lvl = lvl
        self.hp = self.max_hp
        self.ATK = 1
        self.DEF = 1
        self.status_effect = None
        self.alive = True

    @property
    def base_stats(self):
        return self.__base_stats

    @base_stats.setter
    def base_stats(self, value: list):
        self.__base_stats = dict.fromkeys(parameters.stats, 0)
        if type(value) == list:
            self.__base_stats.update(dict(zip(parameters.stats, value)))

    @property
    def max_hp(self):
        return (self.base_stats['END'] * 10) + (self.base_stats['WIS'] * 3) + (self.lvl * 15)

    @property
    def skills(self) -> list[Base_Skill]:
        return self.__skills

    @skills.setter
    def skills(self, skills: list):
        try:
            self.__skills
        except AttributeError:
            self.__skills = []
        self.__skills += [x for x in skills if isinstance(x, Base_Skill) and x not in self.__skills]


    def act(self, action: str, inst: str, target):
        if action == 'Skills':
            if self.status_effect == 'Sealed':
                print(f"{self.name} can't use skills!")
                return False
            return self.use_skill(inst, target)


    def use_skill(self, skill: str, target):
        for x in self.skills:
            if x.name == skill:
                return x.action(self, target)
        return False

    def damage(self, value: float):
        value /= self.DEF
        print(f'{self.name} takes {value} damage!')
        if value < self.hp:
            self.hp -= value
        else:
            self.hp = 0
            self.die()

    def heal(self, value: float):
        self.hp += value
        print(f'{self.name} healed {value} HP')
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def status(self):
        if self.status_effect == 'Toxin':
            self.damage(self.max_hp / 7)

    def die(self):
        print(f'{self.name} is dead')
        self.alive = False
