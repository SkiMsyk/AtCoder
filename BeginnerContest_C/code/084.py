N = int(input())
C = []
S = []
F = []

for i in range(N-1):
    c,s,f = map(int, input().split())
    C.append(c)
    S.append(s)
    F.append(f)

# ci : i -> i+1
# fi : frequency of departure from i-th station
# si : first train time. sec from start.
res = []

for i in range(N-1):
    total = S[i] + C[i]
    for j in range(i+1, N-1):
        if total < S[j]:
            total = S[j] + C[j]
        elif (total - S[j]) % F[j] == 0:
            total += C[j]
        else:
            total += F[j] - (total % F[j])
            total += C[j]
    res.append(total)

res.append(0)

print("\n".join([str(e) for e in res]))