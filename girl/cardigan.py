import operator
from functools import reduce

n = int(input())
result = reduce(operator.mul, range(1, n + 1))
print(result)
