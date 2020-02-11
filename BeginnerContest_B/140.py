# Buffet
import numpy as np

# input
N = int(input())
A = [e - 1 for e in list(map(int, input().split()))]
B = list(map(int, input().split()))
C = list(map(int, input().split()))

# solve
res = 0
for i in range(len(A)):
    res += B[i]
    if i != 0 and A[i-1] + 1 == A[i]:
        res += C[A[i-1]]

# output
print(res)
