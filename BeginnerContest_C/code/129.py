N, M = map(int, input().split())
a = [0] * (N+1)
for _ in range(M):
    i = int(input())
    a[i] = 1

dp = [0] * (N+2)
dp[N] = 1
mod = 1000000007

for i in range(N-1, -1, -1):
    if a[i]:
        dp[i] = 0
        continue
    dp[i] = (dp[i+1] + dp[i+2]) % mod 

print(dp[0])