# Ordinary Number

# libraries
import numpy as np

# input
n = int(input())
p = list(map(int, input().split()))

# solve
res = 0
for i in range(1, n-1):
    s = [p[i-1], p[i], p[i+1]]
    if min(s) < s[1] and s[1] < max(s):
        res += 1

# output
print(res)