# Uneven Numbers

# input
N = int(input())

# solve
res = 0

for i in range(1, N+1):
    res += 1 * (len(str(i)) % 2 != 0)

# output
print(res)