N, M = map(int, input().split())
A = [0]*N
B = [0]*M
for _ in range(N):
    A[_] = input()
for _ in range(M):
    B[_] = input()

res = 'No'

for r in range(N-M+1):
    for c in range(N-M+1):
        if B == [e[r:r+M:1] for e in A[c:c+M:1]]:
            res = 'Yes'
            break

print(res)