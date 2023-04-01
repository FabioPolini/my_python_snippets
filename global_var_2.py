"""
 Global MY_AGE was defined inside age() method - BAD CODE - Pylint cries - Just for demonstrating
"""


def age():
    """ Prints MY_AGE value. Set local var GLOBAL - BAD CODE"""
    global MY_AGE
    MY_AGE = 30
    print(f"My age is: {MY_AGE}")


age()

# Works if age() method was calling, since MY_AGE need to be set
# inside previous method - BAD CODE
print(f"My age is: {MY_AGE}")
