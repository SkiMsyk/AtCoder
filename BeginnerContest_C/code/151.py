n,m = map(int,input().split())
a = [0]*(n+1)
w = [0]*(n+1)
wc = 0
ac = 0
for _ in range(m):
    pi,si = input().split()
    pi = int(pi)
    if (si == 'WA') and (a[pi] == 0) :
        w[pi] += 1
    elif si == 'AC' and (a[pi] == 0):
        a[pi] = 1
        ac += 1
        wc += w[pi]

print(ac, wc)
