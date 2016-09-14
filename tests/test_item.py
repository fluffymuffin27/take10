"""
.. module:: test_item
   :platform: Unix, Windows
   :synopsis: Item tests

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""
import unittest

from context import take10
from take10 import item


class TestItem(unittest.TestCase):

    def test_invalid_params(self):
        """Tests for invalid weight/quantity"""
        with self.assertRaises(ValueError):
            item.Item("Test", -1)
            item.Item("Test", 1, -1)


if __name__ == "__main__":
    unittest.main()
