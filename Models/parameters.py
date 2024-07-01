stats = ["STR", "INT", "WIS", "END", "GUI", "AGI"]

status_ailments = ['EnExhaust', 'Sealed', 'Toxin', 'Exhausted', 'Stunned', 'Death']

traits = ['Fire', 'Wind', 'Water', 'Light']

gear_parts = ['head', 'weapon', 'body']

moves = ['Run', 'Defend', 'Skills', 'Items']

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
