n, k = map(int, input().split())
res = min(abs(k * (n//k) - n), abs(k * (n//k + 1) - n))
print(res)