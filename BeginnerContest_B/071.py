# input 
S = input()

# processing
cand = set('abcdefghijklmnopqrstuvwxyz') - set(S)
if cand:
    res = min(cand)
else:
    res = 'None'

# output    
print(res)