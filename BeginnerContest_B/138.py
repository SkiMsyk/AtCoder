# Resistors in Parallel
import numpy as np

# input
N = int(input())
A = np.array(list(map(int, input().split())))

# solve
res = 1 / np.sum(1 / A)

# output
print(res)