# TAKOYAKI FESTIVAL2019

# libraries
from itertools import combinations

# input
N = int(input())
d = list(map(int, input().split()))

# solve
res = 0
for i, j in combinations(range(N), 2):
    res += d[i] * d[j]

# output
print(res)