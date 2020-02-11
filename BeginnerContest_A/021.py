N = int(input())
g = list()
cand = [1, 2, 4, 8]
while N != 0:
    if N in cand:
        g.append(N)
        N -= N
    else:
        c = max([e for e in cand if e <= N])
        g.append(c)
        N -= c

print(len(g))
for i in g:
    print(str(i))