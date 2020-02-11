def SomeSums(N, A, B):
    total = 0
    for i in range(N+1):
        res = sum([int(k) for k in str(i)])
        if A <= res and res <= B:
            total += i
    return total

N, A, B = map(int, input().split())
res = SomeSums(N=N, A=A, B=B)
print(res)