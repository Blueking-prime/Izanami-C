from ..base_character import Base_Character
from ...Gear.base_gear import Base_Gear

class Base_Player(Base_Character):
    def __init__(self, base_stats: list, lvl: int):
        super().__init__(base_stats, lvl)
        self.sp = self.max_sp
        self.gear = {'head': None, 'body': None, 'weapon': None}

    @property
    def max_sp(self):
        return (self.stats['AGI'] + self.stats['END']) * 3

    def equip_gear(self, item: Base_Gear):
        if isinstance(item, Base_Gear):
            slot = item.slot
            self.gear[slot] = item
            self.update_stats()

    def update_stats(self):
        stats = ["STR", "INT", "WIS", "END", "GUI", "AGI"]
        current_max = (self.max_hp, self.max_sp)

        self.weapon_stats = {
                'STR': 0,
                'INT': 0,
                'WIS': 0,
                'END': 0,
                'GUI': 0,
                'AGI': 0
            }
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
