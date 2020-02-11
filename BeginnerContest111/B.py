import numpy as np
n = int(input())
table = np.array([111*i for i in range(1,10)])
table = table[np.where(table>=n)]
print(table[np.argmin(table-n)])