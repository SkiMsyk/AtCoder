# Picture Frame
H, W = map(int, input().split())
res = ['']*(H+2)
res[0] = '#'*(W+2)
res[-1] = '#'*(W+2)
for _ in range(H):
    res[_+1] = '#' + input() + '#'
for _ in res:
    print(_)