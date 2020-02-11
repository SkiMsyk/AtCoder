from collections import Counter

w = list(input())
if len(w) % 2 == 1:
    print('No')
else:
    res = [0 if e % 2 == 0 else 1 for e in Counter(w).values()]
    if sum(res) == 0:
        print('Yes')
    else:
        print('No')

