C = ['']*4
for _ in range(3,-1,-1):
    C[_] = reversed(list(input().split()))

for _ in range(4):
    print(' '.join(C[_]))
