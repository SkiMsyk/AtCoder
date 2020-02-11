import numpy as np
N,K = map(int, input().split())
cp = np.array(list(map(int, input().split())))

# 正解
res = min(min(abs(l), abs(r)) + r - l for l, r in zip(cp, cp[K-1:]))

print(res)