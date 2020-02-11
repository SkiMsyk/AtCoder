# 1, 5, 10, 50, 100, 500
coin_values = [1, 5, 10, 50, 100, 500]
coin_amounts = [3, 2, 1, 3, 0, 2]
payment = 620

# 方針
# 大きいコインからなるべく多く使っていく

res = [0]*6
for i in range(5,-1,-1):
    # コインを使う枚数 整数商かコインの枚数の小さい方をとる
    t = min(payment // coin_values[i], coin_amounts[i])
    # paymentsから支払分を引く
    payment -= t * coin_values[i]
    # コインの枚数を足しあげる
    res[i] = t

print(res)
print(sum(res))