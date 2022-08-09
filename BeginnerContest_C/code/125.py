def gcd(x,y):
    x, y = max(x,y), min(x,y)
    if y == 0:
        return x
    return gcd(x % y, y)

n = int(input())
a = list(map(int,input().split()))

l = [0]*n
r = [0]*n
for i in range(1,n):
    l[i] = gcd(l[i-1], a[i-1])
    r[-i-1] = gcd(r[-i], a[-i])

ans = 0

for li,ri in zip(l,r):
    ans = max(gcd(li,ri), ans)

print(ans)