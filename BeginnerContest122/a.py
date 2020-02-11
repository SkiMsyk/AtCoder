b = list(input())
res = []
for i in range(len(b)):
    if b[i] == 'A':
        res.append("T")
    elif b[i] == 'T':
        res.append('A')
    elif b[i] == 'C':
        res.append('G')
    elif b[i] == 'G':
        res.append('C')

print(''.join(res))