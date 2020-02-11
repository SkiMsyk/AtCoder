# Good Distance

# libraries
import numpy as np
from itertools import combinations

# input
N, D = map(int, input().split())
X = np.zeros(shape = (N, D))

for i in range(N):
    X[i] = np.array(list(map(int, input().split())))

# solve
def calc_distance(y,z):
    return np.sqrt(np.sum((y - z)**2))

res = 0

for y, z in combinations(X, r = 2):
    distance = calc_distance(y, z)
    if distance - int(distance) == 0:
        res += 1

# output
print(res)