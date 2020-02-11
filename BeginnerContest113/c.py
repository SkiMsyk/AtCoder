import numpy as np

n, m = map(int, input().split())
ps = [[] for _ in range(n)]
res = [[] for _ in range(n)]
pp = []
for i in range(m):
    p, y = map(int, input().split())
    ps[p-1].append(y)
    pp.append(p)

num = [np.argsort(l) for l in ps]

for i in range(len(num)):
    for e in num[i]:
        res[i].append(('0'*(6-len(str(i))) + str(i+1) + '0'*(6-len(str(e+1))) + str(e+1)))

for p in pp:
    print(res[p-1].pop(0))
