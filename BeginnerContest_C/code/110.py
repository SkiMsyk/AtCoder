# module
from string import ascii_lowercase as sl

# input
s = input()
t = input()

# mapping
start = [-1] * 26
goal  = [-1] * 26

# solution 
ans = 'Yes'
for si, ti in zip(s,t):
    sx = sl.index(si)
    tx = sl.index(ti)
    if (start[sx] != -1) or (goal[tx] != -1):
        if (start[sx] != tx) or (goal[tx] != sx):
            ans = 'No'
            break
    start[sx] = tx
    goal[tx] = sx
    # test ---
    print([sl[e] if e != -1 else -1 for e in start])
    print([sl[e] if e != -1 else -1 for e in goal])
    print('-----')
    # ---
    
print(ans)

