n, k = map(int, input().split())
a = list(map(int, input().split()))

# 各桁の値の0, 1の数をカウントして，多い方の逆をとる
digit = len(bin(max(a))[2:])

zero_counter = [0]*digit
one_counter = [0]*digit

def f(x):
    return sum([e ^ x for e in a])

for e in a:
    ebin = list(bin(e)[2:])
    edig = len(ebin)
    zero_counter = [e + 1 if b == "0" else e + 0 for e, b in zip(zero_counter, [0]*(digit-edig)+ebin)]
    one_counter = [e + 1 if b == "1" else e + 0 for e, b in zip(zero_counter, [0]*(digit-edig)+ebin)]

# import ipdb; ipdb.set_trace()

max_digit = len(bin(k)[2:])
argmin_str = ''.join(['1' if e1 >= e2 else '0' for e1, e2 in zip(zero_counter, one_counter)])
argmin = int('1'*(max_digit - len(argmin_str)) + argmin_str, 2)
res = f(argmin)

print(res)
