# HonestOrUnkind2
import numpy as np

# input
N = int(input())
A = [0]*N
X = list()

for i in range(N):
    A[i] = int(input())
    for j in range(A[i]):
        X.append(list(map(int, input().split())))

# output
print(X)