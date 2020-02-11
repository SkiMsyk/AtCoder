# library
from string import ascii_lowercase as a

# input
S = input()
T = input()

# solution
s = ''.join([a[n] for n in sorted([a.index(e) for e in S])])
t = ''.join([a[n] for n in sorted([a.index(e) for e in T], reverse = True)])

# output
if s < t: res = 'Yes'
else: res = 'No'
print(res)