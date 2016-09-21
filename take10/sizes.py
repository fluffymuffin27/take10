"""
.. module:: sizes
   :platform: Unix, Windows
   :synopsis: Size definitions

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

from enum import Enum, unique
from math import inf
from memoize import memoize


@unique
class SizeClass(Enum):
    """
    Standard Paizo size classes.
    """
    Fine = 1
    Diminutive = 2
    Tiny = 3
    Small = 4
    Medium = 5
    Large = 6
    Huge = 7
    Gargantuan = 8
    Colossal = 8


@memoize
def typical_height(csize: SizeClass, metric: bool=False) -> (float, float):
    """
    Returns the minimum/maximum height range for a creature of the given size.

    Values are given in feet by default.

    """
    size_to_height = {
        SizeClass.Fine: (0.0, 0.5),
        SizeClass.Diminutive: (0.5, 1),
        SizeClass.Tiny: (1, 2),
        SizeClass.Small: (2, 4),
        SizeClass.Medium: (4, 8),
        SizeClass.Large: (8, 16),
        SizeClass.Huge: (16, 32),
        SizeClass.Gargantuan: (32, 64),
        SizeClass.Colossal: (64, inf),
    }
    height = size_to_height[csize]
    return height * 0.3048 if metric else height


@memoize
def typical_weight(csize: SizeClass, metric: bool=False) -> (float, float):
    """
    Returns the minimum/maximum weight range for a creature of the given size.

    Values are given in pounds by default.
    """
    size_to_weight = {
        SizeClass.Fine: (0.0, 0.125),
        SizeClass.Diminutive: (0.125, 1),
        SizeClass.Tiny: (1, 8),
        SizeClass.Small: (8, 60),
        SizeClass.Medium: (60, 500),
        SizeClass.Large: (500, 4000),
        SizeClass.Huge: (4000, 32000),
        SizeClass.Gargantuan: (32000, 250000),
        SizeClass.Colossal: (250000, inf),
    }
    weight = size_to_weight[csize]
    return weight * 0.45359237 if metric else weight
