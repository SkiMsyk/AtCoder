import numpy as np
ps = list(map(int, input().split()))
v1 = [ps[2]-ps[0], ps[3]-ps[1]]
res = []
res.append(ps[2]-v1[1])
res.append(ps[3]+v1[0])
res.append(res[0]-v1[0])
res.append(res[1]-v1[1])
print("{} {} {} {}".format(res[0],
                           res[1],
                           res[2],
                           res[3]))