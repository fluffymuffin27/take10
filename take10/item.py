"""
.. module:: item
   :platform: Unix, Windows
   :synopsis: Item definitions

.. moduleauthor:: <fluffymuffin27@posteo.de>

"""


class Item(object):

    def __init__(
            self,
            name: str,
            weight: float,
            quantity: float=1.0,
            desc: str=None):
        """
        :param str name: Item name
        :param float weight: Item weight per 1 quantity
        :param float quantity: 'Amount' of item, defaults to 1
        :param str desc: Description of item (optional)
        :raises: ValueError
        """
        self.name = name  #: Name of the item
        if weight < 0:
            raise ValueError("Weight cannot be less than 0")
        self._weight = weight  #: How much 1 quantity of the item weights,in kg
        if quantity < 0:
            raise ValueError("Quantity cannot be less than zero")
        self._quantity = quantity  #: How many of the item there is (default 1)
        self.desc = desc  #: Description of the item

    @property
    def quantity(self) -> float:
        """Returns the quantity of the item"""
        return self._quantity

    @quantity.setter
    def quantity(self, q: float):
        """Sets the new quantity"""
        if q < 0:
            raise ValueError("Quantity cannot be less than zero")
        self._quantity = q

    @property
    def weight(self) -> float:
        """Returns the weight of one unit/quantity of the item"""
        return self._weight

    @weight.setter
    def weight(self, w: float):
        """Sets the new weight"""
        if w < 0:
            raise ValueError("Weight cannot be less than 0")
        self._weight = w

    def total_weight(self) -> float:
        """Returns the total weight of the item"""
        return self._quantity * self._weight
