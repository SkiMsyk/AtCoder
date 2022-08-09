def dfs(A):
    global ans
    global M
    if len(A) == N+1:
        # calc score
        now = 0
        for i in range(Q):
            if (A[b[i]] - A[a[i]]) == c[i]:
                now += d[i]
        ans = max(ans, now)
        print(A)
        return None

    A.append(A[-1])
    while A[-1] <= M:
        dfs(A)
        A[-1] += 1

N,M,Q = map(int, input().split())
a = [0]*Q
b = [0]*Q
c = [0]*Q
d = [0]*Q
for _ in range(Q):
    a[_], b[_], c[_], d[_] = map(int, input().split())

ans = 0
dfs([1])
print(ans)