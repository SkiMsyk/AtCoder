A, B, K = map(int, input().split())

count = 0
cand = []
denom = 0

for i in range(1, min(A, B)+1):
    denom += 1
    if A % denom == 0 and B % denom == 0:
        cand.append(denom)

print(cand[-K])