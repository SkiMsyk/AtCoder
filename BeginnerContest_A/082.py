a, b = map(int, input().split())
t = (a+b)/2
if t-int(t) >= 0.5:
    print(int(t) + 1)
else:
    print(int(t))
