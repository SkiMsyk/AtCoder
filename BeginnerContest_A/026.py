A = int(input())
res = 0
for i in range(1, A):
    res = max(res, i * (A-i))

print(res)