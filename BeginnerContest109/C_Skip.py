import numpy as np

def gcd(a,b):
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b

N, X = map(int, input().split())
towns = list(map(int, input().split()))
towns.insert(0, X)

diff_towns = np.abs(np.diff(towns))
if len(diff_towns) == 1:
    cand = diff_towns[0]
else:
    cand = gcd(diff_towns[0], diff_towns[1])
    for i in range(2,len(diff_towns)):
        cand = gcd(cand, diff_towns[i])    

print(cand)