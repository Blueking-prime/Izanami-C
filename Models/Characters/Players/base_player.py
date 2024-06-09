from ..base_character import Base_Character, parameters
from ...Gear.base_gear import Base_Gear

class Base_Player(Base_Character):
    def __init__(self, name: str, base_stats: list, lvl: int):
        super().__init__(name, base_stats, lvl)
        self.sp = self.max_sp
        self.gear = dict.fromkeys(parameters.gear_parts)
        self.exp = 0
        self.gold = 0
        self.mag = 0

    @property
    def max_sp(self):
        return (self.stats['AGI'] + self.stats['END']) * 3

    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: list):
        if not self.__items:
           self.__items = []
        # todo: implement item support
        self.__items += [x for x in items if isinstance(x, None) and x not in self.__items]


    def equip_gear(self, item: Base_Gear):
        if isinstance(item, Base_Gear):
            slot = item.slot
            self.gear[slot] = item
            self.update_stats()

    def update_stats(self):
        stats = parameters.stats
        current_max = (self.max_hp, self.max_sp)

        self.weapon_stats = dict.fromkeys(stats, 0)

        for gear in self.gear.values():
            if gear:
                for stat_name, stat in gear.stats.items():
                    self.weapon_stats[stat_name] += stat

        for i in stats:
            self.stats[i] = self.base_stats[i] + self.weapon_stats[i]

        self.update_derived_stats(current_max)

    def update_derived_stats(self, current_max: tuple):
        self.hp = (self.hp/current_max[0]) * self.max_hp
        self.sp = (self.sp/current_max[1]) * self.max_sp

    def level_up(self, value):
        self.level_up_exp = 50 * (2 ** self.lvl) # todo Add function to calculate and scale level up exp

        self.exp += value
        if self.exp >= self.level_up_exp:
            current_max = (self.max_hp, self.max_sp)

            self.exp -= self.level_up_exp
            self.lvl += 1

            self.update_derived_stats(current_max)

    def status(self):
        super().status()
        if self.status_effect == 'EnExhaust':
            self.sp -= self.max_sp / 4
