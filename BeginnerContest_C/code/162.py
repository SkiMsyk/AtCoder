import math

# input
k = int(input())

# solution
res = 0
for i in range(1,k+1):
    for j in range(i, k+1):
        for h in range(j, k+1):
            t = len(set([i,j,h]))
            if t == 1:
                res += math.gcd(math.gcd(i,j), h)
            elif t==2:
                res += math.gcd(math.gcd(i,j), h)*3
            else:
                res += math.gcd(math.gcd(i,j), h)*6
print(res)