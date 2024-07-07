characters = ['Farmer', 'Destitute', 'Doctor', 'Ronin', 'Shinobi']

stats = ["STR", "INT", "WIS", "END", "GUI", "AGI"]

status_ailments = ['EnExhaust', 'Sealed', 'Toxin', 'Exhausted', 'Stunned', 'Death']

traits = ['Fire', 'Wind', 'Water', 'Light']

gear_parts = ['head', 'weapon', 'body']

moves = ['Run', 'Defend', 'Skills', 'Items']

enemies = ['Goblin', 'Imp', 'Hobgoblin', 'Oni', 'Orias', 'Balam', 'Human', 'Ghost', 'Sphinx', 'Belial', 'Gigas', 'Devourer', 'Izanami', 'Crowley', 'Kobagami', 'Whiten']

inventory = {
    'Medicine': 5,
    'Tonic': 2,
    'StaminaPill': 5,
    'SenchaTea': 0,
    'FiveFingerSeal': 2,
    'Antidote': 0,
    'EnergyCandy': 0,
    'Panacea': 0,
    'GreenHerbs': 2,
    'RedHerbs': 2,
    'BlueHerbs': 2,
}

ninjaTools = {
    'Shuriken': 3,
    'PaperBomb': 3,
    'FumaShuriken': 3,
}

equipment = {
    'Turban': 1,
    'Shirt': 1,
    'ShortSword': 1,
}

smithy = {
    # name: price
    'Turban': 65,
    'WoolCap': 50,
    'GoldCrown': 35,
    'BloodiedDagger': 100,
    'Lthr.Armor': 125,
}

apothy = {
    # name: price
    'Medicine': 25,
    'Tonic': 150,
    'StaminaPill': 50,
    'SenchaTea': 100,
    'FiveFingerSeal': 75,
    'Antidote': 75,
    'EnergyCandy': 75,
    'Panacea': 1000,
    'GreenHerbs': 50,
    'RedHerbs': 50,
    'BlueHerbs': 50,
}


items = [
    {
        'name': 'Leaf',
        'type': 'heal',
        'value': 20
    },
    {
        'name': 'Razor',
        'type': 'damage',
        'value': 20
    }
]

gear = [
    # Head
    {
        'name' : 'WoolCap',
        'slot': 'head',
        'stats': {
            'END': 3,
            'AGI': 2
        }
    },
    {
        'name' : 'Turban',
        'slot': 'head',
        'stats': {
            'END': 2,
            'WIS': 2
        }
    },
    {
        'name' : 'Helmet',
        'slot': 'head',
        'stats': {
            'END': 3,
            'STR': 4
        }
    },
    {
        'name' : 'Witch Hat',
        'slot': 'head',
        'stats': {
            'END': 4,
            'WIS': 2
        }
    },
    {
        'name' : 'Demon Horn',
        'slot': 'head',
        'stats': {
            'END': 5,
            'STR': 8
        }
    },
    # Body
    {
        'name' : 'Shirt',
        'slot': 'body',
        'stats': {
            'END': 5,
        }
    },
    {
        'name' : 'Lithr. Armor',
        'slot': 'body',
        'stats': {
            'END': 7,
            'AGI': -3
        }
    },
    {
        'name' : 'Turtle Shell',
        'slot': 'body',
        'stats': {
            'END': 10,
        }
    },
    {
        'name' : 'Ninja Armor',
        'slot': 'body',
        'stats': {
            'END': 6,
            'AGI': 4
        }
    },
    {
        'name' : 'Devourer Chitin',
        'slot': 'body',
        'stats': {
            'END': 10,
            'STR': 5
        }
    },
    # Weapon
    {
        'name' : 'Blood Sword',
        'slot': 'weapon',
        'stats': {
            'STR': 5,
        }
    },
    {
        'name' : 'Gigant Edge',
        'slot': 'weapon',
        'stats': {
            'STR': 7,
        }
    },
    {
        'name' : 'Ninja Sword',
        'slot': 'weapon',
        'stats': {
            'STR': 5,
            'AGI': 4
        }
    },
    {
        'name' : 'Ice Brand',
        'slot': 'weapon',
        'stats': {
            'STR': 7,
        }
    },
    {
        'name' : 'Excalihuh?',
        'slot': 'weapon',
        'stats': {
            'STR': 5,
            'AGI': 5,
            'END': 5
        }
    },
]
