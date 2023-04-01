"""
 Demonstrating use of reduce() function
"""
from functools import reduce
from operator import add

values = [1, 2, 3, 4, 5, 6]
result = reduce(lambda i, j: i + j, values)
print(result)

# for loop example
result = 0
for n in values:
    result += n
print(result)

# using sum()
print(sum(values))


# using user defined function instead lambda
def my_sum(i, j):
    """ add 2 numbers """
    return i + j


print(reduce(my_sum, values))

# using add operator
print(reduce(add, values))
