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
        self.status_effect = None

    @property
    def base_stats(self):
        return self.__base_stats

    @base_stats.setter
    def base_stats(self, value: list):
        self.__base_stats = dict.fromkeys(parameters.stats, 0)
        self.__base_stats = dict.fromkeys(parameters.stats, 0)
        if type(value) == list:
            self.__base_stats.update(dict(zip(parameters.stats, value)))

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


    def act(self, action: str, inst: str, target):
        '''_summary_

        Args:
            action (str): type of action to be performed
            inst (str): specific thing to be done
            target (Base_Character): target of the action

        actions:
        1 - Item
        2 - Skill
        '''

        if self.status_effect == 'Sealed':
            print('You are stunned!')
            return

        match action:
            case 'Item':
                pass
            case 'Skill':
                self.use_skill(inst, target)

    def use_skill(self, skill, target):
        for x in self.skills:
            if x.name == skill:
                x.action(self, target)

    def damage(self, value: float):
        value /= self.DEF
        if value < self.hp:
            self.hp -= value
        else:
            self.hp = 0
            self.die()

    def heal(self, value: float):
        self.hp += value
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def status(self):
        if self.status_effect == 'Toxin':
            self.damage(self.max_hp / 7)

    def die(self):
        pass
