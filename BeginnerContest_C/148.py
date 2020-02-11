# Snack
from collections import deque
import numpy as np
import math


# input
A, B = map(int, input().split())
A, B = max(A,B), min(A,B)

# solve
# -----------------
# 約数列挙
def make_divisor_list(num):
    if num < 1:
        return []
    elif num == 1:
        return [1]
    else:
        divisor_list = deque()
        divisor_list.append(1)
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                divisor_list.append(i)
        divisor_list.append(num)

        return list(divisor_list)
# -----------------

div_A = make_divisor_list(A)
div_B = make_divisor_list(B)

rem = [b for b in div_B if b not in div_A]

if len(rem) != 0:
    for b in [b for b in div_B if b not in div_A]:
        if A * b % B == 0:
            res = A * b
            break
else:
    res = A

# output
print(res)