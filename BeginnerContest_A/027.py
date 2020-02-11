l = list(map(int, input().split()))
if len(set(l)) == 2:
    print(sum([l*2 for l in set(l)]) - sum(l))
else:
    print(l[0])
