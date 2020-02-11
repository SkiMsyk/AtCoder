s = input()
res = ''
for e in s:
    if e != 'B':
        res += e
    else:
        if len(s) != 0:
            res = res[0:len(res)-1]
print(res)