# 9x9
A, B = map(int, input().split())
if A // 10 == 0 and B // 10 == 0:
    print(A * B)
else:
    print(-1)