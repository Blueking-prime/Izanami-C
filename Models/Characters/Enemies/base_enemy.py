from ..base_character import Base_Character, parameters
from ...utils import randint
from ...Skills.enemy_skills import Heal_Skill, default_skills

class Base_Enemy(Base_Character):
    def __init__(self,
                 name: str,
                 base_stats: list,
                 lvl: int = 1):
        super().__init__(name, base_stats, lvl)
        self.skills = default_skills

    @property
    def gold_drop(self):
        return sum(self.stats.values()) * 10

    @property
    def exp_drop(self):
        return sum(self.stats.values()) * 9

    def battle_script(self, player):
        while True:
            try:
                skill_no = randint(0, len(self.skills))
                skill = self.skills[skill_no]
                break
            except IndexError:
                continue
        if isinstance(skill, Heal_Skill):
            skill.action(self, self)
        else:
            skill.action(self, player)
