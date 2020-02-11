A, B, C, K = map(int, input().split())
S, T = map(int, input().split())

res = S*A + T*B

if S + T >= K:
    res -= C*(S+T)

print(res)