"""
 Demonstrating use of Tuples.
 Tuples are ordered, unchangeable, and allow duplicated values.
 Tuples items are indexed.
"""
# setting tuple
values = ("a", "b", "c", "d", "e")

# or
# values = tuple(("a", "b", "c", "d", "e"))

print(values)
print(values[2])
print(values[2:4])

# Negative indexing means starting from the end of the tuple
print(values[-4: -1])

# Since tuples are unchangeable, transforming to list is necessary to make some alterations
# and after tranform to tuple
lst = list(values)
lst[1] = "x"
values = tuple(lst)
print(values)

# merge two tuples
tuple1 = ("a", "b")
tuple2 = ("c", "d")
tuple3 = tuple1 + tuple2
print(tuple3)
