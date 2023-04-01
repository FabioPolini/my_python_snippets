"""
 Snippet demonstrating use of global var
 Bad code, just to demonstrating
"""

MY_AGE = 30


def age():
    """ Prints a fixed age. Changes outside var MY_AGE using Global Statement - bad code """
    global MY_AGE
    MY_AGE = 31
    print(f"My age is: {MY_AGE}")


age()
print(f"My age is: {MY_AGE}")
