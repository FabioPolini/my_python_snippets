"""
 Some operation with lists - python don't have array data type.
 List can be used instead with some restrictions.
 Use Numpy if you need array data type
 Lists are mutable, ordered, can store mix types and allow duplicate values
"""

# init array
lst = ['abc', 'def', 'opq']
print(lst)

# set value at specific index/position
lst[0] = 'ghi'
print(lst)

# append value
lst.append('xyz')
print(lst)

# remove value at specific index/position
lst.pop(1)
print(lst)

# remove specific value - only first occurrence
lst.remove('xyz')
print(lst)

# reverse index/position
lst.reverse()
print(lst)

# insert value at specific index/position
lst.insert(0, 'lmn')
print(lst)

# return index - first occurrence
print(lst.index('lmn'))

# count occurrence
print(lst.count('abc'))

# copy values from one list to another. If you write new_lst = lst, new_lst will create
# a reference to lst var. Any changes made in lst will reflect in new_lst.
new_lst = lst.copy()
# or use built-in method list ()
# new_lst = list(lst)
print(new_lst)

# clear list (None)
print(lst.clear())

# append value
lst.append('zdr')
print(lst)

# add values in the end of list, can be values, lists, etc
lst.append(new_lst)
print(lst)

# init 5 index with same value
lst = ['text'] * 5
print(lst)
