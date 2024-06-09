from ..base_character import Base_Character, parameters

class Base_Enemy(Base_Character):
    def __init__(self,
                 name: str,
                 base_stats: list,
                 lvl: int = 1):
        super().__init__(name, base_stats, lvl)

    @property
    def gold_drop(self):
        return sum(self.stats.values()) * 10

    @property
    def exp_drop(self):
        return sum(self.stats.values()) * 9
