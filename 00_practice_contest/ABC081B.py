import numpy as np
N = int(input())
integers = np.array(list(map(int, input().split())))

test = integers%2==0
n = 0

while sum(test)==N:
    for i in range(N):
        integers[i] = integers[i]/2
    n += 1
    test = integers%2==0

print(n)