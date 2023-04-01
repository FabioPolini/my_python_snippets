"""
 Demonstrating some exceptions - Pylint cries here
"""

# General exception
try:
    print(x)
except Exception as e:
    print(f"throw error: {e}")

try:
    raise 'asd'
except NameError as e:
    print(f"Name error: {e}")
except Exception as e:
    print(f"Other exception: {e}")

try:
    raise 'asd'
except NameError as e:
    print(f"Name error: {e}")
except Exception as e:
    print(f"Other exception: {e}")
finally:
    print("finally")

# raise an exception
try:
    raise Exception('raising an exception')
except Exception as e:
    print(f"Manual exception: {e}")

if not False:
    raise TypeError("Only integer allowed")
