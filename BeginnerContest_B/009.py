N = int(input())
A = list()
for _ in range(N):
    a = int(input())
    if a not in A:
        A.append(a)

A = sorted(A)
print(A[-2])
