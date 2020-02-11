N, L = map(int, input().split())
S = []
master = 'abcdefghijklmnopqrstuvwxyz'

def f(s1, s2, l):
    for i in range(l):
        if master.index(s1[i]) == master.index(s2[i]):
            continue
        elif master.index(s1[i]) > master.index(s2[i]):
            return 'greater'
        elif master.index(s1[i]) < master.index(s2[i]):
            return 'less'
    return 'equal'

for _ in range(N):
    if _ == 0:
        S.append(input())
    else:
        s = input()
        max_iter = len(S)
        for i in range(max_iter):
            compared = f(s, S[i], L)
            if compared == 'greater' and i == max_iter-1:
                S.append(s)
                break
            elif compared == 'less':
                S.insert(i, s)
                break
            elif compared == 'equal':
                S.insert(i, s)
                break
            else:
                continue

print(''.join(S))