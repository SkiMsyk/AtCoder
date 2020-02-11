import numpy as np

N, X = map(int, input().split())
L = np.array([0] + list(map(int, input().split()))) 

res = sum([1 if e <= X else 0 for e in np.cumsum(L)])

print(res)
# pos = 0
# iter = 0



# while pos <= X and N >= iter:
#     iter += 1
#     pos += L[iter-1]
    

# print(iter)
