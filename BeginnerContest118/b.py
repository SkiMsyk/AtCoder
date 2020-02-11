N, M = map(int, input().split())
K = []
A = []
for i in range(N):
    tmp = list(map(int, input().split()))
    K.append(tmp[0])
    A.append(set(tmp[1:]))

res = A[0]
for i in range(1,N):
    res = res & A[i]

print(len(res))