S = list(input())
T = list(input())

def check(s,t):
    if s == t:
        return True
    elif s == '@' and t in list('atcoder'):
        return True
    elif t == '@' and s in list('atcoder'):
        return True
    else:
        return False

flag = 'You can win'

for s, t in zip(S, T):
    if check(s,t):
        continue
    else:
        flag = 'You will lose'
        break

print(flag)