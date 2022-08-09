N = int(input())
A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))

res = 0

for i in range(N,0,-1):
    res = max(res, A1[0] + sum(A1[1:i]) + sum(A2[i-1:]))

print(res)