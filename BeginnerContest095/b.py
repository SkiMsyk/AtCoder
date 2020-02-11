n, x = map(int, input().split())
m = list()
for _ in range(n):
    m.append(int(input()))

# 最低一つずつは作る
rem = x - sum(m)

# 残った粉で一番少ない使用量の物をたくさん作る
res = n + (rem // min(m))

print(res)