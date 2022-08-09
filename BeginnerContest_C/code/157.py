n,m = map(int,input().split())
s = [0]*m
c = [0]*m
for i in range(m):
    si, ci = input().split()
    s[i] = int(si)
    c[i] = ci

ans = -1

for i in range(1000):
    test = True
    e = str(i)
    if len(e) == n:
        for si, ci in zip(s,c):
            if  e[si-1] != ci:
                test = False
                break 
        if test:
            ans = i
            break

print(ans)        