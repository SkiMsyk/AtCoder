X, Y = map(int, input().split())
A = []
cand = X

while cand <= Y:
    A.append(cand)
    cand = cand*2

print(len(A))