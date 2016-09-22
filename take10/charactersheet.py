"""
.. module:: charactersheet
   :platform: Unix, Windows
   :synopsis: Character Sheet definition

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

from enum import Enum, unique

from PyQt5.QtCore import QObject, Q_ENUMS

from abilities import AbilityScores
from races import Race
from skills import SkillSet


class CharacterSheet(QObject):
    """
    Represents a character sheet for a single character.

    Not to be confused with CharacterEntities, which are instances of character
    sheets that are mutable without modifying the CharacterSheet they are based
    on.
    """

    # TODO: Consider moving Alignment elsewhere
    @unique
    class Alignment(Enum):
        """Alignment refers to a character's moral code"""
        LAWFUL_GOOD = 0
        LAWFUL_NEUTRAL = 1
        LAWFUL_EVIL = 2
        NEUTRAL_GOOD = 3
        NEUTRAL_NEUTRAL = 4
        NEUTRAL_EVIL = 5
        CHAOTIC_GOOD = 6
        CHAOTIC_NEUTRAL = 7
        CHAOTIC_EVIL = 8
    Q_ENUMS(Alignment)

    @unique
    class Sex(Enum):
        """Sex refers to a character's biological sex"""
        FEMALE = 0,
        MALE = 1
        ASEXUAL = 2
    Q_ENUMS(Sex)

    def __init__(
        self,
        char_name: str,
        char_desc: str,
        alignment: Alignment,
        race: Race,
        sex: Sex,
        scores: AbilityScores=None,
        skills: SkillSet=None
    ):
        QObject.__init__(self)

        self.char_name = char_name
        self.char_desc = char_desc
        self.alignment = alignment
        self.race = race
        self.sex = sex
        self.ability_scores = scores
        self.skills = skills
