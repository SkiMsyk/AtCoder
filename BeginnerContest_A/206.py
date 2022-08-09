import math
N = int(input())
sales_price = math.floor(N * 1.08)
if sales_price < 206:
    print('Yay!')
elif sales_price == 206:
    print('so-so')
else:
    print(':(')
