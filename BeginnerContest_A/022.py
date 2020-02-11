N, S, T = map(int, input().split())
W = int(input())
a = [int(input()) for _ in range(N-1)]

res = int(S <= W and W <= T)

for i in a:
    W += i
    if S <= W and W <= T:
        res += 1

print(res)