import math

n, k = map(int, input().split())
if k <= math.ceil(n/2):
    print("YES")
else:
    print("NO")