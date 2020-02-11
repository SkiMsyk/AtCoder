S = input()
N = int(input())

# 最初の文字を特定
s1 = N // 5 - int(N % 5 == 0)
# 二つ目の文字列
s2 = N % 5 - 1 + int(N % 5 == 0)*5

print(S[s1] + S[s2])
