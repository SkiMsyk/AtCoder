a = map(int, input().split())
a = sorted(a)
if a[0] == a[1]:
    print(a[2])
elif a[2] == a[1]:
    print(a[0])
else:
    print(0)

    