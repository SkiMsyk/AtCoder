N = int(input())
res = 101
for _ in range(N):
    res = min(res, int(input()))
print(res)
