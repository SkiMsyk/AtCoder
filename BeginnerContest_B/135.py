# 0 or 1 Swap

# libraries
import numpy as np

# input
N = int(input())
p = np.array(list(map(int, input().split())))

# solve
ideal = np.sort(p)

if sum(p != ideal) <= 2:
    print('YES')
else:
    print('NO')