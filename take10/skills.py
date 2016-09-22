"""
.. module:: dice
   :platform: Unix, Windows
   :synopsis: Dice emulators

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

from enum import Enum, unique
from collections import namedtuple

from .abilities import AbilityClass

from multi_key_dict import multi_key_dict
from memoize import memoize


# TODO: Consider making SkillClass a config file
@unique
class SkillClass(Enum):
    """
    Enum representing the various skills characters can invest in.

    These are the standard Pathfinder skills only.
    """
    ACROBATICS = 0
    APPRAISE = 1
    BLUFF = 2
    CLIMB = 3
    CRAFT = 4
    DIPLOMACY = 5
    DISABLE_DEVICE = 6
    DISGUISE = 7
    ESCAPE_ARTIST = 8
    FLY = 9
    HANDLE_ANIMAL = 10
    HEAL = 11
    INTIMIDATE = 12
    KNOWLEDGE_ARCANA = 13
    KNOWLEDGE_DUNGEONEERING = 14
    KNOWLEDGE_ENGINEERING = 15
    KNOWLEDGE_GEOGRAPHY = 16
    KNOWLEDGE_HISTORY = 17
    KNOWLEDGE_LOCAL = 18
    KNOWLEDGE_NATURE = 19
    KNOWLEDGE_NOBILITY = 20
    KNOWLEDGE_PLANES = 21
    KNOWLEDGE_RELIGION = 22
    LINGUISTICS = 23
    PERCEPTION = 24
    PERFORM = 25
    PROFESSION = 26
    RIDE = 27
    SENSE_MOTIVE = 28
    SLEIGHT_OF_HAND = 29
    SPELLCRAFT = 30
    STEALTH = 31
    SURVIVAL = 32
    SWIM = 33
    USE_MAGIC_DEVICE = 34


# TODO: Flesh SkillSet out into its own class
SkillSet = namedtuple(
    "SkillSet",
    [k for k in SkillClass.__members__.keys()]
)


@memoize
def get_skill_ability_class(s: SkillClass) -> AbilityClass:
    """
    Returns the AbilityClass that affects the given SkillClass.

    :param SkillClass s: Skill class to check
    :returns dict Ability class the given skill class is affected by.
    """
    k = multi_key_dict()
    k[
        SkillClass.ACROBATICS,
        SkillClass.DISABLE_DEVICE,
        SkillClass.ESCAPE_ARTIST,
        SkillClass.FLY,
        SkillClass.RIDE,
        SkillClass.SLEIGHT_OF_HAND,
        SkillClass.STEALTH,
    ] = AbilityClass.DEXTERITY
    k[
        SkillClass.APPRAISE,
        SkillClass.CRAFT,
        SkillClass.KNOWLEDGE_ARCANA,
        SkillClass.KNOWLEDGE_DUNGEONEERING,
        SkillClass.KNOWLEDGE_ENGINEERING,
        SkillClass.KNOWLEDGE_GEOGRAPHY,
        SkillClass.KNOWLEDGE_HISTORY,
        SkillClass.KNOWLEDGE_LOCAL,
        SkillClass.KNOWLEDGE_NATURE,
        SkillClass.KNOWLEDGE_NOBILITY,
        SkillClass.KNOWLEDGE_PLANES,
        SkillClass.KNOWLEDGE_RELIGION,
        SkillClass.LINGUISTICS,
        SkillClass.SPELLCRAFT
    ] = AbilityClass.INTELLIGENCE
    k[
        SkillClass.BLUFF,
        SkillClass.DIPLOMACY,
        SkillClass.DISGUISE,
        SkillClass.HANDLE_ANIMAL,
        SkillClass.PERFORM,
        SkillClass.USE_MAGIC_DEVICE,
        SkillClass.INTIMIDATE,
    ] = AbilityClass.CHARISMA
    k[SkillClass.SWIM, SkillClass.CLIMB] = AbilityClass.STRENGTH
    k[
        SkillClass.HEAL,
        SkillClass.PERCEPTION,
        SkillClass.PROFESSION,
        SkillClass.SENSE_MOTIVE,
        SkillClass.SURVIVAL
    ] = AbilityClass.WISDOM
    return k[s]
