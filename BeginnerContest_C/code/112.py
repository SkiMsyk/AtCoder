import numpy as np
n = int(input())
x = [0] * n
y = [0] * n
h = [0] * n
for i in range(n):
    x[i], y[i], h[i] = map(int,input().split())
x = np.array(x)
y = np.array(y)
h = np.array(h)

for cx in range(0,101):
    for cy in range(0,101):
        cand = h + np.abs(x - cx) + np.abs(y - cy)
        # hi = 0 の時は，他のcandの要素よりも低ければOK
        canda = cand[h == 0]
        candb = cand[h != 0]
        if len(canda) != 0:
            if (len(np.unique(candb)) == 1) and (min(canda) >= max(candb)):
                ans = '{} {} {}'.format(cx, cy, max(candb))
                break
        else:
            if len(np.unique(cand)) == 1:
                ans = '{} {} {}'.format(cx, cy, max(cand))
                break

print(ans)
