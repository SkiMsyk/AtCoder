N = int(input())
S = input()
res = S[0]
for _ in range(1,len(S)):
    if res[-1] != S[_]:
        res = res + S[_]

print(len(res))

