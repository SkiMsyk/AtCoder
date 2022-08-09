# on-off switch
# switch s_i1, s_i2,...,s_ikiのうちonになっているswitchの個数を2で割ったあまりがpiに等しい時に点灯する
N, M = map(int, input().split())
cond = []
for _ in range(M):
    k, *s = list(map(int, input().split()))
    s = [e-1 for e in s]
    cond.append(s)
p = list(map(int,input().split()))
dlen = len(format(2**N-1,'b'))

ans = 0
for i in range(2**N):
    d = [0]*M # light states
    s = [int(e) for e in format(i, 'b').zfill(dlen)] # switch state
    for m in range(M):
        # conditions
        condi = cond[m]
        pi    = p[m]
        
        # check
        on_and_connected = sum([s[e] for e in condi])
        if on_and_connected % 2 == pi:
            d[m] = 1
            
    if sum(d) == len(d):
        ans += 1

print(ans)