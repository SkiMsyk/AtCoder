A, B, C = map(int,input().split())
if abs(A-B) > abs(A-C):
    print(B)
elif abs(A-B) == abs(A-C):
    print(A)
else:
    print(C)