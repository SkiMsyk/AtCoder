import math
a, b, x = map(int, input().split())
# if a != b:
#     first = a + ((x - a % x) if a % x != 0 else 0)
#     end = b - (b % x if b % x != 0 else 0)
#     res = (end // x) - (first // x) + 1
#     print(res)
# else:
#     print(0)

def f(n, x = x):
    if n == -1:
        return 0
    else:
        return n // x + 1

print(f(b) - f(a-1))
