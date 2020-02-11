# Power Socket

# input
A, B = map(int, input().split())

# solve
if B == 1:
    res = 0
else:
    res = 1
    tap = A
    while tap < B:
        tap += A - 1
        res += 1

# output
print(res)
    