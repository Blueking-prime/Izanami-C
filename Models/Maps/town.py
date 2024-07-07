from .dungeon import Dungeon
from .. import checks
from .. import parameters
from ..utils import dialog_choice, dialog_choice_shop
from ..Characters.Players.base_player import Base_Player, Base_Gear, Base_Item
from ..Characters.Enemies import enemy_models
from Scripts import dialogue, save
from Scripts.battle import battle


class Town:
    def __init__(self) -> None:
        self.locations = ["Palace", "Church", "Smithy", "Apothecary", "Demonitorium", "Dungeon"]
        self.actions = ['Talk', "Go Somewhere", 'Status']
        self.characters = ["Kobaneko", "White"]

    def main(self, player: Base_Player):
        while True:
            action = dialog_choice("What do you want to do?", self.actions, False)
            match action:
                case 1:
                    self.talk()
                case 2:
                    self.enter(player)
                case 3:
                    self.status(player)

    def talk(self):
        character = dialog_choice('Who do you want to talk to?', self.characters)
        match character:
            case 1:
                dialogue.kobaneko()
            case 2:
                dialogue.white()
        return


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
                self.apothecary(player)
            case 5:
                self.demonitorium(player)
            case 6:
                self.dungeon(player)
        return


    def church(self, player: Base_Player):
        print("The soft scent of incense attacks you. There's a quiet hymn everberating from unknown places.")
        input("Sister Amaka: Come my child, be healed")
        cost = player.lvl * 25
        print(f'Your status is -> HP : {player.hp}/{player.max_hp} | Status Effect : {player.status_effect}')
        heal = dialog_choice(f"Sister Amaka: That will be {cost} yen | Balance: {player.gold}", back=False)
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
        return

    def smithy(self, player: Base_Player):
        print("A wave of heat rolls over you as soon as you step in.")
        while True:
            option = dialog_choice_shop("Old Smithy: What would yer like to purchase, adventurer!", parameters.smithy)
            try:
                cost = parameters.smithy[option]
                confirm = dialog_choice(f"Old Smithy: That will be {cost} yen | Balance: {player.gold}", back=False)
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
            option = dialog_choice_shop("Lenarr, the Alchemist: What would you like to purchase, adventurer!", parameters.apothy)
            try:
                cost = parameters.apothy[option]
                confirm = dialog_choice(f"Lenarr, the Alchemist: That will be {cost} yen | Balance: {player.gold}", back=False)
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

    def demonitorium(self, player: Base_Player):
        print("Unholy sigils paint the walls and howling creatures cackle from cages hanging precariously overhead")
        input("Crowley: Test your skills, adventurer... Anything you carve out is yours.")
        print("Whatever you want, I got it.")
        while True:
            option = dialog_choice("What would you like to purchase? ", ["Buy Mag", "See Demons", "Talk to Crowley"])
            match option:
                case 1:
                    while True:
                        try:
                            x = int(input("How much do you want to buy: [number] "))
                            break
                        except ValueError:
                            continue
                    cost = 10 * x
                    confirm = dialog_choice(f"That will be {cost} yen. | Balance: {player.gold}", back=False)
                    if confirm:
                        if player.gold >= cost:
                            player.gold -= cost
                            player.mag += x
                        else:
                            print("You don't have enough Yen")
                case 2:
                    fights = checks.demon_training
                    while True:
                        fight = dialog_choice_shop('What do you want to fight', fights)
                        try:
                            cost = fights[fight]
                            confirm = dialog_choice(f"That will be {cost} yen | Balance: {player.gold}", back=False)
                            if confirm:
                                if player.gold >= cost:
                                    enemy = getattr(enemy_models, fight)()
                                    battle(player, [enemy])
                                else:
                                    print("Broke ass n*gga")
                        except KeyError:
                            break
                case 3:
                    dialogue.crowley()
                case _:
                    break
        return

    def dungeon(self, player: Base_Player):
        print(f"You are travelling to Dungeon Level {checks.dungeon_level}")
        confirm = dialog_choice('Confirm: ', back=False)
        if confirm:
            match checks.dungeon_level:
                case 1:
                    Dungeon(enemy_types=[enemy_models.Goblin, enemy_models.Oni]).main(player)
                case 2:
                    Dungeon(enemy_types=[enemy_models.Imp, enemy_models.Oni]).main(player)
                case 3:
                    Dungeon(enemy_types=[enemy_models.Imp, enemy_models.Orias]).main(player)
                case 4:
                    Dungeon(enemy_types=[enemy_models.Hobgoblin, enemy_models.Balam]).main(player)
                    battle(player, [enemy_models.Gigas()])
                case 5:
                    Dungeon(enemy_types=[enemy_models.Hobgoblin, enemy_models.Belial]).main(player)
                    dialogue.final_floor(player)
                case _:
                    Dungeon(
                        width=16,
                        height=10,
                        enemy_types=[getattr(enemy_models, i) for i in parameters.enemies]
                    ).main(player)
        return

    def status(self, player: Base_Player):
        while True:
            view = dialog_choice('What do you want to do?', ['Stats', 'Equipment', 'Magic', 'Save'])
            match view:
                case 1:
                    print(f'Name: {player.name}')
                    print(f'HP: {player.hp}/{player.max_hp} | SP: {player.sp}/{player.max_sp}')
                    print(f'Class: {player.__class__.__name__}')
                    print(f'Stats : {player.stats}')
                    print('Weapon:')
                    for i in parameters.gear_parts:
                        try:
                            print(f'\t{i.capitalize()}: {player.gear[i].name} - {player.gear[i].stats}')
                        except AttributeError:
                            print(f'\t{i.capitalize()}: None')
                    print('Inventory:')
                    player.display_inventory()
                case 2:
                    weapons = [i for i in player.inventory if isinstance(i, Base_Gear)]
                    if len(weapons) == 0:
                        print('No equipment in inventory')
                        continue
                    weapon_dict = {i.name: i.stats for i in weapons}
                    while True:
                        try:
                            equip = dialog_choice_shop('Which gear do you want to equip', weapon_dict)
                            for weapon in weapons:
                                if weapon.name == equip:
                                    confirm = dialog_choice(f"Confirm", back=False)
                                    if confirm:
                                        player.equip_gear(weapon)
                                        print(f'{equip} equipped!')
                                    break
                            continue
                        except KeyError:
                            break
                case 3:
                    print('Unavailable')
                case 4:
                    save.save(player)
                    print('Progress saved!')
                case _:
                    break
        return
