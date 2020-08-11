N = int(input())
H = list(map(int, input().split())) + [0]
res = 0
mv = 0
for i in range(1, N):
    if H[i-1] >= H[i]:
        mv += 1
    else:
        res = max(res, mv)
        mv = 0
res = max(res, mv)
print(res)