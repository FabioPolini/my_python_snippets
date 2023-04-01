"""
Demonstrating filter()
"""

# some values

values = [1, 2, 3, 4, 5, 6]

# get only values < 4
result = [i for i in values if i < 4]
print(result)

# filter() function
result2 = list(filter(lambda i: i < 4, values))
print(result2)
