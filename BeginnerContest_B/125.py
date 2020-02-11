# Resale

# libraries
import numpy as np

# input
N = int(input())
V = np.array(list(map(int, input().split())))
C = np.array(list(map(int, input().split())))

# solve
res = sum([max(0, v - c) for v, c in zip(V, C)])

# output
print(res)