S = input()
T = input()

ns = len(S)
nt = len(T)

if ns == nt:
    if S == T:
        ans = 0
    else:
        ans = sum([e[0] != e[1] for e in zip(S,T)])
else:
    ans = 1000
    for i in range(ns-nt):
        s = S[i:i+nt]
        if s == T:
            ans = 0
            break
        else:
            ans = min(ans, sum([e[0] != e[1] for e in zip(s,T)]))

print(ans)