N, M = map(int, input().split())

starts = [0]*N
for _ in range(N):
    starts[_] = list(map(int, input().split()))

ends = [0]*M
for _ in range(M):
    ends[_] = list(map(int, input().split()))

for _ in range(N):
    cand = [abs(s[0] - e[0]) + abs(s[1] - e[1]) for s, e in zip(starts, ends)]
    print(cand.index(min(cand)))

