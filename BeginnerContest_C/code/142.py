import numpy as np

N = int(input())
A = list(map(int, input().split()))
rank = {}
for i in range(N):
    rank[A[i]] = str(i+1)
    
print(' '.join(rank.values()))