# Balance
import numpy as np

# libraries

# input
N = int(input())
W = list(map(int, input().split()))

# solve
diff = np.inf
for _ in range(len(W)):
    s1 = sum(W[:_])
    s2 = sum(W[_:])
    diff = min(diff, abs(s1-s2))

# output
print(diff)