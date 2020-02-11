res = 0
n, h, w = map(int, input().split())
for i in range(n):
    a,b = map(int, input().split())
    if a >= h and b >= w:
        res += 1
print(res)