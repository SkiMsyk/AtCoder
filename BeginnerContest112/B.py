import numpy as np
n, t = map(int, input().split())
cs = list()
ts = list()
for i in range(n):
   cc,tt = map(int, input().split())
   cs.append(cc)
   ts.append(tt)

np_cs = np.array(cs)
np_ts = np.array(ts)

avairable_ind = np.where(np_ts <= t)

if avairable_ind[0].size == 0:
    print("TLE")
else:
    print(np_cs[avairable_ind].min())

