import numpy as np
A, B, C, D = map(int, input().split())

def gcd(a,b):
    rem = a % b
    while rem != 0:
        a = b
        b = rem
        rem = a % b
    return b

g = gcd(C, D)
l = (C*D)//g

x = B - ((B//C) + (B//D) - (B//l))
A = A-1
y = A - ((A//C) + (A//D) - (A//l))

print(x - y)