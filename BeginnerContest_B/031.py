L, H = map(int, input().split())
N = int(input())
for _ in range(N):
    a = int(input())
    if L <= a and a <= H:
        print(0)
    elif a < L:
        print(L-a)
    elif H < a:
        print(-1)

