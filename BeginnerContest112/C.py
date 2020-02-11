import numpy as np
n = int(input())
xyh = list()
for i in range(n):
    x,y,h = map(int, input().split())
    # omit h = 0
    if h == 0:
        continue
    else:
        xyh.append([x,y,h])
xyh = np.array(xyh)
print(xyh)


