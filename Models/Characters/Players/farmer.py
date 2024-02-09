from .base_player import Base_Player

class Farmer(Base_Player):
    desc = "A man of the earth who finds himself in depths far beyond him, you are strong from years of backbreaking labour and have always been known for your wit"

    def __init__(self, base_stats: list = [2,2,2,2,2,2], lvl: int = 1):
        super().__init__(base_stats, lvl)
