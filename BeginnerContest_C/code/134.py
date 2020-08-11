N = int(input())
A = [0] * N
for _ in range(N):
    A[_] = int(input())
    if _ == 1:
        b1 = max(A[0], A[1])
        b2 = min(A[0], A[1])
    elif _ != 0 and A[_] >= b1:
        b2 = b1 
        b1 = A[_]
    elif _ != 0 and A[_] > b2:
        b2 = A[_]

for _ in range(N):
    if A[_] == b1:
        print(b2)
    else:
        print(b1)

    
