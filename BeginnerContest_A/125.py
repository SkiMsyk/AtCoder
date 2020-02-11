# Biscuit Generator
# input
A, B, T = map(int, input().split())

# solution
total = 0
for t in range(1, T+1):
    if t % A == 0:
        total += B

#output
print(total)