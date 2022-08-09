k, n = map(int, input().split())
a = [0] + list(map(int,input().split())) + [k]
d = [0]*(n+1)


for i in range(n+1):
    d[i] = a[i+1] - a[i]

res = sum(d) - max(d[1:-1] + [d[0] + d[-1]])
print(res)
 