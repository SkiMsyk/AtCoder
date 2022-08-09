# input
n = int(input())
a = list(map(int,input().split()))

r = [0]*n
for e in a:
    r[e-1] += 1

for _ in range(n):
    print(r[_])