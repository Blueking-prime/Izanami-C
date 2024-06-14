from .base_enemy import Base_Enemy
# ["STR", "INT", "WIS", "END", "GUI", "AGI"]
# maxhp = E*10 + W*3 + lvl*15
class Goblin(Base_Enemy):
    atk_line = "The Goblin slashes at you with its claws and you take"
    class_base_stats = [1,1,0,2,0,0]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Goblin.__name__
        super().__init__(name, Goblin.class_base_stats, lvl)

class Imp(Base_Enemy):
    atk_line = "The Imp slashes at you with improvised weapons and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Imp.__name__
        super().__init__(name, Imp.class_base_stats, lvl)

class Hobgoblin(Base_Enemy):
    atk_line = "The Hobgoblin slashes at you with a flaming blade and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Hobgoblin.__name__
        super().__init__(name, Hobgoblin.class_base_stats, lvl)

class Oni(Base_Enemy):
    atk_line = "The Oni slams into your chest with a massive club and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Oni.__name__
        super().__init__(name, Oni.class_base_stats, lvl)

class Orias(Base_Enemy):
    atk_line = "The Orias bites into you with myriad serpent heads and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Orias.__name__
        super().__init__(name, Orias.class_base_stats, lvl)

class Balam(Base_Enemy):
    atk_line = "The Balam rams into you sending you flying, you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Balam.__name__
        super().__init__(name, Balam.class_base_stats, lvl)

class Human(Base_Enemy):
    atk_line = "They strike at you with a bladed weapon and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Human.__name__
        super().__init__(name, Human.class_base_stats, lvl)

class Ghost(Base_Enemy):
    atk_line = "The spirit grasps you with its soul stealing hands and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Light'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Ghost.__name__
        super().__init__(name, Ghost.class_base_stats, lvl)

class Sphinx(Base_Enemy):
    atk_line = "The creature swipes at you with sharpened claws and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Water'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Sphinx.__name__
        super().__init__(name, Sphinx.class_base_stats, lvl)

class Belial(Base_Enemy):
    atk_line = "The creature's underlings nip at your heels, you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Water'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Belial.__name__
        super().__init__(name, Belial.class_base_stats, lvl)

class Gigas(Base_Enemy):
    atk_line = "The Iron Gigas slams into you, knocking you down and dealing"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Water'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Gigas.__name__
        super().__init__(name, Gigas.class_base_stats, lvl)

class Devourer(Base_Enemy):
    atk_line = "The devourer attempts to swallow you whole! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Devourer.__name__
        super().__init__(name, Devourer.class_base_stats, lvl)

class Izanami(Base_Enemy):
    atk_line = "The rotten corpse of the goddess ensnares you! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Izanami.__name__
        super().__init__(name, Izanami.class_base_stats, lvl)

class Crowley(Base_Enemy):
    atk_line = "Crowley shoots at you with a firearm! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Crowley.__name__
        super().__init__(name, Crowley.class_base_stats, lvl)

class Kobagami(Base_Enemy):
    atk_line = "The avatar of the demon king strikes you with unreal ferocity! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Kobagami.__name__
        super().__init__(name, Kobagami.class_base_stats, lvl)

class Whiten(Base_Enemy):
    atk_line = "The avatar of the demon king strikes you with unreal ferocity! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        if name == '':
            name = Whiten.__name__
        super().__init__(name, Whiten.class_base_stats, lvl)
