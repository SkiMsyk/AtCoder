import numpy as np
n, k = map(int, input().split())
a = list(map(int, input().split()))

# (N-1)/(K-1)
res = int(np.ceil((n-1)/(k-1)))

print(res)