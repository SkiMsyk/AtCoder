import numpy as np
S = input()
T = input()

nS = np.array([s for s in S])
nT = np.array([s for s in T])
False_position = np.where(nS!=nT)[0]
# import ipdb; ipdb.set_trace()
for i in False_position:
    if S[i] != T[i]:
        S = S.translate(str.maketrans({S[i]:T[i], T[i]:S[i]}))
if S == T:
    print('Yes')
else:
    print('No')