import numpy as np

N, M = map(int, input().split())
edges = np.zeros((N+1,N+1))

for i in range(M):
    u,v = map(int, input().split())
    edges[u][v] = 1
    edges[v][u] = 1

ans = 0

for a in range(N+1):
    for b in range(a+1, N+1):
        for c in range(b+1, N+1):
            if edges[a][b] == 1 and edges[b][c] == 1 and edges[c][a] == 1:
                ans += 1

print(ans)

