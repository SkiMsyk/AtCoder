n, m = map(int, input().split())
if n >=12:
    n -= 12
n = n*5 + m/12
res = abs(min(max(m,n) - min(m,n), 60 - (max(m,n) - min(m,n)))*6)
if res - int(res) == 0:
    res = int(res)
print(res)

