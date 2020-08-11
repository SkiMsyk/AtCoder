N = int(input())
A = list(map(int, input().split()))

res = 0

num = [0]*(N)
cnt = [0]*(N)

for i in range(N):
    if A[i] > N:
        res += 1
    else:
        cnt[A[i]-1] += 1

for i in range(N):
    if cnt[i] < i+1:
        res += cnt[i]
    else:
        res += cnt[i] - (i+1)

print(res)