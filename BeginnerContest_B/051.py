# Sum of Three Integers
K, S = map(int, input().split())
res = 0
for x in range(K+1):
    for y in range(K+1):
        if x + y > S:
            continue
        if S - (x + y) <= K:
            res += 1
print(res)