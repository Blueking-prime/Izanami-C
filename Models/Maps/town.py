from ..utils import dialog_choice, dialog_choice_shop
from .. import parameters
from ..Characters.Players.base_player import Base_Player, Base_Gear, Base_Item

class Town:
    def __init__(self) -> None:
        self.locations = ["Palace", "Church", "Smithy", "Apothecary", "Demonitorium", "Dungeon"]
        self.actions = ['Talk', "Go Somewhere", 'Status']
        self.characters = ["Kobaneko"]

    def main(self):
        while True:
            action = dialog_choice("What do you want to do?", self.actions, False)
            match action:
                case 1:
                    self.talk()
                case 2:
                    self.enter()
                case 3:
                    self.status()

    def talk(self):
        pass

    def enter(self, player: Base_Player):
        destination = dialog_choice("Where do you want to go", self.locations)
        match destination:
            case 1:
                self.palace()
            case 2:
                self.church(player)
            case 3:
                self.smithy(player)
            case 4:
                self.apothecary()
            case 5:
                self.demonitorium()
            case 6:
                self.dungeon()
        return


    def church(self, player: Base_Player):
        print("The soft scent of incense attacks you. There's a quiet hymn everberating from unknown places.")
        input("Sister Amaka: Come my child, be healed")
        cost = player.lvl * 25
        print(f'Your status is -> HP : {player.hp}/{player.max_hp} | Status Effect : {player.status_effect}')
        heal = dialog_choice(f"Sister Amaka: That will be ${cost} yen", back=False)
        if heal:
            while True:
                if player.gold >= cost:
                    option = dialog_choice('Choose: ', ['Healing', 'Purge', 'Blessing'])
                    match option:
                        case 1:
                            player.heal(player.max_hp)
                            input("Sister Amaka: You have been healed. Go now and sin no more")
                        case 2:
                            player.status_effect = None
                            input("Sister Amaka: You have been delivered from ailment. Go now and be free.")
                        case 3:
                            # Do something
                            input("Sister Amaka: Our lord has granted you a boon")
                        case _:
                            break
                    player.gold -= cost
                    continue
                else:
                    print("You don't have enough Yen")
                    break
        return

    def palace(self):
        pass

    def smithy(self, player: Base_Player):
        print("A wave of heat rolls over you as soon as you step in.")
        while True:
            option = dialog_choice_shop("Old Smithy: What would yer like to purchase, adventurer!", list(parameters.smithy.keys()))
            try:
                cost = parameters.smithy[option]
                confirm = dialog_choice(f"Old Smithy: That will be ${cost} yen", back=False)
                if confirm:
                    if player.gold >= cost:
                        for item in parameters.gear:
                            if item['name'] == option:
                                break

                        player.gold -= cost
                        confirm_ = dialog_choice("Old Smithy: Would you like to equip this now?", back=False)
                        if confirm_:
                            player.equip_gear(Base_Gear(item))
                        else:
                            player.inventory.append(Base_Gear(item))
                        continue
                    else:
                        print("You don't have enough Yen")
                        continue
            except KeyError:
                break
        return

    def apothecary(self, player: Base_Player):
        print("An indescribable miasma rises out as you open the door, the smell of ginseng, rabbit foot and other unknowable reagents")
        while True:
            option = dialog_choice_shop("Lenarr, the Alchemist: What would you like to purchase, adventurer!", list(parameters.apothy.keys()))
            try:
                cost = parameters.apothy[option]
                confirm = dialog_choice(f"Lenarr, the Alchemist: That will be ${cost} yen", back=False)
                if confirm:
                    if player.gold >= cost:
                        for item in parameters.items:
                            if item['name'] == option:
                                player.inventory.append(Base_Item(item))
                                player.gold -= cost
                                break
                    else:
                        print("You don't have enough Yen")
                        continue
            except KeyError:
                break
        return

    def demonitorium(self):
        pass

    def dungeon(self):
        pass

    def status(self):
        pass