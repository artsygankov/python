# Program with using reduce
from functools import reduce


def sum_usr(a, b):
    return a * b


print(reduce(sum_usr, [idx for idx in range(100, 1001, 2)]))
