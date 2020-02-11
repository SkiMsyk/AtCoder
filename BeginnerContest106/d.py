# setting
from itertools import accumulate

#------------------
n, m, q = map(int, input().split())

LR = [[0 for _ in range(n-i)] for i in range(n)]
for i in range(m):
    l, r = map(int, input().split())
    LR[l-1][r-l] += 1

for i in range(n-2, -1, -1):
    for j, acc in enumerate(accumulate(LR[i])):
        LR[i][j] = acc  + (0 if j == 0 else LR[i+1][j-1])

res = list()
for i in range(q):
    p,q = map(int, input().split())
    res.append(LR[p-1][q-p])

for r in res:
    print(r)