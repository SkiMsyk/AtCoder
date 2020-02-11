N, M = map(int, input().split())
l, r = map(int, input().split())
flag = 0
if M != 1:
    for i in range(1,M):
        lnew, rnew = map(int, input().split())
        if r < lnew or l > rnew:
            flag = 1
            break
        else:
            l = max(l, lnew)
            r = min(r, rnew)
    if flag:
        res = 0
    else:
        res = r - l + 1
    print(res)
else:
    print(N)