# Fifty-Fifty
d = {}
for s in input():
    if s not in d.keys():
        d[s] = 1
    else:
        d[s] += 1

if list(d.values()) == [2,2]:
    print('Yes')
else:
    print('No')