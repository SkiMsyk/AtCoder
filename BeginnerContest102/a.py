def gcd(a,b):
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b

# 最小公倍数を求める関数
def lcm(a,b):
    return int((a*b)/gcd(a,b))

n = int(input())
print(lcm(2,n))

# 2で割り切れればnだし，割り切れなければ2*nとなるので，もっと早いのは
# if n % 2 == 0:
#     res = n
# else:
#     res = n * 2
# print(res)