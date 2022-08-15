from itertools import combinations
import numpy as np

N = int(input())
seq = np.array(list(map(int, input().split())))
ind = np.arange(1, N+1)

diff = 0
same = 0

for s,i in zip(seq,ind):
    # 添字と要素が同じ場合
    if s == i:
        same += 1
    else:
        # 添字と要素が異なる場合は，要素が添字になっている要素を見にいく
        if seq[s-1] == i:
            diff += 1

if same > 1:
    ans = diff // 2 + (same * (same - 1)) // 2
else:
    ans = diff // 2

print(ans)