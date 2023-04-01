"""
 Demonstrating use of closure
"""


def calculation():
    """ simple method to demonstrate enclosure """
    some_val = 10

    def prt():
        """ this method visible  only inside calculation() method"""
        # var some_val is visible inside calculation() scope
        print(some_val)
    prt()


calculation()


def other_calculation(val_1):
    """ Calling this method will return add() method """
    def add(val_2):
        """ simple sum """
        return val_1 + val_2
    # when returning the method add(), var val_1 will return too, fixing the value
    # successive call will add param val_2 to val_1
    return add


result = other_calculation(100)
print(result(50))
print(result(25))
