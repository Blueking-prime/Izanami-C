from .. import parameters

class Base_Gear:
    def __init__(self, stats: list, slot: str) -> None:
        self.stats = stats
        self.slot = slot

    @property
    def slot(self):
        return self.__slot

    @slot.setter
    def slot(self, value: str):
        if value in parameters.gear_parts:
            self.__slot = value

    @property
    def stats(self):
        return self.__stats

    @stats.setter
    def stats(self, value: list):
        self.__stats = dict(zip(parameters.stats, [0, 0, 0, 0, 0, 0]))
        if type(value) == list:
            self.__stats.update(dict(zip(parameters.stats, value)))
