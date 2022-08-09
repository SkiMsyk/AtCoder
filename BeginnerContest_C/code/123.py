import numpy as np

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

# city = [n,0,0,0,0,0]
# tran = [a,b,c,d,e,0]
# count = 0

# while city[5] < n:
#     m = [min(e[0], e[1]) for e in zip(city, tran)]
#     for i in range(5):
#         city[i] -= m[i]
#         city[i+1] += m[i]
#     count += 1

l = min([a,b,c,d,e])
ans = n // l + (n % l != 0) + 4

print(ans)