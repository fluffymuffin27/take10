"""
.. module:: races
   :platform: Unix, Windows
   :synopsis: Race definitions and utilities

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

from abc import ABC,  abstractmethod
from typing import Iterable

from .abilities import AbilityScores
from .skills import SkillSet


class Race(ABC):
    """
    A race can be thought of the individual species to which a character or
    creature belongs to. Being a member of a specific race means taht you are
    conferred specific bonuses, permanent and temporary, that are unique to
    your race in particular.

    'Half-breeds' of two races that are sexually compatible are treated (for
    whatever reason) as if they were of a separate race, with few exceptions.

    Subclasses are expected to implement these hooks when instantiating a
    particular race.
    """

    @abstractmethod
    def get_starting_ability_bonus(self) -> Iterable(AbilityScores):
        """
        Gets the possible AbilityScore bonuses for a given race.

        Normally, races give the creator of the character a simple bonus to a
        subset of AbilityClasses (e.g. +1 to Intelligence).

        However, some races give the creator a choice of which AbilityClass
        they can choose to increase or decrease certain starting statistics.
        As such, this function may instead return the possible AbilityScore
        bonuses that may be used when creating this particular race.

        :returns All possible AbilityScores for the race's starting bonuses
        """
        ...

    @abstractmethod
    def get_starting_skill_bonus(self) -> Iterable(SkillSet):
        """
        Gets the possible SkillSet bonuses for a given race.

        Normally, races give the creator of the character a simple bonus to a
        subset of skills (e.g. +1 to Swim).

        However, some races give the creator a choice of which SkillClass
        they can choose to increase or decrease certain starting statistics.

        As such, this function may instead return the possible SkillSet
        bonuses that may be used when creating this particular race.

        :returns All possible SkillSets for the race's starting bonuses
        """
        ...
