import math

x = int(input())

pow_list = [1, 1000]
i = 2
while i**2 <= 1000:
    j = 2
    while i**j <= 1000:
        pow_list.append(i**j)
        j += 1
    i += 1

pow_list = set(pow_list)

for i in range(x, 0, -1):
    if i in pow_list:
        res = i
        break

print(res)