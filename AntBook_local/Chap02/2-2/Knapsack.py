# weight : wi,
# value : vi,
# item amount : n
# これらのitemから重さの総和が W を超えないように選んだ時の vi の総和の最大値を求めよ

# input
n = 4
# wv = [(2,3),(1,2),(3,4),(2,2)]
w = [2,1,3,2] # weight
v = [3,2,4,2] # value
W = 5

# 方針1 : それぞれのitemを入れるか入れないかで分岐して探索 O(n^2)
# 愚直な実装
def rec(i, j):
    res = 0
    if i == n:
        # もう品物は残っていない
        res = 0
    elif j < w[i]:
        # もう品物は入らない
        res = rec(i + 1, j)
    else:
        # 入れない場合と入れる場合を両方試す
        res = max(rec(i + 1, j), rec(i+1, j-w[i]) + v[i])
    return res


print(rec(0,W))

# 方針2
# すでに調べたことのあるものは結果を保存しておく
def rec2(i, j):
    memo = [[-1]*(W+1) for _ in range(n+1)]
    
    # ----
    # すでに計算したものはその結果を利用する
    if memo[i][j] >= 0:
        return memo[i][j]
    # ----
    if i == n:
        res = 0;
    elif j < w[i]:
        res = rec2(i + 1, j)
    else:
        res = max(rec2(i + 1, j), rec2(i+1, j-w[i]) + v[i])
    memo[i][j] = res
    return res

print(rec2(0, W))