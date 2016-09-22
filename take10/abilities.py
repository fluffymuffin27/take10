"""
.. module:: abilities
   :platform: Unix, Windows
   :synopsis: Abilities definitions

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

from enum import Enum, unique
from abc import ABC, abstractmethod

from PyQt5.QtCore import QObject, Q_ENUMS, pyqtProperty, pyqtSignal

from .dice import roll


class AbilityScores(QObject):
    """
    AbilityScores are the core statistics for a character.
    """

    @unique
    class AbilityClass(Enum):
        """Standard Pathfinder ability classes"""
        STRENGTH = 0
        DEXTERITY = 1
        INTELLIGENCE = 2
        WISDOM = 3
        CHARISMA = 4
        CONSTITUTION = 5

    Q_ENUMS(AbilityClass)

    def __init__(
        self,
        STRENGTH: int,
        DEXTERITY: int,
        INTELLIGENCE: int,
        WISDOM: int,
        CHARISMA: int,
        CONSTITUTION: int
    ):
        QObject.__init__(self)

        self._strength = STRENGTH
        self._dexterity = DEXTERITY
        self._intelligence = INTELLIGENCE
        self._wisdom = WISDOM
        self._charisma = CHARISMA
        self._constitution = CONSTITUTION

    # Qt Signals for monitoring property changes
    strength_changed = pyqtSignal(int)
    dexterity_changed = pyqtSignal(int)
    intelligence_changed = pyqtSignal(int)
    wisdom_changed = pyqtSignal(int)
    charisma_changed = pyqtSignal(int)
    constitution_changed = pyqtSignal(int)

    # Properties for gated acess to stat fields

    @pyqtProperty(int, notify=strength_changed)
    def strength(self):
        return self._strength

    @strength.setter
    def strength(self, score: int):
        if score < 0:
            raise ValueError("AbilityScores cannot be negative")
        self._strength = score

    @pyqtProperty(int, notify=dexterity_changed)
    def dexterity(self):
        return self._dexterity

    @dexterity.setter
    def dexterity(self, score: int):
        if score < 0:
            raise ValueError("AbilityScores cannot be negative")
        self._dexterity = score

    @pyqtProperty(int, notify=intelligence_changed)
    def intelligence(self):
        return self._intelligence

    @intelligence.setter
    def intelligence(self, score: int):
        if score < 0:
            raise ValueError("AbilityScores cannot be negative")
        self._intelligence = score

    @pyqtProperty(int, notify=wisdom_changed)
    def wisdom(self):
        return self._wisdom

    @wisdom.setter
    def wisdom(self, score: int):
        if score < 0:
            raise ValueError("AbilityScores cannot be negative")
        self._wisdom = score

    @pyqtProperty(int, notify=charisma_changed)
    def charisma(self):
        return self._charisma

    @charisma.setter
    def charisma(self, score: int):
        if score < 0:
            raise ValueError("AbilityScores cannot be negative")
        self._charisma = score

    @pyqtProperty(int, notify=constitution_changed)
    def constitution(self):
        return self._constitution

    @constitution.setter
    def constitution(self, score: int):
        if score < 0:
            raise ValueError("AbilityScores cannot be negative")
        self._constitution = score

    @classmethod
    def get_ability_class_names(cls):
        return cls.AbilityClass.__members__.keys()

    def scores_as_dict(self) -> dict:
        """Returns the ability scores as a dict"""
        return {
            "STRENGTH": self._strength,
            "DEXTERITY": self._dexterity,
            "INTELLIGENCE": self._intelligence,
            "WISDOM": self._wisdom,
            "CHARISMA": self._charisma,
            "CONSTITUTION": self._constitution,
        }


class AbilityScoreGenerator(ABC):
    """
    Abstract base class for algorithms that generate ability scores.
    """

    @staticmethod
    @abstractmethod
    def generate_scores(**kwargs) -> AbilityScores:
        """
        Generates a single AbilityScores tuple using a specified algorithm with
        arbitrary parameters.

        :param AbilityScores kwargs: Optional parameters for score generation.
        :returns AbilityScores
        """
        ...


class StandardScoreGenerator(AbilityScoreGenerator):

    @staticmethod
    def generate_scores(**kwargs) -> AbilityScores:
        """
        #TODO: Assign these totals to your ability scores as you see fit.

        Generates scores using the Standard Pathfinder algorithm. Roll 4d6,
        discard the lowest die result, and add the three remaining results
        together. Record this total and repeat the process until six numbers
        are generated. This method is less random than Classic and tends to
        create characters with above-average ability scores.

        :param dict kwargs: Optional parameters for score generation.
        :returns AbilityScores
        """
        return AbilityScores(**{
            ability: sum(sorted(roll(4, 6))[1:])
            for ability in AbilityScores.get_ability_class_names()
        })


class ClassicScoreGenerator(AbilityScoreGenerator):

    @staticmethod
    def generate_scores(**kwargs) -> AbilityScores:
        """
        #TODO: Assign these totals to your ability scores as you see fit.

        Classic: Roll 3d6 and add the dice together. Record this total and
        repeat the process until you generate six numbers. Assign these results
        to your ability scores as you see fit.

        This method is quite random, and some characters will have clearly
        superior abilities. This randomness can be taken one step further, with
        the totals applied to specific ability scores in the order they are
        rolled. Characters generated using this method are difficult to fit to
        predetermined concepts, as their scores might not support given classes
        or personalities, and instead are best designed around their ability
        scores.

        :param dict kwargs: Optional parameters for score generation.
        :returns AbilityScores
        """
        return AbilityScores(**{
            ability: sum(roll(3, 6))
            for ability in AbilityScores.get_ability_class_names()
        })


class HeroicScoreGenerator(AbilityScoreGenerator):

    @staticmethod
    def generate_scores(**kwargs) -> AbilityScores:
        """
        #TODO: Assign these totals to your ability scores as you see fit.

        Generate Heroic ability scores, easy difficulty.

        Roll 2d6 and add 6 to the sum of the dice. Record this total and
        repeat the process until six numbers are generated. Assign these
        totals to your ability scores as you see fit.

        This is less random than the Standard method and generates characters
        with mostly above-average scores.
        :param dict kwargs: Optional parameters for score generation.
        :returns AbilityScores
        """
        return AbilityScores(**{
            ability: sum(roll(2, 6)) + 6
            for ability in AbilityScores.get_ability_class_names()
        })


#: List of all score generator functions
SCORE_GENERATORS = {
    c.__name__: c.generate_scores
    for c in [
        StandardScoreGenerator,
        HeroicScoreGenerator,
        ClassicScoreGenerator,
    ]
}
