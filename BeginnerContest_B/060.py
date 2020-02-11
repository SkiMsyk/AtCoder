A, B, C = map(int, input().split())
res = 'NO'
for _ in range(A, A*B+1, A):
    if (_ % B) == C:
        res = 'YES'
        break
print(res)
