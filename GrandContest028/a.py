import numpy as np

n, m = map(int, input().split())
s = input()
t = input()

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

# 最初の文字が異なれば -1 
if s[0] != t[0]:
    print(-1)
elif s == t:
    print(len(s))
else:
    LeastCommonMultiple  = lcm(n,m)
    l = int(LeastCommonMultiple)
    nOl = l // n
    mOl = l // m
    sinX = [i * nOl + 1 for i in range(n)]
    tinX = [i * mOl + 1 for i in range(m)]
    matchList = list(set(sinX) & set(tinX))

    scX = [sinX.index(commonIndex) for commonIndex in matchList]
    tcX = [tinX.index(commonIndex) for commonIndex in matchList]

    if [s[sMatch] for sMatch in scX] == [t[tMatch] for tMatch in tcX]:
        print(l)
    else:
        print(-1)