# Count Balls
N, A, B = map(int, input().split())
ans = (N // (A + B)) * A + min(A, N % (A+B))
print(ans)