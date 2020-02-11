N, M = map(int, input().split())
res = [0]*N
for _ in range(M):
    a, b = map(int, input().split())
    res[a-1] += 1
    res[b-1] += 1
for _ in range(N):
    print(res[_])