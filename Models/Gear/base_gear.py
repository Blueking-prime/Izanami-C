class Base_Gear:
    def __init__(self, stats: list, slot: str) -> None:
        self.stats = stats
        self.slot = slot

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value: str):
        if value in ('head', 'body', 'weapon'):
            self.__slot = value

    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, value: list):
        self.__stats = {
                'STR': 0,
                'INT': 0,
                'WIS': 0,
                'END': 0,
                'GUI': 0,
                'AGI': 0
            }
        if type(value) == list:
            self.__stats.update({
                'STR': value[0],
                'INT': value[1],
                'WIS': value[2],
                'END': value[3],
                'GUI': value[4],
                'AGI': value[5]
            })
