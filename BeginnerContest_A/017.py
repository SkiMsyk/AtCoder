dd = []
for i in range(3):
    dd.append(list(map(int, input().split())))

res = sum([e1*e2/10 for e1, e2 in dd])
print(int(res))