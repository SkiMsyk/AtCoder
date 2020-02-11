import numpy as np

# input
N = int(input())
S = [1 if e == 'I' else -1 for e in input()]
print(max(max(np.cumsum(S)), 0))

