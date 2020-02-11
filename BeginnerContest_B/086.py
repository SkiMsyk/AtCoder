# library
import numpy as np

# 1 21
# input
a, b = input().split()

# solution
n = int(a + b)

#-----------
# square_numbers = [1]
# iter = 2
# while square_numbers[-1]**2 < 100100:
#     square_numbers.append(iter ** 2)
#     iter += 1
# if n in square_numbers: res = 'Yes'
# else: res = 'No'
#-----------


if np.sqrt(n) - int(np.sqrt(n)) == 0:
    res = 'Yes'
else:
    res = 'No'

# output
print(res)