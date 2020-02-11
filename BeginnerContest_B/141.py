# Tap Dance

# input
S = input()

# solve
cond1 = sum([s == 'L' for s in S[::2]])
cond2 = sum([s == 'R' for s in S[1::2]])

# output
if cond1 == 0 and cond2 == 0:
    print('Yes')
else:
    print('No')
