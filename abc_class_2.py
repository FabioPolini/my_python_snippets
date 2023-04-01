"""
 Snippet to demonstrating the usage of Abstract Class
"""
import random
from abc import ABC, abstractmethod


class Food(ABC):
    """ Base Class - Abstract """
    def __init__(self, order):
        self.order = order

    @abstractmethod
    def order_number(self):
        """ Random order number - prone to collision"""


class Shop(Food):
    """ This Class inherit Base Class"""
    def snacks(self):
        """ prints order quantity """
        print(f"Snacks: {self.order}")

    def order_number(self):
        return random.randint(1, 99999)


class Delivery(Shop):
    """ This Class inherit Shop Class """
    def zomato(self):
        """ print order quantity """
        print(f"Zomato: {self.order}")

    def order_number(self):
        return random.randint(1, 99999)


obj = Delivery(5)
obj.snacks()
obj.zomato()
print(obj.order_number())
