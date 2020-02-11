N = int(input())
S = list()
for _ in range(N):
    S.append(list(input()))

for _ in range(N):
    print(''.join([S[i][_] for i in range(N-1, -1, -1)]))