from .base_player import Base_Player

class Ronin(Base_Player):
    desc = "A former samurai who has performed a slight against his lord, whether intentionally or not, whether righteously or not"

    def __init__(self, base_stats: list = [6,0,0,2,0,4], lvl: int = 1):
        super().__init__(base_stats, lvl)
