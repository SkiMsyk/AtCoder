# Distance
import math
N,D = map(int,input().split())
ans = 0
for _ in range(N):
    x,y = map(int,input().split())
    ans += [0, 1][math.sqrt(x**2 + y**2) <= D]
print(ans)