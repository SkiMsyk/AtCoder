import math
n = int(input())
x = list(map(int, input().split()))
t = sum(x) / n
cand = [math.floor(t),math.ceil(t)]
diff = [abs(t-e) for e in cand]
p    = cand[diff.index(min(diff))]

ans = 0
for i in range(n):
    ans += (x[i]-p)**2
    
print(ans)