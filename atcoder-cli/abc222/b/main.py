import numpy as np

N, P = map(int, input().split())
a = np.array(list(map(int, input().split())))

ans = sum(a < P)

print(ans)
