A, B = map(int, input().split())

# 回文数とは，先頭に0をつけない10進表記を文字列としてみたとき，
# 前から読んでも後ろから読んでも同じ文字列になるような正の整数
# 制約 10000 <= A <= B <= 99999
# 5桁で固定
# 3桁目まで決まれば回文は一つに定まるので3桁めまで見れば良い

res = 0

for i in range(10):
    for j in range(10):
        for k in range(10):
            cand = int(''.join([str(i), str(j), str(k), str(j), str(i)]))
            if A <= cand <= B:
                res += 1

print(res)