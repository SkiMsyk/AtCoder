import numpy as np
from itertools import combinations, permutations
import math

N = int(input())
t = np.zeros((N, 2))
for _ in range(N):
    t[_] = np.array(list(map(int, input().split())))

def distance(i, j):
    return np.sqrt(np.sum((t[i] - t[j])**2))

dm = np.zeros((N,N))

for i, j in combinations(range(N), 2):
    dm[i, j] = distance(i, j)

total = 0
for r in permutations(range(N), N):
    r = list(r)
    for i, j in zip(r[:-1], r[1:]):
        total += dm[min(i,j),max(i,j)]
    
res = total / math.factorial(N)
print(res)
