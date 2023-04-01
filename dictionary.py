"""
 Demonstrating use of dictionaries.
 Dictionaries are ordered, changeable, and does not allow duplicates
"""

# dict constructor to make new dictionary
# pylint cries here
test = dict(a='cars', b='bikes', c='cycle')
print(test)

# or
k = {'a': 'cars', 'b': 'bikes', 'c': 'cycle'}
print(k)

# dict keys, values and items
print(k.keys())
print(k.values())
print(k.items())

# dict keys and values as list
print(list(k.keys()))
print(list(k.values()))
print(list(k.items()))

# pick value with key name
print(k['b'])

# or
print(k.get('b'))

# update value
k['b'] = 'tractor'
print(k)

# iterate through dictionary values
for i in k:
    print(i)

# iterate through dictionary values
# pylint cries here, and he is right - iterate with k.items()
for i in k:
    print(k[i])

# or
for i in k:
    print(k.get(i))

# or
for i in k.values():
    print(i)

# or
for i, j in k.items():
    print(i, j)

# loop through
if "cycle" in k.values():
    print(True)

# append values
k['d'] = 'motor'
print(k)


# remove key-pair from dict
k.pop('d')
print(k)

# or
del k['c']
print(k)

# remove last key-pair item from dict
k.popitem()
print(k)

# take copy of the existing dict. If you use m = k, a reference will be created and alteration in k
# will reflect in m dict.
m = k.copy()
n = dict(k)
print(m)
print(n)

# removes all key-pair value from dict
k.clear()
print(k)

# nested dictionary
x = {0: {'a': 'love', 'b': 'peace'}, 1: {'c': 'pasta', 'd': 'noodles'}, 2: {'e': 'tea'}}
print(x)

# call from outside
d1 = {'a': 'love', 'b': 'peace'}
d2 = {'c': 'pasta', 'b': 'noodles'}
d3 = {'e': 'tea'}
d = {
    0: d1,
    1: d2,
    2: d3
}
print(d)
