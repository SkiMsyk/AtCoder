N = int(input())
V = sorted(list(map(int, input().split())))
res = (V[0] + V[1])/2
for i in range(2,N):
    res = (res + V[i]) / 2
print(res)