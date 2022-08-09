n = int(input())
a = list(map(int,input().split()))

half = 2**(n-1)

if a.index(max(a)) < half:
    res = a.index(max(a[half:]))
else:
    res = a.index(max(a[:half]))

print(res+1)