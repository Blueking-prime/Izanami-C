from .. import parameters
from random import randint

class Base_Skill:
    def __init__(self,
                # value: int = 0,
                 name: str,
                 stats: list = [],
                 stat_multiplier: int = 0,
                 boost: tuple = (1, 1),
                 cost: int = 0) -> None:
        self.name = name
        self.value = 0
        self.status_effect = None
        self.stat_list = stats
        self.stat_multiplier = stat_multiplier
        self.boost = boost
        self.cost = cost

    def action(self, obj, target):
        if obj.status_effect == 'Exhausted':
            return

        stat_total = 0

        rand_num = randint(0, 10)
        if rand_num <= 1:
            crit_value = 0.5
        if rand_num >= 8:
            crit_value = 2
        else:
            crit_value = 1

        for stat, value in obj.stats.items():
            if stat in self.stat_list:
                self.stat_total += value

        self.value = stat_total * self.stat_multiplier * crit_value

        obj.ATK, obj.DEF = self.boost

        target.status_effect = self.status_effect


class Offensive_Skill(Base_Skill):
    def action(self, obj, target):
        super().action(obj, target)
        target.damage(self.value)

class Heal_skill(Base_Skill):
    def action(self, obj, target):
        super().action(obj, target)
        target.heal(self.value)
