N = int(input())
a = list(map(int, input().split()))
test = sum(a) % N
each = sum(a) // N
if test != 0:
    print(-1)
else:
    total = 0
    for i in range(N):
        if sum(a[:i]) == each*i and sum(a[i:]) == each*(N-i):
            continue
        else:
            total += 1
    print(total)
