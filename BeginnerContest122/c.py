N, Q = map(int, input().split())
S = input()
ls = list()
rs = list()
for _ in range(Q):
    l, r = map(int, input().split())
    ls.append(l)
    rs.append(r)

cumsum = [0]

for i in range(1,N):
    if S[i-1:i+1] == "AC":
        cumsum.append(cumsum[i-1] + 1)
    else:
        cumsum.append(cumsum[i-1])

for l, r in zip(ls, rs):
    print(cumsum[r-1] - cumsum[l-1])

