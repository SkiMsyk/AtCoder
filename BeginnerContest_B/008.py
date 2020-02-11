N = int(input())
S = dict()
for _ in range(N):
    s = input()
    if s in S.keys():
        S[s] += 1
    else:
        S[s] = 1

res = 0
for k,v in S.items():
    if v > res:
        res = v
        name = k

print(name)