N, M = map(int, input().split())

starts = [0]*N
for _ in range(N):
    starts[_] = list(map(int, input().split()))

ends = [0]*M
for _ in range(M):
    ends[_] = list(map(int, input().split()))

for _ in range(N):
    cand = [abs(starts[_][0] - e[0]) + abs(starts[_][1] - e[1]) for e in ends]
    print(cand.index(min(cand))+1)
