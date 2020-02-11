# 81

# libraries
from itertools import combinations

# input
N = int(input())

# solve
l = list(range(1,10))
if N in [i*j for i, j in combinations(l+l, 2)]:
    print('Yes')
else:
    print('No')
