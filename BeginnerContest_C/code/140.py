N = int(input())
B = [10**5+1] + list(map(int, input().split())) + [10**5+1]
res = 0
for i in range(1, N+1):
    res += min(B[i-1], B[i])
print(res)
