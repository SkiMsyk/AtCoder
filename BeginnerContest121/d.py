import numpy as np

A, B = map(int, input().split())
bbin = np.array([int(e) for e in bin(B)[2:]])
blen = len(bbin)
# N = B-1
# while N >= A:
#     nbin = [int(e) for e in bin(N)[2:]]
#     nlen = len(nbin)
#     if nlen < blen:
#         nbin = [0]*(blen - nlen) + nbin
#     pbin = np.array(nbin)
#     bbin = bbin + pbin
#     N -= 1

# print(int(''.join(['1' if e % 2 != 0 else '0' for e in bbin]), 2))

# Bが決まると全て決まる
# (2^n - 1) からの差で決まる

thresh_number = []
res = 0
iter = 0
while res < 10 ** 12:
    res = (2 ** iter)
    iter += 1
    thresh_number.append(res)

A_rem = []
B_rem = []

for th in thresh_number:
    if A % th:
    A_rem.insert(0, A // th + (A % th))
    B_rem.insert(0, B // th + (B % th) - (th // 2 - 1))

print(A_rem)
print(B_rem)