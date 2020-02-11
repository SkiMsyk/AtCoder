# B Cakes and Donuts

# input
N = int(input())

cake_max = N // 4
donut_max = N // 7

res = 'No'

for cake in range(cake_max+1):
    if cake * 4 == N:
        res = 'Yes'
        break
    for donut in range(donut_max+1):
        if (N - cake*4) % 7 == 0:
            res = 'Yes'
            break

print(res)