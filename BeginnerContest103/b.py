s = list(input())
t = list(input())

if s == t:
    print('Yes')
else:
    sCopy = s.copy()
    while sCopy != t:
        sCopy.insert(0, sCopy[-1])
        sCopy.pop(-1)
        if sCopy == t:
            res = 'Yes'
            break
        if sCopy == s:
            res = 'No'
            break
    print(res)
