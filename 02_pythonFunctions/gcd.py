# 最大公約数を求める関数
def gcd(a,b):
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b

# 最小公倍数を求める関数
def lcm(a,b):
    return (a*b)/gcd(a,b)