A, B = map(int, input().split())
if B % A == 0 and B >= A:
    print(A+B)
else:
    print(B-A)