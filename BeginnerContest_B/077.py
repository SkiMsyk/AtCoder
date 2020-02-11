# input
N = int(input())

# solution
import numpy as np
for i in range(N, 0, -1):
    if np.sqrt(i) - int(np.sqrt(i)) == 0:
        print(i)
        break
