N, K = map(int, input().split())
nK = (N // K)
if K % 2 == 0:
    if (K//2) <= (N % K):
        rnK = nK + 1
    else:
        rnK = nK
else:
    rnK = 0
print(nK**3 + rnK**3)
