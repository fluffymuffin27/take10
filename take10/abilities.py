"""
.. module:: abilities
   :platform: Unix, Windows
   :synopsis: Abilities definitions

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

from enum import Enum, unique
from abc import ABC, abstractmethod
from collections import namedtuple

from .dice import roll


@unique
class AbilityClass(Enum):
    """Standard Pathfinder ability classes"""
    STRENGTH = 0,
    DEXTERITY = 1
    INTELLIGENCE = 2
    WISDOM = 3
    CHARISMA = 4
    CONSTITUTION = 5


#: AbilityScores are named tuples containing the same fields as AbilityClass
AbilityScores = namedtuple(
    "AbilityScores",
    [k for k in AbilityClass.__members__.keys()]
)


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
            for ability in AbilityClass.__members__.keys()
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
            for ability in AbilityClass.__members__.keys()
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
            for ability in AbilityClass.__members__.keys()
        })
