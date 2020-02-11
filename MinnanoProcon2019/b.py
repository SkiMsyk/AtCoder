a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())
a3, b3 = map(int, input().split())

l = [a1, a2, a3, b1, b2, b3]

res = [sum([1 for _ in l if _ == __]) for __ in [1,2,3,4]]

if 3 in res:
    print("NO")
else:
    print("YES")
