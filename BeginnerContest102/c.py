import numpy as np

n = int(input())
a = np.array(list(map(int, input().split())))
a2 = np.sort(a - np.arange(1,n+1))

# 中央値が正解
b = int(np.median(a2))
res = sum(abs(a2-b))

print(res)