k, a, b = map(int, input().split())

if a < b - 2 and k >= a + 1:
    k -= a - 1
    res = a
    res += (k//2) * (b - a) + (k % 2)
else:
    res = k + 1

print(res)