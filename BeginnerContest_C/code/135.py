N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

total = 0
for i in range(N):
    total += min(A[i], B[i])
    rem = max(0, B[i] - A[i])
    total += min(A[i+1], rem)
    A[i+1] = max(0, A[i+1] - rem)

print(total)

