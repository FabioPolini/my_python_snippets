"""
 Demonstrating use of Sets
  Set items are unchangeable, unordered, and do not allow duplicates, but you can remove/add items
"""
# setting the Set
transports = {"cars", "bikes", "cycle"}
print(transports)

# add some item
transports.add("boat")
print(transports)

# remove some item
transports.remove("boat")
print(transports)

# check if item in items
print("cars" in transports)

# add items in existing Set
transports.update(["airplane", "bus", "truck"])
print(transports)

# removes specific item
transports.discard("cycle")
print(transports)

# removes a RANDOM item
transports.pop()
print(transports)

# clear th Set
transports.clear()
print(transports)

# or del if you desire get rid of var
# del transports


a = {1, 2, 3}
b = {4, 5, 6}

# union
c = a.union(b)
print(c)
