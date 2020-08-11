N = int(input())
d = sorted(list(map(int, input().split())))
if N % 2 == 0:
    # even case 
    res = d[N // 2] - d[N // 2 - 1]
else:
    # odd case
    res = 0
print(res)

