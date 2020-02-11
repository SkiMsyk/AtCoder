a,b,c,d = map(int, input().split())
d_ab = abs(a-b)
d_bc = abs(b-c)
d_ac = abs(a-c)

if d_ac <= d:
    print("Yes")
elif d_ab <= d and d_bc <= d:
    print("Yes")
else:
    print("No")