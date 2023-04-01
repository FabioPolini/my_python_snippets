"""
 Bool operations
"""

print(bool('abc'))
print(bool(23))

# False
print(bool(False))
print(bool(0))
print(bool(None))
print(bool(''))
print(bool())
print(bool(()))
print(bool({}))
print(bool([]))


class TrueClass:
    """ Base Class to return True when call len() method against Class.
        Just to demonstrating the examples below. To be honest, this is
        the worst example.
    """
    def __len__(self):
        return 10


print(TrueClass())
print(len(TrueClass()))
print(bool(TrueClass))
print(bool(len(TrueClass())))
