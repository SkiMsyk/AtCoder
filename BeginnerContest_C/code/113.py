n,m = map(int,input().split())
d = {}
for i in range(m):
    pi, yi = map(int,input().split())
    pi = str(pi).zfill(6)
    if pi not in d.keys():
        d[pi] = []
    d[pi].append([i,yi])

ans = []

for k,v in d.items():
    for i,l in enumerate(sorted(v, key=lambda x:(x[1]))):
        ans.append([l[0], k+str(i+1).zfill(6)])

for e in sorted(ans):
    print(e[1])