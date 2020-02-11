# Digital Gifts
# settings
BIT_unit = 380000

# input
N = int(input())
total = 0
for i in range(N):
    x, u = input().split()
    if u == 'BTC':
        total += float(x) * BIT_unit
    else:
        total += float(x)

# output
print(total)
