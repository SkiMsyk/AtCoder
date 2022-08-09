N,M,Q = map(int, input().split())
a = [0]*Q
b = [0]*Q
c = [0]*Q
d = [0]*Q
for _ in range(Q):
    a[_], b[_], c[_], d[_] = map(int, input().split())

ans = 0

for i1 in range(1, M+1):
    for i2 in range(i1, M+1):
        for i3 in range(i2, M+1):
            for i4 in range(i3, M+1):
                for i5 in range(i4, M+1):
                    for i6 in range(i5, M+1):
                        for i7 in range(i6, M+1):
                            for i8 in range(i7, M+1):
                                for i9 in range(i8, M+1):
                                    for i10 in range(i9, M+1):
                                        score = 0
                                        A = [0, i1, i2, i3, i4, i5, i6, i7, i8, i9, i10]
                                        for j in range(Q):
                                            if A[b[j]] - A[a[j]] == c[j]:
                                                score += d[j]
                                        ans = max(ans, score)

print(ans)
