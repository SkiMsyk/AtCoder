# Five Dishes

# input
menu = list()
for _ in range(5):
    x = int(input())
    t = x % 10 + (10 * (x % 10 == 0))
    menu.append([t, x])

menu = sorted(menu, reverse = True)

total = 0
for e in menu[:-1]:
    total += e[1] + (10 - e[0]) * (e[0] != 10)

total += menu[-1][1]
print(total)