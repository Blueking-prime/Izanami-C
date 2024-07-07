from ..utils import rand_chance, randint

class Base_Skill:
    def __init__(self,
                # value: int = 0,
                 name: str,
                 stats: list = [],
                 stat_multiplier: int = 1,
                 boost: tuple = (1, 1),
                 cost: int = 0,
                 flavour_text: str = '',
                 status_effect: str | tuple | None = None) -> None:
        self.name = name
        self.value = 0
        self.status_effect = status_effect
        self.stat_list = stats
        self.stat_multiplier = stat_multiplier
        self.boost = boost
        self.cost = cost
        self.flavour_text = flavour_text

    def action(self, obj, target):
        if obj.status_effect == 'Exhausted':
            return False

        if obj.sp <= 0:
            print('Out of SP')
            return False

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
                stat_total += value

        if crit_value > 1:
            print('CRIT!')
        elif crit_value < 1:
            print('Whiffed...')
        self.value = stat_total * self.stat_multiplier * crit_value

        obj.ATK *= self.boost[0]
        obj.DEF *= self.boost[1]

        if type(self.status_effect) is tuple:
            if rand_chance(self.status_effect[1]):
                target.status_effect = self.status_effect[0]
            else:
                print('Miss!')
        else:
            target.status_effect = self.status_effect

        return True


class Offensive_Skill(Base_Skill):
    def __init__(self,
                 name: str,
                 trait: str | None = None,
                 stats: list = [],
                 stat_multiplier: int = 1,
                 boost: tuple = (1, 1),
                 cost: int = 0,
                 flavour_text: str = '',
                 status_effect: str | None = None) -> None:
        super().__init__(name, stats, stat_multiplier, boost, cost, flavour_text)
        self.trait = trait

    def action(self, obj, target):
        super().action(obj, target)
        try:
            if self.trait == target.trait:
                self.value *= 2
        except AttributeError:
            pass
        self.value *= obj.ATK
        target.damage(self.value)

class Heal_Skill(Base_Skill):
    def action(self, obj, target):
        super().action(obj, target)
        target.heal(self.value)
