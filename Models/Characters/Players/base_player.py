from ..base_character import Base_Character, parameters
from ...Equipment.base_gear import Base_Gear
from ...Equipment.base_item import Base_Item
from ...Skills.player_skills import default_skills

class Base_Player(Base_Character):
    def __init__(self, name: str, base_stats: list, lvl: int):
        super().__init__(name, base_stats, lvl)
        self.sp = self.max_sp
        self.gear = dict.fromkeys(parameters.gear_parts)
        self.exp = 0
        self.gold = 0
        self.level_up_exp = 50 * (2 ** self.lvl)
        self.mag = 0
        self.level_stats = []
        self.skills = default_skills
        self.inventory = []

    @property
    def max_sp(self):
        return (self.stats['AGI'] + self.stats['END']) * 3

    @property
    def items(self):
        return [x for x in self.inventory if isinstance(x, Base_Item)]

    def restore(self):
        self.sp += self.stats['END'] * 3
        if self.sp > self.max_sp:
            self.sp = self.max_sp

    def use_items(self, item: str, target):
        for x in self.items:
            if x.name == item:
                self.inventory.remove(x)
                x.use(target)
                return True
        return False

    def act(self, action: str, inst: str, target):
        x = super().act(action, inst, target)
        if x:
            return x
        if action == 'Items':
            return self.use_items(inst, target)

    def equip_gear(self, item: Base_Gear):
        if isinstance(item, Base_Gear):
            slot = item.slot
            if self.gear[slot]:
                self.inventory.append(self.gear[slot])
            self.gear[slot] = item
            self.update_stats()

    def display_inventory(self):
        item_dict = {}
        weapon_dict = {}
        for i in self.inventory:
            if isinstance(i, Base_Item):
                try:
                    item_dict[i.name] += 1
                except KeyError:
                    item_dict[i.name] = 1
            elif isinstance(i, Base_Gear):
                weapon_dict[i.name] = i.stats
            else:
                print(i.name)

        for i in weapon_dict.keys():
            print(f'{i} Stats: {weapon_dict[i]}')

        for i in item_dict.keys():
            print(f'{i} x{item_dict[i]}')

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
        # if self.sp < 0:
        #     self.status_effect = exhausted
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

    def die(self):
        super().die()
        # Add death screen and shit
