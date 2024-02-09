from .base_player import Base_Player

class Destitute(Base_Player):
    desc = "Born into poverty, not even the scraps on your back belong to you. Your birth was insignificant and your life a meaningless struggle, but alas you may yet find your worth in the pit."

    def __init__(self, base_stats: list = [-1,-1,-1,-1,-1,-1], lvl: int = 1):
        super().__init__(base_stats, lvl)
