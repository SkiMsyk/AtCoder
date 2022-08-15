N = int(input())
P = [0,0] + list(map(int, input().split()))

# 同じ親がいる可能性があるので
# 親の親を見る
ans = 1
p = P[-1]
while p != 1:
    ans += 1
    p = P[p]
print(ans)
