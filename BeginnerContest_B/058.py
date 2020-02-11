O = list(input())
E = list(input())
res = ''
iter = 0
while len(O) != 0 or len(E) != 0:
    if len(O) > 0:
        res += O.pop(0)
    if len(E) > 0:
        res += E.pop(0)
    iter += 1
print(res)


