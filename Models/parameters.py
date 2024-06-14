stats = ["STR", "INT", "WIS", "END", "GUI", "AGI"]

status_ailments = ['EnExhaust', 'Sealed', 'Toxin', 'Exhausted']

traits = ['Fire', 'Wind', 'Water', 'Light']

gear_parts = ['head', 'weapon', 'body']

moves = ['Skills', 'Defend', 'Items', 'Run']

gear = {
    # Head
    'WoolCap': {
        'slot': 'head',
        'stats': {
            'END': 3,
            'AGI': 2
        }
    },
    'Turban': {
        'slot': 'head',
        'stats': {
            'END': 2,
            'WIS': 2
        }
    },
    'Helmet': {
        'slot': 'head',
        'stats': {
            'END': 3,
            'STR': 4
        }
    },
    'Witch Hat': {
        'slot': 'head',
        'stats': {
            'END': 4,
            'WIS': 2
        }
    },
    'Demon Horn': {
        'slot': 'head',
        'stats': {
            'END': 5,
            'STR': 8
        }
    },
    # Body
    'Shirt': {
        'slot': 'body',
        'stats': {
            'END': 5,
        }
    },
    'Lithr. Armor': {
        'slot': 'body',
        'stats': {
            'END': 7,
            'AGI': -3
        }
    },
    'Turtle Shell': {
        'slot': 'body',
        'stats': {
            'END': 10,
        }
    },
    'Ninja Armor': {
        'slot': 'body',
        'stats': {
            'END': 6,
            'AGI': 4
        }
    },
    'Devourer Chitin': {
        'slot': 'body',
        'stats': {
            'END': 10,
            'STR': 5
        }
    },
    # Weapon
    'Blood Sword': {
        'slot': 'weapon',
        'stats': {
            'STR': 5,
        }
    },
    'Gigant Edge': {
        'slot': 'weapon',
        'stats': {
            'STR': 7,
        }
    },
    'Ninja Sword': {
        'slot': 'weapon',
        'stats': {
            'STR': 5,
            'AGI': 4
        }
    },
    'Ice Brand': {
        'slot': 'weapon',
        'stats': {
            'STR': 7,
        }
    },
    'Excalihuh?': {
        'slot': 'weapon',
        'stats': {
            'STR': 5,
            'AGI': 5,
            'END': 5
        }
    },
}

