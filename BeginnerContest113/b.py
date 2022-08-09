import numpy as np

# x: T-x * 0.006
# 平均気温がA度に最も近い点を選ぶ
n = int(input())
t, a = map(int, input().split())
h = np.array(list(map(int, input().split())))
h2 = abs((t-h*0.006) - a)
res = np.where(h2==min(h2))[0][0] + 1

print(res)