from .base_player import Base_Player

class Shinobi(Base_Player):
    desc = "The shinobi are warriors whose existence is myth. They dance in shadow and attack only when moonlight strikes their targets eyes."

    def __init__(self, base_stats: list = [0,4,0,0,0,8], lvl: int = 1):
        super().__init__(base_stats, lvl)
