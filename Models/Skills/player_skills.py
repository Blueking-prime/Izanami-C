from .base_skill import Base_Skill, Offensive_Skill, Heal_Skill
from ..utils import rand_chance

default_skills = [
    Offensive_Skill(
        'Attack',
        stats=['STR']
    ),
    Offensive_Skill(
        'Strong Strike',
        stats=['STR'],
        stat_multiplier= 3,
        cost=15,
        flavour_text="You spend your pent up energy and swing with gusto"
    )
]

ronin_skills = [
    Offensive_Skill(
        'Ichimonji',
        stats=['STR'],
        stat_multiplier= 4,
        cost=24,
        boost=(1, 0.5),
        flavour_text="Letting go of your guard, ignorant of all defense, you put your very soul into one devastating swing"
    ),
    Offensive_Skill(
        'Moon Swallow',
        stats=['STR'],
        stat_multiplier= 2,
        cost=10,
        flavour_text="Channeling the power of the moon you perform a dazzling strike",
        status_effect=('Stunned', 0.25)
    ),
    Base_Skill(
        'Gambol Shroud',
        cost=35,
        boost=(1, 0.5),
        status_effect=('Death', 0.0625),
        flavour_text="You strike at your opponent's very soul, aiming to fell them in one strike. This technique leaves you wild open"
    ),
    #todo: Add Demon Blade hakiri
]

shinobi_skills = [
    Base_Skill(
        'Shigan',
        cost=27,
        status_effect=('Stunned', 0.5), # todo: update chance
        flavour_text="You strike at your targets pressure points in an attempt to paralyze them"
    ),
    Offensive_Skill(
        'Tekkai',
        stats=['AGI'],
        cost=32,
        boost=(1, 2),
        flavour_text="You harden the breath in your lungs, dealing a palm strike while holding your guard up"
    ),
    Offensive_Skill(
        'Rankyaku',
        stats=['AGI'],
        trait='Wind',
        cost=22,
        stat_multiplier=3,
        flavour_text="You deliver a powerful kick, kicking up a gust of wind weakness"
    ),
    # add soru
    # add shiogan
]

scion_skills = [
    # add royal vow
    # add blood oath
    # add bastard howl
]
