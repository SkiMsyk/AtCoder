import math
n,k = map(int,input().split())
ans = 0
for i in range(1,n+1):
    x = max(0,math.ceil(math.log2(k/i)))
    p = (1/n) * (1/2)**x
    ans += p
print(ans)
    