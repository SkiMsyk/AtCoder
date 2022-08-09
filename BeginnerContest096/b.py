l = list(map(int,input().split()))
k = int(input())

res = max(l) * (2**k) + sum(l) - max(l)
print(res)

