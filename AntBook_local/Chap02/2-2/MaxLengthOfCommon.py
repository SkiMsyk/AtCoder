# 最長共通部分列問題（LCS : Longest Common Subsequence）
# 2つの文字列
# s1, s2,..., sn
# t1, t2,..., tm
# が与えられる．この二つの共通部分列の長さの最大値を求めよ

# input

n = int(input())
m = int(input())
s = input()
t = input()

# dp[i][j] = s1,...,si と t1,...,tj に対するLCSの長さ
dp = [[0]*(n+1) for _ in range(m+1)]

for i in range(n):
    for j in range(m):
        if s[i] == t[j]:
            dp[i+1][j+1] = dp[i][j] + 1
        else:
            dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])

print(dp[n][m])