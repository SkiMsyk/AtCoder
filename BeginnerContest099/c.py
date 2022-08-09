import numpy as np
n = int(input())

origins = []
uses = []

sixs = [6**i for i in range(1,7)]
for e in sixs:
    origins += [e*i for i in range(1,7)]
    uses += [i for i in range(1,7)]

nines = [6**i for i in range(1,6)]
for e in nines:
    origins += [e*i for i in range(1,6)]
    uses += [i for i in range(1,6)]

min6 = n
counts = 0

while min6 > 6:
    pm = [min6 > e for e in origins]
    dd = [min6 - e for e in origins]
    mm = min([e for b,e in zip(pm, dd) if b])
    ind = dd.index(mm)
    min6 = mm
    counts += uses[ind]
    print(origins[ind])
    print(uses[ind])

import ipdb; ipdb.set_trace()
res = counts + min6

print(res)

# これはだめ この問題むずかしいのでいつかまた