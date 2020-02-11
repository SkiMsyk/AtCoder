import math
N, K = map(int, input().split())

if K == 1:
    total = 1
else:
    total = 0
    for i in range(1, N+1):
        if K <= i:
            total += 1/N
        else:
            x = math.ceil((math.log(K) - math.log(i))/(math.log(2)))
            total += (1/N) * (1/(2**x))
print(total)