n, m = map(int, input().split())
x = sorted(list(map(int, input().split()))) # 昇順に並び替え
diff = sorted([abs(e1 - e2) for e1, e2 in zip(x, [x[0]]+x[:-1])], reverse = True)

# 2個目以降はコストが大きいものから消えていくと考える
if n >= m:
    res = 0
else:
    res = sum(diff[n-1:])

print(res)