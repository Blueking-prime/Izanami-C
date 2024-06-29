from .. import parameters

class Base_Gear:
    def __init__(self, data: dict) -> None:
        self.name = data['name']
        self.stats = data['stats']
        self.slot = data['slot']

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
    def stats(self, value: dict):
        self.__stats = dict.fromkeys(parameters.stats, 0)
        if type(value) == dict:
            self.__stats.update(value)
