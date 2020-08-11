import numpy as np 
import math

def comb2(n):
    return math.factorial(n) // (math.factorial(n-2) * math.factorial(2))

N = int(input())
S = {}
for i in range(N):
    s = ''.join(sorted(input()))
    if s in S.keys():
        S[s] += 1
    else:
        S[s] = 1
      
res = [comb2(e) if e>1 else 0 for e in S.values()]
print(sum(res))