from ..base_character import Base_Character, parameters
from ...Gear.base_gear import Base_Gear
from ...Skills.player_skills import default_skills
# from ...Maps.dungeon import Dungeon

class Base_Player(Base_Character):
    def __init__(self, name: str, base_stats: list, lvl: int):
        super().__init__(name, base_stats, lvl)
        self.sp = self.max_sp
        self.gear = dict.fromkeys(parameters.gear_parts)
        self.exp = 0
        self.gold = 0
        self.mag = 0
        self.level_stats = []
        self.skills = default_skills
        self.inventory = []

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
        self.level_up_exp = 50 * (2 ** self.lvl)

        self.exp += value
        if self.exp >= self.level_up_exp:
            current_max = (self.max_hp, self.max_sp)

            self.exp -= self.level_up_exp
            self.lvl += 1

            curr_stats = self.base_stats
            for i in self.level_stats:
                curr_stats[i] += 1
            self.base_stats = list(curr_stats.values())

            self.update_derived_stats(current_max)
        self.level_up_exp = 50 * (2 ** self.lvl)


    def status(self):
        super().status()
        if self.status_effect == 'EnExhaust':
            self.sp -= self.max_sp / 4

    def move(self, map, direction: str):
        x, y = map.player_pos
        match direction:
            case 'u':
                map.player_pos = (x, y - 1)
            case 'd':
                map.player_pos = (x, y + 1)
            case 'l':
                map.player_pos = (x - 1, y)
            case 'r':
                map.player_pos = (x + 1, y)
            case _:
                pass
        map.check_tile(self)
