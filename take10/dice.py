"""
.. module:: dice
   :platform: Unix, Windows
   :synopsis: Dice emulators

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

from random import randint


def roll(num_dice: int, dice_type: int):
    """Emulates rolling a dice_type-sided die num_dice times.

    :param num_dice: number of dice to roll
    :type num_dice: int.
    :param dice_type: how many sides each dice has
    :type dice_type: int.
    :returns: iterator of dice values, or value if only 1 die specified
    :raises: ValueError
    """
    if num_dice < 0 or dice_type < 0:
        raise ValueError("Invalid values for dice_type/num_dice")
    if num_dice == 1:
        return randint(1, dice_type)
    else:
        return (randint(1, dice_type) for _ in range(num_dice))
