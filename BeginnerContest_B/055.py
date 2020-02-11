import numpy as np
N = int(input())
res = 1
for _ in range(1, N+1):
    res = (res * _) % (10**9 + 7)
print(res)
