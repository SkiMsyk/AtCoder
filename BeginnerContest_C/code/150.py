from itertools import permutations

n = int(input())
p = ''.join(list(input().split()))
q = ''.join(list(input().split()))

S = sorted([''.join(i) for i in permutations([str(e) for e in range(1,n+1)], r=n)])
ans = abs(S.index(p) - S.index(q))
print(ans)
