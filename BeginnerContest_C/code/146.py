def price(a,b,n):
    return a*n + b*len(str(n))

a, b, x = map(int, input().split())

h = 10**9
l = 1

if price(a,b,h) < x:
    res = h
elif x < price(a,b,l):
    res = 0
else:
    while (h-l) > 1:
        m = (l+h)//2
        if price(a,b,m) <= x:
            l = m
        else:
            h = m
    
    res = l
    
print(res)