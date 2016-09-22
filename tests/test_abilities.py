"""
.. module:: test_dice
   :platform: Unix, Windows
   :synopsis: Tests for ability score generation

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""

import unittest

from context import take10
from take10 import abilities


class TestAbilities(unittest.TestCase):
    """#TODO: Write ability score tests"""

    def test_ability_generators(self):
        """Tests the ability score generators"""
        for name, score_gen in abilities.SCORE_GENERATORS.items():
            scores = score_gen().scores_as_dict()
            self.assertListEqual(
                [],
                list(filter(lambda v: v < 0, scores.values())),
                "AbilityScores cannot be less than 0"
            )

    def test_ability_set(self):
        """Tests setting invalid ability values"""
        scores = abilities.ClassicScoreGenerator.generate_scores()
        scores.strength = 10     # Should be ok
        scores.intelligence = 0  # Should also be ok
        with self.assertRaises(ValueError):
            scores.charisma = -1


if __name__ == "__main__":
    unittest.main()
