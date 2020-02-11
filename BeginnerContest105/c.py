n = int(input())
res = []
if n == 0:
    print(0)
else:
    while n != 0:
        if (n % 2) == 1:
            n = (n-1)/(-2)
            res.append(1)
        else:
            n = n/(-2)
            res.append(0)
    print(''.join([str(e) for e in res[-1::-1]]))
