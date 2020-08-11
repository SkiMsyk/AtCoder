N, Y = map(int, input().split())

A = 10000
B = 5000
C = 1000

x = -1
y = -1
z = -1

for a in range(N+1):
    for b in range(N+1):
        if a + b > N:
            continue
        else:
            total = A*a + B*b + C*(N - (a + b))
            if total == Y:
                x = a
                y = b
                z = N - (a + b)
                break

print(x, y, z)