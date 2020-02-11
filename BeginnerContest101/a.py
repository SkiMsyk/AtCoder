s = list(input())
res = 0
for e in s:
    if e == "+":
        res += 1
    else:
        res -= 1
print(res)