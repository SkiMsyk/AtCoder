S = input()
res = 0
count = 0
for s in S:
    if s in ['A', 'C', 'G', 'T']:
        count += 1
    else:
        count = 0
    res = max(count, res)

print(res)
