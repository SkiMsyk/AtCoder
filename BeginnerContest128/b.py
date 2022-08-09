N = int(input())
d = dict()
for _ in range(N):
    S, P = input().split()
    if S not in d.keys():
        d[S] = dict()
        d[S][_+1] = int(P)
    else:
        d[S][_+1]