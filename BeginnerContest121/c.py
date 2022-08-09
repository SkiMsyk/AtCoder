N, M = map(int, input().split())
AB = list()
for i in range(N):
    AB.append(list(map(int, input().split())))

AB = sorted(AB)

drink = 0
money = 0
iter = 0
while drink < M:
    add = min(AB[iter][1], M-drink)
    drink += add
    money += add*AB[iter][0]
    iter += 1

print(money)


