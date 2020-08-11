N, K, Q = map(int,input().split())

A = [0] * N
for i in range(Q):
    a = int(input())
    A[a-1] += 1

print('\n'.join(['No' if K-Q+e <= 0 else 'Yes' for e in A]))