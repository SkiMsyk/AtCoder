# Bite Eating
import numpy as np

# input
N, L = map(int, input().split())

def taste(i, L=L):
    return L + i -1

T = [taste(i) for i in range(1, N+1)]

# solve
diff_value = np.inf
diff_total = np.inf

for i in range(N):
    if diff_value > abs(T[i]) and diff_total > abs(sum(T) - (sum(T) - T[i])):
        diff_value = abs(T[i])
        diff_total = abs(sum(T) - (sum(T) - T[i]))
        res = sum(T) - T[i]

# output
print(res)
