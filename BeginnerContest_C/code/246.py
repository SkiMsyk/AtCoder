from math import remainder
import numpy as np

# input
N, K, X = map(int, input().split())

# sort in decreasing
A = np.sort(np.array(list(map(int, input().split()))))[::-1]
total_raw_price = sum(A)

# solution
# クーポンの使い方を２つのタイプに分けて考える
# 1. price >= X の時
# 2. 0 < price < X の時
# 1の使い方で何枚使えるかを計算した後
# 2の使い方で最も金額を減らせる方法を積み上げる

# 0円にならないような使い方でできるだけ使う
coupons_used_type_1 = 0
for i, a in enumerate(A):
    if K == 0:
        break
    tmp = min(K, a // X)
    coupons_used_type_1 += tmp
    K -= tmp
    A[i] = a - (tmp * X)

discount_type1 = coupons_used_type_1 * X

# 0円以下になるような場合は金額が大きいものから使う
# Xで割ったあまりで並び替えた配列
A_modX = np.sort(A % X)[::-1]

# 残りのクーポン枚数だけ足し上げる
discount_type2 = sum(A_modX[:K]) if K > 0 else 0

# 割引金額の合計
total_discount = discount_type1 + discount_type2

# 合計金額を表示
print(total_raw_price - total_discount)