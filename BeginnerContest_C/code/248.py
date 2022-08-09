# library
# input
N,M,K = map(int, input().split())

# const
divider = (998244353)

# solution
# dp = np.zeros((N+1, K+1))
dp = [[0] * (K + 1) for _ in range(N + 1)]
dp[0][0] = 1
for i in range(N):
    for j in range(K):
        for k in range(1, M+1):
            if j + k <= K:
                dp[i+1][j+k] += dp[i][j]

answer = sum(dp[-1]) % divider
print(answer)