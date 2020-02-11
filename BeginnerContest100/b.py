# d is in {0, 1, 2}
# n is greater than or equal to 1 and less than or equal to 100

d, n = map(int, input().split())
if n == 100:
    res = 101 * (100**d)
else:
    res = n * (100**d)

print(res)