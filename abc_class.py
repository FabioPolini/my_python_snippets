"""
 Snippet demonstrating the usage of Abstract Class
"""

from abc import ABCMeta, abstractmethod


class BaseClass(metaclass=ABCMeta):
    """ Base Class - abstract """
    @abstractmethod
    def attrib1(self):
        """ method abstract """

    @abstractmethod
    def attrib2(self):
        """ method abstract """


class ConcreteClass(BaseClass):
    """ This Class inherits Base Class"""
    def attrib1(self):
        pass

    def attrib2(self):
        pass


instance = ConcreteClass()
