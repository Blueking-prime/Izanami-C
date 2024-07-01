from .. import parameters

class Base_Item:
    '''For value,
        if buff, (ATK, DEF)
        if cleanse, Debuff
    '''
    def __init__(self, data: dict) -> None:
        self.name = data['name']
        self.type = data['type']
        self.value = data['value']
        self.desc = data.get('desc', None)

    def use(self, target):
        match self.type:
            case 'buff':
                self.use_buff(target)
            case 'heal':
                self.use_heal(target)
            case 'damage':
                self.use_damage(target)
            case 'cleanse':
                self.use_cleanse(target)

        del self

    def use_buff(self, target):
        target.ATK *= self.value[0]
        target.DEF *= self.value[1]

    def use_heal(self, target):
        target.heal(self.value)

    def use_damage(self, target):
        target.damage(self.value)

    def use_cleanse(self, target):
        if target.status_effect == self.value:
            target.status_effect = None
        else:
            print('No effect')
