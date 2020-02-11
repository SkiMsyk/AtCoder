n = int(input())
res = n

if n == 1:
    print(0)
else:
    for i in range(1,n):
        for j in range(1, (n // i) + 1):
                res = min(abs(i - j) + n - (i * j), res)
    print(res)