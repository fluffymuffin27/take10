"""
.. module:: test_dice
   :platform: Unix, Windows
   :synopsis: Tests for dice emulators

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

import unittest

from context import take10
from take10 import dice


class TestDice(unittest.TestCase):

    def test_roll_single_dice(self):
        """Tests for single dice roll"""
        roll = dice.roll(1, 6)  # Emulates rolling 1d6
        self.assertLessEqual(roll, 6)

    def test_roll_multidice(self):
        """Tests for multiple dice rolls"""
        rolls = dice.roll(4, 10)  # Emulates rolling 4d10
        self.assertIsNotNone(rolls)
        for roll in rolls:
            self.assertLessEqual(roll, 10)

    def test_valid_values(self):
        """Tests for (in)valid dice values"""
        with self.assertRaises(ValueError):
            dice.roll(-1, 2)
            dice.roll(2, -1)
        # Should return empty iterators
        with self.assertRaises(StopIteration):
            self.assertIsNone(next(dice.roll(0, 0)))
            self.assertIsNone(next(dice.roll(10, 0)))


if __name__ == "__main__":
    unittest.main()
