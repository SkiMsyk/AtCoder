# Guidebook

# libraries
import numpy as np

# input
N = int(input())
res = []
for _ in range(N):
    s, p = input().split()
    res.append([s, -int(p), _+1])

# solve and output
for e in sorted(res):
    print(e[2])
