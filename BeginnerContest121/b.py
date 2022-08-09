import numpy as np

N, M, C = map(int, input().split())
B = np.array(list(map(int, input().split())))

res = 0

for i in range(N):
    A = np.array(list(map(int, input().split())))
    if sum(A*B) + C > 0:
        res += 1

print(res)

