# 全ての要素の積 x は全ての要素 ei で割り切れる
# すなわち(x-1)は各要素 ei で割った時のあまりが ei-1 となる
# よって m = x-1 の時f(m)は最大値を取る
n = int(input())
res = sum(list(map(int, input().split()))) - n
print(res)