import numpy as np
A = np.array(sorted(list(map(int, input().split()))))
res = sum(np.abs(np.diff(A)))
print(res)
