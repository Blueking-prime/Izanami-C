from .base_enemy import Base_Enemy
from ...Skills import enemy_skills
# ["STR", "INT", "WIS", "END", "GUI", "AGI"]
# maxhp = E*10 + W*3 + lvl*15
class Goblin(Base_Enemy):
    atk_line = "The Goblin slashes at you with its claws and you take"
    class_base_stats = [1,1,0,2,0,0]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Goblin.__name__ + name
        super().__init__(name, Goblin.class_base_stats, lvl)
        self.skills = enemy_skills.goblin_skills

class Imp(Base_Enemy):
    atk_line = "The Imp slashes at you with improvised weapons and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Imp.__name__ + name
        super().__init__(name, Imp.class_base_stats, lvl)
        self.skills = enemy_skills.imp_skills

class Hobgoblin(Base_Enemy):
    atk_line = "The Hobgoblin slashes at you with a flaming blade and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Hobgoblin.__name__ + name
        super().__init__(name, Hobgoblin.class_base_stats, lvl)
        self.skills = enemy_skills.hobgoblin_skills

class Oni(Base_Enemy):
    atk_line = "The Oni slams into your chest with a massive club and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Oni.__name__ + name
        super().__init__(name, Oni.class_base_stats, lvl)
        self.skills = enemy_skills.oni_skills

class Orias(Base_Enemy):
    atk_line = "The Orias bites into you with myriad serpent heads and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Orias.__name__ + name
        super().__init__(name, Orias.class_base_stats, lvl)
        self.skills = enemy_skills.orias_skills

class Balam(Base_Enemy):
    atk_line = "The Balam rams into you sending you flying, you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Balam.__name__ + name
        super().__init__(name, Balam.class_base_stats, lvl)
        self.skills = enemy_skills.balam_skills

class Human(Base_Enemy):
    atk_line = "They strike at you with a bladed weapon and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Human.__name__ + name
        super().__init__(name, Human.class_base_stats, lvl)
        self.skills = enemy_skills.human_skills

class Ghost(Base_Enemy):
    atk_line = "The spirit grasps you with its soul stealing hands and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Light'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Ghost.__name__ + name
        super().__init__(name, Ghost.class_base_stats, lvl)
        self.skills = enemy_skills.ghost_skills

class Sphinx(Base_Enemy):
    atk_line = "The creature swipes at you with sharpened claws and you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Water'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Sphinx.__name__ + name
        super().__init__(name, Sphinx.class_base_stats, lvl)
        self.skills = enemy_skills.sphinx_skills

class Belial(Base_Enemy):
    atk_line = "The creature's underlings nip at your heels, you take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Water'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Belial.__name__ + name
        super().__init__(name, Belial.class_base_stats, lvl)
        self.skills = enemy_skills.belial_skills

class Gigas(Base_Enemy):
    atk_line = "The Iron Gigas slams into you, knocking you down and dealing"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Water'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Gigas.__name__ + name
        super().__init__(name, Gigas.class_base_stats, lvl)
        self.skills = enemy_skills.gigas_skills

class Devourer(Base_Enemy):
    atk_line = "The devourer attempts to swallow you whole! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Devourer.__name__ + name
        super().__init__(name, Devourer.class_base_stats, lvl)
        self.skills = enemy_skills.devourer_skills

class Izanami(Base_Enemy):
    atk_line = "The rotten corpse of the goddess ensnares you! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Izanami.__name__ + name
        super().__init__(name, Izanami.class_base_stats, lvl)
        self.skills = enemy_skills.izanami_skills

class Crowley(Base_Enemy):
    atk_line = "Crowley shoots at you with a firearm! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Crowley.__name__ + name
        super().__init__(name, Crowley.class_base_stats, lvl)
        self.skills = enemy_skills.crowley_skills

class Kobagami(Base_Enemy):
    atk_line = "The avatar of the demon king strikes you with unreal ferocity! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Fire'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Kobagami.__name__ + name
        super().__init__(name, Kobagami.class_base_stats, lvl)
        self.skills = enemy_skills.kobagami_skills

class Whiten(Base_Enemy):
    atk_line = "The avatar of the demon king strikes you with unreal ferocity! You take"
    class_base_stats = [3,3,2,4,2,2]
    trait = 'Wind'

    def __init__(self, name: str = '', lvl: int = 1):
        name = Whiten.__name__ + name
        super().__init__(name, Whiten.class_base_stats, lvl)
        self.skills = enemy_skills.whiten_skills
