""""
 Demonstrtaing use of map()
"""

# mapping values ^ 2
values = [12, 43, 33, 1, 13]
print(list(map(pow, values, [2] * len(values))))

# or this way - better than previous
print([i ** 2 for i in values])
