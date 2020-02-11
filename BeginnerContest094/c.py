n = int(input())
x = list(map(int, input().split()))

if n == 2:
    print(x[1])
    print(x[0])
else:
    y = sorted(x)
    m1 = y[int(n/2)-1]
    m2 = y[int(n/2)]
    if m1 == m2:
        for _ in range(n):
            print(m1)
    else:
        for i in range(n):
            if x[i] <= m1:
                print(m2)
            elif x[i] >= m2:
                print(m1)
